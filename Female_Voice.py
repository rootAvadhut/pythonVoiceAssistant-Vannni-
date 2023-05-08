# import Modules
import pyttsx3

engine =   pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
global voice
voice = engine.setProperty('voice', voices[1].id)


