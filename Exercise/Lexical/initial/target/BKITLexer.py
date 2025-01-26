# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("G\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\6\2\32\n\2")
        buf.write("\r\2\16\2\33\3\3\3\3\3\3\7\3!\n\3\f\3\16\3$\13\3\3\3\3")
        buf.write("\3\5\3(\n\3\3\4\3\4\3\5\3\5\3\6\5\6/\n\6\3\6\6\6\62\n")
        buf.write("\6\r\6\16\6\63\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\n\6\n")
        buf.write("?\n\n\r\n\16\n@\3\n\3\n\3\13\3\13\3\13\2\2\f\3\3\5\4\7")
        buf.write("\2\t\2\13\2\r\5\17\6\21\7\23\b\25\t\3\2\7\3\2c|\4\2\62")
        buf.write(";c|\3\2\62;\3\2\63;\5\2\13\f\17\17\"\"\2I\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\'\3\2\2\2\7)\3\2")
        buf.write("\2\2\t+\3\2\2\2\13.\3\2\2\2\r\65\3\2\2\2\17\67\3\2\2\2")
        buf.write("\219\3\2\2\2\23>\3\2\2\2\25D\3\2\2\2\27\31\t\2\2\2\30")
        buf.write("\32\t\3\2\2\31\30\3\2\2\2\32\33\3\2\2\2\33\31\3\2\2\2")
        buf.write("\33\34\3\2\2\2\34\4\3\2\2\2\35(\7\62\2\2\36\"\5\t\5\2")
        buf.write("\37!\5\13\6\2 \37\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2")
        buf.write("\2\2#%\3\2\2\2$\"\3\2\2\2%&\b\3\2\2&(\3\2\2\2\'\35\3\2")
        buf.write("\2\2\'\36\3\2\2\2(\6\3\2\2\2)*\t\4\2\2*\b\3\2\2\2+,\t")
        buf.write("\5\2\2,\n\3\2\2\2-/\7a\2\2.-\3\2\2\2./\3\2\2\2/\61\3\2")
        buf.write("\2\2\60\62\5\7\4\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3")
        buf.write("\2\2\2\63\64\3\2\2\2\64\f\3\2\2\2\65\66\7=\2\2\66\16\3")
        buf.write("\2\2\2\678\7<\2\28\20\3\2\2\29:\7X\2\2:;\7c\2\2;<\7t\2")
        buf.write("\2<\22\3\2\2\2=?\t\6\2\2>=\3\2\2\2?@\3\2\2\2@>\3\2\2\2")
        buf.write("@A\3\2\2\2AB\3\2\2\2BC\b\n\3\2C\24\3\2\2\2DE\13\2\2\2")
        buf.write("EF\b\13\4\2F\26\3\2\2\2\t\2\33\"\'.\63@\5\3\3\2\b\2\2")
        buf.write("\3\13\3")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    INTEGER = 2
    SEMI = 3
    COLON = 4
    VAR = 5
    WS = 6
    ERROR_CHAR = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':'", "'Var'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INTEGER", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR" ]

    ruleNames = [ "ID", "INTEGER", "DIGIT", "NON_ZERO_DIGIT", "DIGIT_UNDERSCORE", 
                  "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.INTEGER_action 
            actions[9] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     


