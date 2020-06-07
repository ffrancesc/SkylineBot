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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\5\2\31\n\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4&\n\4\f\4")
        buf.write("\16\4)\13\4\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\5\bH\n\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\bY\n\b\f\b\16\b")
        buf.write("\\\13\b\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\2\3\16")
        buf.write("\f\2\4\6\b\n\f\16\20\22\24\2\2\2g\2\30\3\2\2\2\4\32\3")
        buf.write("\2\2\2\6\"\3\2\2\2\b*\3\2\2\2\n,\3\2\2\2\f\60\3\2\2\2")
        buf.write("\16G\3\2\2\2\20]\3\2\2\2\22a\3\2\2\2\24c\3\2\2\2\26\31")
        buf.write("\5\16\b\2\27\31\5\20\t\2\30\26\3\2\2\2\30\27\3\2\2\2\31")
        buf.write("\3\3\2\2\2\32\33\7\3\2\2\33\34\5\22\n\2\34\35\7\4\2\2")
        buf.write("\35\36\5\22\n\2\36\37\7\4\2\2\37 \5\22\n\2 !\7\5\2\2!")
        buf.write("\5\3\2\2\2\"\'\5\4\3\2#$\7\4\2\2$&\5\4\3\2%#\3\2\2\2&")
        buf.write(")\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(\7\3\2\2\2)\'\3\2\2\2")
        buf.write("*+\5\4\3\2+\t\3\2\2\2,-\7\6\2\2-.\5\6\4\2./\7\7\2\2/\13")
        buf.write("\3\2\2\2\60\61\7\b\2\2\61\62\5\22\n\2\62\63\7\4\2\2\63")
        buf.write("\64\5\22\n\2\64\65\7\4\2\2\65\66\5\22\n\2\66\67\7\4\2")
        buf.write("\2\678\5\22\n\289\7\4\2\29:\5\22\n\2:;\7\t\2\2;\r\3\2")
        buf.write("\2\2<=\b\b\1\2=H\5\b\5\2>H\5\n\6\2?H\5\f\7\2@H\5\24\13")
        buf.write("\2AB\7\3\2\2BC\5\16\b\2CD\7\5\2\2DH\3\2\2\2EF\7\n\2\2")
        buf.write("FH\5\16\b\bG<\3\2\2\2G>\3\2\2\2G?\3\2\2\2G@\3\2\2\2GA")
        buf.write("\3\2\2\2GE\3\2\2\2HZ\3\2\2\2IJ\f\7\2\2JK\7\13\2\2KY\5")
        buf.write("\16\b\bLM\f\5\2\2MN\7\f\2\2NY\5\16\b\6OP\f\6\2\2PQ\7\13")
        buf.write("\2\2QY\5\22\n\2RS\f\4\2\2ST\7\f\2\2TY\5\22\n\2UV\f\3\2")
        buf.write("\2VW\7\n\2\2WY\5\22\n\2XI\3\2\2\2XL\3\2\2\2XO\3\2\2\2")
        buf.write("XR\3\2\2\2XU\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[\17")
        buf.write("\3\2\2\2\\Z\3\2\2\2]^\5\24\13\2^_\7\r\2\2_`\5\16\b\2`")
        buf.write("\21\3\2\2\2ab\7\16\2\2b\23\3\2\2\2cd\7\17\2\2d\25\3\2")
        buf.write("\2\2\7\30\'GXZ")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'['", "']'", "'{'", 
                     "'}'", "'-'", "'*'", "'+'", "':='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUM", "IDENT", "WS" ]

    RULE_root = 0
    RULE_edifici = 1
    RULE_edificis = 2
    RULE_simple = 3
    RULE_compost = 4
    RULE_random = 5
    RULE_skyline = 6
    RULE_assig = 7
    RULE_num = 8
    RULE_ident = 9

    ruleNames =  [ "root", "edifici", "edificis", "simple", "compost", "random", 
                   "skyline", "assig", "num", "ident" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    NUM=12
    IDENT=13
    WS=14

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
                self.state = 20
                self.skyline(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.assig()
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

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.NumContext)
            else:
                return self.getTypedRuleContext(SkylineParser.NumContext,i)


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
            self.num()
            self.state = 26
            self.match(SkylineParser.T__1)
            self.state = 27
            self.num()
            self.state = 28
            self.match(SkylineParser.T__1)
            self.state = 29
            self.num()
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

        def edifici(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.EdificiContext)
            else:
                return self.getTypedRuleContext(SkylineParser.EdificiContext,i)


        def getRuleIndex(self):
            return SkylineParser.RULE_edificis

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdificis" ):
                return visitor.visitEdificis(self)
            else:
                return visitor.visitChildren(self)




    def edificis(self):

        localctx = SkylineParser.EdificisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_edificis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.edifici()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkylineParser.T__1:
                self.state = 33
                self.match(SkylineParser.T__1)
                self.state = 34
                self.edifici()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
            self.state = 40
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
            self.state = 42
            self.match(SkylineParser.T__3)
            self.state = 43
            self.edificis()
            self.state = 44
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

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.NumContext)
            else:
                return self.getTypedRuleContext(SkylineParser.NumContext,i)


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
            self.state = 46
            self.match(SkylineParser.T__5)
            self.state = 47
            self.num()
            self.state = 48
            self.match(SkylineParser.T__1)
            self.state = 49
            self.num()
            self.state = 50
            self.match(SkylineParser.T__1)
            self.state = 51
            self.num()
            self.state = 52
            self.match(SkylineParser.T__1)
            self.state = 53
            self.num()
            self.state = 54
            self.match(SkylineParser.T__1)
            self.state = 55
            self.num()
            self.state = 56
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


        def ident(self):
            return self.getTypedRuleContext(SkylineParser.IdentContext,0)


        def skyline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.SkylineContext)
            else:
                return self.getTypedRuleContext(SkylineParser.SkylineContext,i)


        def num(self):
            return self.getTypedRuleContext(SkylineParser.NumContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_skyline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkyline" ):
                return visitor.visitSkyline(self)
            else:
                return visitor.visitChildren(self)



    def skyline(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.SkylineContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_skyline, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 59
                self.simple()
                pass

            elif la_ == 2:
                self.state = 60
                self.compost()
                pass

            elif la_ == 3:
                self.state = 61
                self.random()
                pass

            elif la_ == 4:
                self.state = 62
                self.ident()
                pass

            elif la_ == 5:
                self.state = 63
                self.match(SkylineParser.T__0)
                self.state = 64
                self.skyline(0)
                self.state = 65
                self.match(SkylineParser.T__2)
                pass

            elif la_ == 6:
                self.state = 67
                self.match(SkylineParser.T__7)
                self.state = 68
                self.skyline(6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 86
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 71
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 72
                        self.match(SkylineParser.T__8)
                        self.state = 73
                        self.skyline(6)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 74
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 75
                        self.match(SkylineParser.T__9)
                        self.state = 76
                        self.skyline(4)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 77
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 78
                        self.match(SkylineParser.T__8)
                        self.state = 79
                        self.num()
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 80
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 81
                        self.match(SkylineParser.T__9)
                        self.state = 82
                        self.num()
                        pass

                    elif la_ == 5:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 83
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 84
                        self.match(SkylineParser.T__7)
                        self.state = 85
                        self.num()
                        pass

             
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssigContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(SkylineParser.IdentContext,0)


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
            self.state = 91
            self.ident()
            self.state = 92
            self.match(SkylineParser.T__10)
            self.state = 93
            self.skyline(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_num

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)




    def num(self):

        localctx = SkylineParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(SkylineParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SkylineParser.IDENT, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_ident

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdent" ):
                return visitor.visitIdent(self)
            else:
                return visitor.visitChildren(self)




    def ident(self):

        localctx = SkylineParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ident)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(SkylineParser.IDENT)
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
        self._predicates[6] = self.skyline_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def skyline_sempred(self, localctx:SkylineContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




