import pyttsx3

Robot_memory= " Xin chào bạn"
def Robot_speak(text) :
        speak = pyttsx3.init()
        voices = speak.getProperty('voice')
        speak.setProperty('voice',voices[3].id)
        print("Robot :"+Robot_memory)
        speak.say(Robot_memory)
        speak.runAndWait()