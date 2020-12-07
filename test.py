import pandas as pd


def csv_to_excel(name_file):  # chuyển đội csv sang excel
    df_new = pd.read_csv("File\\" + name_file + "\\csv.csv")
    myfile = pd.ExcelWriter("File\\" + name_file + "\\xlsx.xlsx")

    df_new.to_excel(myfile, index= False)
    myfile.save()

csv_to_excel("test")