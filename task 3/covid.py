import http.client
import re
from tkinter import *

def get_info():
    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()
    temp = data.decode("utf-8")
    return temp

def cut(info):
    country = re.search('rank', info)
    end_country = country.end()
    info = info[end_country:]
    return info

def get_country_info(info):
    country = 'Country: '
    country += search('Country', info)
    tc = 'Total Cases: '
    tc += search('TotalCases', info)
    td = 'Total Death: '
    td += search('TotalDeath', info)
    tt = 'Total Tests: '
    tt += search('TotalTests', info)
    result = country + '\n' + tc + '\n' + td + '\n' + tt
    return result

def search(key_word, info):
    result = re.search(key_word, info)
    start = result.start()
    data = ''
    st = False
    i = 0
    while True:
        if info[i+start] == ',':
                return data
        if info[i+start] == ':':
            st = True
        elif st == True:
            if info[i+start] != '"':
                data += info[i+start]
        i += 1

def search_one_country(info):
    country = ent.get()
    info = cut(info)
    while True:
        result = search('Country', info)
        if country == result:
            text = get_country_info(info)
            search_country['text'] = text
            break
        else:
            try:
                info = cut(info)
            except:
                search_country['text'] = "Ничего не найдено"
                break

def top_five(info):
    info = cut(info)
    text = get_country_info(info)
    country1['text'] = text
    info = cut(info)
    text = get_country_info(info)
    country2['text'] = text
    info = cut(info)
    text = get_country_info(info)
    country3['text'] = text
    info = cut(info)
    text = get_country_info(info)
    country4['text'] = text
    info = cut(info)
    text = get_country_info(info)
    country5['text'] = text

conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "38c5d9519dmsheea62898366a299p1762d0jsn3212521cbd80",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

root = Tk()
root.title("Covid-19 in Europe") 
root.geometry("1000x450")
root.resizable(False, False)
lab_top = Label(root, text="Top 5 country by morbidity", font="Arial 18")
lab_top.place(x = 200, y = 25)
lab_search = Label(root, text="Search", font="Arial 18")
lab_search.place(x = 820, y = 25)
country1 = Label(root, text="1 country", font="Arial 12")
country1.place(x = 50, y = 90)
country2 = Label(root, text="2 country", font="Arial 12")
country2.place(x = 250, y = 90)
country3 = Label(root, text="3 country", font="Arial 12")
country3.place(x = 450, y = 90)
country4 = Label(root, text="4 country", font="Arial 12")
country4.place(x = 140, y = 240)
country5 = Label(root, text="5 country", font="Arial 12")
country5.place(x = 350, y = 240)
ent = Entry(root, width=20,bd=1)
ent.place(x = 785, y = 70)
but = Button(root, text='🔍', width=3, height=1, bd=1, command = lambda: search_one_country(info)).place(x = 912, y = 67)
search_country = Label(root, text="", font="Arial 12")
search_country.place(x = 780, y = 110)
info = get_info()
top_five(info)
root.mainloop()



    
