import os
import cv2
import random
import logging
import textwrap
import subprocess
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
from utils import ensure_dir_exists

class VideoCreator:
    def __init__(self, settings):
        """Initialize VideoCreator with settings"""
        self.settings = settings
        self.logger = logging.getLogger(__name__)
        
        # Log paths
        self.logger.info(f"Assets directory: {settings['paths']['assets_dir']}")
        self.logger.info(f"Temp directory: {settings['paths']['temp_dir']}")
        self.logger.info(f"Font path: {settings['paths']['font_path']}")
        
        # Ensure directories exist
        ensure_dir_exists(settings['paths']['assets_dir'])
        ensure_dir_exists(settings['paths']['temp_dir'])
        
    def create_video(self, title, description, images, audio_text):
        """Create a video with the given content"""
        try:
            # Create title frame
            title_frame_path = os.path.join(self.settings['paths']['temp_dir'], "frame_title.png")
            self._create_title_frame(title, description, title_frame_path)
            
            # Create content frames
            content_frames = []
            for i, image_path in enumerate(images):
                frame_path = os.path.join(self.settings['paths']['temp_dir'], f"frame_content_{i}.png")
                self._create_content_frame(image_path, frame_path)
                content_frames.append(frame_path)
                
            # Create video from frames
            video_path = os.path.join(self.settings['paths']['temp_dir'], "temp_video.avi")
            self._create_video_from_frames([title_frame_path] + content_frames, video_path)
            
            # Create audio
            audio_path = os.path.join(self.settings['paths']['temp_dir'], "temp_audio.mp3")
            self._create_audio(audio_text, audio_path)
            
            # Combine video and audio
            final_path = os.path.join(self.settings['paths']['temp_dir'], "final_video.mp4")
            self._add_audio_to_video(video_path, audio_path, final_path)
            
            return final_path
            
        except Exception as e:
            self.logger.error(f"Error creating video: {str(e)}")
            return None
            
    def _create_title_frame(self, title, description, output_path):
        """Create title frame with text overlay"""
        try:
            # Select random background
            bg_dir = os.path.join(self.settings['paths']['assets_dir'], "backgrounds")
            bg_files = [f for f in os.listdir(bg_dir) if f.endswith(('.jpg', '.png'))]
            bg_path = os.path.join(bg_dir, random.choice(bg_files))
            self.logger.info(f"Using background: {bg_path}")
            
            # Create frame
            img = Image.open(bg_path)
            draw = ImageDraw.Draw(img)
            
            # Load fonts
            title_font = ImageFont.truetype(self.settings['paths']['font_path'], 55)
            desc_font = ImageFont.truetype(self.settings['paths']['font_path'], 25)
            
            # Add title
            bbox = draw.textbbox((0, 0), title, font=title_font)
            text_width = bbox[2] - bbox[0]
            x = (img.width - text_width) // 2
            draw.text((x, 75), title, (0, 0, 0), font=title_font)
            
            # Add description
            margin = 245
            for line in textwrap.wrap(description, width=54):
                bbox = draw.textbbox((0, 0), line, font=desc_font)
                text_width = bbox[2] - bbox[0]
                x = (img.width - text_width) // 2
                draw.text((x, margin), line, (0, 0, 0), font=desc_font)
                margin += desc_font.size + 10
                
            # Save frame
            self.logger.info(f"Saving frame to: {output_path}")
            img.save(output_path)
            
        except Exception as e:
            self.logger.error(f"Error creating title frame: {str(e)}")
            raise
            
    def _create_content_frame(self, image_path, output_path):
        """Create content frame from image"""
        try:
            self.logger.info(f"Loading image: {image_path}")
            self.logger.info(f"Creating content frame from: {image_path}")
            
            # Load and resize image if needed
            img = Image.open(image_path)
            if img.size != (1280, 720):
                img = img.resize((1280, 720), Image.LANCZOS)
                
            # Save frame
            self.logger.info(f"Saving frame to: {output_path}")
            img.save(output_path)
            
        except Exception as e:
            self.logger.error(f"Error creating content frame: {str(e)}")
            raise
            
    def _create_video_from_frames(self, frame_paths, output_path):
        """Create video from frames"""
        try:
            self.logger.info(f"Creating video at: {output_path}")
            
            # Read first frame to get dimensions
            frame = cv2.imread(frame_paths[0])
            height, width, _ = frame.shape
            
            # Create video writer
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(output_path, fourcc, 1.0, (width, height))
            
            # Add each frame
            for frame_path in frame_paths:
                frame = cv2.imread(frame_path)
                # Add frame multiple times for duration
                for _ in range(5):  # 5 seconds per frame
                    out.write(frame)
                    
            out.release()
            
        except Exception as e:
            self.logger.error(f"Error creating video: {str(e)}")
            raise
            
    def _create_audio(self, text, output_path):
        """Create audio from text"""
        try:
            self.logger.info(f"Creating audio at: {output_path}")
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(output_path)
            
        except Exception as e:
            self.logger.error(f"Error creating audio: {str(e)}")
            raise
            
    def _add_audio_to_video(self, video_path, audio_path, output_path):
        """Combine video and audio"""
        try:
            self.logger.info(f"Creating final video at: {output_path}")
            subprocess.call([
                'ffmpeg', '-i', video_path,
                '-i', audio_path,
                '-c:v', 'copy',
                '-c:a', 'aac',
                '-strict', 'experimental',
                output_path
            ])
            
        except Exception as e:
            self.logger.error(f"Error adding audio to video: {str(e)}")
            raise
            
    def cleanup(self):
        """Temp klasöründeki dosyaları temizle"""
        try:
            temp_dir = self.settings['paths']['temp_dir']
            for filename in os.listdir(temp_dir):
                file_path = os.path.join(temp_dir, filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    self.logger.error(f"Error deleting {file_path}: {str(e)}")
            self.logger.info("Temp files cleaned up successfully")
        except Exception as e:
            self.logger.error(f"Error during cleanup: {str(e)}") 