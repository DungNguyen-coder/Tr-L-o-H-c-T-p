from mypackage.library import*
from mypackage.speak_hear import speak, hear

def open_website(text):  #oke
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain +".com"
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
        return True
    else:
        return False

def open_google_and_search(text):  #oke
    search_for = text.split("kiếm", 1)[1]
    speak('Okay!')
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)
    speak("bạn muốn mình giúp gì nữa không")


def send_email():   
    speak("Xin lỗi chức năng này mình đang được nâng cấp, bạn có thể sử dụng lần sau ạ. Không biết mình có thể giúp bạn việc gì khác không ?")
    '''
    speak('Bạn gửi email cho ai nhỉ')
    recipient = hear()
    
    if 'dũng' in recipient:
        speak('Nội dung bạn muốn gửi là gì')
        content = hear()
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        #mail.ehlo()
        mail.starttls()
        mail.login('vandung1521@gmail.com', 'kudoshinichi')
        mail.sendmail('vandung1521@gmail.com',"videoxxx6969to12a1@gmail.com", content.encode('utf-8'))
        mail.close()
        speak('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')      
    else:
        speak('Trợ lý P&P không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?')

# do khi mở youtube 1 bài hát hoặc 1 file âm thanh bất kì sẽ ảnh hưởng đến nhận diện giọng nói trợ lý ảo nên anh đề nghị
# là mình sẽ chỉ mở tìm kiếm trên youtube mà không mở nó

def play_song():     
    speak('Xin mời bạn chọn tên bài hát')
    mysong = hear()
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
             break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Bài hát" + mysong + "đã được mở. Trợ lý ảo sẽ được tắt trong khi bạn nghe. Hẹn gặp lại")

def watch_movie():
    speak('Bạn muốn xem phim gì ạ')
    myfilm = hear()
    while True:
        result = YoutubeSearch(myfilm, max_results=10).to_dict()
        if result:
                break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Bộ phim " + myfilm + "đã được mở. Trợ lý ảo sẽ được tắt trong khi bạn xem phim. Hẹn gặp lại")
'''
def play_song():   #oke
    speak("bạn muốn nghe bài hát nào vậy ?")
    mysong = hear()
    mysong ="+".join( mysong.split(" "))
    
    url = "https://www.youtube.com/results?search_query={song}".format(song = mysong)
    webbrowser.open(url)
    speak("Bạn có muốn giúp gì nữa không")

def watch_movie():   #oke
    speak("bạn muốn xem phim nào vậy ?")
    myfilm = hear()
    myfilm ="+".join( myfilm.split(" "))
    
    url = "https://www.youtube.com/results?search_query={song}".format(song = myfilm)
    webbrowser.open(url)
    speak("Bạn có muốn giúp gì nữa không nhỉ")

def tell_me_about():   #oke
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

        speak('Cảm ơn bạn đã lắng nghe. Bạn muốn mình giúp gì nữa không')
    except:
        speak("Trợ lý P&P không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")


def current_weather():   #oke, nên hỏi thời tiết về địa điểm khác Việt Nam
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = hear()
    if not city:
        speak("Tôi không nghe rõ bạn nói gì. Bạn có muốn hỏi gì khác không")
        pass
    else:
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
            Bạn muốn hỏi gì nữa không ? """.format(
                day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                hourset = sunset.hour, minset = sunset.minute, 
                temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
            
            speak(content)
            #time.sleep(20)
        else:
            speak("Không tìm thấy địa chỉ của bạn. Bạn có muốn thử lại không ?")
            text = hear()
            if "có" in text: current_weather()
            else: speak("Mình có thể giúp bạn gì khác không ?")

def read_news():
    '''
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
    '''
    speak("chức năng này của mình đang được nâng cấp, bạn hãy quay lại lần sau nhá. Mình có thể giúp bạn gì khác không")


