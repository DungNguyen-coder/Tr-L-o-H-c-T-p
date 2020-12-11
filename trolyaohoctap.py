from mypackage.speak_hear import*
from mypackage.open_app import*
from mypackage.open_browser import*
from mypackage.other_funtion import*
from mypackage.excel_funtion import*



def Tro_ly_ao():
    speak("Xin chào, bạn tên là gì nhỉ?")
    name = hear()
    if True:
        speak("Chào bạn "+ str(name))
        box2_speak(dohoa1.tro_ly)
        speak("Bạn cần Trợ lý P&P có thể giúp gì ạ?")
        box2_speak(dohoa1.tro_ly)
        while True:
            
            text = hear()
            box1_hear(dohoa1.hoc_sinh)

            if not text:
                speak("mình không nghe rõ bạn nói lại được không")
            elif "dừng" in text or "tạm biệt" in text or "chào bạn" in text or "ngủ thôi" in text:
                stop()
                break
            elif "toán" in text or "hệ phương trình" in text:
                he_phuong_trinh_bac_2()
                time.sleep(1)
                speak("Bạn cần mình giúp gì nữa không ?")
            elif "có thể làm gì" in text:
                help_me()
            elif "chào" in text:
                hello(name)
            elif "giờ" in text or "ngày" in text:
                get_time(text)
            elif 'mở google' in text and "tìm kiếm" in text:
                open_google_and_search(text)
            elif "facebook" in text:
                webbrowser.open("www.facebook.com")
                speak("Facebook đã được mở. Bạn muốn mình giúp gì nữa không ?")
            elif "zalo" in text:
                webbrowser.open("https://chat.zalo.me/")
                speak("Zalo đã được mở. Bạn muốn mình giúp gì nữa không ?")
            
            elif "ứng dụng" in text:
                speak("Tên ứng dụng bạn muốn mở là ")
                text1 = hear()
                open_application(text1)
            #elif "email" in text or "mail" in text or "gmail" in text:
            #    send_email(text)
            elif "thời tiết" in text:
                current_weather()
            elif "chơi nhạc" in text or  "bài hát" in text:
                play_song()
            elif "hình nền" in text:
                change_wallpaper()
            elif "đọc báo" in text:
                read_news()
            elif "định nghĩa" in text or "tìm hiểu" in text or "thông tin" in text:
                tell_me_about()
            
            elif "phim" in text or "video" in text:
                watch_movie()
            elif "nhập điểm" in text :
                text = Nhap_Diem()
                csv_to_excel(text)
                speak("Mình đã nhập điểm thành công, bạn muốn giúp gì nữa không")
            elif "excel" in text or "tạo cho mình" in text:
                name_file = ""
                while name_file == "":
                    speak("Bạn muốn đặt tên file là gì  ? ")
                    name_file = hear()
                name_file = name_file.lower()
                mkdir("file\\" + name_file)

                lst = init()
                init_csv(lst, name_file)
                csv_to_excel(name_file)
                speak("Mình đã tạo thành công, bạn cần mình giúp gì nữa không")
            elif "tâm sự" in text or "nói chuyện" in text or "chia sẻ" in text:
                chat_with_me()
            elif "cảm ơn" in text :
                speak("Không có gì đâu, mình rất vui khi được giúp bạn")
            elif "email" in text or "tin nhắn" in text:
                send_email()
            elif "mở" in text:
                open_website(text)
            else:
                speak("Bạn cần Trợ lý P&P giúp gì ạ?")

            box2_speak(dohoa1.tro_ly)


# Chạy đa luồng
thread = Thread(target= Tro_ly_ao)
thread.start()

root.mainloop()


            

