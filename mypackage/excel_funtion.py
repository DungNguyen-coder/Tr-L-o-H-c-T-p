from mypackage.library import*
from mypackage.speak_hear import speak, hear

'''
    Đầu tiên mình sẽ tạo ra 1 file .csv (do file này dễ viết auto và có khả năng chuyển đổi thành .xlsx)
    Sau đó, mình sẽ chuyển đổi .csv thành excel
'''
# Nhập điểm tự động

def subject(text):
    lst = ["toán", 'lý', 'anh', 'văn', 'quốc', 'tin', 'sử', 'địa', "công", "sinh", "hóa"]
    lst_subject = ["Điểm Toán", "Điểm Vật Lý", "Điểm Tiếng Anh", "Điểm Ngữ Văn", "Điểm Giáo Dục Quốc Phòng", "Điểm Tin Học", "Điểm Lịch Sử", "Điểm Địa Lý", "Điểm Giáo Dục Công Dân", "Điểm Sinh Học", "Điểm Hóa Học"]
    row1 = "Học và Tên"
    row2 = []
    stt = []
    for i in range(0, len(lst)) :
        if lst[i] in text :
            row1 += ',' + lst_subject[i]
            row2.append(lst_subject[i])
            stt.append(i + 1)
    return [row1, row2, stt]

def Nhap_Diem():
    speak("bạn muốn để tên file excel là gì ?")

    name_file = hear().lower()
    if "kết thúc" in name_file or name_file == "" :
        return "kết thúc"
    mkdir("File\\" + name_file)

    f1 = open("File\\" + name_file + "\\csv.csv", mode = 'w', encoding= 'utf8')
    
    speak("Bạn muốn nhập điểm những môn nào ?")
    
    text = hear().lower()
    
    row = subject(text)     #chứa thông tin các cột và các môn cần nhập điểm

    f1.write(row[0] + '\n')
    while True :
        speak("Họ và Tên")
        
        name = hear()
        if "kết thúc" in name.lower() or name == "" :
            break 
        text1 = name
        for i in range(0, len(row[1])):
            
            speak(row[1][i])
            
            s = hear()
            if "," in str(s):
                s = s.split(",")
                s = ".".join(s)

            text1 += ',' + str(s)
        f1.write(text1 + '\n')
    return name_file

def csv_to_excel(name_file):  # chuyển đội csv sang excel
    df_new = pd.read_csv("File\\" + name_file + "\\csv.csv")
    myfile = pd.ExcelWriter("File\\" + name_file + "\\xlsx.xlsx")

    df_new.to_excel(myfile, index= False)
    myfile.save()

# Tạo 1 file excel bất kì


def init():
    speak("Bạn muốn tạo những cột nào trong excel")
    i = 1
    lst = []
    while True:
        speak("Cột " + str(i)  + " tên là gì vậy")
        you = hear()
        if you == "": continue
        if "kết thúc" in you.lower() or "hết" in you.lower(): break
        lst.append(you.upper())
        i += 1

    return lst

def init_csv(lst, name_file):
    speak("Bắt đầu tạo file")
    f1 = open("File\\" + name_file + "\\csv.csv", mode = "w" , encoding= "utf8" )
    s1 = lst[0]
    for i in range(1, len(lst)):
        s1 += "," + lst[i]
    f1.write(s1 + "\n")

    while True :
        speak(lst[0] + " là gì vậy")
        s = hear()
        if "kết thúc" in s.lower() or "hết" in s.lower() : break
        for i in range(1, len(lst)):
            speak(lst[i])
            you = hear()
            if you == "" : continue
            s += "," + you
        f1.write(s + "\n")

