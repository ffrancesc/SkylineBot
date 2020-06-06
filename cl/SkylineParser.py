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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("=\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\5\2\21\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4#\n\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\64\n\4")
        buf.write("\f\4\16\4\67\13\4\3\5\3\5\3\5\3\5\3\5\2\3\6\6\2\4\6\b")
        buf.write("\2\2\2@\2\20\3\2\2\2\4\22\3\2\2\2\6\"\3\2\2\2\b8\3\2\2")
        buf.write("\2\n\13\5\6\4\2\13\f\7\2\2\3\f\21\3\2\2\2\r\16\5\b\5\2")
        buf.write("\16\17\7\2\2\3\17\21\3\2\2\2\20\n\3\2\2\2\20\r\3\2\2\2")
        buf.write("\21\3\3\2\2\2\22\23\7\7\2\2\23\24\7\n\2\2\24\25\7\t\2")
        buf.write("\2\25\26\7\n\2\2\26\27\7\t\2\2\27\30\7\n\2\2\30\31\7\b")
        buf.write("\2\2\31\5\3\2\2\2\32\33\b\4\1\2\33#\5\4\3\2\34\35\7\7")
        buf.write("\2\2\35\36\5\6\4\2\36\37\7\b\2\2\37#\3\2\2\2 !\7\3\2\2")
        buf.write("!#\5\6\4\b\"\32\3\2\2\2\"\34\3\2\2\2\" \3\2\2\2#\65\3")
        buf.write("\2\2\2$%\f\7\2\2%&\7\4\2\2&\64\5\6\4\b\'(\f\5\2\2()\7")
        buf.write("\5\2\2)\64\5\6\4\6*+\f\6\2\2+,\7\4\2\2,\64\7\n\2\2-.\f")
        buf.write("\4\2\2./\7\5\2\2/\64\7\n\2\2\60\61\f\3\2\2\61\62\7\3\2")
        buf.write("\2\62\64\7\n\2\2\63$\3\2\2\2\63\'\3\2\2\2\63*\3\2\2\2")
        buf.write("\63-\3\2\2\2\63\60\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2")
        buf.write("\65\66\3\2\2\2\66\7\3\2\2\2\67\65\3\2\2\289\7\13\2\29")
        buf.write(":\7\6\2\2:;\5\6\4\2;\t\3\2\2\2\6\20\"\63\65")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'*'", "'+'", "':='", "'('", "')'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "O_BRA", "C_BRA", "COMA", "NUM", "IDENT", 
                      "WS" ]

    RULE_root = 0
    RULE_literal = 1
    RULE_skyline = 2
    RULE_assig = 3

    ruleNames =  [ "root", "literal", "skyline", "assig" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    O_BRA=5
    C_BRA=6
    COMA=7
    NUM=8
    IDENT=9
    WS=10

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




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.T__0, SkylineParser.O_BRA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.skyline(0)
                self.state = 9
                self.match(SkylineParser.EOF)
                pass
            elif token in [SkylineParser.IDENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.assig()
                self.state = 12
                self.match(SkylineParser.EOF)
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


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def O_BRA(self):
            return self.getToken(SkylineParser.O_BRA, 0)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.COMA)
            else:
                return self.getToken(SkylineParser.COMA, i)

        def C_BRA(self):
            return self.getToken(SkylineParser.C_BRA, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_literal




    def literal(self):

        localctx = SkylineParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(SkylineParser.O_BRA)
            self.state = 17
            self.match(SkylineParser.NUM)
            self.state = 18
            self.match(SkylineParser.COMA)
            self.state = 19
            self.match(SkylineParser.NUM)
            self.state = 20
            self.match(SkylineParser.COMA)
            self.state = 21
            self.match(SkylineParser.NUM)
            self.state = 22
            self.match(SkylineParser.C_BRA)
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

        def literal(self):
            return self.getTypedRuleContext(SkylineParser.LiteralContext,0)


        def O_BRA(self):
            return self.getToken(SkylineParser.O_BRA, 0)

        def skyline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.SkylineContext)
            else:
                return self.getTypedRuleContext(SkylineParser.SkylineContext,i)


        def C_BRA(self):
            return self.getToken(SkylineParser.C_BRA, 0)

        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_skyline



    def skyline(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.SkylineContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_skyline, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 25
                self.literal()
                pass

            elif la_ == 2:
                self.state = 26
                self.match(SkylineParser.O_BRA)
                self.state = 27
                self.skyline(0)
                self.state = 28
                self.match(SkylineParser.C_BRA)
                pass

            elif la_ == 3:
                self.state = 30
                self.match(SkylineParser.T__0)
                self.state = 31
                self.skyline(6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 49
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 34
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 35
                        self.match(SkylineParser.T__1)
                        self.state = 36
                        self.skyline(6)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 37
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 38
                        self.match(SkylineParser.T__2)
                        self.state = 39
                        self.skyline(4)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 40
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 41
                        self.match(SkylineParser.T__1)
                        self.state = 42
                        self.match(SkylineParser.NUM)
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 43
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 44
                        self.match(SkylineParser.T__2)
                        self.state = 45
                        self.match(SkylineParser.NUM)
                        pass

                    elif la_ == 5:
                        localctx = SkylineParser.SkylineContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 46
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 47
                        self.match(SkylineParser.T__0)
                        self.state = 48
                        self.match(SkylineParser.NUM)
                        pass

             
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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

        def IDENT(self):
            return self.getToken(SkylineParser.IDENT, 0)

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_assig




    def assig(self):

        localctx = SkylineParser.AssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(SkylineParser.IDENT)
            self.state = 55
            self.match(SkylineParser.T__3)
            self.state = 56
            self.skyline(0)
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
        self._predicates[2] = self.skyline_sempred
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
         




