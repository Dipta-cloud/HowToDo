import pyttsx3
import speech_recognition as sr
import datetime
import pywikihow
from tkinter import *
from PIL import Image,ImageTk
import webbrowser


def onclick():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 180)

    def speak(audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()

    def take_command():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=300, phrase_time_limit=5)

            try:
                print("Recognising.....")
                text = r.recognize_google(audio, language="en-in")
                print(f"User Said {text}")

            except Exception as e:
                # speak("Say That Again Please....")
                return "none"
            return text

    def wish_me():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour <= 12:
            speak("Good morning")
        elif hour >= 12 and hour <= 16:
            speak("Good afternoon")
        else:
            speak("Good evening")
        speak("I am Nolu , Please tell me what you want to know")

    if __name__ == "__main__":
        wish_me()
        while True:
            text = take_command().lower()
            if "hello" in text:
                speak("yes tell me, i will try my best to make you knowledgeable")
                how = take_command()
                max_results = 1
                how_to = pywikihow.search_wikihow(how, max_results)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)
            elif "goodbye" in text:
                speak("bye sir, hope to assist you soon,take care")
                quit()


def onclick2():
    webbrowser.open_new(r'c:\Users\hp\Desktop\My_App\instructions 2.pdf')


root = Tk()
root.title("Desi Tech")
root.geometry('700x500')
load = Image.open('di.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root, image = render)
img.place(x=0, y=0)
img = PhotoImage(file='Desi-Tech.png')
b = Button(root, image = img, bd=0, bg = "#F5F5F5", activebackground = "#F5F5F5" )
b.place(x=150, y=0)
img1 = PhotoImage(file='start.png')
b1 = Button(root, image = img1, bd=0, bg = "#F5F5F5", activebackground = "#F5F5F5", command=onclick )
b1.place(x=522, y=200)
img2 = PhotoImage(file='USER GUIDE.png')
b2 = Button(root, image = img2, bd=0, bg = "#F5F5F5", activebackground = "#F5F5F5", command=onclick2 )
b2.place(x=512, y=300)
img3 = PhotoImage(file='htd.png')
b3 = Button(root, image = img3, bd=0, bg = "#F5F5F5", activebackground = "#F5F5F5" )
b3.place(x=0, y=450)
root.mainloop()

















