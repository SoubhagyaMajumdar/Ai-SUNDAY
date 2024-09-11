import eel
from Engine.command import speak
from Engine.config import ASSISTANT_NAME

def Introduce():
    speak("Hello , I am "+ASSISTANT_NAME+" , an AI language model developed by Team Innovators, designed to assist with a wide range of tasks. Currently, I am under development, so I cannot completely understand your feelings and reply to you, but my creators are trying hard to improve me so that I can be as much friendly and useful as possible.")
    
def HowAreYou():
    speak("I am Great!. Thank you for asking.")
    
def Bye():
    speak("Have a nice day. Good bye")