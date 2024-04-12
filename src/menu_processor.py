from re import search
from os import name
from sys import stdin
from .audio_processor import download_audio, audio_forming
from .video_processor import download_video

class GetChar():
    def win():
        try:
            if name == 'nt':
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
    scan_char.unix


def show_menu():
    while True:
        print(f"{'='*8}\n  Menu\n{'='*8}")
        print(
            f"\033[92m1. Audio\033[0m\n\033[94m2. Video\033[0m\n\033[91me. Exit\033[0m\n")
        print("Choose an option (1/2) = ", end='', flush=True)
        choice = scan_char()
        if choice == 'e':
            print()
            exit()
        if choice not in ['1', '2']:
            print("\nInvalid choice. Please choose again.")
            continue
        print(choice)
        link = input("Link = ")
        mode = "Audio" if choice == '1' else "Video"
        try:
            process_link(link, mode)
        except:
            pass

def process_link(link, option):
    if option == "Audio":
        download_audio(link)
        audio_name = audio_forming(link)
        return audio_name
    elif option == "Video":
        download_video(link)

