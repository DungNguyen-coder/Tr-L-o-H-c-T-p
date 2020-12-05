from mypackage.library import*

def hear():
    print("Trợ lý P&P: đang nghe....")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit = 8)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text.lower()
        except:
            print("...")
            return 0

def speak(text):
    print("Trợ lý P&P: {}".format(text))
    tts = gTTS(text= text, lang= "vi", slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", True)
    os.remove("sound.mp3")



