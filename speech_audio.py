#import library

import speech_recognition as sr
import pyttsx3

# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable

while(1):

    try:
        with sr.Microphone() as source:
            # read the audio data from the default microphone
            print("Start Speaking...")
            audio_data = r.record(source, duration=4)
            print("Recognizing...")
            # convert speech to text
            text = r.recognize_google(audio_data)
            print(text)
            SpeakText(text)
        

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occured")

