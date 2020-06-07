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
TEXT_GREET = "Hola {}, sóc el SkylineBot!"
TEXT_NOT_START = "_ Encara no has començat cap conversa amb el bot, o si ho has fet, se li ha oblidat! Per a començar, usa /start _"
TEXT_AUTHOR_INFO = "El meu autor és el *Francesc Salar Gavagnach*\n Correu: francesc.salar@est.fib.upc.edu"
TEXT_HELP = """*Comandes disponibles: \n*
/start - Inicia la conversa.
/help - Mostra totes les possibles comandes.
/author - Mostra l'autor del bot.
/lst - Mostra els skylines definits i la seva corresponent àrea.
/clean  - Esborra tots els skylines definits.
/save id - Guarda l'skyline id.
/load id - Carrega l'skyline id.
"""
TEXT_SKYLINE_INFO = "àrea: {}\nalçada: {}"
TEXT_NONE_IDENTIFIER = "No hi ha cap skyline definit encara!"
TEXT_LIST_IDENTIFIERS = "*Skylines definits: *\n"
TEXT_INFO_IDENTIFIER = "id: {} - àrea: {}\n"
TEXT_ERROR_MESSAGE = "No t'he entès... 💣 "

VISITOR = "visitor"
TOKEN = open('token.txt').read().strip()


# inicialitza el chat.
def cmd_start(update, context):
    context.user_data[VISITOR] = EvalVisitor()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=TEXT_GREET.format(update.effective_chat.first_name))


# decorador per assegurar que s'ha cridat /start.
def ensure_start(func):
    def f(update, context):
        if VISITOR not in context.user_data:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=TEXT_NOT_START,
                parse_mode=telegram.ParseMode.MARKDOWN)
        else:
            func(update, context)
    return f


# mostra la llista de les commandes
@ensure_start
def cmd_help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=TEXT_HELP,
        parse_mode=telegram.ParseMode.MARKDOWN)


# mostra l'autor
@ensure_start
def cmd_author(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=TEXT_AUTHOR_INFO,
        parse_mode=telegram.ParseMode.MARKDOWN)


# llista els identificadors definits i les seves arees
@ensure_start
def cmd_lst(update, context):
    ids = context.user_data[VISITOR].identificadors
    txt = TEXT_LIST_IDENTIFIERS
    if ids:
        for i in ids:
            txt += TEXT_INFO_IDENTIFIER.format(i, ids[i].area())
    else:
        txt = TEXT_NONE_IDENTIFIER

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=txt,
        parse_mode=telegram.ParseMode.MARKDOWN)


# borra els identificadors definits (reinstancialitzant el visitor).
@ensure_start
def cmd_clean(update, context):
    context.user_data[VISITOR].identificadors = {}


@ensure_start
def cmd_save(update, context):
    None


@ensure_start
def cmd_load(update, context):
    None


@ensure_start
def message(update, context):
    try:
        # agafa el text i el visitor de l'usuari.
        txt = update.message.text
        visitor = context.user_data[VISITOR]

        # tokenitza, parseja i visita
        input_stream = InputStream(txt)
        lexer = SkylineLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SkylineParser(token_stream)
        tree = parser.root()

        # dibuixa l'skyline resultant
        s = visitor.visit(tree)
        tmp_image = 'tmp.png'
        s.plot().savefig(tmp_image, bbox_inches='tight')

        # contesta amb la imatge i la info de l'skyline
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(tmp_image, 'rb'))

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=TEXT_SKYLINE_INFO.format(s.area(), s.alçada()))

        os.remove(tmp_image)

    except Exception:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=TEXT_ERROR_MESSAGE)


def main():
    matplotlib.pyplot.switch_backend('Agg')

    # instancia els objectes de Telegram
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # tractament de comandes
    dispatcher.add_handler(CommandHandler('start', cmd_start))
    dispatcher.add_handler(CommandHandler('help', cmd_help))
    dispatcher.add_handler(CommandHandler('author', cmd_author))
    dispatcher.add_handler(CommandHandler('lst', cmd_lst))
    dispatcher.add_handler(CommandHandler('clean', cmd_clean))
    dispatcher.add_handler(CommandHandler('save', cmd_save))
    dispatcher.add_handler(CommandHandler('load', cmd_load))

    # tractament de missatges
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), message))

    # engega el bot
    updater.start_polling()


if __name__ == '__main__':
    main()