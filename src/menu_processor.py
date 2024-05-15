from os import name
from sys import stdin

from .audio_processor import audio_forming
from .video_processor import download_video


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


def show_menu(dir):
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
            process_link(url, choice, dir)
        except:
            pass


def process_link(url, option, dir):
    if option == "1":
        return audio_forming(url=url, dir=dir)
    elif option == "2":
        return download_video(url=url, dir=dir)
