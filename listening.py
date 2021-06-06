import speech_recognition as sr
def robot_listen():
    listen  = sr.Recognizer()
    with sr.Recognizer() as source :
        print("Adjusting noise")
        listen.adjust_for_ambient_noise(source,duration=1)
        print("Recording  for 4 seconds")
        recorded_audio= listen.listen(source,timeout=4)
        print("Done recording")
        try:
            print("Convert speech to text ")
            your_text = listen.recognize_google(recorded_audio,language="vi")
            print("----Robot convert speech to text : ", your_text)
        except:
            your_text = "Xin lỗi , tôi không nghe rõ "
            print("----Robot : ", your_text)
            return  0