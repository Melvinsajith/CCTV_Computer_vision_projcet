# 📹 CCTV Computer Vision System with Telegram Alerts

This is a Python-based CCTV surveillance system that uses **OpenCV** to detect faces and bodies in real-time and **sends Telegram alerts** with images when someone is detected. It also records video clips of the detected events and logs them with timestamps.

---

## 🚀 Features

- 👤 Real-time **face and full-body detection** using Haar Cascade classifiers.
- 🎥 **Automatic recording** triggered on detection.
- ⏱ Continues recording for a few seconds **after** motion stops (customizable).
- 📸 Saves **snapshot images** of intruders.
- 📤 Sends **Telegram messages and images** to a group or user.
- 🗂 Logs all events in a text file, organized by date.

---

## 🛠 Requirements

- Python 3.x
- Webcam (USB or built-in)
- Telegram Bot token and chat ID

---

## 📦 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/cctv-computer-vision.git
   cd cctv-computer-vision

Install dependencies

pip install -r requirements.txt

Edit the script

    Replace the bot token and chat_id in the script (cctv_main.py) with your own:

    bot = telegram.Bot(token='YOUR_BOT_TOKEN')
    chat_id = 'YOUR_CHAT_ID'

Create necessary folders

    mkdir -p /home/nano/python_3IA/cctv_videos
    mkdir -p /home/nano/python_3IA/cctv_vid

🧠 How It Works

    The webcam feed is processed frame by frame.

    Face and full-body detection is performed using Haar cascades.

    If detection occurs:

        A message and snapshot are sent to a Telegram chat.

        A screenshot is saved locally.

        A video file starts recording.

    Recording continues until no detection is observed for 10 seconds.

    A .txt log file is updated with each event.

🗂 File Structure

cctv-computer-vision/
├── cctv_main.py               # Main Python script
├── requirements.txt           # Dependency list
├── README.md                  # This file
├── /cctv_videos/              # Auto-created directory for video recordings
├── /cctv_vid/                 # Auto-created directory for image snapshots
├── YYYY-MM-DDcctv_system.txt  # Daily log files (auto-generated)

📷 Telegram Alert Sample

Message:

Person detected in 23-04-2025-----14-23-11

Image:

    Automatically captured and sent via the Telegram bot.

🧪 Future Enhancements

    ✅ Motion detection using frame differencing

    ✅ Object tracking for movement prediction

    ✅ GUI interface for live view and controls

    ✅ Email or cloud storage integration

    ✅ Support for multiple cameras

