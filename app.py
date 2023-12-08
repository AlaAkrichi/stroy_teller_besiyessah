import tkinter as tk
from storyMaker import makeStory
import os
import playsound
import threading
from gtts import gTTS # google text to speech
def generate_story():
    # Get the user input from the entry widget
    prompt = prompt_entry.get(1.0, tk.END)

    # Generate the story using the makeStory function
    story = makeStory(prompt)

    # Display the generated story in the text widget
    output_text.delete(1.0, tk.END)  # Clear existing text
    output_text.insert(tk.END, story)

def speak_story():
    text=output_text.get(1.0, tk.END)
    toSpeak = gTTS(text = text, lang ='en', slow = False)
    # saving the audio file given by google text to speech
    file = "stroy.mp3"
    toSpeak.save(file)
     
    # playsound package is used to play the same file.
    threading.Thread(target=playsound.playsound, args=(file,True)).start()

app = tk.Tk()

app.title("Story Generator")
prompt_label = tk.Label(app, text="what the story is about ?",font=("Helvetica", 16))
prompt_entry = tk.Text(app, wrap=tk.WORD, width=60, height=5)
generate_button = tk.Button(app, text="Generate Story", command=generate_story)
output_text = tk.Text(app)
# Pack widgets
prompt_label.pack(padx=10,pady=10)
prompt_entry.pack(padx=10,pady=10)
generate_button.pack(padx=10,pady=10)
output_text.pack(padx=10,pady=10)
playerfarame=tk.Frame(app)
playerfarame.pack(padx=10,pady=10)
playerfarame.columnconfigure(0, weight=1)
playerfarame.columnconfigure(1, weight=1)
playerfarame.columnconfigure(2, weight=1)

speaker_button = tk.Button(playerfarame, text="Speak Story",command=speak_story)
speaker_button.grid(row=0, column=0)
# Start the application loop
app.mainloop()