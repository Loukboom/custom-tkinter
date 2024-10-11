import customtkinter
import webbrowser

customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("400x300") # here you can resize to watever you want

def button_event():
    webbrowser.open("https://discord.gg/swHVUU5hGb")  # Replace with your desired URL !

button = customtkinter.CTkButton(app, text="Open Webpage", command=button_event)
button.pack(pady=90)  # Add some padding and pack the button into the window

app.mainloop()