from glob import glob
from os import path, remove, listdir, makedirs
from shutil import copy
from re import sub, search
from yt_dlp import YoutubeDL
from mutagen.id3 import ID3, APIC
from PIL import Image
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC


async def cover_change(mp3_file_path):
    audio = MP3(mp3_file_path, ID3=ID3)
    audio.tags.add(APIC(encoding=0, mime='image/png', type=1,
                   desc='32x32 icon', data=open('./cover.png', 'rb').read()))
    audio.tags.add(APIC(encoding=0, mime='image/png', type=2,
                   desc='Icon', data=open('./cover.png', 'rb').read()))
    audio.tags.add(APIC(encoding=0, mime='image/png', type=3,
                   desc='Cover (front)', data=open('./cover.png', 'rb').read()))
    audio.tags.add(APIC(encoding=0, mime='image/png', type=4,
                   desc='Cover (back)', data=open('./cover.png', 'rb').read()))
    audio.save()


async def extract_video_id(url):
    pattern = r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([\w-]+)'
    match = search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None


async def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


async def download_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


async def audio_process(url):
    directory = './'
    pattern = r'\[.*?\]'
    mp3_files = glob(path.join(directory, "*.mp3"))
    try:
        for file in mp3_files:
            await preview_download(url)
            await preview_cleaner()
            folder_name = "./media/" + await extract_video_id(url)
            if not path.exists(folder_name):
                makedirs(folder_name)
            cleaned_name = folder_name + sub(pattern, '', file)
            copy(file, cleaned_name)
            await cover_change(cleaned_name)
            remove(file)
            remove("cover.png")
            return cleaned_name
    except Exception as e:
        print(e)


async def preview_set(file):
    another = "./cover.jpg"
    matching_files = glob(another)
    with open(matching_files[0], 'rb') as f:
        data = f.read()
        apic = APIC(3, 'image/jpeg', 3, 'Front cover', data=data)
        audio = ID3(file)
        audio.delall('APIC')
        audio.add(apic)
        audio.save()


async def preview_cleaner():
    files = listdir("./")
    for file in files:
        if file.startswith("maxresdefault [maxresdefault]") or file.startswith("sddefault [sddefault]"):
            await convert_webp_to_png(file)
            file_path = path.join("./", file)
            remove(file_path)


async def preview_download(url):
    ydl = YoutubeDL()
    info_dict = ydl.extract_info(url, download=False)
    thumbnail_url = info_dict['thumbnail']
    ydl.download([thumbnail_url])


async def convert_webp_to_png(webp_path):
    with Image.open(webp_path) as img:
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img.save("cover.png", 'PNG')
