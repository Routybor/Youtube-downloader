from src.menu_processor import show_menu
from os import path
from json import load, dump

CONFIG_FILE = "./CONFIG.json"


def load_config():
    if path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            config = load(file)
    else:
        config = {}
    return config


def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        dump(config, file, indent=4)


def get_basedir():
    config = load_config()
    basedir = config.get("BASEDIR")
    if not basedir:
        basedir = input("Enter the BASEDIR: ").strip()
        if basedir:
            config["BASEDIR"] = basedir
            save_config(config)
        else:
            print("BASEDIR cannot be empty. Please provide a valid directory.")
            return get_basedir()

    return basedir


def main():
    download_directory = get_basedir()
    show_menu(dir=download_directory)


if __name__ == "__main__":
    main()
