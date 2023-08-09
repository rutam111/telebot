import telebot
import webbrowser 
from telebot.types import ReplyKeyboardMarkup ,KeyboardButton

bot = telebot.TeleBot('6635632791:AAEOSo1GSFQuIHSbgV8HzOuJ_OS-6lt5NAU')

def main_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    
    button1 = KeyboardButton('Когда родился Амир Темур?')
    button2 = KeyboardButton('За Сколько долларов Microsoft купил Майнкрафт')
    button4 = KeyboardButton('Кто такой Путин')
    button5 = KeyboardButton('Когда родился  iphone')
    button6 = KeyboardButton('Контакты')
    button7 = KeyboardButton('Наш адрес')
    button8 = KeyboardButton('Про нас')
    button9 = KeyboardButton('Каталог')
    button10 = KeyboardButton('Сотрудничество')    
    
    kb.add(button1,button2,button4,button5,button6  ,button7,button8,button9,button10)
    
    return kb
    
@bot.message_handler(commands=['site', 'website'])
def site(message): 
    webbrowser.open('https://www.instagram.com/reel/CtpVntRoMlf/?igshid=MzRlODBiNWFlZA==')    

@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет меня зовут,{message.from_user.first_name} {message.from_user.last_name}', reply_markup=main_button())
        
@bot.message_handler(content_types=['text'])
def mecho(message):
        
    if message.text.lower() == 'Привет':
        bot.send_message(message.chat.id, f'Привет меня зовут,{message.from_user.first_name} {message.from_user.last_name},.Это теграм бот помагает  найти парки,отели , рестараны и фаст фуды спасибо что прочитали наслаждайтеcь  в Ташкенде.  ')
    elif message.text.lower() == 'id ':
        bot.reply_to(message,  f'ID :{message.from_user.id}')
    elif message.text.lower() == 'привет':
           bot.send_message(message.from_user.id, f'hello')
    elif  message.text.lower() == 'кто тебя создал':
           bot.send_message(message.from_user.id,'меня создал', {message.from_user.first_name})
    elif  message.text.lower() == 'что такое тесла':
           bot.send_message(message.from_user.id,'Тесла это машина которая создал илон маск')  
    elif message.text.lower() == 'кто такой илон маск':
        bot.send_message(message.from_user.id,'Илон маск челловек марианец')             
    elif  message.text.lower() == 'что такоек':
        bot.send_message(message.from_user.id,'iphone это разумный телефон' )
    elif  message.text.lower() == 'что такое бедрок':
        bot.send_message(message.from_users.id,'бедрок это который делается из ноки если вы напишие /site или /website вы увидтете ')
    elif  message.text.lower() == 'кто ты ы чеппионате в брал старсе и в бедварсе':
        bot.send_message(message.from_users.id,'я бот ')    
    elif message.text.lower() == 'qrcode':
        with open('./qr_code.png ', 'rb') as qr_photo:
            bot.send_photo(message.from_user.id, qr_photo)
    elif message.text == 'Когда родился Амир Темур?':
        bot.send_message(message.from_user.id, '9 апреля 1336 г.')
    elif message.text == 'За Сколько долларов Microsoft купил Майнкрафт':
        bot.send_message(message.from_user.id, 'В 2014 году корпорация Microsoft приобрела права на Minecraft вместе со студией Mojang AB за 2,5 миллиарда долларов.')         
    elif message.text == 'Кто такой Путин':
        bot.send_message(message.from_user.id, 'Влади́мир Влади́мирович Пу́тин — российский государственный и политический деятель. Действующий президент Российской Федерации, председатель Государственного Совета Российской Федерации и Совета Безопасности Российской Федерации; Верховный главнокомандующий Вооружёнными силами Российской Федерации с 7 мая 2012 года') 
    elif message.text == 'Когда родился  iphone':
        bot.send_message(message.from_user.id, 'Первый iPhone был представлен Стивом Джобсом 9 января 2007 года на конференции Macworld Conference & Expo в Сан-Франциско. В своём выступлении Джобс сказал: «Я с нетерпением ждал этого в течение двух с половиной лет» и «сегодня Apple собирается переизобрести телефон».')          
    elif message.text == 'Контакты':
        bot.send_message(message.from_user.id, '9000118190')
    elif message.text == 'Наш адрес':
        bot.send_message(message.from_user.id,'Yunusobod filiali')         
    elif message.text == 'Про нас':
        bot.send_message(message.from_user.id, 'Impossible is opssible') 
    elif message.text == 'Каталог':
        bot.send_message(message.from_user.id, '1234')         
    elif message.text == 'Сотрудничество':
        bot.send_message(message.from_user.id, 'Best')          

@bot.message_handler(commands=['audio'])
def audio(message):
    with open('./SOLO PRISMO.mp3','rb') as audio: 
        bot.send_audio(message.from_user.id, audio)  
        


@bot.message_handler(content_types=['photo'])
def photo(message):
    file = message.photo[-1].file_id
    print(file)

    bot.send_photo(message.from_user.id, file)


@bot.message_handler(content_types=['sticker'])
def sticker(message):
    sticker = message.sticker.file_id
    print(sticker)

    bot.send_sticker(message.from_user.id, sticker)    

@bot.message_handler(content_types=['video'])
def vidio(message):
    video = message.video.file_id
    
    bot.send_video(message.from_user.id, video)

@bot.message_handler(content_types=['audio'])
def audio(message):
    audio = message.audio.file_id

    bot.send_audio(message.from_user.id, audio)
    
    
@bot.message_handler(content_types=['qrcode'])
def qrcode(message):
    with open('./qr_code.png ', 'rb') as qr_photo:

        bot.send_phpto(message.from_user.id, qrcode)
    

bot.polling()