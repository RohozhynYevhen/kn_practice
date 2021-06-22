import http.client
import re
from tkinter import *

def search_info(key_word, temp, info, num):
    result = re.search(key_word, temp)
    start = result.start() # Positions where the line starts
    st = False
    i = 0
    while True:
        if temp[i+start] == ',':
            if num == 0:
                lab0['text'] = info
            elif num == 1:
                lab1['text'] = info
            elif num == 2:
                lab2['text'] = info
            elif num == 3:
                lab3['text'] = info
            elif num == 4:
                lab4['text'] = info
            elif num == 5:
                lab5['text'] = info
            elif num == 6:
                lab6['text'] = info
            elif num == 7:
                lab7['text'] = info
            elif num == 8:
                lab8['text'] = info
            elif num == 9:
                lab9['text'] = info
            elif num == 10:
                lab10['text'] = info
            elif num == 11:
                lab11['text'] = info
            num = i+start
            return num
        if temp[i+start] == ':': # Place after which the required information
            i += 1
            st = True
        if st == True:
            if temp[i+start] != '"': # Create a line with information
                info += temp[i+start]
        i += 1
    

def output_info(temp):
    search_info("TotalCases", temp, 'Total Cases: ', 0) 
    search_info("NewCases", temp, 'New Cases: ', 1)
    search_info("Infection_Risk", temp, 'Infection Risk: ', 2)
    search_info("ActiveCases", temp, 'Active Cases: ', 3)
    search_info("Serious_Critical", temp, 'Serious Critical: ', 4)
    search_info("TotalRecovered", temp, 'Total Recovered: ', 5)
    search_info("TotalDeaths", temp, 'Total Deaths: ', 6)
    search_info("NewDeaths", temp, 'New Deaths: ', 7)
    search_info("Case_Fatality_Rate", temp, 'Case Fatality Rate: ', 8)
    search_info("TotalTests", temp, 'Total Tests: ', 9)
    search_info("Test_Percentage", temp, 'Test Percentage: ', 10)
    num = search_info("Recovery_Proporation", temp, 'Recovery Proporation: ', 11)
    
    # Cut the line to search for the following countries
    new_str = ''
    for j in range(num, len(temp)):
        new_str += temp[j]
        j += 1
    temp = new_str
    return temp

def select_country(lab_country):
    country_var = var.get()
    if country_var == 0:
        lab_country['text'] = 'France' # Change the name of the country
        conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
        res = conn.getresponse()
        data = res.read()
        temp = data.decode("utf-8")
        temp = output_info(temp) # Change the info of the country
    elif country_var == 1:
        lab_country['text'] = 'Russia'
        conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
        res = conn.getresponse()
        data = res.read()
        temp = data.decode("utf-8")
        for i in range(2):
            temp = output_info(temp)
    elif country_var == 2:
        lab_country['text'] = 'UK'
        conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
        res = conn.getresponse()
        data = res.read()
        temp = data.decode("utf-8")
        for i in range(3):
            temp = output_info(temp)
    elif country_var == 3:
        lab_country['text'] = 'Italy'
        conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
        res = conn.getresponse()
        data = res.read()
        temp = data.decode("utf-8")
        for i in range(4):
            temp = output_info(temp)
    elif country_var == 4:
        lab_country['text'] = 'Spain'
        conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
        res = conn.getresponse()
        data = res.read()
        temp = data.decode("utf-8")
        for i in range(5):
            temp = output_info(temp)
    

conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "38c5d9519dmsheea62898366a299p1762d0jsn3212521cbd80",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

root = Tk()
root.title("Covid-19 in Europe")
root.geometry("600x300")
root["bg"] = "#041f3a"

# country name
lab_country = Label(root, text="France", font = "Arial 15", fg='#FFFFFF', bg='#041f3a')
lab_country.place(x = 20, y = 10)

# first column
lab0 = Label(root, text="Total Cases: ", font="Arial 13", fg='#FFFFFF', bg='#041f3a')
lab0.place(x = 20, y = 40)
lab1 = Label(root, text="New Cases: ", font="Arial 13", fg='#FFFFFF', bg='#041f3a')
lab1.place(x = 20, y = 65)
lab2 = Label(root, text="Infection Risk: ", font="Arial 13", fg='#FFFFFF', bg='#041f3a')
lab2.place(x = 20, y = 90)
lab3 = Label(root, text="Active Cases: ", font="Arial 13", fg='#FFFFFF', bg='#041f3a')
lab3.place(x = 20, y = 115)
lab4 = Label(root, text="Serious Critical: ", font="Arial 13", fg='#FFFFFF', bg='#041f3a')
lab4.place(x = 20, y = 140)
lab5 = Label(root, text="Total Recovered: ", font="Arial 13", fg='#FFFFFF', bg='#041f3a')
lab5.place(x = 20, y = 165)

# second column
lab6 = Label(root, text="Total Deaths: ", font="Arial 13", fg='#FFFFFF', bg='#041f3a')
lab6.place(x = 240, y = 40)
lab7 = Label(root, text="New Deaths: ", font="Arial 13", fg='#FFFFFF', bg='#041f3a')
lab7.place(x = 240, y = 65)
lab8 = Label(root, text="Case Fatality Rate: ", font="Arial 13", fg='#FFFFFF', bg='#041f3a')
lab8.place(x = 240, y = 90)
lab9 = Label(root, text="Total Tests: ", font="Arial 13", fg='#FFFFFF', bg='#041f3a')
lab9.place(x = 240, y = 115)
lab10 = Label(root, text="Test Percentage: ", font="Arial 13", fg='#FFFFFF', bg='#041f3a')
lab10.place(x = 240, y = 140)
lab11 = Label(root, text="Recovery Proporation: ", font="Arial 13", fg='#FFFFFF', bg='#041f3a')
lab11.place(x = 240, y = 165)

# RadioButton to select a country
var=IntVar()
var.set(0)
rad0 = Radiobutton(root, text="France", variable=var, value=0, command = lambda: select_country(lab_country), fg='#ffffff', bg='#041f3a',
                            activebackground='#041f3a', activeforeground='#ffffff', selectcolor='#041f3a').place(x = 510, y = 20)
rad1 = Radiobutton(root, text="Russia", variable=var, value=1, command = lambda: select_country(lab_country), fg='#ffffff', bg='#041f3a',
                            activebackground='#041f3a', activeforeground='#ffffff', selectcolor='#041f3a').place(x = 510, y = 40)
rad2 = Radiobutton(root, text="UK", variable=var, value=2, command = lambda: select_country(lab_country), fg='#ffffff', bg='#041f3a',
                            activebackground='#041f3a', activeforeground='#ffffff', selectcolor='#041f3a').place(x = 510, y = 60)
rad3 = Radiobutton(root, text="Italy", variable=var, value=3, command = lambda: select_country(lab_country), fg='#ffffff', bg='#041f3a',
                            activebackground='#041f3a', activeforeground='#ffffff', selectcolor='#041f3a').place(x = 510, y = 80)
rad4 = Radiobutton(root, text="Spain", variable=var, value=4, command = lambda: select_country(lab_country), fg='#ffffff', bg='#041f3a',
                            activebackground='#041f3a', activeforeground='#ffffff', selectcolor='#041f3a').place(x = 510, y = 100)


select_country(lab_country)

root.mainloop()


    
