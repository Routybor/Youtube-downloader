from glob import glob
from os import path, remove, listdir
from shutil import copy
from re import sub
from yt_dlp import YoutubeDL
from mutagen.id3 import ID3, APIC


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
    for file in mp3_files:
        cleaned_name = "Music/" + sub(pattern, '', file)
        copy(file, cleaned_name)
        try:
            preview_download(url)
            preview_set(file)
            preview_cleaner()
        except:
            pass
        remove(file)


def preview_set(file):
    another = "./maxresdefault*"
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
            file_path = path.join("./", file)
            remove(file_path)


def preview_download(url):
    ydl = YoutubeDL()
    info_dict = ydl.extract_info(url, download=False)
    thumbnail_url = info_dict['thumbnail']
    ydl.download([thumbnail_url])


yt_url = str(input("Video link = "))
request = int(input("Audio/Video => 1/2 = "))
if request == 1:
    download_audio(yt_url)
    audio_process(yt_url)
elif request == 2:
    download_video(yt_url)