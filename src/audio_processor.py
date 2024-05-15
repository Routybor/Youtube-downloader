from glob import glob
from os import path, remove, listdir, makedirs
from shutil import copy
from re import sub, compile
from yt_dlp import YoutubeDL
from mutagen.id3 import ID3, APIC
from PIL import Image
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC


def audio_forming(url, dir):
    download_audio(url=url)
    directory = "./"
    pattern = r"\[.*?\]"
    mp3_files = glob(pathname=path.join(directory, "*.mp3"))
    try:
        for file in mp3_files:
            preview_forming(url=url)
            folder_name = dir + "\\" +  extract_video_id(url=url)
            if not path.exists(path=folder_name):
                makedirs(name=folder_name)
            cleaned_name = folder_name + sub(pattern=pattern, repl="", string=file)
            copy(src=file, dst=cleaned_name)
            cover_set(mp3_file_path=cleaned_name)
            remove(path=file)
            remove(path="cover.png")
            return cleaned_name
    except Exception as e:
        print(e)


def preview_set(file):
    another = "./cover.jpg"
    matching_files = glob(pathname=another)
    with open(file=matching_files[0], mode="rb") as f:
        data = f.read()
        apic = APIC(3, "image/jpeg", 3, "Front cover", data=data)
        audio = ID3(file)
        audio.delall(key="APIC")
        audio.add(frame=apic)
        audio.save()


def preview_forming(url):
    preview_download(url=url)
    files = listdir(path="./")
    for file in files:
        if file.startswith("maxresdefault [maxresdefault]") or file.startswith(
            "sddefault [sddefault]"
        ):
            webp_to_png(webp_path=file)
            file_path = path.join("./", file)
            remove(path=file_path)


def preview_download(url):
    ydl = YoutubeDL()
    info_dict = ydl.extract_info(url, download=False)
    thumbnail_url = info_dict["thumbnail"]
    ydl.download(url_list=[thumbnail_url])


def webp_to_png(webp_path):
    with Image.open(fp=webp_path) as img:
        if img.mode != "RGB":
            img = img.convert(mode="RGB")
        img.save(fp="cover.png", format="PNG")


def cover_set(mp3_file_path):
    audio = MP3(mp3_file_path, ID3=ID3)
    cover = open(file="./cover.png", mode="rb").read()
    mtype = "image/png"
    audio.tags.add(APIC(encoding=0, mime=mtype, type=1, desc="32x32 icon", data=cover))
    audio.tags.add(APIC(encoding=0, mime=mtype, type=2, desc="Icon", data=cover))
    audio.tags.add(
        APIC(encoding=0, mime=mtype, type=3, desc="Cover (front)", data=cover)
    )
    audio.tags.add(
        APIC(encoding=0, mime=mtype, type=4, desc="Cover (back)", data=cover)
    )
    audio.save()


def download_audio(url):
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with YoutubeDL(params=ydl_opts) as ydl:
        ydl.download(url_list=[extract_video_id(url=url)])


def extract_video_id(url):
    regex = compile(
        pattern=r'(?:youtu\.be\/|youtube\.com(?:\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=|shorts\/)|youtu\.be\/|embed\/|v\/|m\/|watch\?(?:[^=]+=[^&]+&)*?v=))([^"&?\/\s]{11})'
    )
    match = regex.search(string=url)
    if match:
        return match.group(1)
    else:
        return None
