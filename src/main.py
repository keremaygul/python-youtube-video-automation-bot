import os
import sys
import time
import logging
from datetime import datetime
from config_manager import ConfigManager
from video_creator import VideoCreator
from youtube_uploader import YouTubeUploader
from utils import setup_logging, ensure_dir_exists

def main():
    logger = logging.getLogger(__name__)
    logger.info("Starting YouTube Video Automation Bot...")

    try:
        # Load configuration
        logger.info("Loading configuration...")
        config_manager = ConfigManager()
        settings = config_manager.load_settings()
        
        # Ensure directories exist
        ensure_dir_exists(settings['paths']['assets_dir'])
        ensure_dir_exists(settings['paths']['temp_dir'])
        ensure_dir_exists(os.path.dirname(settings['paths']['font_path']))
        
        # Initialize video creator
        logger.info("Initializing video creator...")
        video_creator = VideoCreator(settings)
        
        # Initialize YouTube uploader
        logger.info("Initializing YouTube uploader...")
        uploader = YouTubeUploader(settings['youtube']['chrome_driver_path'])
        
        # Get content items to process
        logger.info("Getting content items...")
        items = config_manager.get_content_items()
        logger.info(f"Found {len(items)} items to process")
        
        # Process each item
        for item in items:
            try:
                logger.info(f"Processing content item: {item['title']}")
                
                # Create video
                logger.info("Creating video...")
                video_path = video_creator.create_video(
                    title=item['title'],
                    description=item['description'],
                    images=item['images'],
                    audio_text=item['audio_text']
                )
                
                if video_path:
                    logger.info(f"Video created successfully: {video_path}")
                    
                    # Video yükleme işlemi
                    logger.info("Uploading video to YouTube...")
                    
                    title = f"{item['title']} - {datetime.now().strftime('%B %Y')}"
                    description = item['description']
                    thumbnail_path = os.path.join(settings['paths']['temp_dir'], "frame_title.png")
                    video_path = os.path.join(settings['paths']['temp_dir'], "final_video.mp4")
                    
                    success = uploader.upload_video(
                        video_path=video_path,
                        title=title,
                        description=description,
                        thumbnail_path=thumbnail_path
                    )
                    
                    if success:
                        logger.info("Video uploaded successfully")
                        config_manager.mark_as_completed(item['id'])
                    else:
                        logger.error("Failed to upload video")
                        
                    # Temp dosyaları temizle
                    video_creator.cleanup()
                    
                    # Bir sonraki video için bekle
                    time.sleep(5)
                
            except Exception as e:
                logger.error(f"Error processing item {item['id']}: {str(e)}")
                continue
                
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        
    logger.info("Processing complete")

if __name__ == "__main__":
    setup_logging()
    main() 