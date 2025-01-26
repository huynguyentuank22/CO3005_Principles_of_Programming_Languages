# Generated from c:/Users/Huy/Documents/Tuan_Huy/CO3005_PPL/Exercise/Syntax/initial/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,19,102,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,
        0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,
        1,11,1,11,1,12,1,12,1,13,1,13,1,14,4,14,80,8,14,11,14,12,14,81,1,
        15,4,15,85,8,15,11,15,12,15,86,1,16,1,16,1,16,1,16,1,17,4,17,94,
        8,17,11,17,12,17,95,1,17,1,17,1,18,1,18,1,18,0,0,19,1,1,3,2,5,3,
        7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,
        31,16,33,17,35,18,37,19,1,0,3,2,0,65,90,97,122,1,0,48,57,3,0,9,10,
        13,13,32,32,104,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,
        0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,
        0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,
        0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,
        1,39,1,0,0,0,3,41,1,0,0,0,5,43,1,0,0,0,7,45,1,0,0,0,9,47,1,0,0,0,
        11,51,1,0,0,0,13,57,1,0,0,0,15,64,1,0,0,0,17,66,1,0,0,0,19,68,1,
        0,0,0,21,70,1,0,0,0,23,72,1,0,0,0,25,74,1,0,0,0,27,76,1,0,0,0,29,
        79,1,0,0,0,31,84,1,0,0,0,33,88,1,0,0,0,35,93,1,0,0,0,37,99,1,0,0,
        0,39,40,5,42,0,0,40,2,1,0,0,0,41,42,5,47,0,0,42,4,1,0,0,0,43,44,
        5,45,0,0,44,6,1,0,0,0,45,46,5,43,0,0,46,8,1,0,0,0,47,48,5,105,0,
        0,48,49,5,110,0,0,49,50,5,116,0,0,50,10,1,0,0,0,51,52,5,102,0,0,
        52,53,5,108,0,0,53,54,5,111,0,0,54,55,5,97,0,0,55,56,5,116,0,0,56,
        12,1,0,0,0,57,58,5,114,0,0,58,59,5,101,0,0,59,60,5,116,0,0,60,61,
        5,117,0,0,61,62,5,114,0,0,62,63,5,110,0,0,63,14,1,0,0,0,64,65,5,
        59,0,0,65,16,1,0,0,0,66,67,5,44,0,0,67,18,1,0,0,0,68,69,5,40,0,0,
        69,20,1,0,0,0,70,71,5,41,0,0,71,22,1,0,0,0,72,73,5,123,0,0,73,24,
        1,0,0,0,74,75,5,125,0,0,75,26,1,0,0,0,76,77,5,61,0,0,77,28,1,0,0,
        0,78,80,7,0,0,0,79,78,1,0,0,0,80,81,1,0,0,0,81,79,1,0,0,0,81,82,
        1,0,0,0,82,30,1,0,0,0,83,85,7,1,0,0,84,83,1,0,0,0,85,86,1,0,0,0,
        86,84,1,0,0,0,86,87,1,0,0,0,87,32,1,0,0,0,88,89,3,31,15,0,89,90,
        5,46,0,0,90,91,3,31,15,0,91,34,1,0,0,0,92,94,7,2,0,0,93,92,1,0,0,
        0,94,95,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,97,1,0,0,0,97,98,
        6,17,0,0,98,36,1,0,0,0,99,100,9,0,0,0,100,101,6,18,1,0,101,38,1,
        0,0,0,4,0,81,86,95,2,6,0,0,1,18,0
    ]

class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    INT = 5
    FLOAT = 6
    RETURN = 7
    SEMICOLON = 8
    COMMA = 9
    LB = 10
    RB = 11
    LCB = 12
    RCB = 13
    ASSIGN = 14
    ID = 15
    INTLIT = 16
    FLOATLIT = 17
    WS = 18
    ERROR_CHAR = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'-'", "'+'", "'int'", "'float'", "'return'", 
            "';'", "','", "'('", "')'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "RETURN", "SEMICOLON", "COMMA", "LB", "RB", 
            "LCB", "RCB", "ASSIGN", "ID", "INTLIT", "FLOATLIT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "INT", "FLOAT", "RETURN", 
                  "SEMICOLON", "COMMA", "LB", "RB", "LCB", "RCB", "ASSIGN", 
                  "ID", "INTLIT", "FLOATLIT", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[18] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


