import os
import logging
import subprocess
from datetime import datetime

def ensure_dir_exists(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)

def setup_logging():
    """Configure logging to output to both file and console"""
    # Create logs directory if it doesn't exist
    logs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))
    ensure_dir_exists(logs_dir)
    
    # Create log file with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = os.path.join(logs_dir, f'bot_{timestamp}.log')
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
        
def clean_text(text):
    """Clean text by removing special characters and extra spaces"""
    # Remove special characters
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    # Remove extra spaces
    text = ' '.join(text.split())
    return text
    
def get_video_duration(video_path):
    """Get video duration in seconds using ffprobe"""
    try:
        result = subprocess.run([
            'ffprobe',
            '-v', 'error',
            '-show_entries', 'format=duration',
            '-of', 'default=noprint_wrappers=1:nokey=1',
            video_path
        ], capture_output=True, text=True)
        
        return float(result.stdout)
    except Exception as e:
        logging.error(f"Error getting video duration: {str(e)}")
        return 0 