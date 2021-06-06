import speech_recognition as sr
import pyttsx3
from datetime import date
from datetime import datetime
from youtube_search import YoutubeSearch
import json
import requests
import time
import pandas as pd
import wikipedia
import webbrowser
def Robot_listen():
    listen =sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting noise")
        listen.adjust_for_ambient_noise(source,duration=1)
        print("Recording  for 4 seconds")
        recorded_audio= listen.listen(source,timeout=4)
        print("Done recording")
    try:
        print("Convert speech to text ")
        your_text = listen.recognize_google(recorded_audio,language="vi")
        print("-----Robot convert speech to text : " , your_text)
        return your_text;
    except:
        your_text = ""
        print("----Robot : ", your_text)
        return  your_text
# Robot_memory= " Xin chào bạn"
def Robot_speak(text) :
        speak = pyttsx3.init()
        voices = speak.getProperty('voices')
        speak.setProperty('voice',voices[1].id)
        speak.say(text)
        speak.runAndWait()
def welcome():
    Robot_speak("Xin chào , bạn tên gì")
    yourname= Robot_listen()
    if yourname :
        now = datetime.now()
        time_char = now.strftime("%H")
        time = int (time_char)
        if time >=6 and time <12 :
            Robot_memory = ("Chào buổi sáng " + yourname)
            print("-----Robot :" + Robot_memory)
            Robot_speak(Robot_memory)
        elif time >= 12 and time <18 :
            Robot_memory = ("Chào buổi trưa " + yourname)
            print("-----Robot :" + Robot_memory)
            Robot_speak(Robot_memory)
        elif time >= 18 and time <24 :
            Robot_memory = ("Chào buổi tối " + yourname)
            print("-----Robot :" + Robot_memory)
            Robot_speak(Robot_memory)
        Robot_memory = "Tôi có thể giúp gì cho bạn "
        print("-----Robot : "+ Robot_memory)
        Robot_speak(Robot_memory)
def CheckCovid():
    Robot_memory = "Xin chào bạn , vui lòng bạn khai báo y tế"
    print("-----Robot : " + Robot_memory)
    Robot_speak(Robot_memory)

    data1 = pd.ExcelFile('mydata.xlsx')
    df1 = pd.read_excel(data1)
    Robot_memory = "Họ và tên "
    print("-----Robot : " + Robot_memory)
    Robot_speak(Robot_memory)
    name = Robot_listen().lower()

    Robot_memory = "Năm sinh"
    print("-----Robot :" + Robot_memory)
    Robot_speak(Robot_memory)
    ns = Robot_listen().lower()
    yearOfBirth = (ns)

    Robot_memory = "Giới tính"
    print("-----Robot : " + Robot_memory)
    Robot_speak(Robot_memory)
    maleOrFemale = Robot_listen().lower()

    Robot_memory = "Địa chỉ"
    print("-----Robot : " + Robot_memory)
    Robot_speak(Robot_memory)
    address = Robot_listen().lower()

    Robot_memory = "Số điện thoại"
    print("-----Robot : " + Robot_memory)
    Robot_speak(Robot_memory)
    number = Robot_listen().lower()
    myphone = (number)

    Robot_memory = "Sức khỏe"
    print("-----Robot : " + Robot_memory)
    Robot_speak(Robot_memory)
    healthy = Robot_listen().lower()

    Robot_memory = "Tiếp xúc"
    print("-----Robot : " + Robot_memory)
    Robot_speak(Robot_memory)
    comnunicate = Robot_listen().lower()

    data2 = {'Họ và tên': [name], 'Năm sinh': [yearOfBirth], 'Giới tính': [maleOrFemale],
             'Địa chỉ': [address], 'Số điện thoại': [myphone],
             'Sức khỏe': [healthy], 'Tiếp xúc': [comnunicate]}

    df2 = pd.DataFrame(data2)

    df = df1.append(df2, ignore_index=True)
    df.drop(df.filter(regex="Unnamed"), axis=1, inplace=True)
    df.to_excel('myData.xlsx')
    print(df)
def searchCovid():
    data = pd.ExcelFile('mydata.xlsx')
    df1 = pd.read_excel(data, index_col=None)
    df1.drop(df1.filter(regex="Unnamed"), axis=1, inplace=True)

    Robot_memory = "Nhập sộ điện thoại của bạn"
    print("-----Robot : " + Robot_memory)
    Robot_speak(Robot_memory)
    sdt = Robot_listen().lower();
    myphone = int(sdt)
    dk = df1[df1['Số điện thoại'] == myphone]

    data1 = dk.iloc[0, 0]
    data11 = "Họ và tên :" + data1
    Robot_memory = data11
    print("-----Robot : " + Robot_memory)
    Robot_speak(Robot_memory)

    data2 = str(dk.iloc[0, 1])
    data22 = "Năm sinh :" + data2
    Robot_memory = data22
    print("-----Robot : " + Robot_memory)
    Robot_speak(Robot_memory)

    data3 = dk.iloc[0, 2]
    data33 = "Giới tính :" + data3
    Robot_memory = data33
    print("-----Robot : " + Robot_memory)
    Robot_speak(Robot_memory)

    data4 = dk.iloc[0, 3]
    data44 = "Địa chỉ :" + data4
    Robot_memory = data44
    print("-----Robot : " + Robot_memory)
    Robot_speak(Robot_memory)

    data5 = str(dk.iloc[0, 4])
    data55 = "Số điện thoại :" + data5
    Robot_memory = data55
    print("-----Robot : " + Robot_memory)
    Robot_speak(Robot_memory)

    data6 = dk.iloc[0, 5]
    data66 = "Sức khỏe:" + data6
    Robot_memory = data66
    print("-----Robot : " + Robot_memory)
    Robot_speak(Robot_memory)

    data7 = dk.iloc[0, 6]
    data77 = "Tiếp xúc:" + data7
    Robot_memory = data77
    print("-----Robot : " + Robot_memory)
    Robot_speak(Robot_memory)
def Weather():
    Robot_speak("Bạn muốn xem thời tiết ở đâu ạ.")
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = Robot_listen().lower()
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
        sunrise = datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.now()
        Robot_memory = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".\
            format(day = now.day,month = now.month, year= now.year,
                   hourrise = sunrise.hour, minrise = sunrise.minute,
                     hourset = sunset.hour, minset = sunset.minute,
                    temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
        print("-----RoBot:",Robot_memory)
        Robot_speak(Robot_memory)
        time.sleep(20)
    else:
        Robot_speak("Không tìm thấy địa chỉ của bạn")
def Hour():
    now = datetime.now()
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")
    Robot_memory = ("Bây giờ là " + hour + "giờ" + minute + "phút" + second + "giây")
    print("-----Robot: " + Robot_memory)
    Robot_speak(Robot_memory)
def Day():
    today = date.today()
    day = today.strftime("%d")
    mouth = today.strftime("%m")
    year = today.strftime("%Y")
    Robot_memory = ("Hôm nay là " + day + " tháng" + mouth + " năm" + year)
    print("-----Robot: " + Robot_memory)
    Robot_speak(Robot_memory)

def Search():
    Robot_memory = "Bạn muốn tìm kiếm nội dung gì trên Google"
    print("-----Robot" + Robot_memory)
    Robot_speak(Robot_memory)
    search = Robot_listen().lower()
    url = f"https://www.google.com.vn/search?q={search}"
    webbrowser.get().open(url, new=1)
    Robot_speak(f'Kết quả tìm kiếm {search} trên Google')
    print(f'Kết quả tìm kiếm {search} trên Google')

def SearchYoutube():
    Robot_memory = "Bạn cần tìm kiếm gì trên Youtube"
    print("-----Robot: " + Robot_memory)
    Robot_speak(Robot_memory)
    search = Robot_listen().lower()
    url = f'https://www.youtube.com/search?q={search}'
    webbrowser.get().open(url, new=1)
    Robot_speak(f'Kết quả tìm kiếm {search} trên Youtube')
    print(f'Kết quả tìm kiếm {search} trên Youtube')

def WatchYoutube():
    Robot_memory = "Xin mời chọn tên chương trình"
    print("-----Robot: " + Robot_memory)
    Robot_speak(Robot_memory)
    program = Robot_listen().lower()
    search_result = YoutubeSearch(program, max_results=1).to_json()
    result = json.loads(search_result)
    for v in result['videos']:
        url = 'https://www.youtube.com/watch?v=' + v['id']
        webbrowser.open(url)
        Robot_speak("Chương trình yêu thích của bạn đã được mở")
        time.sleep(20)

def Newspaper():
    Robot_memory = "Bạn muốn đọc tin tức gì "
    print("-----Robot: " + Robot_memory)
    Robot_speak(Robot_memory)
    newspapaer = Robot_listen().lower()
    url = f"https://zingnews.vn/tieu-diem/{newspapaer}.html"
    webbrowser.get().open(url, new=1)
    Robot_speak("Đã mở tin tức cho " + newspapaer)

def Information():
    Robot_memory = "Bạn muốn biết thông tin gì ?"
    print("-----Robot: " + Robot_memory)
    Robot_speak(Robot_memory)
    information = Robot_listen().lower()
    wikipedia.set_lang("vi")
    Robot_memory = wikipedia.summary(information, sentences=5)
    print("-----Robot :" + Robot_memory)
    Robot_speak(Robot_memory)

def Facebook():
    Robot_speak("Đang mở Facebook")
    url = f"https://www.facebook.com/"
    webbrowser.get().open(url, new=1)

def TurnOnLed():
    webbrowser.open('http://192.168.1.101/5/on', new=1)
    Robot_memory = "đã bật đèn"
    print("-----Robot: " + Robot_memory)
    Robot_speak(Robot_memory)

def TurnOffLed():
    webbrowser.open('http://192.168.1.101/5/off', new=1)
    Robot_memory = "đã tắt đèn"
    print("-----Robot: " + Robot_memory)
    Robot_speak(Robot_memory)

def Option():
    Robot_memory = "1.Chào hỏi." \
                   "\n2.Ngày và giờ. Vui lòng nói Ngày hoặc Giờ để thực hiện " \
                   "\n3.Tìm kiếm trên Google. Vui lòng nói Tìm để thực hiên" \
                   "\n4.Tìm kiếm trên Youtube. Vui lòng nói Xem Youtube để thực hiện" \
                   "\n5.Xem chương trình trên Youtube.Vui lòng nói Chương Trình để thực hiện" \
                   "\n6.Đọc báo trên Zing. Vui lòng nói Đọc Báo để thực hiện" \
                   "\n7.Thông tin bách khao toàn thư. Vui lòng nói Thông Tin để thực hiện" \
                   "\n8.Truy cập Facebook. Vui lòng nói Mạng Xã Hội để thực hiện" \
                   "\n9.Bật đèn trên NodeMCU. Vui lòng nói Bật Đèn để thực hiện" \
                   "\n10.Tắt đèn trên NodeMCU.Vui lòng nói Tắt Đèn để thực hiện" \
                   "\n11.Nhập dữ liệu cho database. Vui lòng nói Nhập để thực hiện" \
                   "\n12.Xuất dữ liệu từ database. Vui lòng nói Xuất để thực hiện" \
                   "\n13.Cập nhật thời tiết hôm nay. Vui lòng nói Thời Tiết để thực hiện" \
                   "\n14.Chức năng của PYROBOT. Vui lòng nói Chức Năng để thực hiện" \
                   "\n15.Dừng chương trình. Vui lòng nói Tạm Biệt hoặc Ngủ đi để thực hiện"
    print("-----Robot: " + Robot_memory)
    Robot_speak(Robot_memory)

if __name__ == "__main__":
    welcome()
    while True:
        your_text = Robot_listen().lower();
        if your_text=="":
            Robot_memory="Xin lỗi, tôi không nghe rõ "
            print("-----Robot : "+Robot_memory)
            Robot_speak(Robot_memory)
        elif "giờ" in your_text or "mấy giờ" in your_text :
            Hour()
        elif "ngày" in your_text or "ngày mấy" in your_text :
            Day()
        elif "tìm" in your_text :
            Search()
        elif "xem youtube" in your_text :
            SearchYoutube()
        elif "chương trình" in your_text:
            WatchYoutube()
        elif "đọc báo" in your_text :
            Newspaper()
        elif "thông tin" in your_text:
            Information()
        elif "mạng xã hội" in your_text:
            Facebook()
        elif "bật đèn" in your_text :
            TurnOnLed()
        elif "tắt đèn" in your_text :
            TurnOffLed()
        elif "nhập dữ liệu" in your_text :
            CheckCovid()
        elif "xuất dữ liệu" in your_text:
            searchCovid()
        elif "thời tiết" in your_text:
            Weather()
        elif "chức năng" in your_text :
            Option()
        elif "tạm biệt " or "ngủ đi " in your_text :
            Robot_memory="Tạm biệt , hẹn gặp lại"
            print("-----Robot: "+Robot_memory)
            Robot_speak(Robot_memory)
            break
