import customtkinter as ctk
import threading
import time

class CounterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Counter GUI with Progress Bar and Start/Stop Button")
        self.geometry("300x300")

        # Initializing the counter variable
        self.counter = 0
        self.running = False  # Flag to control the thread

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

    def update_label_and_progress(self):
        # Updating the label text in a thread-safe manner
        self.label.configure(text=f"{self.counter}")

        # Calculating the progress bar value (0.0 to 1.0)
        progress_value = self.counter / 99
        self.progress_bar.set(progress_value)

    def update_counter(self):
        while self.running:
            time.sleep(0.1)
            self.counter = (self.counter + 1) % 100
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
