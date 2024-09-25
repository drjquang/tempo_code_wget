import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("200x300")
app.attributes("-fullscreen", True)
app.title("Raspberry SQL")

app.mainloop()
