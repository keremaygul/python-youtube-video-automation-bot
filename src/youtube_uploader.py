import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class YouTubeUploader:
    def __init__(self, chrome_driver_path):
        self.chrome_driver_path = chrome_driver_path
        self.logger = logging.getLogger(__name__)

    def _setup_driver(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def _navigate_to_upload(self, driver):
        driver.get("https://studio.youtube.com")
        wait = WebDriverWait(driver, 180)
        upload_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="upload-icon"]')))
        upload_button.click()
        time.sleep(3)

    def _upload_file(self, driver, video_path):
        file_input = driver.find_element(By.XPATH, '//*[@id="content"]/input')
        abs_path = os.path.abspath(video_path)
        file_input.send_keys(abs_path)
        time.sleep(7)

    def _set_title_description(self, driver, title, description):
        # Başlık alanını temizle ve yeni başlığı gir
        title_input = driver.find_element(
            By.XPATH, '//*[@id="textbox"]')
        driver.execute_script("arguments[0].innerText = '';", title_input)
        title_input.send_keys(title)
        
        # Açıklama alanını bul ve metni gir
        desc_input = driver.find_element(
            By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-video-description/div/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div')
        desc_input.send_keys(description)
        time.sleep(3)

    def _set_not_made_for_kids(self, driver):
        try:
            not_for_kids_radio = driver.find_element(
                By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK")
            not_for_kids_radio.click()
        except Exception as e:
            self.logger.error(f"Could not set 'Not made for kids': {str(e)}")
        time.sleep(3)

    def _set_visibility(self, driver, visibility="unlisted"):
        # Next butonlarına tıkla
        for _ in range(3):
            next_button = driver.find_element(By.ID, "next-button")
            next_button.click()
            time.sleep(1)

        # Visibility radio butonunu bul ve tıkla
        try:
            visibility_radio = driver.find_element(
                By.XPATH, '//*[@id="privacy-radios"]/tp-yt-paper-radio-button[3]')
            visibility_radio.click()
            time.sleep(2)
        except Exception as e:
            self.logger.error(f"Could not set visibility: {str(e)}")
            raise

    def upload_video(self, video_path, title, description, thumbnail_path=None):
        """Upload a video to YouTube.
        
        Args:
            video_path (str): Path to the video file
            title (str): Video title
            description (str): Video description
            thumbnail_path (str, optional): Path to thumbnail image
        """
        try:
            driver = self._setup_driver()
            self._navigate_to_upload(driver)
            self._upload_file(driver, video_path)
            
            if thumbnail_path:
                thumbnail_input = driver.find_element(By.XPATH, '//input[@type="file"][@accept="image/jpeg,image/png"]')
                abs_thumb_path = os.path.abspath(thumbnail_path)
                thumbnail_input.send_keys(abs_thumb_path)
                time.sleep(3)
            
            self._set_title_description(driver, title, description)
            self._set_not_made_for_kids(driver)
            self._set_visibility(driver)
            
            done_button = driver.find_element(By.ID, "done-button")
            done_button.click()
            
            self.logger.info("Video upload completed successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error uploading video: {str(e)}")
            return False 