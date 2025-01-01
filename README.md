# 🇬 YouTube Video Automation Bot

<div align="center">

🇬🇧 [English](#english) | 🇹🇷 [Türkçe](#turkish)

</div>

---

<div id="english">

# 🤖 YouTube Video Automation Bot

> An automated solution for creating and uploading videos to YouTube using Python. This bot can generate videos from images, add text overlays, create voiceovers, and automatically upload them to YouTube.

<p align="center">
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python Version">
<img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="Build Status">
</p>

## ✨ Features

### 🎥 Automated Video Creation
- 🖼️ Create videos from multiple images
- 📝 Add title and description overlays
- 🗣️ Text-to-speech voiceover generation
- 🎬 Professional transitions and effects
- ⚙️ Customizable video duration and frame rates

### 📺 YouTube Integration
- 🚀 Automated video upload to YouTube Studio
- 📋 Set video title and description
- 🖼️ Custom thumbnail support
- 🔒 Privacy settings management (Public/Private/Unlisted)
- 👶 Not Made for Kids setting

### 📁 Asset Management
- 🎨 Built-in background image library
- 🔤 Custom font support
- 🧹 Temporary file cleanup
- 📂 Asset organization in dedicated directories

## 📋 Prerequisites

- 🐍 Python 3.8 or higher
- 🌐 Chrome browser
- 🚗 ChromeDriver (matching your Chrome version)
- 🎞️ FFmpeg installed and added to PATH

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/youtube-video-automation-bot.git
cd youtube-video-automation-bot
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up the directory structure:
```
youtube-video-automation-bot/
├── 📁 assets/
│   ├── 🖼️ backgrounds/    # Background images (included)
│   ├── 🔤 fonts/         # Fonts for text overlay (included)
│   ├── 🖼️ thumbnails/    # Generated thumbnails
│   └── 📁 temp/          # Temporary files
├── ⚙️ config/
│   ├── ⚙️ settings.json  # Bot configuration
│   └── 📋 content.json   # Content items to process
├── 📝 logs/              # Log files
└── 💻 src/              # Source code
```

## ⚙️ Configuration

### settings.json
```json
{
    "paths": {
        "assets_dir": "assets",
        "temp_dir": "assets/temp",
        "font_path": "assets/fonts/default.ttf"
    },
    "youtube": {
        "chrome_driver_path": "chromedriver.exe"
    },
    "video": {
        "width": 1280,
        "height": 720,
        "fps": 1,
        "frame_duration": 5
    }
}
```

### content.json
```json
[
    {
        "id": "video1",
        "title": "Your Video Title",
        "description": "Video description text",
        "images": [
            "backgrounds/image1.jpg",
            "backgrounds/image2.jpg",
            "backgrounds/image3.jpg"
        ],
        "audio_text": "Text to be converted to speech"
    }
]
```

## 🎯 Usage

1. Start Chrome in debug mode:
```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"
```

> **💡 Note**: Make sure to create the directory `C:\selenum\ChromeProfile` before running the command. This directory will store your Chrome profile data, including your YouTube login session.

2. Log in to YouTube Studio in the debug Chrome instance

3. Run the bot:
```bash
cd src
python main.py
```

The bot will:
1. 📖 Read content items from `content.json`
2. 🎥 Create videos using specified images and text
3. 🔊 Generate audio from the provided text
4. 📤 Upload videos to YouTube with specified settings
5. ✅ Mark completed items in `completed.txt`

## 📦 Included Assets

- 🖼️ **Background Images**: 3 random background images included in `assets/backgrounds/`
- 🔤 **Fonts**: Default font (Bebas Neue) included in `assets/fonts/`

## 🏗️ Project Structure

- 🎯 `src/main.py`: Main entry point
- 🎥 `src/video_creator.py`: Video creation and processing
- 📤 `src/youtube_uploader.py`: YouTube upload automation
- ⚙️ `src/config_manager.py`: Configuration management
- 🔧 `src/utils.py`: Utility functions

## ⚠️ Error Handling

- 📝 Comprehensive error logging
- 🧹 Automatic cleanup of temporary files
- 🔄 Failed upload retry mechanism
- 📊 Detailed logging in `logs/` directory

## 🤝 Contributing

1. 🔱 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feature/amazing-feature`)
3. ✍️ Commit your changes (`git commit -m 'Add amazing feature'`)
4. 🚀 Push to the branch (`git push origin feature/amazing-feature`)
5. 🎯 Open a Pull Request

## 🙏 Acknowledgments

- 🌐 Selenium WebDriver for YouTube automation
- 🎬 FFmpeg for video processing
- 🗣️ gTTS for text-to-speech conversion
- 🖼️ OpenCV and Pillow for image processing

## 💬 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

</div>

---

<div id="turkish">

# 🤖 YouTube Video Otomasyon Botu

> Python kullanarak YouTube'a video oluşturma ve yükleme işlemlerini otomatikleştiren bir çözüm. Bu bot, görüntülerden video oluşturabilir, metin ekleyebilir, sesli anlatım oluşturabilir ve videoları otomatik olarak YouTube'a yükleyebilir.

<p align="center">
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python Versiyon">
<img src="https://img.shields.io/badge/durum-aktif-brightgreen.svg" alt="Durum">
</p>

## ✨ Özellikler

### 🎥 Otomatik Video Oluşturma
- 🖼️ Birden fazla görüntüden video oluşturma
- 📝 Başlık ve açıklama metni ekleme
- 🗣️ Metinden sese dönüştürme ile sesli anlatım
- 🎬 Profesyonel geçişler ve efektler
- ⚙️ Özelleştirilebilir video süresi ve kare hızı

### 📺 YouTube Entegrasyonu
- 🚀 YouTube Studio'ya otomatik video yükleme
- 📋 Video başlığı ve açıklama ayarlama
- 🖼️ Özel küçük resim desteği
- 🔒 Gizlilik ayarları yönetimi (Herkese Açık/Gizli/Liste Dışı)
- 👶 Çocuklar İçin Değil ayarı

### 📁 İçerik Yönetimi
- 🎨 Dahili arka plan görüntü kütüphanesi
- 🔤 Özel yazı tipi desteği
- 🧹 Geçici dosya temizleme
- 📂 Özel dizinlerde içerik organizasyonu

## 📋 Gereksinimler

- 🐍 Python 3.8 veya üstü
- 🌐 Chrome tarayıcı
- 🚗 ChromeDriver (Chrome sürümünüzle uyumlu)
- 🎞️ FFmpeg kurulu ve PATH'e eklenmiş

## 🚀 Kurulum

1. Depoyu klonlayın:
```bash
git clone https://github.com/yourusername/youtube-video-automation-bot.git
cd youtube-video-automation-bot
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. Dizin yapısını oluşturun:
```
youtube-video-automation-bot/
├── 📁 assets/
│   ├── 🖼️ backgrounds/    # Arka plan görselleri (dahil)
│   ├── 🔤 fonts/         # Metin için yazı tipleri (dahil)
│   ├── 🖼️ thumbnails/    # Oluşturulan küçük resimler
│   └── 📁 temp/          # Geçici dosyalar
├── ⚙️ config/
│   ├── ⚙️ settings.json  # Bot yapılandırması
│   └── 📋 content.json   # İşlenecek içerik öğeleri
├── 📝 logs/              # Log dosyaları
└── 💻 src/              # Kaynak kod
```

## ⚙️ Yapılandırma

### settings.json
```json
{
    "paths": {
        "assets_dir": "assets",
        "temp_dir": "assets/temp",
        "font_path": "assets/fonts/default.ttf"
    },
    "youtube": {
        "chrome_driver_path": "chromedriver.exe"
    },
    "video": {
        "width": 1280,
        "height": 720,
        "fps": 1,
        "frame_duration": 5
    }
}
```

### content.json
```json
[
    {
        "id": "video1",
        "title": "Video Başlığınız",
        "description": "Video açıklama metni",
        "images": [
            "backgrounds/image1.jpg",
            "backgrounds/image2.jpg",
            "backgrounds/image3.jpg"
        ],
        "audio_text": "Sese dönüştürülecek metin"
    }
]
```

## 🎯 Kullanım

1. Chrome'u hata ayıklama modunda başlatın:
```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"
```

> **💡 Not**: Komutu çalıştırmadan önce `C:\selenum\ChromeProfile` dizinini oluşturduğunuzdan emin olun. Bu dizin, YouTube oturum bilgileriniz dahil Chrome profil verilerinizi saklayacaktır.

2. Hata ayıklama Chrome penceresinde YouTube Studio'ya giriş yapın

3. Botu çalıştırın:
```bash
cd src
python main.py
```

Bot şunları yapacaktır:
1. 📖 `content.json` dosyasından içerik öğelerini okur
2. 🎥 Belirtilen görüntüler ve metinlerle videolar oluşturur
3. 🔊 Verilen metinden ses dosyası oluşturur
4. 📤 Videoları belirtilen ayarlarla YouTube'a yükler
5. ✅ Tamamlanan öğeleri `completed.txt` dosyasına kaydeder

## 📦 Dahil Edilen İçerikler

- 🖼️ **Arka Plan Görselleri**: `assets/backgrounds/` içinde 3 örnek arka plan görseli
- 🔤 **Yazı Tipleri**: `assets/fonts/` içinde varsayılan yazı tipi (Bebas Neue)

## 🏗️ Proje Yapısı

- 🎯 `src/main.py`: Ana giriş noktası
- 🎥 `src/video_creator.py`: Video oluşturma ve işleme
- 📤 `src/youtube_uploader.py`: YouTube yükleme otomasyonu
- ⚙️ `src/config_manager.py`: Yapılandırma yönetimi
- 🔧 `src/utils.py`: Yardımcı fonksiyonlar

## ⚠️ Hata Yönetimi

- 📝 Kapsamlı hata günlükleme
- 🧹 Geçici dosyaların otomatik temizlenmesi
- 🔄 Başarısız yükleme yeniden deneme mekanizması
- 📊 `logs/` dizininde detaylı günlük kaydı

## 🤝 Katkıda Bulunma

1. 🔱 Depoyu fork edin
2. 🌿 Özellik dalınızı oluşturun (`git checkout -b özellik/harika-özellik`)
3. ✍️ Değişikliklerinizi commit edin (`git commit -m 'Harika özellik eklendi'`)
4. 🚀 Dalınıza push yapın (`git push origin özellik/harika-özellik`)
5. 🎯 Bir Pull Request açın

## 🙏 Teşekkürler

- 🌐 YouTube otomasyonu için Selenium WebDriver
- 🎬 Video işleme için FFmpeg
- 🗣️ Metinden sese dönüşüm için gTTS
- 🖼️ Görüntü işleme için OpenCV ve Pillow

## 💬 Destek

Destek için lütfen GitHub deposunda bir konu açın veya geliştiricilerle iletişime geçin.

</div> 