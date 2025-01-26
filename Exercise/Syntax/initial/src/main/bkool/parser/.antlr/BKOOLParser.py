# Generated from c:/Users/Huy/Documents/Tuan_Huy/CO3005_PPL/Exercise/Syntax/initial/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,155,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,4,0,33,8,0,11,0,12,0,34,1,0,1,0,1,1,1,1,1,1,1,
        1,1,2,1,2,1,2,5,2,46,8,2,10,2,12,2,49,9,2,1,3,1,3,1,3,1,3,3,3,55,
        8,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,63,8,4,10,4,12,4,66,9,4,1,5,1,5,
        1,5,1,5,5,5,72,8,5,10,5,12,5,75,9,5,1,6,1,6,5,6,79,8,6,10,6,12,6,
        82,9,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,90,8,7,1,8,1,8,1,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,9,5,9,102,8,9,10,9,12,9,105,9,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,5,11,126,8,11,10,11,12,11,129,9,11,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,3,12,139,8,12,1,13,1,13,1,13,1,13,1,13,5,13,
        146,8,13,10,13,12,13,149,9,13,1,13,1,13,1,14,1,14,1,14,0,1,22,15,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,2,1,0,1,2,1,0,5,6,158,
        0,32,1,0,0,0,2,38,1,0,0,0,4,42,1,0,0,0,6,50,1,0,0,0,8,59,1,0,0,0,
        10,67,1,0,0,0,12,76,1,0,0,0,14,89,1,0,0,0,16,91,1,0,0,0,18,96,1,
        0,0,0,20,109,1,0,0,0,22,113,1,0,0,0,24,138,1,0,0,0,26,140,1,0,0,
        0,28,152,1,0,0,0,30,33,3,2,1,0,31,33,3,6,3,0,32,30,1,0,0,0,32,31,
        1,0,0,0,33,34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,36,1,0,0,0,
        36,37,5,0,0,1,37,1,1,0,0,0,38,39,3,28,14,0,39,40,3,4,2,0,40,41,5,
        8,0,0,41,3,1,0,0,0,42,47,5,15,0,0,43,44,5,9,0,0,44,46,5,15,0,0,45,
        43,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,5,1,0,0,
        0,49,47,1,0,0,0,50,51,3,28,14,0,51,52,5,15,0,0,52,54,5,10,0,0,53,
        55,3,8,4,0,54,53,1,0,0,0,54,55,1,0,0,0,55,56,1,0,0,0,56,57,5,11,
        0,0,57,58,3,12,6,0,58,7,1,0,0,0,59,64,3,10,5,0,60,61,5,8,0,0,61,
        63,3,10,5,0,62,60,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,
        0,0,65,9,1,0,0,0,66,64,1,0,0,0,67,68,3,28,14,0,68,73,5,15,0,0,69,
        70,5,9,0,0,70,72,5,15,0,0,71,69,1,0,0,0,72,75,1,0,0,0,73,71,1,0,
        0,0,73,74,1,0,0,0,74,11,1,0,0,0,75,73,1,0,0,0,76,80,5,12,0,0,77,
        79,3,14,7,0,78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,
        0,0,81,83,1,0,0,0,82,80,1,0,0,0,83,84,5,13,0,0,84,13,1,0,0,0,85,
        90,3,2,1,0,86,90,3,16,8,0,87,90,3,18,9,0,88,90,3,20,10,0,89,85,1,
        0,0,0,89,86,1,0,0,0,89,87,1,0,0,0,89,88,1,0,0,0,90,15,1,0,0,0,91,
        92,5,15,0,0,92,93,5,14,0,0,93,94,3,22,11,0,94,95,5,8,0,0,95,17,1,
        0,0,0,96,97,5,15,0,0,97,98,5,10,0,0,98,103,3,22,11,0,99,100,5,9,
        0,0,100,102,3,22,11,0,101,99,1,0,0,0,102,105,1,0,0,0,103,101,1,0,
        0,0,103,104,1,0,0,0,104,106,1,0,0,0,105,103,1,0,0,0,106,107,5,11,
        0,0,107,108,5,8,0,0,108,19,1,0,0,0,109,110,5,7,0,0,110,111,3,22,
        11,0,111,112,5,8,0,0,112,21,1,0,0,0,113,114,6,11,-1,0,114,115,3,
        24,12,0,115,127,1,0,0,0,116,117,10,4,0,0,117,118,7,0,0,0,118,126,
        3,22,11,5,119,120,10,3,0,0,120,121,5,3,0,0,121,126,3,22,11,4,122,
        123,10,2,0,0,123,124,5,4,0,0,124,126,3,22,11,3,125,116,1,0,0,0,125,
        119,1,0,0,0,125,122,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,
        128,1,0,0,0,128,23,1,0,0,0,129,127,1,0,0,0,130,139,3,26,13,0,131,
        139,5,15,0,0,132,139,5,16,0,0,133,139,5,17,0,0,134,135,5,10,0,0,
        135,136,3,22,11,0,136,137,5,11,0,0,137,139,1,0,0,0,138,130,1,0,0,
        0,138,131,1,0,0,0,138,132,1,0,0,0,138,133,1,0,0,0,138,134,1,0,0,
        0,139,25,1,0,0,0,140,141,5,15,0,0,141,142,5,10,0,0,142,147,3,22,
        11,0,143,144,5,9,0,0,144,146,3,22,11,0,145,143,1,0,0,0,146,149,1,
        0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,150,1,0,0,0,149,147,1,
        0,0,0,150,151,5,11,0,0,151,27,1,0,0,0,152,153,7,1,0,0,153,29,1,0,
        0,0,13,32,34,47,54,64,73,80,89,103,125,127,138,147
    ]

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
        self.checkVersion("4.13.1")
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
                if not (_la==5 or _la==6):
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
            while _la==9:
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
            if _la==5 or _la==6:
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
            while _la==8:
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
            while _la==9:
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 32992) != 0):
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
            while _la==9:
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
                        if not(_la==1 or _la==2):
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
            while _la==9:
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




    def types(self):

        localctx = BKOOLParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
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
         




