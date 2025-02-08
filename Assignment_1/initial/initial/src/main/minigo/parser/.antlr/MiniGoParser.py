# Generated from c:/Users/Huy/Documents/Tuan_Huy/CO3005_PPL/Assignment_1/initial/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
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
        4,1,69,550,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,1,0,4,0,112,8,0,11,0,12,0,113,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,126,8,1,1,2,1,2,1,2,3,2,131,8,2,1,
        3,1,3,1,4,3,4,136,8,4,1,4,1,4,1,4,1,4,3,4,142,8,4,1,4,1,4,3,4,146,
        8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,
        3,7,163,8,7,1,7,1,7,1,7,3,7,168,8,7,1,7,1,7,3,7,172,8,7,1,7,1,7,
        5,7,176,8,7,10,7,12,7,179,9,7,1,7,1,7,1,7,1,8,1,8,3,8,186,8,8,1,
        8,1,8,1,8,3,8,191,8,8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,199,8,9,10,9,12,
        9,202,9,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,5,11,212,8,11,
        10,11,12,11,215,9,11,1,12,1,12,3,12,219,8,12,1,13,1,13,1,13,3,13,
        224,8,13,1,14,1,14,1,15,1,15,1,16,1,16,4,16,232,8,16,11,16,12,16,
        233,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,3,17,245,8,17,1,
        17,1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,3,19,257,8,19,1,
        20,1,20,1,20,4,20,262,8,20,11,20,12,20,263,1,21,1,21,1,21,1,22,1,
        22,1,22,1,22,5,22,273,8,22,10,22,12,22,276,9,22,1,22,1,22,1,23,1,
        23,3,23,282,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,
        25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,5,27,304,8,
        27,10,27,12,27,307,9,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,3,28,
        316,8,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,5,29,325,8,29,10,29,
        12,29,328,9,29,3,29,330,8,29,1,29,1,29,1,30,1,30,1,30,1,30,1,31,
        1,31,1,31,1,31,1,31,1,32,1,32,1,32,5,32,346,8,32,10,32,12,32,349,
        9,32,1,32,1,32,1,33,1,33,1,33,3,33,356,8,33,1,33,1,33,3,33,360,8,
        33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,3,34,370,8,34,1,34,1,
        34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,
        34,1,34,4,34,388,8,34,11,34,12,34,389,1,34,1,34,1,34,5,34,395,8,
        34,10,34,12,34,398,9,34,1,35,1,35,1,35,1,35,1,35,1,35,3,35,406,8,
        35,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,417,8,36,1,
        37,1,37,5,37,421,8,37,10,37,12,37,424,9,37,1,37,1,37,1,37,1,37,1,
        38,1,38,1,38,1,38,1,38,1,38,5,38,436,8,38,10,38,12,38,439,9,38,1,
        38,1,38,5,38,443,8,38,10,38,12,38,446,9,38,1,38,1,38,1,38,5,38,451,
        8,38,10,38,12,38,454,9,38,1,38,3,38,457,8,38,1,38,1,38,1,39,1,39,
        1,39,1,39,1,39,1,39,1,39,5,39,468,8,39,10,39,12,39,471,9,39,1,39,
        1,39,1,40,1,40,1,40,1,40,5,40,479,8,40,10,40,12,40,482,9,40,1,40,
        1,40,1,40,1,41,1,41,1,41,3,41,490,8,41,1,42,3,42,493,8,42,1,42,1,
        42,3,42,497,8,42,1,42,1,42,3,42,501,8,42,1,43,1,43,1,43,1,43,1,44,
        1,44,5,44,509,8,44,10,44,12,44,512,9,44,1,44,1,44,1,44,1,45,1,45,
        1,45,1,45,1,45,1,45,1,45,1,46,1,46,1,46,1,47,1,47,1,47,1,48,1,48,
        3,48,532,8,48,1,48,1,48,1,49,1,49,1,50,1,50,1,51,1,51,1,52,1,52,
        1,53,1,53,1,53,1,53,1,54,1,54,1,54,0,1,68,55,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,
        102,104,106,108,0,9,2,0,53,53,58,61,1,0,10,13,1,0,36,37,2,0,1,1,
        62,62,1,0,33,35,1,0,22,26,1,0,27,32,1,0,38,42,2,0,52,52,66,66,566,
        0,111,1,0,0,0,2,125,1,0,0,0,4,130,1,0,0,0,6,132,1,0,0,0,8,135,1,
        0,0,0,10,149,1,0,0,0,12,154,1,0,0,0,14,160,1,0,0,0,16,185,1,0,0,
        0,18,195,1,0,0,0,20,203,1,0,0,0,22,208,1,0,0,0,24,216,1,0,0,0,26,
        223,1,0,0,0,28,225,1,0,0,0,30,227,1,0,0,0,32,229,1,0,0,0,34,239,
        1,0,0,0,36,248,1,0,0,0,38,253,1,0,0,0,40,261,1,0,0,0,42,265,1,0,
        0,0,44,268,1,0,0,0,46,281,1,0,0,0,48,283,1,0,0,0,50,290,1,0,0,0,
        52,295,1,0,0,0,54,300,1,0,0,0,56,310,1,0,0,0,58,319,1,0,0,0,60,333,
        1,0,0,0,62,337,1,0,0,0,64,342,1,0,0,0,66,352,1,0,0,0,68,369,1,0,
        0,0,70,405,1,0,0,0,72,416,1,0,0,0,74,418,1,0,0,0,76,429,1,0,0,0,
        78,460,1,0,0,0,80,474,1,0,0,0,82,489,1,0,0,0,84,492,1,0,0,0,86,502,
        1,0,0,0,88,506,1,0,0,0,90,516,1,0,0,0,92,523,1,0,0,0,94,526,1,0,
        0,0,96,529,1,0,0,0,98,535,1,0,0,0,100,537,1,0,0,0,102,539,1,0,0,
        0,104,541,1,0,0,0,106,543,1,0,0,0,108,547,1,0,0,0,110,112,3,72,36,
        0,111,110,1,0,0,0,112,113,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,
        0,114,115,1,0,0,0,115,116,5,0,0,1,116,1,1,0,0,0,117,126,3,14,7,0,
        118,126,3,8,4,0,119,126,3,10,5,0,120,126,3,12,6,0,121,126,3,34,17,
        0,122,126,3,36,18,0,123,126,3,52,26,0,124,126,3,62,31,0,125,117,
        1,0,0,0,125,118,1,0,0,0,125,119,1,0,0,0,125,120,1,0,0,0,125,121,
        1,0,0,0,125,122,1,0,0,0,125,123,1,0,0,0,125,124,1,0,0,0,126,3,1,
        0,0,0,127,131,3,32,16,0,128,131,3,50,25,0,129,131,3,48,24,0,130,
        127,1,0,0,0,130,128,1,0,0,0,130,129,1,0,0,0,131,5,1,0,0,0,132,133,
        3,16,8,0,133,7,1,0,0,0,134,136,5,15,0,0,135,134,1,0,0,0,135,136,
        1,0,0,0,136,137,1,0,0,0,137,145,5,62,0,0,138,141,3,30,15,0,139,140,
        5,36,0,0,140,142,3,68,34,0,141,139,1,0,0,0,141,142,1,0,0,0,142,146,
        1,0,0,0,143,144,5,36,0,0,144,146,3,68,34,0,145,138,1,0,0,0,145,143,
        1,0,0,0,146,147,1,0,0,0,147,148,3,108,54,0,148,9,1,0,0,0,149,150,
        5,62,0,0,150,151,5,37,0,0,151,152,3,68,34,0,152,153,3,108,54,0,153,
        11,1,0,0,0,154,155,5,14,0,0,155,156,5,62,0,0,156,157,5,36,0,0,157,
        158,3,68,34,0,158,159,3,108,54,0,159,13,1,0,0,0,160,162,5,6,0,0,
        161,163,3,20,10,0,162,161,1,0,0,0,162,163,1,0,0,0,163,164,1,0,0,
        0,164,165,5,62,0,0,165,167,5,44,0,0,166,168,3,22,11,0,167,166,1,
        0,0,0,167,168,1,0,0,0,168,169,1,0,0,0,169,171,5,45,0,0,170,172,3,
        26,13,0,171,170,1,0,0,0,171,172,1,0,0,0,172,173,1,0,0,0,173,177,
        5,46,0,0,174,176,3,72,36,0,175,174,1,0,0,0,176,179,1,0,0,0,177,175,
        1,0,0,0,177,178,1,0,0,0,178,180,1,0,0,0,179,177,1,0,0,0,180,181,
        5,47,0,0,181,182,3,108,54,0,182,15,1,0,0,0,183,184,5,62,0,0,184,
        186,5,43,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,187,1,0,0,0,187,
        188,5,62,0,0,188,190,5,44,0,0,189,191,3,18,9,0,190,189,1,0,0,0,190,
        191,1,0,0,0,191,192,1,0,0,0,192,193,5,45,0,0,193,194,3,108,54,0,
        194,17,1,0,0,0,195,200,3,68,34,0,196,197,5,50,0,0,197,199,3,68,34,
        0,198,196,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,
        0,201,19,1,0,0,0,202,200,1,0,0,0,203,204,5,44,0,0,204,205,5,62,0,
        0,205,206,5,62,0,0,206,207,5,45,0,0,207,21,1,0,0,0,208,213,3,24,
        12,0,209,210,5,50,0,0,210,212,3,24,12,0,211,209,1,0,0,0,212,215,
        1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,23,1,0,0,0,215,213,1,
        0,0,0,216,218,5,62,0,0,217,219,3,26,13,0,218,217,1,0,0,0,218,219,
        1,0,0,0,219,25,1,0,0,0,220,224,3,30,15,0,221,224,3,38,19,0,222,224,
        5,62,0,0,223,220,1,0,0,0,223,221,1,0,0,0,223,222,1,0,0,0,224,27,
        1,0,0,0,225,226,7,0,0,0,226,29,1,0,0,0,227,228,7,1,0,0,228,31,1,
        0,0,0,229,231,5,62,0,0,230,232,3,106,53,0,231,230,1,0,0,0,232,233,
        1,0,0,0,233,231,1,0,0,0,233,234,1,0,0,0,234,235,1,0,0,0,235,236,
        5,36,0,0,236,237,3,68,34,0,237,238,3,108,54,0,238,33,1,0,0,0,239,
        240,5,15,0,0,240,244,5,62,0,0,241,245,3,38,19,0,242,243,5,36,0,0,
        243,245,3,42,21,0,244,241,1,0,0,0,244,242,1,0,0,0,245,246,1,0,0,
        0,246,247,3,108,54,0,247,35,1,0,0,0,248,249,5,62,0,0,249,250,5,37,
        0,0,250,251,3,42,21,0,251,252,3,108,54,0,252,37,1,0,0,0,253,256,
        3,40,20,0,254,257,3,30,15,0,255,257,5,62,0,0,256,254,1,0,0,0,256,
        255,1,0,0,0,257,39,1,0,0,0,258,259,5,48,0,0,259,260,5,53,0,0,260,
        262,5,49,0,0,261,258,1,0,0,0,262,263,1,0,0,0,263,261,1,0,0,0,263,
        264,1,0,0,0,264,41,1,0,0,0,265,266,3,38,19,0,266,267,3,44,22,0,267,
        43,1,0,0,0,268,269,5,46,0,0,269,274,3,46,23,0,270,271,5,50,0,0,271,
        273,3,46,23,0,272,270,1,0,0,0,273,276,1,0,0,0,274,272,1,0,0,0,274,
        275,1,0,0,0,275,277,1,0,0,0,276,274,1,0,0,0,277,278,5,47,0,0,278,
        45,1,0,0,0,279,282,3,44,22,0,280,282,3,28,14,0,281,279,1,0,0,0,281,
        280,1,0,0,0,282,47,1,0,0,0,283,284,5,62,0,0,284,285,5,43,0,0,285,
        286,5,62,0,0,286,287,5,36,0,0,287,288,3,68,34,0,288,289,3,108,54,
        0,289,49,1,0,0,0,290,291,5,62,0,0,291,292,5,37,0,0,292,293,3,58,
        29,0,293,294,3,108,54,0,294,51,1,0,0,0,295,296,5,7,0,0,296,297,5,
        62,0,0,297,298,3,54,27,0,298,299,3,108,54,0,299,53,1,0,0,0,300,301,
        5,8,0,0,301,305,5,46,0,0,302,304,3,56,28,0,303,302,1,0,0,0,304,307,
        1,0,0,0,305,303,1,0,0,0,305,306,1,0,0,0,306,308,1,0,0,0,307,305,
        1,0,0,0,308,309,5,47,0,0,309,55,1,0,0,0,310,315,5,62,0,0,311,316,
        3,30,15,0,312,316,3,38,19,0,313,316,3,54,27,0,314,316,5,62,0,0,315,
        311,1,0,0,0,315,312,1,0,0,0,315,313,1,0,0,0,315,314,1,0,0,0,316,
        317,1,0,0,0,317,318,3,108,54,0,318,57,1,0,0,0,319,320,5,62,0,0,320,
        329,5,46,0,0,321,326,3,60,30,0,322,323,5,50,0,0,323,325,3,60,30,
        0,324,322,1,0,0,0,325,328,1,0,0,0,326,324,1,0,0,0,326,327,1,0,0,
        0,327,330,1,0,0,0,328,326,1,0,0,0,329,321,1,0,0,0,329,330,1,0,0,
        0,330,331,1,0,0,0,331,332,5,47,0,0,332,59,1,0,0,0,333,334,5,62,0,
        0,334,335,5,51,0,0,335,336,3,68,34,0,336,61,1,0,0,0,337,338,5,7,
        0,0,338,339,5,62,0,0,339,340,3,64,32,0,340,341,3,108,54,0,341,63,
        1,0,0,0,342,343,5,9,0,0,343,347,5,46,0,0,344,346,3,66,33,0,345,344,
        1,0,0,0,346,349,1,0,0,0,347,345,1,0,0,0,347,348,1,0,0,0,348,350,
        1,0,0,0,349,347,1,0,0,0,350,351,5,47,0,0,351,65,1,0,0,0,352,353,
        5,62,0,0,353,355,5,44,0,0,354,356,3,22,11,0,355,354,1,0,0,0,355,
        356,1,0,0,0,356,357,1,0,0,0,357,359,5,45,0,0,358,360,3,26,13,0,359,
        358,1,0,0,0,359,360,1,0,0,0,360,361,1,0,0,0,361,362,3,108,54,0,362,
        67,1,0,0,0,363,364,6,34,-1,0,364,365,5,35,0,0,365,370,3,68,34,5,
        366,367,5,23,0,0,367,370,3,68,34,4,368,370,3,70,35,0,369,363,1,0,
        0,0,369,366,1,0,0,0,369,368,1,0,0,0,370,396,1,0,0,0,371,372,10,9,
        0,0,372,373,5,34,0,0,373,395,3,68,34,10,374,375,10,8,0,0,375,376,
        5,33,0,0,376,395,3,68,34,9,377,378,10,7,0,0,378,379,3,102,51,0,379,
        380,3,68,34,8,380,395,1,0,0,0,381,382,10,6,0,0,382,383,3,100,50,
        0,383,384,3,68,34,7,384,395,1,0,0,0,385,387,10,3,0,0,386,388,3,106,
        53,0,387,386,1,0,0,0,388,389,1,0,0,0,389,387,1,0,0,0,389,390,1,0,
        0,0,390,395,1,0,0,0,391,392,10,2,0,0,392,393,5,43,0,0,393,395,5,
        62,0,0,394,371,1,0,0,0,394,374,1,0,0,0,394,377,1,0,0,0,394,381,1,
        0,0,0,394,385,1,0,0,0,394,391,1,0,0,0,395,398,1,0,0,0,396,394,1,
        0,0,0,396,397,1,0,0,0,397,69,1,0,0,0,398,396,1,0,0,0,399,406,5,62,
        0,0,400,406,3,28,14,0,401,402,5,44,0,0,402,403,3,68,34,0,403,404,
        5,45,0,0,404,406,1,0,0,0,405,399,1,0,0,0,405,400,1,0,0,0,405,401,
        1,0,0,0,406,71,1,0,0,0,407,417,3,2,1,0,408,417,3,4,2,0,409,417,3,
        6,3,0,410,417,3,74,37,0,411,417,3,76,38,0,412,417,3,80,40,0,413,
        417,3,92,46,0,414,417,3,94,47,0,415,417,3,96,48,0,416,407,1,0,0,
        0,416,408,1,0,0,0,416,409,1,0,0,0,416,410,1,0,0,0,416,411,1,0,0,
        0,416,412,1,0,0,0,416,413,1,0,0,0,416,414,1,0,0,0,416,415,1,0,0,
        0,417,73,1,0,0,0,418,422,5,62,0,0,419,421,3,106,53,0,420,419,1,0,
        0,0,421,424,1,0,0,0,422,420,1,0,0,0,422,423,1,0,0,0,423,425,1,0,
        0,0,424,422,1,0,0,0,425,426,3,104,52,0,426,427,3,68,34,0,427,428,
        3,108,54,0,428,75,1,0,0,0,429,430,5,2,0,0,430,431,5,44,0,0,431,432,
        3,68,34,0,432,433,5,45,0,0,433,437,5,46,0,0,434,436,3,72,36,0,435,
        434,1,0,0,0,436,439,1,0,0,0,437,435,1,0,0,0,437,438,1,0,0,0,438,
        440,1,0,0,0,439,437,1,0,0,0,440,444,5,47,0,0,441,443,3,78,39,0,442,
        441,1,0,0,0,443,446,1,0,0,0,444,442,1,0,0,0,444,445,1,0,0,0,445,
        456,1,0,0,0,446,444,1,0,0,0,447,448,5,3,0,0,448,452,5,46,0,0,449,
        451,3,72,36,0,450,449,1,0,0,0,451,454,1,0,0,0,452,450,1,0,0,0,452,
        453,1,0,0,0,453,455,1,0,0,0,454,452,1,0,0,0,455,457,5,47,0,0,456,
        447,1,0,0,0,456,457,1,0,0,0,457,458,1,0,0,0,458,459,3,108,54,0,459,
        77,1,0,0,0,460,461,5,3,0,0,461,462,5,2,0,0,462,463,5,44,0,0,463,
        464,3,68,34,0,464,465,5,45,0,0,465,469,5,46,0,0,466,468,3,72,36,
        0,467,466,1,0,0,0,468,471,1,0,0,0,469,467,1,0,0,0,469,470,1,0,0,
        0,470,472,1,0,0,0,471,469,1,0,0,0,472,473,5,47,0,0,473,79,1,0,0,
        0,474,475,5,4,0,0,475,476,3,82,41,0,476,480,5,46,0,0,477,479,3,72,
        36,0,478,477,1,0,0,0,479,482,1,0,0,0,480,478,1,0,0,0,480,481,1,0,
        0,0,481,483,1,0,0,0,482,480,1,0,0,0,483,484,5,47,0,0,484,485,3,108,
        54,0,485,81,1,0,0,0,486,490,3,68,34,0,487,490,3,84,42,0,488,490,
        3,90,45,0,489,486,1,0,0,0,489,487,1,0,0,0,489,488,1,0,0,0,490,83,
        1,0,0,0,491,493,3,86,43,0,492,491,1,0,0,0,492,493,1,0,0,0,493,494,
        1,0,0,0,494,496,3,108,54,0,495,497,3,68,34,0,496,495,1,0,0,0,496,
        497,1,0,0,0,497,498,1,0,0,0,498,500,3,108,54,0,499,501,3,88,44,0,
        500,499,1,0,0,0,500,501,1,0,0,0,501,85,1,0,0,0,502,503,5,62,0,0,
        503,504,7,2,0,0,504,505,3,68,34,0,505,87,1,0,0,0,506,510,5,62,0,
        0,507,509,3,106,53,0,508,507,1,0,0,0,509,512,1,0,0,0,510,508,1,0,
        0,0,510,511,1,0,0,0,511,513,1,0,0,0,512,510,1,0,0,0,513,514,3,104,
        52,0,514,515,3,68,34,0,515,89,1,0,0,0,516,517,7,3,0,0,517,518,5,
        50,0,0,518,519,5,62,0,0,519,520,5,37,0,0,520,521,5,18,0,0,521,522,
        5,62,0,0,522,91,1,0,0,0,523,524,5,17,0,0,524,525,3,108,54,0,525,
        93,1,0,0,0,526,527,5,16,0,0,527,528,3,108,54,0,528,95,1,0,0,0,529,
        531,5,5,0,0,530,532,3,68,34,0,531,530,1,0,0,0,531,532,1,0,0,0,532,
        533,1,0,0,0,533,534,3,108,54,0,534,97,1,0,0,0,535,536,7,4,0,0,536,
        99,1,0,0,0,537,538,7,5,0,0,538,101,1,0,0,0,539,540,7,6,0,0,540,103,
        1,0,0,0,541,542,7,7,0,0,542,105,1,0,0,0,543,544,5,48,0,0,544,545,
        3,68,34,0,545,546,5,49,0,0,546,107,1,0,0,0,547,548,7,8,0,0,548,109,
        1,0,0,0,48,113,125,130,135,141,145,162,167,171,177,185,190,200,213,
        218,223,233,244,256,263,274,281,305,315,326,329,347,355,359,369,
        389,394,396,405,416,422,437,444,452,456,469,480,489,492,496,500,
        510,531
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'_'", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "':='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "IF", "ELSE", "FOR", "RETURN", 
                      "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                      "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                      "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "EQ", "NEQ", "LT", "LE", "GT", "GE", 
                      "AND", "OR", "NOT", "ASSIGN", "DECLARE_ASSIGN", "PLUS_ASSIGN", 
                      "MINUS_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "DOT", "LB", "RB", "LCB", "RCB", "LSB", "RSB", "COMMA", 
                      "COLON", "SEMICOLON", "INT_LITERAL", "DECIMAL_LITERAL", 
                      "BINARY_LITERAL", "OCTAL_LITERAL", "HEX_LITERAL", 
                      "FLOAT_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                      "NIL_LITERAL", "IDENTIFIER", "LINE_COMMENT", "COMMENT", 
                      "WS", "EOS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_assign = 2
    RULE_call = 3
    RULE_var_decl = 4
    RULE_short_var_decl = 5
    RULE_const_decl = 6
    RULE_func_decl = 7
    RULE_func_call = 8
    RULE_args = 9
    RULE_method = 10
    RULE_param_list = 11
    RULE_param = 12
    RULE_types = 13
    RULE_literals = 14
    RULE_primitive_type = 15
    RULE_assign_array = 16
    RULE_array_decl = 17
    RULE_short_array_decl = 18
    RULE_array_type = 19
    RULE_dimensions = 20
    RULE_array_literal = 21
    RULE_ele_list = 22
    RULE_ele = 23
    RULE_access_struct = 24
    RULE_assign_struct = 25
    RULE_struct_decl = 26
    RULE_struct_type = 27
    RULE_fields = 28
    RULE_struct_literal = 29
    RULE_field_lit = 30
    RULE_interface_decl = 31
    RULE_interface_type = 32
    RULE_method_decl = 33
    RULE_expr = 34
    RULE_primary_expr = 35
    RULE_stmt = 36
    RULE_asm_stmt = 37
    RULE_if_stmt = 38
    RULE_else_if_stmt = 39
    RULE_for_stmt = 40
    RULE_for_clause = 41
    RULE_fully_clause = 42
    RULE_init = 43
    RULE_update = 44
    RULE_range_clause = 45
    RULE_break_stmt = 46
    RULE_continue_stmt = 47
    RULE_return_stmt = 48
    RULE_boolean_ops = 49
    RULE_arithmetic_ops = 50
    RULE_relational_ops = 51
    RULE_assign_ops = 52
    RULE_index_ops = 53
    RULE_eos = 54

    ruleNames =  [ "program", "decl", "assign", "call", "var_decl", "short_var_decl", 
                   "const_decl", "func_decl", "func_call", "args", "method", 
                   "param_list", "param", "types", "literals", "primitive_type", 
                   "assign_array", "array_decl", "short_array_decl", "array_type", 
                   "dimensions", "array_literal", "ele_list", "ele", "access_struct", 
                   "assign_struct", "struct_decl", "struct_type", "fields", 
                   "struct_literal", "field_lit", "interface_decl", "interface_type", 
                   "method_decl", "expr", "primary_expr", "stmt", "asm_stmt", 
                   "if_stmt", "else_if_stmt", "for_stmt", "for_clause", 
                   "fully_clause", "init", "update", "range_clause", "break_stmt", 
                   "continue_stmt", "return_stmt", "boolean_ops", "arithmetic_ops", 
                   "relational_ops", "assign_ops", "index_ops", "eos" ]

    EOF = Token.EOF
    T__0=1
    IF=2
    ELSE=3
    FOR=4
    RETURN=5
    FUNC=6
    TYPE=7
    STRUCT=8
    INTERFACE=9
    STRING=10
    INT=11
    FLOAT=12
    BOOLEAN=13
    CONST=14
    VAR=15
    CONTINUE=16
    BREAK=17
    RANGE=18
    NIL=19
    TRUE=20
    FALSE=21
    ADD=22
    SUB=23
    MUL=24
    DIV=25
    MOD=26
    EQ=27
    NEQ=28
    LT=29
    LE=30
    GT=31
    GE=32
    AND=33
    OR=34
    NOT=35
    ASSIGN=36
    DECLARE_ASSIGN=37
    PLUS_ASSIGN=38
    MINUS_ASSIGN=39
    MULT_ASSIGN=40
    DIV_ASSIGN=41
    MOD_ASSIGN=42
    DOT=43
    LB=44
    RB=45
    LCB=46
    RCB=47
    LSB=48
    RSB=49
    COMMA=50
    COLON=51
    SEMICOLON=52
    INT_LITERAL=53
    DECIMAL_LITERAL=54
    BINARY_LITERAL=55
    OCTAL_LITERAL=56
    HEX_LITERAL=57
    FLOAT_LITERAL=58
    STRING_LITERAL=59
    BOOLEAN_LITERAL=60
    NIL_LITERAL=61
    IDENTIFIER=62
    LINE_COMMENT=63
    COMMENT=64
    WS=65
    EOS=66
    ERROR_CHAR=67
    ILLEGAL_ESCAPE=68
    UNCLOSE_STRING=69

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
            return self.getToken(MiniGoParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 110
                self.stmt()
                self.state = 113 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018427633908) != 0)):
                    break

            self.state = 115
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def short_var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Short_var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declContext,0)


        def short_array_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Short_array_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.var_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.short_var_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
                self.const_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 121
                self.array_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 122
                self.short_array_decl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 123
                self.struct_decl()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 124
                self.interface_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_array(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_arrayContext,0)


        def assign_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_structContext,0)


        def access_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Access_structContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign




    def assign(self):

        localctx = MiniGoParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.assign_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.assign_struct()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.access_struct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call




    def call(self):

        localctx = MiniGoParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.func_call()
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

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 134
                self.match(MiniGoParser.VAR)


            self.state = 137
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 13]:
                self.state = 138
                self.primitive_type()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 139
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 140
                    self.expr(0)


                pass
            elif token in [36]:
                self.state = 143
                self.match(MiniGoParser.ASSIGN)
                self.state = 144
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 147
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Short_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_short_var_decl




    def short_var_decl(self):

        localctx = MiniGoParser.Short_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_short_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 150
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 151
            self.expr(0)
            self.state = 152
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(MiniGoParser.CONST)
            self.state = 155
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 156
            self.match(MiniGoParser.ASSIGN)
            self.state = 157
            self.expr(0)
            self.state = 158
            self.eos()
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

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def method(self):
            return self.getTypedRuleContext(MiniGoParser.MethodContext,0)


        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(MiniGoParser.FUNC)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 161
                self.method()


            self.state = 164
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 165
            self.match(MiniGoParser.LB)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 166
                self.param_list()


            self.state = 169
            self.match(MiniGoParser.RB)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611967493404113920) != 0):
                self.state = 170
                self.types()


            self.state = 173
            self.match(MiniGoParser.LCB)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018427633908) != 0):
                self.state = 174
                self.stmt()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 180
            self.match(MiniGoParser.RCB)
            self.state = 181
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def args(self):
            return self.getTypedRuleContext(MiniGoParser.ArgsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 183
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 184
                self.match(MiniGoParser.DOT)


            self.state = 187
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 188
            self.match(MiniGoParser.LB)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8944166486511976448) != 0):
                self.state = 189
                self.args()


            self.state = 192
            self.match(MiniGoParser.RB)
            self.state = 193
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_args




    def args(self):

        localctx = MiniGoParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.expr(0)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 196
                self.match(MiniGoParser.COMMA)
                self.state = 197
                self.expr(0)
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method




    def method(self):

        localctx = MiniGoParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(MiniGoParser.LB)
            self.state = 204
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 205
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 206
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParamContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_param_list




    def param_list(self):

        localctx = MiniGoParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.param()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 209
                self.match(MiniGoParser.COMMA)
                self.state = 210
                self.param()
                self.state = 215
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

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611967493404113920) != 0):
                self.state = 217
                self.types()


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

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_types




    def types(self):

        localctx = MiniGoParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_types)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.primitive_type()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.array_type()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.match(MiniGoParser.IDENTIFIER)
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


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(MiniGoParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MiniGoParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(MiniGoParser.STRING_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MiniGoParser.BOOLEAN_LITERAL, 0)

        def NIL_LITERAL(self):
            return self.getToken(MiniGoParser.NIL_LITERAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literals




    def literals(self):

        localctx = MiniGoParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4332462841530417152) != 0)):
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


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_type




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0)):
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


    class Assign_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def index_ops(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Index_opsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Index_opsContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_array




    def assign_array(self):

        localctx = MiniGoParser.Assign_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assign_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 231 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 230
                self.index_ops()
                self.state = 233 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==48):
                    break

            self.state = 235
            self.match(MiniGoParser.ASSIGN)
            self.state = 236
            self.expr(0)
            self.state = 237
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_decl




    def array_decl(self):

        localctx = MiniGoParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(MiniGoParser.VAR)
            self.state = 240
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.state = 241
                self.array_type()
                pass
            elif token in [36]:
                self.state = 242
                self.match(MiniGoParser.ASSIGN)
                self.state = 243
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 246
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Short_array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_short_array_decl




    def short_array_decl(self):

        localctx = MiniGoParser.Short_array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_short_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 249
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 250
            self.array_literal()
            self.state = 251
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionsContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.dimensions()
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 13]:
                self.state = 254
                self.primitive_type()
                pass
            elif token in [62]:
                self.state = 255
                self.match(MiniGoParser.IDENTIFIER)
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


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LSB)
            else:
                return self.getToken(MiniGoParser.LSB, i)

        def INT_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INT_LITERAL)
            else:
                return self.getToken(MiniGoParser.INT_LITERAL, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RSB)
            else:
                return self.getToken(MiniGoParser.RSB, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimensions




    def dimensions(self):

        localctx = MiniGoParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_dimensions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 258
                self.match(MiniGoParser.LSB)
                self.state = 259
                self.match(MiniGoParser.INT_LITERAL)
                self.state = 260
                self.match(MiniGoParser.RSB)
                self.state = 263 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==48):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def ele_list(self):
            return self.getTypedRuleContext(MiniGoParser.Ele_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.array_type()
            self.state = 266
            self.ele_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ele_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def ele(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.EleContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.EleContext,i)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ele_list




    def ele_list(self):

        localctx = MiniGoParser.Ele_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ele_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(MiniGoParser.LCB)
            self.state = 269
            self.ele()
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 270
                self.match(MiniGoParser.COMMA)
                self.state = 271
                self.ele()
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 277
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ele_list(self):
            return self.getTypedRuleContext(MiniGoParser.Ele_listContext,0)


        def literals(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ele




    def ele(self):

        localctx = MiniGoParser.EleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ele)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.ele_list()
                pass
            elif token in [53, 58, 59, 60, 61]:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.literals()
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


    class Access_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_access_struct




    def access_struct(self):

        localctx = MiniGoParser.Access_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_access_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 284
            self.match(MiniGoParser.DOT)
            self.state = 285
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 286
            self.match(MiniGoParser.ASSIGN)
            self.state = 287
            self.expr(0)
            self.state = 288
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_struct




    def assign_struct(self):

        localctx = MiniGoParser.Assign_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assign_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 291
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 292
            self.struct_literal()
            self.state = 293
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(MiniGoParser.TYPE)
            self.state = 296
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 297
            self.struct_type()
            self.state = 298
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def fields(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FieldsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FieldsContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type




    def struct_type(self):

        localctx = MiniGoParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_struct_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(MiniGoParser.STRUCT)
            self.state = 301
            self.match(MiniGoParser.LCB)
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 302
                self.fields()
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 308
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fields




    def fields(self):

        localctx = MiniGoParser.FieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 13]:
                self.state = 311
                self.primitive_type()
                pass
            elif token in [48]:
                self.state = 312
                self.array_type()
                pass
            elif token in [8]:
                self.state = 313
                self.struct_type()
                pass
            elif token in [62]:
                self.state = 314
                self.match(MiniGoParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 317
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def field_lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Field_litContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Field_litContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 320
            self.match(MiniGoParser.LCB)
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 321
                self.field_lit()
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==50:
                    self.state = 322
                    self.match(MiniGoParser.COMMA)
                    self.state = 323
                    self.field_lit()
                    self.state = 328
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 331
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_lit




    def field_lit(self):

        localctx = MiniGoParser.Field_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_field_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 334
            self.match(MiniGoParser.COLON)
            self.state = 335
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def interface_type(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_typeContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(MiniGoParser.TYPE)
            self.state = 338
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 339
            self.interface_type()
            self.state = 340
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def method_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Method_declContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Method_declContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type




    def interface_type(self):

        localctx = MiniGoParser.Interface_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_interface_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(MiniGoParser.INTERFACE)
            self.state = 343
            self.match(MiniGoParser.LCB)
            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 344
                self.method_decl()
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 350
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 353
            self.match(MiniGoParser.LB)
            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 354
                self.param_list()


            self.state = 357
            self.match(MiniGoParser.RB)
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611967493404113920) != 0):
                self.state = 358
                self.types()


            self.state = 361
            self.eos()
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

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def primary_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Primary_exprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def relational_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Relational_opsContext,0)


        def arithmetic_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Arithmetic_opsContext,0)


        def index_ops(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Index_opsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Index_opsContext,i)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.state = 364
                self.match(MiniGoParser.NOT)
                self.state = 365
                self.expr(5)
                pass
            elif token in [23]:
                self.state = 366
                self.match(MiniGoParser.SUB)
                self.state = 367
                self.expr(4)
                pass
            elif token in [44, 53, 58, 59, 60, 61, 62]:
                self.state = 368
                self.primary_expr()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 396
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 394
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 371
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 372
                        self.match(MiniGoParser.OR)
                        self.state = 373
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 374
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 375
                        self.match(MiniGoParser.AND)
                        self.state = 376
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 377
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 378
                        self.relational_ops()
                        self.state = 379
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 381
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 382
                        self.arithmetic_ops()
                        self.state = 383
                        self.expr(7)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 385
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 387 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 386
                                self.index_ops()

                            else:
                                raise NoViableAltException(self)
                            self.state = 389 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                        pass

                    elif la_ == 6:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 391
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 392
                        self.match(MiniGoParser.DOT)
                        self.state = 393
                        self.match(MiniGoParser.IDENTIFIER)
                        pass

             
                self.state = 398
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Primary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def literals(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralsContext,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primary_expr




    def primary_expr(self):

        localctx = MiniGoParser.Primary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_primary_expr)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [62]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [53, 58, 59, 60, 61]:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.literals()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 401
                self.match(MiniGoParser.LB)
                self.state = 402
                self.expr(0)
                self.state = 403
                self.match(MiniGoParser.RB)
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


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def assign(self):
            return self.getTypedRuleContext(MiniGoParser.AssignContext,0)


        def call(self):
            return self.getTypedRuleContext(MiniGoParser.CallContext,0)


        def asm_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Asm_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_stmt)
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 409
                self.call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 410
                self.asm_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 411
                self.if_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 412
                self.for_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 413
                self.break_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 414
                self.continue_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 415
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asm_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def assign_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opsContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def index_ops(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Index_opsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Index_opsContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_asm_stmt




    def asm_stmt(self):

        localctx = MiniGoParser.Asm_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_asm_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 419
                self.index_ops()
                self.state = 424
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 425
            self.assign_ops()
            self.state = 426
            self.expr(0)
            self.state = 427
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def LCB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LCB)
            else:
                return self.getToken(MiniGoParser.LCB, i)

        def RCB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RCB)
            else:
                return self.getToken(MiniGoParser.RCB, i)

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def else_if_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Else_if_stmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Else_if_stmtContext,i)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(MiniGoParser.IF)
            self.state = 430
            self.match(MiniGoParser.LB)
            self.state = 431
            self.expr(0)
            self.state = 432
            self.match(MiniGoParser.RB)
            self.state = 433
            self.match(MiniGoParser.LCB)
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018427633908) != 0):
                self.state = 434
                self.stmt()
                self.state = 439
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 440
            self.match(MiniGoParser.RCB)
            self.state = 444
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 441
                    self.else_if_stmt() 
                self.state = 446
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

            self.state = 456
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 447
                self.match(MiniGoParser.ELSE)
                self.state = 448
                self.match(MiniGoParser.LCB)
                self.state = 452
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018427633908) != 0):
                    self.state = 449
                    self.stmt()
                    self.state = 454
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 455
                self.match(MiniGoParser.RCB)


            self.state = 458
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_stmt




    def else_if_stmt(self):

        localctx = MiniGoParser.Else_if_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_else_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(MiniGoParser.ELSE)
            self.state = 461
            self.match(MiniGoParser.IF)
            self.state = 462
            self.match(MiniGoParser.LB)
            self.state = 463
            self.expr(0)
            self.state = 464
            self.match(MiniGoParser.RB)
            self.state = 465
            self.match(MiniGoParser.LCB)
            self.state = 469
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018427633908) != 0):
                self.state = 466
                self.stmt()
                self.state = 471
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 472
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def for_clause(self):
            return self.getTypedRuleContext(MiniGoParser.For_clauseContext,0)


        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(MiniGoParser.FOR)
            self.state = 475
            self.for_clause()
            self.state = 476
            self.match(MiniGoParser.LCB)
            self.state = 480
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018427633908) != 0):
                self.state = 477
                self.stmt()
                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 483
            self.match(MiniGoParser.RCB)
            self.state = 484
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def fully_clause(self):
            return self.getTypedRuleContext(MiniGoParser.Fully_clauseContext,0)


        def range_clause(self):
            return self.getTypedRuleContext(MiniGoParser.Range_clauseContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_clause




    def for_clause(self):

        localctx = MiniGoParser.For_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_for_clause)
        try:
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.fully_clause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 488
                self.range_clause()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fully_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.EosContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.EosContext,i)


        def init(self):
            return self.getTypedRuleContext(MiniGoParser.InitContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def update(self):
            return self.getTypedRuleContext(MiniGoParser.UpdateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fully_clause




    def fully_clause(self):

        localctx = MiniGoParser.Fully_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_fully_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 491
                self.init()


            self.state = 494
            self.eos()
            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8944166486511976448) != 0):
                self.state = 495
                self.expr(0)


            self.state = 498
            self.eos()
            self.state = 500
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 499
                self.update()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_init




    def init(self):

        localctx = MiniGoParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 503
            _la = self._input.LA(1)
            if not(_la==36 or _la==37):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 504
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def assign_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opsContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def index_ops(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Index_opsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Index_opsContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_update




    def update(self):

        localctx = MiniGoParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_update)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 510
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 507
                self.index_ops()
                self.state = 512
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 513
            self.assign_ops()
            self.state = 514
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_range_clause




    def range_clause(self):

        localctx = MiniGoParser.Range_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_range_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            _la = self._input.LA(1)
            if not(_la==1 or _la==62):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 517
            self.match(MiniGoParser.COMMA)
            self.state = 518
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 519
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 520
            self.match(MiniGoParser.RANGE)
            self.state = 521
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(MiniGoParser.BREAK)
            self.state = 524
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(MiniGoParser.CONTINUE)
            self.state = 527
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.match(MiniGoParser.RETURN)
            self.state = 531
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8944166486511976448) != 0):
                self.state = 530
                self.expr(0)


            self.state = 533
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_opsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_boolean_ops




    def boolean_ops(self):

        localctx = MiniGoParser.Boolean_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_boolean_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60129542144) != 0)):
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


    class Arithmetic_opsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arithmetic_ops




    def arithmetic_ops(self):

        localctx = MiniGoParser.Arithmetic_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_arithmetic_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 130023424) != 0)):
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


    class Relational_opsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniGoParser.NEQ, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GE(self):
            return self.getToken(MiniGoParser.GE, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LE(self):
            return self.getToken(MiniGoParser.LE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_relational_ops




    def relational_ops(self):

        localctx = MiniGoParser.Relational_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_relational_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8455716864) != 0)):
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


    class Assign_opsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS_ASSIGN(self):
            return self.getToken(MiniGoParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(MiniGoParser.MINUS_ASSIGN, 0)

        def MULT_ASSIGN(self):
            return self.getToken(MiniGoParser.MULT_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_ops




    def assign_ops(self):

        localctx = MiniGoParser.Assign_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_assign_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8521215115264) != 0)):
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


    class Index_opsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_index_ops




    def index_ops(self):

        localctx = MiniGoParser.Index_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_index_ops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            self.match(MiniGoParser.LSB)
            self.state = 544
            self.expr(0)
            self.state = 545
            self.match(MiniGoParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def EOS(self):
            return self.getToken(MiniGoParser.EOS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_eos




    def eos(self):

        localctx = MiniGoParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_eos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            _la = self._input.LA(1)
            if not(_la==52 or _la==66):
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
        self._predicates[34] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




