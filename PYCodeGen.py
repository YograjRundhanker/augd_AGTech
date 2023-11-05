import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import re

# Initialize the Tkinter GUI
app = tk.Tk()
app.title("AI Code Generator")
app.geometry("800x400")

# Define a blue color theme
app.style = ttk.Style()
app.style.theme_use("clam")

# Function to generate code
def generate_code():
    input_text = input_text_box.get("1.0", "end-1c")
    
    # Remove comments from code using regular expressions
    code_without_comments = re.sub(r'#.*', '', input_text)
    
    output_text_box.delete("1.0", "end")
    output_text_box.insert("1.0", code_without_comments)

# Function to convert audio to text
def convert_audio_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        audio_text = r.recognize_google(audio)
        input_text_box.delete("1.0", "end")
        input_text_box.insert("1.0", audio_text)
    except sr.UnknownValueError:
        input_text_box.delete("1.0", "end")
        input_text_box.insert("1.0", "Could not understand the audio input")

# Create input text box
input_text_box = tk.Text(app, height=10, width=40)
input_text_box.pack(pady=10)

# Create output text box
output_text_box = tk.Text(app, height=10, width=40)
output_text_box.pack(pady=10)

# Create buttons
generate_button = ttk.Button(app, text="Generate Code", command=generate_code)
generate_button.pack()

audio_to_text_button = ttk.Button(app, text="Audio to Text", command=convert_audio_to_text)
audio_to_text_button.pack()

# Start the GUI
app.mainloop()
