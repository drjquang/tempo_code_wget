# from read_sql import read_latest_record

import customtkinter as ctk
import threading
import time
import random


class CounterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Guest information")
        self.geometry("300x400")

        # Initializing the counter variable
        self.counter = 0
        self.running = False  # Flag to control the thread

        self.guest_info = {
            "Guest ID:": "999-9999-999",
            "Guest Name:": "Itachi Uchiha",
            "Total Points:": 12000,
            "Current Points:": 100
        }

        # -------------------------------------------------------------------------------------------------------------

        # Creating a label to display the number
        self.label = ctk.CTkLabel(self, text=f"{self.counter}", font=("Arial", 30))
        self.label.pack(pady=20)

        # Creating a progress bar widget
        self.progress_bar = ctk.CTkProgressBar(self, width=200, height=20)
        self.progress_bar.set(0)  # Set initial value to 0
        self.progress_bar.pack(pady=20)

        # Creating the start/stop button
        self.toggle_button = ctk.CTkButton(self, text="Start", command=self.toggle_counter)
        self.toggle_button.pack(pady=20)

        # Creating a frame to contain guest information
        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Loop through guest_info dictionary to add labels
        for idx, (label_text, value_text) in enumerate(self.guest_info.items()):
            # Create left-aligned labels for categories
            label = ctk.CTkLabel(frame, text=label_text, anchor="w")
            label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")

            # Create right-aligned labels for values
            value = ctk.CTkLabel(frame, text=str(value_text), anchor="e")
            value.grid(row=idx, column=1, padx=10, pady=5, sticky="e")

            # Save the reference for the "Current Points" label to update it later
            if label_text == "Current Points:":
                global label_current_points_value
                label_current_points_value = value
                label_current_points_value.configure(text_color="red")

    def update_label_and_progress(self):
        # Updating the label text in a thread-safe manner
        self.label.configure(text=f"{self.counter}")

        # Calculating the progress bar value (0.0 to 1.0)
        progress_value = self.counter / 99
        self.progress_bar.set(progress_value)



    def update_counter(self):
        while self.running:
            time.sleep(0.1)
            if self.counter == 100:
                self.counter = 0
                # ------------------------------------------------------------------------------------------------------
                # latest_record = read_latest_record()
                # print(latest_record)
                new_value = random.randint(1, 1000)  # Generate random number between 1 and 1000
                label_current_points_value.configure(text=str(new_value))  # Update the label
                # ------------------------------------------------------------------------------------------------------
            self.counter = (self.counter + 1)
            self.after(0, self.update_label_and_progress)

    def toggle_counter(self):
        if not self.running:
            # Start the counter thread
            self.running = True
            self.counter_thread = threading.Thread(target=self.update_counter)
            self.counter_thread.daemon = True
            self.counter_thread.start()
            self.toggle_button.configure(text="Stop")
        else:
            # Stop the counter thread
            self.running = False
            self.toggle_button.configure(text="Start")


# Create and run the application
if __name__ == "__main__":
    ctk.set_appearance_mode("light")  # Optional: light or dark mode
    app = CounterApp()
    app.mainloop()
