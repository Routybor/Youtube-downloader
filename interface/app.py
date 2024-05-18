from src.audio_processor import audio_forming
import customtkinter
import threading

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Youtube download")
        self.geometry(f"{500}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure((0, 3), weight=1)
        self.grid_columnconfigure((1, 2), weight=0)

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Link")
        self.entry.grid(row=0, columnspan=4, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.combobox_1 = customtkinter.CTkComboBox(
            master=self,
            values=["Audio", "Video"],
            command=self.combobox_selection_changed  # Add command to combobox
        )
        self.combobox_1.grid(column=1, padx=20, pady=(5, 20))
        self.main_button_1 = customtkinter.CTkButton(
            master=self,
            text="Submit",
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            command=self.print_entry_text,  # Set the button command
        )
        self.main_button_1.grid(
            padx=(20, 20), pady=(5, 20), sticky="nsew", column=2, row=1
        )

        # Create the second button but do not display it yet
        self.second_button = customtkinter.CTkButton(
            master=self,
            text="Second Button",
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            command=self.second_button_action,
        )

        # Create a label for loading message
        self.loading_label = customtkinter.CTkLabel(
            master=self,
            text="",
            fg_color="transparent",
            text_color=("gray10", "#DCE4EE"),
        )
        self.loading_label.grid(row=2, columnspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.entry.bind("<Return>", self.print_entry_text)

    def print_entry_text(self, event=None):
        entry_text = self.entry.get()
        combobox_value = self.combobox_1.get()
        if combobox_value == "Audio":
            self.start_audio_forming_thread(entry_text)
        print(f"Entry: {entry_text}, Combobox: {combobox_value}")

    def start_audio_forming_thread(self, entry_text):
        self.loading_label.configure(text="Loading...")
        threading.Thread(target=self.run_audio_forming, args=(entry_text,)).start()

    def run_audio_forming(self, entry_text):
        audio_forming(url=entry_text, dir="./")
        self.loading_label.configure(text="Finished")

    def combobox_selection_changed(self, event=None):
        if self.combobox_1.get() == "Video":
            self.show_second_button()
        else:
            self.hide_second_button()

    def show_second_button(self):
        self.second_button.grid(
            row=3, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew"
        )

    def hide_second_button(self):
        self.second_button.grid_forget()

    def second_button_action(self):
        print("Second button pressed")


if __name__ == "__main__":
    app = App()
    app.mainloop()
