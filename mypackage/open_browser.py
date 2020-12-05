from mypackage.library import*
from mypackage.speak_hear import speak, hear

def open_website(text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
        return True
    else:
        return False

def open_google_and_search(text):
    search_for = text.split("kiếm", 1)[1]
    speak('Okay!')
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)
    time.sleep(10)

def send_email(text):
    speak('Bạn gửi email cho ai nhỉ')
    recipient = hear()
    
    if 'oanh' in recipient:
        speak('Nội dung bạn muốn gửi là gì')
        content = hear()
        # mail = smtplib.SMTP('smtp.gmail.com', 587)
        # mail.ehlo()
        # mail.starttls()
        # mail.login('luongngochungcntt@gmail.com', 'hung23081997')
        # mail.sendmail('luongngochungcntt@gmail.com',
        #               'hungdhv97@gmail.com', content.encode('utf-8'))
        # mail.close()
        speak('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')      
    else:
        speak('Trợ lý P&P không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?')

class myyoutube:
    def __init__(self):
        pass
    
    def play_song(self):
        speak('Xin mời bạn chọn tên bài hát')
        mysong = hear()
        while True:
            result = YoutubeSearch(mysong, max_results=10).to_dict()
            if result:
                break
        url = 'https://www.youtube.com' + result[0]['url_suffix']
        webbrowser.open(url)
        speak("Bài hát bạn yêu cầu đã được mở.")

    def watch_movie(self):
        speak('Bạn muốn xem phim gì ạ')
        mysong = hear()
        while True:
            result = YoutubeSearch(mysong, max_results=10).to_dict()
            if result:
                break
        url = 'https://www.youtube.com' + result[0]['url_suffix']
        webbrowser.open(url)
        speak("Bộ phim bạn yêu thích đã được mở.")

def tell_me_about():
    try:
        speak("Bạn muốn nghe về gì ạ")
        text = hear()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0].split(".")[0])
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không")
            ans = hear()
            if "có" not in ans:
                break    
            speak(content)

        speak('Cảm ơn bạn đã lắng nghe!!!')
    except:
        speak("Trợ lý P&P không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")

def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    time.sleep(3)
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = hear()
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
        speak(content)
        time.sleep(28)
    else:
        speak("Không tìm thấy địa chỉ của bạn")
        time.sleep(2)


def read_news():
    speak("Bạn muốn đọc báo về gì")
    queue = hear()
    params = {
        'apiKey': '30d02d187f7140faacf9ccd27a1441ad',
        "q": queue,
    }
    api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
    api_response = api_result.json()
    print("Tin tức")

    for number, result in enumerate(api_response['articles'], start=1):
        print(f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}
    """)
        if number <= 3:
            webbrowser.open(result['url'])

    time.sleep(5)


