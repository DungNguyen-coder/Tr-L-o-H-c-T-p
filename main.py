from mypackage.speak_hear import*
from mypackage.open_app import*
from mypackage.open_browser import*
from mypackage.other_funtion import*
from mypackage.excel_funtion import*

'''
speak("Xin chào, bạn tên là gì nhỉ?")
name = hear()
  '''  
name = True
if name:
    speak("Chào bạn {}".format(name))

    speak("Bạn cần Trợ lý P&P có thể giúp gì ạ?")

    while True:
        text = hear()
        if not text:
            speak("mình không nghe rõ bạn nói lại được không")
        elif "dừng" in text or "tạm biệt" in text or "chào bạn" in text or "ngủ thôi" in text:
            stop()
            break
        elif "có thể làm gì" in text:
            help_me()
        elif "chào" in text:
            hello(name)
        elif "giờ" in text or "ngày" in text:
            get_time(text)
        elif 'mở google và tìm kiếm' in text:
            open_google_and_search(text)
        elif "mở " in text:
            open_website(text)
        elif "ứng dụng" in text:
            speak("Tên ứng dụng bạn muốn mở là ")
            text1 = hear()
            open_application(text1)
        #elif "email" in text or "mail" in text or "gmail" in text:
        #    send_email(text)
        elif "thời tiết" in text:
            current_weather()
        elif "chơi nhạc" in text:
            play_song()
        elif "hình nền" in text:
            change_wallpaper()
        elif "đọc báo" in text:
            read_news()
        elif "định nghĩa" in text:
            tell_me_about()
        
        elif "xem phim" in text:
            watch_movie()
        elif "nhập điểm" in text :
            text = Nhap_Diem()
            csv_to_excel(text)
            speak("Mình đã nhập điểm thành công, bạn muốn giúp gì nữa không")
        elif "excel" in text:
            name_file = ""
            while name_file == "":
                print("Bạn muốn đặt tên file là gì  ? ")
                name_file = hear().lower()
            mkdir("file\\" + name_file)

            lst = init()
            init_csv(lst, name_file)
            csv_to_excel(name_file)
        elif "tâm sự" in text or "nói chuyện" in text:
            chat_with_me()
        elif "cảm ơn" in text :
            speak("Không có gì đâu, mình rất vui khi được giúp bạn")
        else:
            speak("Bạn cần Trợ lý P&P giúp gì ạ?")
            

