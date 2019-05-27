import time
import random
import telegram
import requests
import apiai,json
from bs4 import BeautifulSoup
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from modules import *



#--------------------------------------------------------
#Functions for each command
#--------------------------------------------------------


def gif(bot,update):
    data=dict()
    global db,user,root    
    chat_id = update.message.chat_id
    username=update.message.from_user.first_name
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    gif,thumb,caption=get_gif()
    bot.send_animation(chat_id, animation=gif, duration=10, width=536, height=354, thumb=thumb, caption=caption)


def meme(bot,update):
    data=dict()
    global db,user,root
    chat_id = update.message.chat_id
    username=update.message.from_user.first_name
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    meme=get_meme()
    bot.send_photo(chat_id=chat_id, photo=meme)

    

def joke(bot,update):
    data=dict()
    global db,user,root
    chat_id = update.message.chat_id
    username=update.message.from_user.first_name
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    joke = get_joke()
    bot.send_message(chat_id=chat_id, text=joke)

   

def youtube(bot,update):
    data=dict()
    global db,user,root
    chat_id = update.message.chat_id
    username=update.message.from_user.first_name
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    link=get_youtube()
    bot.send_message(chat_id=chat_id, text="[ ]("+link+").", parse_mode=telegram.ParseMode.MARKDOWN)


def wallpaper(bot, update):
    data=dict()
    global db,user,root
    chat_id = update.message.chat_id
    username=update.message.from_user.first_name
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    image_url = get_image()
    bot.send_photo(chat_id=chat_id, photo=image_url)

       
def currency(bot, update):
    data=dict()
    global db,user,root
    chat_id = update.message.chat_id
    username=update.message.from_user.first_name
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    currency=get_currency()
    bot.send_message(chat_id=chat_id, text=currency)


def bitcoin(bot,update):
    data=dict()
    global db,user,root
    chat_id = update.message.chat_id
    username=update.message.from_user.first_name
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    bitcoin=get_bitcoin()
    bot.send_message(chat_id=chat_id, text=bitcoin)




def start(bot,update):
    try:
        data=dict()
        global db,user,root
        chat_id = update.message.chat_id
        username=update.message.from_user.first_name
        bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
        bot.send_message(chat_id=chat_id, text="Hai.. "+username+"\n\nI'm am Bulo98 your personal chatbot, Lets get to bussiness...")
        help_text=print_help()   
        time.sleep(2.0)
        bot.send_message(chat_id=chat_id, text=help_text) 
    except Exception as e:
        print("Error!: ",str(e))    

def profile_gen(bot,update):
    data=dict()
    global db,user,root
    chat_id = update.message.chat_id
    username=update.message.from_user.first_name
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    profile=get_fake_data()
    bot.send_message(chat_id=chat_id, text=profile)


def quote(bot,update):
    data=dict()
    global db,user,root
    chat_id = update.message.chat_id
    username=update.message.from_user.first_name
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    quote=get_quote()
    lines="               \n"
    qt='"'
    bot.send_message(chat_id=chat_id, text=qt+quote['Quote']+qt+"\n"+lines+"By: "+quote['Author']+"\n"+lines+"Category: "+quote['Category'])



def not_command(bot,update):
    data=dict()
    global db,user,root
    chat_id = update.message.chat_id
    username=update.message.from_user.first_name
    bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    user_response=update.message.text
    user_response=user_response.lower()
    print(user_response)
    request=apiai.ApiAI('Your-Dialog-flow-api-key-goes-here').text_request()
    request.lang='en'
    request.session_id='any-random-number-with-string'
    request.query=user_response
    responseJson=json.loads(request.getresponse().read().decode('utf-8'))
    response=responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=update.message.chat_id,text=response)
    else:
        response=search(str(user_response))
        if response=="":
            no_result=["Sorry...I guess my 6th sense is down!","Sorry..there is something wrong with my systems.","I can't fetch you any infomation on that!","Pardon Me...I don't know.","I have no answers for that.","Sorry for dissappointing you..I'll be better."]
            response=str(random.choice(no_result))
            bot.send_message(chat_id=update.message.chat_id,text=str(response))
        else:
            bot.send_message(chat_id=update.message.chat_id,text=str(response))
               


def main():
    TOKEN = "Your-telegram-bot-token"

    updater = Updater(TOKEN)
    dp = updater.dispatcher
    text_message_handler=MessageHandler(Filters.text,not_command)
    dp.add_handler(text_message_handler)   #Following are command handlers
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('wallpaper',wallpaper))
    dp.add_handler(CommandHandler('bitcoin',bitcoin))
    dp.add_handler(CommandHandler('currency',currency))
    dp.add_handler(CommandHandler('joke',joke))
    dp.add_handler(CommandHandler('meme',meme))    
    dp.add_handler(CommandHandler('gif',gif))
    dp.add_handler(CommandHandler('video',youtube))
    dp.add_handler(CommandHandler('profile',profile_gen))
    dp.add_handler(CommandHandler('quote',quote))
  

    updater.start_polling(clean=True) #Async happens here
    updater.idle()
    


if __name__ == '__main__':
    main()
