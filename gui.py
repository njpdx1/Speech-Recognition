import tkinter as tk
import search
from PIL import Image, ImageTk

def search_wikipedia():
    text = search.speech_to_text()
    if text == "exit":
        root.quit()    
    search.wiki_query(text)

def toggle_glowing():
    current_state = search_button.cget("image")
    if current_state == mic_icon:
        search_button.config(image=mic_glow_icon)
    else:
        search_button.config(image=mic_icon)
    root.after(500, toggle_glowing)
def stop_glowing():
    root.after_cancel(toggle_glowing)
root = tk.Tk()
root.title("Speech")
#Window Size
root.geometry("700x700")

input_label = tk.Label(root, text="Speak and click Search:")
input_label.pack()

# Load the microphone icon and glowing microphone icon
mic_image = Image.open("Assests/microphone.png")  
mic_image = mic_image.resize((50, 50))
mic_icon = ImageTk.PhotoImage(mic_image)
red_mic = Image.open("Assests/red_microphone.jpg")  
red_mic = red_mic.resize((50, 50))
mic_glow_icon = ImageTk.PhotoImage(red_mic)

search_button = tk.Button(root, image=mic_icon, command=search_wikipedia, compound=tk.LEFT)
search_button.pack()

toggle_glowing() # Start the animation

root.mainloop()
