from mypackage.library import*
from mypackage.speak_hear import speak, hear

def open_application(text):  #phần này anh thấy nên bỏ tại mỗi laptop sẽ có 1 path tới các app khác nhau dễ sinh ra lôi 
    if "google" in text:
        speak("Mở Google Chrome")
        os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    elif "word" in text:
        speak("Mở Microsoft Word")
        os.startfile("C:\\Users\\MS BEN\\Desktop\\Word 2016.lnk")
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        os.startfile("C:\\Users\\MS BEN\\Desktop\\Excel 2016.lnk")
    elif "cốc cốc" in text:
        speak("Mở cốc cốc")
        os.startfile("C:\\Users\\MS BEN\\AppData\\Local\\CocCoc\\Browser\\Application\\browser.exe")
    elif "zalo" in text:
        speak("Mở zalo")
        os.startfile("C:\\Users\\MS BEN\\Desktop\\Zalo.lnk")
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")