from glob import glob
from os import path, remove, listdir, makedirs
from shutil import copy
from re import sub, compile
from yt_dlp import YoutubeDL
from mutagen.id3 import ID3, APIC
from PIL import Image
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC


def audio_forming(url: str, dir: str) -> str:
    """
    Downloads audio from youtube and forms audio preview

    Args:
        url (str): video url
        dir (str): base directory to download video

    Returns:
        str: cleaned name of audio file
    """
    download_audio(url=url)
    directory = "./"
    pattern = r"\[.*?\]"
    mp3_files = glob(pathname=path.join(directory, "*.mp3"))
    try:
        for file in mp3_files:
            preview_forming(url=url)
            folder_name = dir + "\\" + extract_video_id(url=url)
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


def preview_forming(url: str) -> None:
    """
    Genetas suitable preview image file to set on mp3 track

    Args:
        url (str): video url
    """
    preview_download(url=url)
    files = listdir(path="./")
    for file in files:
        if file.startswith("maxresdefault [maxresdefault]") or file.startswith(
            "sddefault [sddefault]"
        ):
            webp_to_png(webp_path=file)
            file_path = path.join("./", file)
            remove(path=file_path)


def preview_download(url: str) -> None:
    """
    Downloads preview from youtube

    Args:
        url (str): video url
    """
    ydl = YoutubeDL()
    info_dict = ydl.extract_info(url=url, download=False)
    thumbnail_url = info_dict["thumbnail"]
    ydl.download(url_list=[thumbnail_url])


def webp_to_png(webp_path: str) -> None:
    """
    Converts webp image to png

    Args:
        webp_path (str): path of downloaded preview
    """
    with Image.open(fp=webp_path) as img:
        if img.mode != "RGB":
            img = img.convert(mode="RGB")
        img.save(fp="cover.png", format="PNG")


def cover_set(mp3_file_path: str) -> None:
    """
    Adds png cover to mp3 track

    Args:
        mp3_file_path (str): path of downloaded mp3 file
    """
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


def download_audio(url: str) -> None:
    """
    Downloads audio from youtube

    Args:
        url (str): video url
    """
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


def extract_video_id(url: str) -> str | None:
    """
    Use patterns to remove excess information from link

    Args:
        url (str): "dirty" video link (may be clean)

    Returns:
        str | None: cleaned video link(url)
    """
    regex = compile(
        pattern=r'(?:youtu\.be\/|youtube\.com(?:\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=|shorts\/)|youtu\.be\/|embed\/|v\/|m\/|watch\?(?:[^=]+=[^&]+&)*?v=))([^"&?\/\s]{11})'
    )
    match = regex.search(string=url)
    if match:
        return match.group(1)
    else:
        return None
