from src.functions import process_link, getch


def main():
    while True:
        print(f"{'='*8}\n  Menu\n{'='*8}")
        print(
            f"\033[92m1. Audio\033[0m\n\033[94m2. Video\033[0m\n\033[91me. Exit\033[0m\n")
        print("Choose an option (1/2) = ", end='', flush=True)
        choice = getch()
        if choice == 'e':
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


if __name__ == "__main__":
    main()
