# use and external module and perform an operation of your interest
# pyttsx3 is text to speech module
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()