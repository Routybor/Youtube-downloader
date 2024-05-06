from os import name
from sys import stdin
from glob import glob
from os import path, remove, listdir, makedirs
from shutil import copy
from re import sub, compile
from yt_dlp import YoutubeDL
from mutagen.id3 import ID3, APIC
from PIL import Image
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
from yt_dlp import YoutubeDL


def download_video(url):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def audio_forming(url):
    download_audio(url)
    directory = "./"
    pattern = r"\[.*?\]"
    mp3_files = glob(path.join(directory, "*.mp3"))
    try:
        for file in mp3_files:
            preview_forming(url)
            folder_name = "./Music/"
            if not path.exists(folder_name):
                makedirs(folder_name)
            cleaned_name = folder_name + sub(pattern, "", file)
            copy(file, cleaned_name)
            cover_set(cleaned_name)
            remove(file)
            remove("cover.png")
            return cleaned_name
    except Exception as e:
        print(e)


def preview_set(file):
    another = "./cover.jpg"
    matching_files = glob(another)
    with open(matching_files[0], "rb") as f:
        data = f.read()
        apic = APIC(3, "image/jpeg", 3, "Front cover", data=data)
        audio = ID3(file)
        audio.delall("APIC")
        audio.add(apic)
        audio.save()


def preview_forming(url):
    preview_download(url)
    files = listdir("./")
    for file in files:
        if file.startswith("maxresdefault [maxresdefault]") or file.startswith(
            "sddefault [sddefault]"
        ):
            webp_to_png(file)
            file_path = path.join("./", file)
            remove(file_path)


def preview_download(url):
    ydl = YoutubeDL()
    info_dict = ydl.extract_info(url, download=False)
    thumbnail_url = info_dict["thumbnail"]
    ydl.download([thumbnail_url])


def webp_to_png(webp_path):
    with Image.open(webp_path) as img:
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.save("cover.png", "PNG")


def cover_set(mp3_file_path):
    audio = MP3(mp3_file_path, ID3=ID3)
    cover = open("./cover.png", "rb").read()
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
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([extract_video_id(url)])


def extract_video_id(url):
    regex = compile(
        r'(?:youtu\.be\/|youtube\.com(?:\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=|shorts\/)|youtu\.be\/|embed\/|v\/|m\/|watch\?(?:[^=]+=[^&]+&)*?v=))([^"&?\/\s]{11})'
    )
    match = regex.search(url)
    if match:
        return match.group(1)
    else:
        return None


class GetChar:
    def win():
        try:
            if name == "nt":
                return msvcrt.getch().decode()
        except Exception as e:
            print(e)
        return None

    def unix():
        fd = stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = stdin.read(1)
        except Exception as e:
            print(e)
            return None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


scan_char = None
try:
    import msvcrt

    scan_char = GetChar.win

except ImportError:
    import termios
    import tty

    scan_char = GetChar.unix


def show_menu():
    while True:
        print(f"{'='*8}\n  Menu\n{'='*8}")
        print(
            f"\033[92m1. Audio\033[0m\n\033[94m2. Video\033[0m\n\033[91me. Exit\033[0m\n"
        )
        print("Choose an option (1/2) = ", end="", flush=True)
        choice = scan_char()
        if choice == "e":
            print()
            exit()
        if choice not in ["1", "2"]:
            print("\nInvalid choice. Please choose again.")
            continue
        print(choice)
        url = input("Link = ")
        try:
            process_link(url, choice)
        except:
            pass


def process_link(url, option):
    if option == "1":
        return audio_forming(url)
    elif option == "2":
        return download_video(url)


def main():
    show_menu()


if __name__ == "__main__":
    main()
