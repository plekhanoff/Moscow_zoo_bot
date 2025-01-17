import telebot
from telebot import types
import media

 
bot = telebot.TeleBot('7106904439:AAFkdOzKs2txhylsU__QyaVuIDHhNIOVnZU')
 
points = {}
 
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Викторина")
    item2 = types.KeyboardButton("Зоопарк")
    markup.add(item1, item2)
    bot.send_message(m.chat.id, 'Нажми: \nВикторина - для определения твоего тотемного зверя\nЗоопарк - чтобы смотреть котиков', reply_markup=markup)
 
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Викторина':
        start_quiz(message)

    elif message.text.strip() == 'Зоопарк':
        bot.send_message(message.chat.id, 'Класс! Теперь можно посмотреть картинки!')
        start_zoo(message)
        
 
def start_quiz(message):
    points = 0
   
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('обезжиренное')
    item2 = types.KeyboardButton('2.5')
    item3 = types.KeyboardButton('3.6')
    markup.add(item1, item2, item3)
    
    bot.send_message(message.chat.id, 'Какой жирности молоко предпочитаете употреблять в пищу?', reply_markup=markup)
    bot.register_next_step_handler(message, handle_answer)
     
def handle_answer(message):
    global points
    points = 0
    
    if message.text == 'обезжиренное':
        points  += 1
    elif message.text == '2.5':
        points += 2
    elif message.text == '3.6':
        points += 3
    start__quiz(message)
 
            
def start__quiz(message):
    global points
    
        
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('фарш домашний')
    item2 = types.KeyboardButton('стейк средней прожарки')
    item3 = types.KeyboardButton('салатик')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Какое мясо предпочитаете употреблять в пищу?',reply_markup=markup)
    bot.register_next_step_handler(message, handle__answer)
    
def handle__answer(message):
    global points
   
    if message.text == 'фарш домашний':
        points += 2
    elif message.text == 'стейк средней прожарки':
        points += 3
    elif message.text == 'салатик':
        points += 1
    start___quiz(message)
    
def start___quiz(message):
    global points
    
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('помогу')
    item2 = types.KeyboardButton('подтолкну')
    item3 = types.KeyboardButton('пройду мимо')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Если рядом кто-то потерял равновесие, ваши действия?', reply_markup=markup)
    bot.register_next_step_handler(message, handle___answer)
    
def handle___answer(message):
    global points
    if message.text == 'помогу':
        points += 2
    elif message.text == 'подтолкну':
        points += 3
    elif message.text == 'пройду мимо':
        points += 1
   
    if points == 3:
            result = 'вы червяк. Червячный червяк'
            photo_path = 'media/snake.png'
            if photo_path:
                with open(photo_path, 'rb') as photo:
                    bot.send_photo(message.chat.id, photo)
                    bot.send_message(message.chat.id, "Вы также можете стать опекуном своего тотемного животного. Обязательно переходите по ссылке (https://moscowzoo.ru/about/guardianship)")
    elif points == 4:
            result = 'вы сурикат. Хотя бы не червяк'
            photo_path = 'media/meercat.png'
            if photo_path:
                with open(photo_path, 'rb') as photo:
                    bot.send_photo(message.chat.id, photo)
                    bot.send_message(message.chat.id, "Вы также можете стать опекуном своего тотемного животного. Обязательно переходите по ссылке (https://moscowzoo.ru/about/guardianship)")
    elif points == 5:
            result = 'вы Сурок.Не самый отстой'
            photo_path = 'media/surok.png'
            if photo_path:
                with open(photo_path, 'rb') as photo:
                    bot.send_photo(message.chat.id, photo)
                    bot.send_message(message.chat.id, "Вы также можете стать опекуном своего тотемного животного. Обязательно переходите по ссылке (https://moscowzoo.ru/about/guardianship)")
    elif points == 6:
            result = 'вы типа волк'
            photo_path = 'media/wolf.png'
            if photo_path:
                with open(photo_path, 'rb') as photo:
                    bot.send_photo(message.chat.id, photo)
                    bot.send_message(message.chat.id, "Вы также можете стать опекуном своего тотемного животного. Обязательно переходите по ссылке (https://moscowzoo.ru/about/guardianship)")
    elif points == 7:
            result = 'вы слон, харе жрать'
            photo_path = 'media/elefant.png'
            if photo_path:
                with open(photo_path, 'rb') as photo:
                    bot.send_photo(message.chat.id, photo)
                    bot.send_message(message.chat.id, "Вы также можете стать опекуном своего тотемного животного. Обязательно переходите по ссылке (https://moscowzoo.ru/about/guardianship)")
    elif points == 8:
            result = 'вы просто тигр!'
            photo_path = 'media/tiger.png'
            if photo_path:
                with open(photo_path, 'rb') as photo:
                    bot.send_photo(message.chat.id, photo)
                    bot.send_message(message.chat.id, "Вы также можете стать опекуном своего тотемного животного. Обязательно переходите по ссылке (https://moscowzoo.ru/about/guardianship)")
    elif points == 9:
            result = 'Да вы просто Лэопард!'
            photo_path = 'media/leopard.png'
            if photo_path:
                with open(photo_path, 'rb') as photo:
                    bot.send_photo(message.chat.id, photo)
                    bot.send_message(message.chat.id, "Вы также можете стать опекуном своего тотемного животного. Обязательно переходите по ссылке (https://moscowzoo.ru/about/guardianship)")
    else:
            result = 'расчёт окончен.Данные не стреляют. скорее всего ошибочка'
 
    bot.send_message(message.chat.id, f'Поздравляю: \n{result}')
 
    del points          
    bot.send_message(message.chat.id, 'теперь введите /start, чтобы продолжить')
    chat = message.chat
 


def start_zoo(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('Леопард', callback_data='leopard')
    item2 = types.InlineKeyboardButton('тигр', callback_data='tiger')
    item3 = types.InlineKeyboardButton('червяк', callback_data='snake')
    item4 = types.InlineKeyboardButton('Слон', callback_data='elefant')
    item5 = types.InlineKeyboardButton('Сурикат', callback_data='meercat')
    item6 = types.InlineKeyboardButton('Сурок', callback_data='surok')
    item7 = types.InlineKeyboardButton('Волк', callback_data='wolf')
    item8= types.InlineKeyboardButton('манул', callback_data='manul')
    markup.add(item, item2, item3, item4, item5, item6, item7,item8)
    bot.send_message(message.chat.id, 'Кого посмтрим?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
        if call.message:
            if call.data == 'leopard':
                try:
                    with open('./media/leopard.png', 'rb') as photo:
                       bot.send_photo(call.message.chat.id, photo)
                    bot.send_message(call.message.chat.id, "Вы также можете стать опекуном животного. Обязательно переходите по ссылке (https://moscowzoo.ru/about/guardianship)")
                except Exception as e:
                   print(f"Ошибка: {e}")

            elif call.data == 'tiger':
                try:
                    with open('./media/tiger.png', 'rb') as photo:
                        bot.send_photo(call.message.chat.id, photo)
                    bot.send_message(call.message.chat.id, "Вы также можете стать опекуном животного. Обязательно переходите по ссылке (https://moscowzoo.ru/about/guardianship)")
                except Exception as e:
                        print(f"Ошибка: {e}")

            elif call.data == 'elefant':
                try:
                    with open('./media/elefant.png', 'rb') as photo:
                        bot.send_photo(call.message.chat.id, photo)
                    bot.send_message(call.message.chat.id, "Вы также можете стать опекуном животного. Обязательно переходите по ссылке (https://moscowzoo.ru/about/guardianship)")
                except Exception as e:
                    print(f"Ошибка: {e}")

            elif call.data == 'manul':
                try:
                    with open('./media/manul.png', 'rb') as photo:
                        bot.send_photo(call.message.chat.id, photo)
                    bot.send_message(call.message.chat.id, "Вы также можете стать опекуном животного. Обязательно переходите по ссылке (https://moscowzoo.ru/about/guardianship)")
                except Exception as e:
                    print(f"Ошибка: {e}")

            elif call.data == 'snake':
                try:
                    with open('./media/snake.png', 'rb') as photo:
                        bot.send_photo(call.message.chat.id, photo)
                    bot.send_message(call.message.chat.id, "Вы также можете стать опекуном животного. Обязательно переходите по ссылке (https://moscowzoo.ru/about/guardianship)")
                except Exception as e:
                    print(f"Ошибка: {e}")

            elif call.data == 'surok':
                try:
                    with open('./media/surok.png', 'rb') as photo:
                        bot.send_photo(call.message.chat.id, photo)
                    bot.send_message(call.message.chat.id, "Вы также можете стать опекуном животного. Обязательно переходите по ссылке (https://moscowzoo.ru/about/guardianship)")
                except Exception as e:
                    print(f"Ошибка: {e}")

            elif call.data == 'wolf':
                try:
                    with open('./media/wolf.png', 'rb') as photo:
                        bot.send_photo(call.message.chat.id, photo)
                    bot.send_message(call.message.chat.id, "Вы также можете стать опекуном животного. Обязательно переходите по ссылке (https://moscowzoo.ru/about/guardianship)")
                except Exception as e:
                    print(f"Ошибка: {e}")

            elif call.data == 'meercat':
                try:
                    with open('./media/meercat.png', 'rb') as photo:
                        bot.send_photo(call.message.chat.id, photo)
                    bot.send_message(call.message.chat.id, "Вы также можете стать опекуном животного. Обязательно переходите по ссылке (https://moscowzoo.ru/about/guardianship)")
                except Exception as e:
                    print(f"Ошибка: {e}")





        
        
   

bot.polling(none_stop=True)

