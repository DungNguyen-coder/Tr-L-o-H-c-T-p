from mypackage.library import*
from mypackage.speak_hear import speak, hear


def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút %d giây' % (now.hour, now.minute, now.second))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        speak("Trợ lý P&P chưa hiểu ý của bạn. Bạn nói lại được không?")

def stop():
    speak("Hẹn gặp lại bạn sau!")

def hello(name):
    day_time = int(strftime('%H'))
    if  0 <= day_time < 11:
        speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 11<= day_time < 1:
        speak("Chào buổi tr bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    elif 11<= day_time < 20:
        speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))


def talk_conversation(text):
    speak("Bạn muốn biết gì về tôi nào")
    if "tên gì" in text:
        speak("Tôi tên là trợ lý ảo P&P")
    elif "đâu" in text:
        speak("Tôi đến từ trường trung học phổ thông Nguyễn Huệ")
    elif "địa chỉ" in text:
        speak("Trường tôi có địa chỉ ở Quỳnh Hưng, Quỳnh Phụ, Thái Bình")
    elif "hiệu trưởng" in text :
        speak("Hiệu trưởng trường tôi là thầy giáo Nguyễn Văn Hoàng")
    elif " hiệu phó" in text:
        speak("Hiệu phó trường tôi là thầy giáo Nguyễn Đức Giang")
    elif "bí thư" in text:
        speak("Bí thư Đoàn trường là thầy Phan Thế Định")
        speak("Và tôi rất tự hào vì trường, tôi mới được trao bằng khen từ bộ giáo dục")

def help_me():
    speak("""Trợ lý P&P có thể giúp bạn thực hiện các câu lệnh sau đây:
    1. Chào hỏi
    2. Hiển thị giờ
    3. Mở website, application
    4. Tìm kiếm trên Google
    5. Gửi email
    6. Dự báo thời tiết
    7. Mở nhạc
    8. Thay đổi hình nền máy tính
    9. Đọc báo hôm nay
    10. Kể bạn biết về thế giới
    11. Xem phim 
    12. Trò chuyện""")


def change_wallpaper():
    api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
    url = 'https://api.unsplash.com/photos/random?client_id=' + \
        api_key  # pic from unspalsh.com
    f = urllib2.urlopen(url)
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']
    # Location where we download the image to.
    urllib2.urlretrieve(photo, "D:\\Download____CocCoc\\a.png")
    image=os.path.join("D:\\Download____CocCoc\\a.png")
    ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
    speak('Hình nền máy tính vừa được thay đổi')

