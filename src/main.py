#testing the bot api
import time
import random
import telegram
import apiai,json
from telegram import ParseMode
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
from telegram.chataction import ChatAction
from telegram.ext.dispatcher import run_async
from modules import *


@run_async
def start(update,context):
    try:
        chat_id = update.message.chat_id
        username=update.message.from_user
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        context.bot.send_message(chat_id=chat_id, text="Hai.. {}{}\n\nI'm am Bulo98 your personal chatbot, Lets get to bussiness...".format(username['first_name'],username['last_name']))
        help_text=print_help()   
        time.sleep(2.0)
        context.bot.send_message(chat_id=chat_id, text=help_text) 
    except Exception as e:
        print("Error!: ",str(e)) 

@run_async
def gif(update,context):
    chat_id = update.message.chat_id
    username=update.message.from_user
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    gif,thumb,caption=get_gif()
    context.bot.send_animation(chat_id, animation=gif, duration=10, width=536, height=354, thumb=thumb, caption=caption)

@run_async
def meme(update,context):
    chat_id = update.message.chat_id
    username=update.message.from_user
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    meme=get_meme()
    context.bot.send_photo(chat_id=chat_id, photo=meme)

    
@run_async
def joke(update,context):
    chat_id = update.message.chat_id
    username=update.message.from_user
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    joke = get_joke()
    context.bot.send_message(chat_id=chat_id, text=joke)

   
@run_async
def youtube(update,context):
    chat_id = update.message.chat_id
    username=update.message.from_user
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    link=get_youtube()
    context.bot.send_message(chat_id=chat_id, text="[ ]("+link+").", parse_mode=ParseMode.MARKDOWN)
   
@run_async
def wallpaper(update,context):
    chat_id = update.message.chat_id
    username=update.message.from_user
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    image_url = get_image()
    context.bot.send_photo(chat_id=chat_id, photo=image_url)
   
@run_async       
def currency(update,context):
    chat_id = update.message.chat_id
    username=update.message.from_user
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    currency=get_currency()
    context.bot.send_message(chat_id=chat_id, text=currency)

@run_async    
def bitcoin(update,context):
    chat_id = update.message.chat_id
    username=update.message.from_user
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    bitcoin=get_bitcoin()
    context.bot.send_message(chat_id=chat_id, text=bitcoin)
   
           
@run_async
def profile_gen(update,context):
    chat_id = update.message.chat_id
    username=update.message.from_user
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    profile=get_fake_data()
    context.bot.send_message(chat_id=chat_id, text=profile)
 
@run_async   
def quote(update,context):
    chat_id = update.message.chat_id
    username=update.message.from_user
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    quote = get_quote()
    lines="               \n"
    qt='"'
    context.bot.send_message(chat_id=chat_id, text=qt+quote['content']+qt+"\n"+lines+"By: "+quote['author'])
    

@run_async
def not_command(update,context):
    chat_id = update.message.chat_id
    username=update.message.from_user
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    user_response=update.message.text
    user_response=user_response.lower()
    print(user_response)
    request=apiai.ApiAI('Google-Dialogflow-Apikey').text_request()
    request.lang='en'
    request.session_id='RandomGod2367'
    request.query=user_response
    responseJson=json.loads(request.getresponse().read().decode('utf-8'))
    response=responseJson['result']['fulfillment']['speech']
    if response:
        context.bot.send_message(chat_id=update.message.chat_id,text=response)
    else:
        response=search(str(user_response))
        print(response)
        if response=="":
            no_result=["Sorry...I guess my 6th sense is down!","Sorry..there is something wrong with my systems.","I can't fetch you any infomation on that!","Pardon Me...I don't know.","I have no answers for that.","Sorry for dissappointing you..I'll be better."]
            response=str(random.choice(no_result))
            context.bot.send_message(chat_id=update.message.chat_id,text=str(response))
        else:
            context.bot.send_message(chat_id=update.message.chat_id,text=str(response))          


def main():
    TOKEN = "Your-Telegram-Bot-Token"

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
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
    text_message_handler=MessageHandler(Filters.text,not_command)
    dp.add_handler(text_message_handler)
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
