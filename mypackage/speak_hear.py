from mypackage.library import*

class do_hoa:
    tro_ly = ""
    hoc_sinh = ""

dohoa1 = do_hoa()

from tkinter import *
from PIL import Image, ImageTk
from threading import Thread
# đồ họa

root = Tk()
root.title("TRỢ LÝ ẢO HỌC TẬP")
root.geometry("900x830")
root.iconbitmap("data_dohoa\\logo.ico")

load = Image.open("data_dohoa\\background.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image = render)
img.place(x = 0, y = 0)

name = Label(root, text = "TRỢ LÝ ẢO HỌC TẬP", fg = '#FFFFFF', bd = 0, bg = "#03152D")
name.config(font = ("Transformers Movie", 35))
name.pack(pady = 10)

# box 1
name1 = Label(root, text = "NGƯỜI DÙNG", fg = '#FFFFFF', bd = 0, bg = "#03152D")
name1.config(font = ("Transformers Movie", 20))
name1.pack(pady = 30)

box1 = Text(root, width = 48, height = 8, font = ("ROBOTO", 16))
box1.pack(pady = 0)


name2 = Label(root, text = "TRỢ LÝ ẢO", fg = '#FFFFFF', bd = 0, bg = "#03153D")
name2.config(font = ("Transformers Movie", 20))
name2.pack(pady = 30)

box2 = Text(root, width = 48, height = 8, font = ("ROBOTO", 16))
box2.pack(pady = 0)


def box1_hear(text):
    box1.delete(1.0, END)
    box1.insert(END, text)
def box2_speak(text):
    box2.delete(1.0, END)
    box2.insert(END, text)

#đồ họa

def hear():
    print("Trợ lý P&P: đang nghe....")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit = 3)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            dohoa1.hoc_sinh = text
            box1_hear(text)
            return text.lower()
        except:
            print("...")
            return 0

def speak(text):
    dohoa1.tro_ly = text
    box2_speak(text)
    print("Trợ lý P&P: {}".format(dohoa1.tro_ly))
    tts = gTTS(text= text, lang= "vi", slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", True)
    os.remove("sound.mp3")



