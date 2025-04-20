#listens to whatever u say on specified mic 

import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone(device_index=3)#device index=3 is for airdopes 141
with mic as source:
    print("Say something...") 
    audio = recognizer.listen(source)

    try:
        #use Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
   
