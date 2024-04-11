**Project Name: YouTube-Downloader**

**Description:**
This Python project allows download YouTube videos and MP3 audio from video and also set audio cover image from video preview frame.

**Installation:**
1. Clone the repository:
   ```
   git clone https://github.com/Routybor/Youtube-downloader.git
   ```
2. Navigate to the project directory:
   ```
   cd YouTube-downloader
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
4. Install ffmpeg:
   - **Windows:** Download ffmpeg from [ffmpeg.org](https://ffmpeg.org/download.html) and add its bin directory to your system's PATH.
   - **MacOS:** Install ffmpeg using Homebrew:
     ```
     brew install ffmpeg
     ```
   - **Linux (Ubuntu/Debian):**
     ```
     sudo apt update
     sudo apt install ffmpeg
     ```

**Usage:**
1. Run the Python script `main.py`:
   ```
   python main.py
   ```
2. Enter the YouTube video link when prompted.
3. The script will download the video, extract its audio, fetch its cover image, and embed the cover image into the MP3 audio file.
4. The MP3 file with the cover image embedded will be saved in the media/ directory.

**Requirements:**
- Python 3.x
- ffmpeg
- Required Python packages (specified in `requirements.txt`)

**Contributing:**
Contributions are welcome! If you want to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request.

**License:**
This project is licensed under the MIT License. See the `LICENSE` file for details.

**Disclaimer:**
This project is intended for personal use only. Respect copyright laws and terms of service of YouTube when using this tool. The developers of this project are not responsible for any misuse of this tool.
