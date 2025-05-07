
# 🤖 Cadd: A Python-Based Virtual Voice Assistant

Cadd is a personal voice assistant built using Python that can listen to your voice commands and respond intelligently. It supports a wide range of functionalities—from playing songs on YouTube, telling jokes, fetching the latest news, to taking pictures and opening system applications like Notepad, Camera, or Calculator.

---

### 🚀 Features

- 🎤 **Voice Recognition** using `speech_recognition`
- 🗣️ **Text-to-Speech Interaction** with `pyttsx3`
- 📷 **Capture Photos** using `OpenCV`
- 📰 **Get Live News Headlines** via NewsAPI
- 🎵 **Play YouTube Songs** with `pywhatkit`
- 📚 **Wikipedia Summary** for quick info lookups
- 📬 **Open Gmail, YouTube, and Web Browser**
- 🌡️ **Real-time Weather/Temperature** updates
- 🤣 **Tell Random Jokes**
- ⏰ **Time Queries and Greeting System**
- 🖼️ **Open Recently Captured Images**
- 🧠 **Personalized Greetings Based on Time of Day**
- 👨‍💻 **Launch System Apps** like CMD, Calculator, Notepad, OneNote, WhatsApp

---

### ⚙️ Tech Stack

- Python 3.x  
- Libraries:
  - `speech_recognition`
  - `pyttsx3`
  - `pywhatkit`
  - `datetime`, `os`, `sys`, `subprocess`
  - `wikipedia`
  - `pyjokes`
  - `requests` + `BeautifulSoup`
  - `opencv-python` (`cv2`)
  - `webbrowser`

---

### 💡 How to Use

1. **Clone this repo**
   ```bash
   git clone https://github.com/your-username/cadd-virtual-assistant.git
   cd cadd-virtual-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the assistant**
   ```bash
   python cadd.py
   ```

4. 🎙️ **Speak to interact!**
   Say things like:
   - `"play Shape of You"`
   - `"what's the time?"`
   - `"tell me a joke"`
   - `"open notepad"`
   - `"temperature in Noida"`
   - `"take a picture"`

---

### 📌 Prerequisites

- Microphone access is required
- Internet connection for YouTube, Wikipedia, and News
- Camera access for OpenCV features
- Windows OS (some system commands are Windows-specific)

---

### 📦 Future Improvements

- 📋 Add a to-do list feature
- ⏰ Implement alarm setting functionality
- 🌦️ Get weather info for any global location
- 📧 Enable sending emails via voice
- 🌍 Search for and navigate to any location on maps
- 🧮 Support basic arithmetic operations

---

### 👨‍💻 Author

**Vicky Mahajan**  
Python Developer | MERN Stack | AI Enthusiast  
[LinkedIn](https://www.linkedin.com/in/vickymahajan-s55/) • [GitHub](https://github.com/VickyMahajanGitHub)
