# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\13\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2")
        buf.write("\t\2\4\3\2\2\2\4\5\7\7\2\2\5\6\7\6\2\2\6\7\7\3\2\2\7\b")
        buf.write("\7\5\2\2\b\t\7\2\2\3\t\3\3\2\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "';'", "':'", 
                     "'Var'" ]

    symbolicNames = [ "<INVALID>", "ID", "INTEGER", "SEMI", "COLON", "VAR", 
                      "WS", "ERROR_CHAR" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    ID=1
    INTEGER=2
    SEMI=3
    COLON=4
    VAR=5
    WS=6
    ERROR_CHAR=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(BKITParser.VAR)
            self.state = 3
            self.match(BKITParser.COLON)
            self.state = 4
            self.match(BKITParser.ID)
            self.state = 5
            self.match(BKITParser.SEMI)
            self.state = 6
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





