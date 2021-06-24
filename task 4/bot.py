import telebot
import config
from telebot import types
import http.client
import re

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
    country = 'Страна: '
    country += search('Country', info)
    tc = 'Всего случаев: '
    tc += search('TotalCases', info)
    td = 'Всего сметей: '
    td += search('TotalDeath', info)
    tt = 'Всего тестов: '
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

def search_one_country(info, country):
    info = cut(info)
    while True:
        result = search('Country', info)
        if country == result:
            text = get_country_info(info)
            return text
        else:
            try:
                info = cut(info)
            except:
                text = "Ничего не найдено 😕"
                return text

def top_five(info):
    info = cut(info)
    text = 'Первое место\n'
    text += get_country_info(info)
    info = cut(info)
    text += '\n\nВторое место\n' + get_country_info(info)
    info = cut(info)
    text += '\n\nТретье место\n' + get_country_info(info)
    info = cut(info)
    text += '\n\nЧетвертое место\n' + get_country_info(info)
    info = cut(info)
    text += '\n\nПятое место\n' + get_country_info(info)
    file = open('statistic.txt', 'w')
    file.write(text)
    file.close()
    return text

def search_bot(message):
    country = message.text
    info = get_info()
    text = search_one_country(info, country)
    bot.send_message(message.chat.id, text)
    

conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "38c5d9519dmsheea62898366a299p1762d0jsn3212521cbd80",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    global country1, country2, country3, country4, country5
    sti = open('stickers/nice.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Топ 5 стран по заболеваемости")
    item2 = types.KeyboardButton("Поиск")

    markup.add(item1, item2)
    
    bot.send_message(message.chat.id, "Привет, я бот который поможет тебе узнать небольшую статистику по заболеваеммости на covid-19 в Европе.",
                     reply_markup=markup)
    
    
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Топ 5 стран по заболеваемости':
            info = get_info()
            text = top_five(info)
            markup = types.InlineKeyboardMarkup(row_width = 1)
            item = types.InlineKeyboardButton('Отправить файлом', callback_data='file')
            markup.add(item)
            bot.send_message(message.chat.id, text, reply_markup=markup)
        elif message.text == 'Поиск':
            msg = bot.send_message(message.chat.id, "Введи название страны (На английском)")
            bot.register_next_step_handler(msg, search_bot)
        else:
            sti = open('stickers/Hmmm.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, "Даже не знаю что сказать")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'file':
                txt = open('statistic.txt', 'rb')
                bot.send_document(call.message.chat.id, txt)
                bot.send_document(call.message.chat.id, "FILEID")
    except Exception as e:
        print(repr(e))
                
bot.polling(none_stop=True)
