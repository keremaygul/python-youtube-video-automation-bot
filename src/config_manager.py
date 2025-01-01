import os
import json
import logging
from typing import List, Dict, Any

class ConfigManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.config_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config'))
        self.logger.info(f"Config directory: {self.config_dir}")
        
        self.settings_path = os.path.join(self.config_dir, 'settings.json')
        self.logger.info(f"Settings path: {self.settings_path}")
        
        self.content_path = os.path.join(self.config_dir, 'content.json')
        self.logger.info(f"Content path: {self.content_path}")
        
        self.completed_path = os.path.join(self.config_dir, 'completed.txt')
        
    def load_settings(self) -> Dict[str, Any]:
        """Load settings from settings.json"""
        try:
            with open(self.settings_path, 'r') as f:
                settings = json.load(f)
                
            # Convert relative paths to absolute
            base_dir = os.path.dirname(self.config_dir)
            settings['paths']['assets_dir'] = os.path.abspath(os.path.join(base_dir, settings['paths']['assets_dir']))
            settings['paths']['temp_dir'] = os.path.abspath(os.path.join(base_dir, settings['paths']['temp_dir']))
            settings['paths']['font_path'] = os.path.abspath(os.path.join(base_dir, settings['paths']['font_path']))
            
            self.logger.info("Settings loaded successfully")
            return settings
            
        except Exception as e:
            self.logger.error(f"Error loading settings: {str(e)}")
            raise
            
    def get_content_items(self) -> List[Dict[str, Any]]:
        """Get content items that haven't been processed yet"""
        try:
            # Load completed items
            completed_items = self._load_completed_items()
            self.logger.info(f"Loaded {len(completed_items)} completed items")
            
            # Load content items
            with open(self.content_path, 'r') as f:
                content_items = json.load(f)
                
            self.logger.info(f"Loaded {len(content_items)} content items from file")
            
            # Filter out completed items
            items_to_process = [
                item for item in content_items
                if str(item['id']) not in completed_items
            ]
            
            self.logger.info(f"Found {len(items_to_process)} items to process after filtering")
            return items_to_process
            
        except Exception as e:
            self.logger.error(f"Error getting content items: {str(e)}")
            return []
            
    def mark_as_completed(self, item_id: str):
        """Mark an item as completed"""
        try:
            with open(self.completed_path, 'a') as f:
                f.write(f"{item_id}\n")
            self.logger.info(f"Marked item {item_id} as completed")
            
        except Exception as e:
            self.logger.error(f"Error marking item as completed: {str(e)}")
            
    def _load_completed_items(self) -> set:
        """Load the set of completed item IDs"""
        try:
            if not os.path.exists(self.completed_path):
                return set()
                
            with open(self.completed_path, 'r') as f:
                return set(line.strip() for line in f if line.strip())
                
        except Exception as e:
            self.logger.error(f"Error loading completed items: {str(e)}")
            return set() 