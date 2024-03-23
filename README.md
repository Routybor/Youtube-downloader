**Project Name: YouTube-to-MP3-with-Cover**

**Description:**
This Python project allows users to convert YouTube videos into MP3 audio files while also embedding the video's cover image into the audio file. It utilizes the YouTube API for fetching video metadata and ffmpeg for audio extraction and cover embedding.

**Installation:**
1. Clone the repository:
   ```
   git clone https://github.com/your_username/YouTube-to-MP3-with-Cover.git
   ```
2. Navigate to the project directory:
   ```
   cd YouTube-to-MP3-with-Cover
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
1. Run the Python script `youtube_to_mp3_with_cover.py`:
   ```
   python youtube_to_mp3_with_cover.py
   ```
2. Enter the YouTube video link when prompted.
3. The script will download the video, extract its audio, fetch its cover image, and embed the cover image into the MP3 audio file.
4. The MP3 file with the cover image embedded will be saved in the project directory.

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
