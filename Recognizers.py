import speech_recognition as sr
import Female_Voice
def recognize():
    try:  
        r  =  sr.Recognizer()
        with sr.Microphone() as source:
          Female_Voice.pyttsx3.speak('start saying...')
          audio = r.listen(source)
          Female_Voice.pyttsx3.speak('i got it... please wait..!!')
        global ch
        ch = r.recognize_google(audio)
        ch = ch.lower()
        # print(ch)
        
    except:
        recognize()
