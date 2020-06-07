# Generated from Skyline.g by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("I\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\r\6\r8\n\r\r\r\16\r9\3\16\3\16\7\16>\n\16\f\16\16")
        buf.write("\16A\13\16\3\17\6\17D\n\17\r\17\16\17E\3\17\3\17\2\2\20")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\3\2\6\3\2\62;\4\2C\\c|\5\2\62;C\\c|\4")
        buf.write("\2\f\f\"\"\2K\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5!\3\2\2\2")
        buf.write("\7#\3\2\2\2\t%\3\2\2\2\13\'\3\2\2\2\r)\3\2\2\2\17+\3\2")
        buf.write("\2\2\21-\3\2\2\2\23/\3\2\2\2\25\61\3\2\2\2\27\63\3\2\2")
        buf.write("\2\31\67\3\2\2\2\33;\3\2\2\2\35C\3\2\2\2\37 \7*\2\2 \4")
        buf.write("\3\2\2\2!\"\7.\2\2\"\6\3\2\2\2#$\7+\2\2$\b\3\2\2\2%&\7")
        buf.write("]\2\2&\n\3\2\2\2\'(\7_\2\2(\f\3\2\2\2)*\7}\2\2*\16\3\2")
        buf.write("\2\2+,\7\177\2\2,\20\3\2\2\2-.\7/\2\2.\22\3\2\2\2/\60")
        buf.write("\7,\2\2\60\24\3\2\2\2\61\62\7-\2\2\62\26\3\2\2\2\63\64")
        buf.write("\7<\2\2\64\65\7?\2\2\65\30\3\2\2\2\668\t\2\2\2\67\66\3")
        buf.write("\2\2\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:\32\3\2\2\2;?\t")
        buf.write("\3\2\2<>\t\4\2\2=<\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2")
        buf.write("\2@\34\3\2\2\2A?\3\2\2\2BD\t\5\2\2CB\3\2\2\2DE\3\2\2\2")
        buf.write("EC\3\2\2\2EF\3\2\2\2FG\3\2\2\2GH\b\17\2\2H\36\3\2\2\2")
        buf.write("\6\29?E\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    NUM = 12
    IDENT = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "','", "')'", "'['", "']'", "'{'", "'}'", "'-'", "'*'", 
            "'+'", "':='" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "IDENT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "NUM", "IDENT", "WS" ]

    grammarFileName = "Skyline.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


