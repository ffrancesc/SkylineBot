# Generated from Skyline.g by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("J\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\2\5\2\31\n\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4")
        buf.write(")\n\4\f\4\16\4,\13\4\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\5\bD\n\b\3\t\3\t\3\t\3\t\3\t\2\3\6\n\2\4\6\b\n\f\16\20")
        buf.write("\2\2\2F\2\30\3\2\2\2\4\32\3\2\2\2\6\"\3\2\2\2\b-\3\2\2")
        buf.write("\2\n/\3\2\2\2\f\63\3\2\2\2\16C\3\2\2\2\20E\3\2\2\2\22")
        buf.write("\23\5\16\b\2\23\24\7\2\2\3\24\31\3\2\2\2\25\26\5\20\t")
        buf.write("\2\26\27\7\2\2\3\27\31\3\2\2\2\30\22\3\2\2\2\30\25\3\2")
        buf.write("\2\2\31\3\3\2\2\2\32\33\7\3\2\2\33\34\7\13\2\2\34\35\7")
        buf.write("\4\2\2\35\36\7\13\2\2\36\37\7\4\2\2\37 \7\13\2\2 !\7\5")
        buf.write("\2\2!\5\3\2\2\2\"#\b\4\1\2#$\5\4\3\2$*\3\2\2\2%&\f\3\2")
        buf.write("\2&\'\7\4\2\2\')\5\4\3\2(%\3\2\2\2),\3\2\2\2*(\3\2\2\2")
        buf.write("*+\3\2\2\2+\7\3\2\2\2,*\3\2\2\2-.\5\4\3\2.\t\3\2\2\2/")
        buf.write("\60\7\6\2\2\60\61\5\6\4\2\61\62\7\7\2\2\62\13\3\2\2\2")
        buf.write("\63\64\7\b\2\2\64\65\7\13\2\2\65\66\7\4\2\2\66\67\7\13")
        buf.write("\2\2\678\7\4\2\289\7\13\2\29:\7\4\2\2:;\7\13\2\2;<\7\4")
        buf.write("\2\2<=\7\13\2\2=>\7\t\2\2>\r\3\2\2\2?D\5\b\5\2@D\5\n\6")
        buf.write("\2AD\5\f\7\2BD\7\f\2\2C?\3\2\2\2C@\3\2\2\2CA\3\2\2\2C")
        buf.write("B\3\2\2\2D\17\3\2\2\2EF\7\f\2\2FG\7\n\2\2GH\5\16\b\2H")
        buf.write("\21\3\2\2\2\5\30*C")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'['", "']'", "'{'", 
                     "'}'", "':='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "IDENT", "WS" ]

    RULE_root = 0
    RULE_edifici = 1
    RULE_edificis = 2
    RULE_simple = 3
    RULE_compost = 4
    RULE_random = 5
    RULE_skyline = 6
    RULE_assig = 7

    ruleNames =  [ "root", "edifici", "edificis", "simple", "compost", "random", 
                   "skyline", "assig" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    NUM=9
    IDENT=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def assig(self):
            return self.getTypedRuleContext(SkylineParser.AssigContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.skyline()
                self.state = 17
                self.match(SkylineParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.assig()
                self.state = 20
                self.match(SkylineParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdificiContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_edifici

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdifici" ):
                return visitor.visitEdifici(self)
            else:
                return visitor.visitChildren(self)




    def edifici(self):

        localctx = SkylineParser.EdificiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_edifici)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(SkylineParser.T__0)
            self.state = 25
            self.match(SkylineParser.NUM)
            self.state = 26
            self.match(SkylineParser.T__1)
            self.state = 27
            self.match(SkylineParser.NUM)
            self.state = 28
            self.match(SkylineParser.T__1)
            self.state = 29
            self.match(SkylineParser.NUM)
            self.state = 30
            self.match(SkylineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdificisContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edifici(self):
            return self.getTypedRuleContext(SkylineParser.EdificiContext,0)


        def edificis(self):
            return self.getTypedRuleContext(SkylineParser.EdificisContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_edificis

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdificis" ):
                return visitor.visitEdificis(self)
            else:
                return visitor.visitChildren(self)



    def edificis(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.EdificisContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_edificis, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.edifici()
            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SkylineParser.EdificisContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_edificis)
                    self.state = 35
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 36
                    self.match(SkylineParser.T__1)
                    self.state = 37
                    self.edifici() 
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SimpleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edifici(self):
            return self.getTypedRuleContext(SkylineParser.EdificiContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_simple

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple" ):
                return visitor.visitSimple(self)
            else:
                return visitor.visitChildren(self)




    def simple(self):

        localctx = SkylineParser.SimpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.edifici()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompostContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edificis(self):
            return self.getTypedRuleContext(SkylineParser.EdificisContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_compost

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompost" ):
                return visitor.visitCompost(self)
            else:
                return visitor.visitChildren(self)




    def compost(self):

        localctx = SkylineParser.CompostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_compost)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(SkylineParser.T__3)
            self.state = 46
            self.edificis(0)
            self.state = 47
            self.match(SkylineParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RandomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_random

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandom" ):
                return visitor.visitRandom(self)
            else:
                return visitor.visitChildren(self)




    def random(self):

        localctx = SkylineParser.RandomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_random)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(SkylineParser.T__5)
            self.state = 50
            self.match(SkylineParser.NUM)
            self.state = 51
            self.match(SkylineParser.T__1)
            self.state = 52
            self.match(SkylineParser.NUM)
            self.state = 53
            self.match(SkylineParser.T__1)
            self.state = 54
            self.match(SkylineParser.NUM)
            self.state = 55
            self.match(SkylineParser.T__1)
            self.state = 56
            self.match(SkylineParser.NUM)
            self.state = 57
            self.match(SkylineParser.T__1)
            self.state = 58
            self.match(SkylineParser.NUM)
            self.state = 59
            self.match(SkylineParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkylineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple(self):
            return self.getTypedRuleContext(SkylineParser.SimpleContext,0)


        def compost(self):
            return self.getTypedRuleContext(SkylineParser.CompostContext,0)


        def random(self):
            return self.getTypedRuleContext(SkylineParser.RandomContext,0)


        def IDENT(self):
            return self.getToken(SkylineParser.IDENT, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_skyline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkyline" ):
                return visitor.visitSkyline(self)
            else:
                return visitor.visitChildren(self)




    def skyline(self):

        localctx = SkylineParser.SkylineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_skyline)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.simple()
                pass
            elif token in [SkylineParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.compost()
                pass
            elif token in [SkylineParser.T__5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.random()
                pass
            elif token in [SkylineParser.IDENT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.match(SkylineParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssigContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SkylineParser.IDENT, 0)

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_assig

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig" ):
                return visitor.visitAssig(self)
            else:
                return visitor.visitChildren(self)




    def assig(self):

        localctx = SkylineParser.AssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(SkylineParser.IDENT)
            self.state = 68
            self.match(SkylineParser.T__7)
            self.state = 69
            self.skyline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.edificis_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def edificis_sempred(self, localctx:EdificisContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




