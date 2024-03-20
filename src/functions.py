from glob import glob
from os import path, remove, listdir
from shutil import copy
from re import sub
from yt_dlp import YoutubeDL
from mutagen.id3 import ID3, APIC
from PIL import Image

from moviepy.editor import *

def add_cover_image(audio_file, output_file):
    # Load the audio file
    audio = AudioFileClip(audio_file)

    # Create a video clip with the cover image
    cover_clip = ImageClip("./cover.jpg")

    # Set the duration of the cover clip to match the duration of the audio
    cover_clip = cover_clip.set_duration(audio.duration)

    # Set the audio of the cover clip to match the audio file
    cover_clip = cover_clip.set_audio(audio)

    # Write the result to an MP3 file
    cover_clip.audio.write_audiofile(output_file, codec='mp3')

    # Close the clips
    audio.close()
    cover_clip.close()


def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '19F2',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def audio_process(url):
    directory = './'
    pattern = r'\[.*?\]'
    mp3_files = glob(path.join(directory, "*.mp3"))
    try:
        for file in mp3_files:
            preview_download(url)
            preview_cleaner()
            cleaned_name = "./audio" + sub(pattern, '', file)
            add_cover_image(file, cleaned_name)
            # copy(file, cleaned_name)
            # remove(file)
    except Exception as e:
        print(e, "\n\n\n\n!!!\n\n\n\n")


def preview_set(file):
    another = "./cover.jpg"
    matching_files = glob(another)
    with open(matching_files[0], 'rb') as f:
        data = f.read()
        apic = APIC(3, 'image/jpeg', 3, 'Front cover', data=data)
        audio = ID3(file)
        audio.delall('APIC')
        audio.add(apic)
        audio.save()


def preview_cleaner():
    files = listdir("./")
    for file in files:
        if file.startswith("maxresdefault [maxresdefault]") or file.startswith("sddefault [sddefault]"):
            convert_webp_to_jpeg(file)
            if not (path.isfile(file) and file.lower().endswith('.jpg')):
                file_path = path.join("./", file)
                remove(file_path)


def preview_download(url):
    ydl = YoutubeDL()
    info_dict = ydl.extract_info(url, download=False)
    thumbnail_url = info_dict['thumbnail']
    ydl.download([thumbnail_url])


def convert_webp_to_jpeg(webp_path):
    with Image.open(webp_path) as img:
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img.save("cover.jpg", 'JPEG')