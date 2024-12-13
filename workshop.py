import tkinter as tk  # import the tkinter library for creating GUI applications
from gtts import gTTS  # import the gTTS (Google Text-to-Speech) library
import os  # import the os library for handling file operations (not actually needed in this case)
from playsound import playsound  # import the playsound library to play audio files

# Function to convert text to speech and play it
def text_to_speech():
    text = entry.get()  # Get the text from the text entry box
    if text:  # Check if the text is not empty
        tts = gTTS(text=text, lang='en')  # Create a gTTS object with the input text and set language to English
        tts.save("output.mp3")  # Save the speech output as an MP3 file named "output.mp3"
        playsound("output.mp3")  # Play the saved MP3 file using the playsound library

# Create the main window of the application
root = tk.Tk()
root.title("Text to Speech Converter")  # Set the title of the window

# Add a label to the window 
label = tk.Label(root, text="Enter text to convert to speech:", font=("Arial", 12))  # Create a label with text and font size 
label.pack(pady=10)  

# Add a text entry box where the user can input text
entry = tk.Entry(root, width=60)  # Create a text entry box 
entry.pack(pady=10)  

# Add a "Play" button to trigger the text-to-speech function
play_button = tk.Button(root, text="Play", command=text_to_speech, width=20, height=2)  # Create a button with text "Play", set width and height
play_button.pack(pady=10)  

# Add an "Exit" button to close the application
exit_button = tk.Button(root, text="Exit", command=root.quit, width=20, height=2) 
exit_button.pack(pady=10)  

# Start the Tkinter event loop (this keeps the window running and responsive)s
root.mainloop()
