# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("\u009d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\6\2#\n\2\r\2\16\2$\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4\60\n\4\f\4\16\4")
        buf.write("\63\13\4\3\5\3\5\3\5\3\5\5\59\n\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\7\6A\n\6\f\6\16\6D\13\6\3\7\3\7\3\7\3\7\7\7J\n\7")
        buf.write("\f\7\16\7M\13\7\3\b\3\b\7\bQ\n\b\f\b\16\bT\13\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\5\t\\\n\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\7\13h\n\13\f\13\16\13k\13\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\7\r\u0080\n\r\f\r\16\r\u0083\13\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u008d\n")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\7\17\u0094\n\17\f\17\16\17")
        buf.write("\u0097\13\17\3\17\3\17\3\20\3\20\3\20\2\3\30\21\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36\2\4\3\2\3\4\3\2\7\b")
        buf.write("\2\u00a0\2\"\3\2\2\2\4(\3\2\2\2\6,\3\2\2\2\b\64\3\2\2")
        buf.write("\2\n=\3\2\2\2\fE\3\2\2\2\16N\3\2\2\2\20[\3\2\2\2\22]\3")
        buf.write("\2\2\2\24b\3\2\2\2\26o\3\2\2\2\30s\3\2\2\2\32\u008c\3")
        buf.write("\2\2\2\34\u008e\3\2\2\2\36\u009a\3\2\2\2 #\5\4\3\2!#\5")
        buf.write("\b\5\2\" \3\2\2\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3")
        buf.write("\2\2\2%&\3\2\2\2&\'\7\2\2\3\'\3\3\2\2\2()\5\36\20\2)*")
        buf.write("\5\6\4\2*+\7\n\2\2+\5\3\2\2\2,\61\7\21\2\2-.\7\13\2\2")
        buf.write(".\60\7\21\2\2/-\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62")
        buf.write("\3\2\2\2\62\7\3\2\2\2\63\61\3\2\2\2\64\65\5\36\20\2\65")
        buf.write("\66\7\21\2\2\668\7\f\2\2\679\5\n\6\28\67\3\2\2\289\3\2")
        buf.write("\2\29:\3\2\2\2:;\7\r\2\2;<\5\16\b\2<\t\3\2\2\2=B\5\f\7")
        buf.write("\2>?\7\n\2\2?A\5\f\7\2@>\3\2\2\2AD\3\2\2\2B@\3\2\2\2B")
        buf.write("C\3\2\2\2C\13\3\2\2\2DB\3\2\2\2EF\5\36\20\2FK\7\21\2\2")
        buf.write("GH\7\13\2\2HJ\7\21\2\2IG\3\2\2\2JM\3\2\2\2KI\3\2\2\2K")
        buf.write("L\3\2\2\2L\r\3\2\2\2MK\3\2\2\2NR\7\16\2\2OQ\5\20\t\2P")
        buf.write("O\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2SU\3\2\2\2TR\3")
        buf.write("\2\2\2UV\7\17\2\2V\17\3\2\2\2W\\\5\4\3\2X\\\5\22\n\2Y")
        buf.write("\\\5\24\13\2Z\\\5\26\f\2[W\3\2\2\2[X\3\2\2\2[Y\3\2\2\2")
        buf.write("[Z\3\2\2\2\\\21\3\2\2\2]^\7\21\2\2^_\7\20\2\2_`\5\30\r")
        buf.write("\2`a\7\n\2\2a\23\3\2\2\2bc\7\21\2\2cd\7\f\2\2di\5\30\r")
        buf.write("\2ef\7\13\2\2fh\5\30\r\2ge\3\2\2\2hk\3\2\2\2ig\3\2\2\2")
        buf.write("ij\3\2\2\2jl\3\2\2\2ki\3\2\2\2lm\7\r\2\2mn\7\n\2\2n\25")
        buf.write("\3\2\2\2op\7\t\2\2pq\5\30\r\2qr\7\n\2\2r\27\3\2\2\2st")
        buf.write("\b\r\1\2tu\5\32\16\2u\u0081\3\2\2\2vw\f\6\2\2wx\t\2\2")
        buf.write("\2x\u0080\5\30\r\7yz\f\5\2\2z{\7\5\2\2{\u0080\5\30\r\6")
        buf.write("|}\f\4\2\2}~\7\6\2\2~\u0080\5\30\r\5\177v\3\2\2\2\177")
        buf.write("y\3\2\2\2\177|\3\2\2\2\u0080\u0083\3\2\2\2\u0081\177\3")
        buf.write("\2\2\2\u0081\u0082\3\2\2\2\u0082\31\3\2\2\2\u0083\u0081")
        buf.write("\3\2\2\2\u0084\u008d\5\34\17\2\u0085\u008d\7\21\2\2\u0086")
        buf.write("\u008d\7\22\2\2\u0087\u008d\7\23\2\2\u0088\u0089\7\f\2")
        buf.write("\2\u0089\u008a\5\30\r\2\u008a\u008b\7\r\2\2\u008b\u008d")
        buf.write("\3\2\2\2\u008c\u0084\3\2\2\2\u008c\u0085\3\2\2\2\u008c")
        buf.write("\u0086\3\2\2\2\u008c\u0087\3\2\2\2\u008c\u0088\3\2\2\2")
        buf.write("\u008d\33\3\2\2\2\u008e\u008f\7\21\2\2\u008f\u0090\7\f")
        buf.write("\2\2\u0090\u0095\5\30\r\2\u0091\u0092\7\13\2\2\u0092\u0094")
        buf.write("\5\30\r\2\u0093\u0091\3\2\2\2\u0094\u0097\3\2\2\2\u0095")
        buf.write("\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\3\2\2\2")
        buf.write("\u0097\u0095\3\2\2\2\u0098\u0099\7\r\2\2\u0099\35\3\2")
        buf.write("\2\2\u009a\u009b\t\3\2\2\u009b\37\3\2\2\2\17\"$\618BK")
        buf.write("R[i\177\u0081\u008c\u0095")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'-'", "'+'", "'int'", "'float'", 
                     "'return'", "';'", "','", "'('", "')'", "'{'", "'}'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "FLOAT", "RETURN", "SEMICOLON", 
                      "COMMA", "LB", "RB", "LCB", "RCB", "ASSIGN", "ID", 
                      "INTLIT", "FLOATLIT", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_var_decl = 1
    RULE_var = 2
    RULE_func_decl = 3
    RULE_params = 4
    RULE_param = 5
    RULE_body = 6
    RULE_stm = 7
    RULE_assign_stm = 8
    RULE_call_stm = 9
    RULE_return_stm = 10
    RULE_expr = 11
    RULE_operand = 12
    RULE_func = 13
    RULE_types = 14

    ruleNames =  [ "program", "var_decl", "var", "func_decl", "params", 
                   "param", "body", "stm", "assign_stm", "call_stm", "return_stm", 
                   "expr", "operand", "func", "types" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    INT=5
    FLOAT=6
    RETURN=7
    SEMICOLON=8
    COMMA=9
    LB=10
    RB=11
    LCB=12
    RCB=13
    ASSIGN=14
    ID=15
    INTLIT=16
    FLOATLIT=17
    WS=18
    ERROR_CHAR=19

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

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declContext,i)


        def func_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Func_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Func_declContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 30
                    self.var_decl()
                    pass

                elif la_ == 2:
                    self.state = 31
                    self.func_decl()
                    pass


                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.INT or _la==BKOOLParser.FLOAT):
                    break

            self.state = 36
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(BKOOLParser.TypesContext,0)


        def var(self):
            return self.getTypedRuleContext(BKOOLParser.VarContext,0)


        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = BKOOLParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.types()
            self.state = 39
            self.var()
            self.state = 40
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = BKOOLParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(BKOOLParser.ID)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 43
                self.match(BKOOLParser.COMMA)
                self.state = 44
                self.match(BKOOLParser.ID)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(BKOOLParser.TypesContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def params(self):
            return self.getTypedRuleContext(BKOOLParser.ParamsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = BKOOLParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.types()
            self.state = 51
            self.match(BKOOLParser.ID)
            self.state = 52
            self.match(BKOOLParser.LB)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.INT or _la==BKOOLParser.FLOAT:
                self.state = 53
                self.params()


            self.state = 56
            self.match(BKOOLParser.RB)
            self.state = 57
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ParamContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ParamContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SEMICOLON)
            else:
                return self.getToken(BKOOLParser.SEMICOLON, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = BKOOLParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.param()
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.SEMICOLON:
                self.state = 60
                self.match(BKOOLParser.SEMICOLON)
                self.state = 61
                self.param()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(BKOOLParser.TypesContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.types()
            self.state = 68
            self.match(BKOOLParser.ID)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 69
                self.match(BKOOLParser.COMMA)
                self.state = 70
                self.match(BKOOLParser.ID)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(BKOOLParser.LCB)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.ID))) != 0):
                self.state = 77
                self.stm()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 83
            self.match(BKOOLParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Var_declContext,0)


        def assign_stm(self):
            return self.getTypedRuleContext(BKOOLParser.Assign_stmContext,0)


        def call_stm(self):
            return self.getTypedRuleContext(BKOOLParser.Call_stmContext,0)


        def return_stm(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stmContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm" ):
                return visitor.visitStm(self)
            else:
                return visitor.visitChildren(self)




    def stm(self):

        localctx = BKOOLParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stm)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.assign_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.call_stm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.return_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assign_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stm" ):
                return visitor.visitAssign_stm(self)
            else:
                return visitor.visitChildren(self)




    def assign_stm(self):

        localctx = BKOOLParser.Assign_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assign_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(BKOOLParser.ID)
            self.state = 92
            self.match(BKOOLParser.ASSIGN)
            self.state = 93
            self.expr(0)
            self.state = 94
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_call_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stm" ):
                return visitor.visitCall_stm(self)
            else:
                return visitor.visitChildren(self)




    def call_stm(self):

        localctx = BKOOLParser.Call_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_call_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(BKOOLParser.ID)
            self.state = 97
            self.match(BKOOLParser.LB)

            self.state = 98
            self.expr(0)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 99
                self.match(BKOOLParser.COMMA)
                self.state = 100
                self.expr(0)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(BKOOLParser.RB)
            self.state = 107
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_return_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stm" ):
                return visitor.visitReturn_stm(self)
            else:
                return visitor.visitChildren(self)




    def return_stm(self):

        localctx = BKOOLParser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_return_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(BKOOLParser.RETURN)
            self.state = 110
            self.expr(0)
            self.state = 111
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(BKOOLParser.OperandContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 125
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 116
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 117
                        _la = self._input.LA(1)
                        if not(_la==BKOOLParser.T__0 or _la==BKOOLParser.T__1):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 118
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 119
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 120
                        self.match(BKOOLParser.T__2)
                        self.state = 121
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 122
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 123
                        self.match(BKOOLParser.T__3)
                        self.state = 124
                        self.expr(3)
                        pass

             
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func(self):
            return self.getTypedRuleContext(BKOOLParser.FuncContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKOOLParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_operand)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.func()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.match(BKOOLParser.INTLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 133
                self.match(BKOOLParser.FLOATLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 134
                self.match(BKOOLParser.LB)
                self.state = 135
                self.expr(0)
                self.state = 136
                self.match(BKOOLParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = BKOOLParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(BKOOLParser.ID)
            self.state = 141
            self.match(BKOOLParser.LB)

            self.state = 142
            self.expr(0)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 143
                self.match(BKOOLParser.COMMA)
                self.state = 144
                self.expr(0)
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = BKOOLParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.INT or _la==BKOOLParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
        self._predicates[11] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




