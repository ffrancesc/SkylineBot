# importa l'API de Telegram
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from antlr4 import *
import matplotlib
import os

from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.EvalVisitor import EvalVisitor

# Constants del bot
TEXT_GREET = "Hola! Soc el SkylineBot!"
TEXT_AUTHOR_INFO = "Francesc Salar Gavagnach\nfrancesc.salar@est.fib.upc.edu"
TEXT_HELP = """*Llista de totes les comandes possibles:*
/start - Inicia la conversa amb el bot.
/help - Mostra informació sobre totes les possibles comandes.
/author - Mostra informatió sobre l'autor del bot.
/lst - Mostra els identificadors definits i la seva corresponent àrea.
/clean  - Esborra tots els identificadors definits.
/save id - Guarda l'skyline id.
/load id - Carrega l'skyline id.
"""


# defineix una funció que saluda i que s'executarà amb /start
def cmd_start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=TEXT_GREET)


def cmd_help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=TEXT_HELP,
        parse_mode=telegram.ParseMode.MARKDOWN)


def cmd_author(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=TEXT_AUTHOR_INFO,
        parse_mode=telegram.ParseMode.MARKDOWN)


def cmd_lst(update, context):
    None


def cmd_clean(update, context):
    None


def cmd_save(update, context):
    None


def cmd_load(update, context):
    None


def message(update, context):
    try:
        txt = update.message.text
        input_stream = InputStream(txt)
        lexer = SkylineLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SkylineParser(token_stream)
        tree = parser.root()
        visitor = EvalVisitor()
        s = visitor.visit(tree)
        tmp_image = 'tmp.png'

        s.plot().savefig(tmp_image, bbox_inches='tight')
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(tmp_image, 'rb'))
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='area: {}\n alçada {}'.format(s.area(), s.alçada()))
        os.remove(tmp_image)
    except Exception as e:
        print(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣')

# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()


matplotlib.pyplot.switch_backend('Agg')

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
