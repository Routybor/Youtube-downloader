from os import name
from sys import stdin
from typing import NoReturn

from .audio_processor import audio_forming
from .video_processor import download_video


class GetChar:
    def win() -> str | None:
        """
        Scans chars from input in WIN systems

        Returns:
            str | None: scanned char
        """
        try:
            if name == "nt":
                return msvcrt.getch().decode()
        except Exception as e:
            print(e)
        return None

    def unix() -> str | None:
        """
        Scans chars from input in UNIX systems

        Returns:
            str | None: scanned char
        """

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


# ? It's essential to define user's system to scan chars from input to use different scan methods for different systems.
scan_char = None
try:
    import msvcrt

    scan_char = GetChar.win

except ImportError:
    import termios
    import tty

    scan_char = GetChar.unix


def show_menu(dir: str) -> None:
    """
    Shows menu in terminal and processes user's choice

    Args:
        dir (str): config dir to download file into
    """
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
            process_link(url=url, option=choice, dir=dir)
        except Exception as e:
            print(e)


def process_link(url: str, option: str, dir: str) -> None:
    """
    Defines programs work mode (video/audio)

    Args:
        url (str): video url
        option (str): chose mode
        dir (str): config dir to download file into`
    """
    if option == "1":
        audio_forming(url=url, dir=dir)
    elif option == "2":
        download_video(url=url, dir=dir)
