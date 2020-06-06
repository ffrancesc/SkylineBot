# importa l'API de Telegram
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import constants

# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
def cmd_start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=constants.TEXT_GREET)
    
def cmd_help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=constants.TEXT_HELP,
        parse_mode=telegram.ParseMode.MARKDOWN
    )

def cmd_author(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=constants.TEXT_AUTHOR_INFO, parse_mode=telegram.ParseMode.MARKDOWN)

def cmd_lst(update, context):
    None

def cmd_clean(update, context):
    None

def cmd_save(update, context):
    None

def cmd_load(update, context):
    None

def message(update, context):
    None

# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start', cmd_start, pass_user_data=True))
dispatcher.add_handler(CommandHandler('help', cmd_help))
dispatcher.add_handler(CommandHandler('author', cmd_author))
dispatcher.add_handler(CommandHandler('lst', cmd_lst))
dispatcher.add_handler(CommandHandler('clean', cmd_clean))
dispatcher.add_handler(CommandHandler('save', cmd_save))
dispatcher.add_handler(CommandHandler('load', cmd_load))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), message))
# engega el bot
updater.start_polling()