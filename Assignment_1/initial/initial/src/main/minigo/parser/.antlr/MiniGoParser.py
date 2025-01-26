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
        4,1,68,517,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,1,0,4,0,102,8,0,11,0,12,0,103,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,114,8,1,1,2,1,2,1,2,3,2,119,
        8,2,1,3,1,3,1,4,3,4,124,8,4,1,4,1,4,1,4,1,4,3,4,130,8,4,1,4,1,4,
        3,4,134,8,4,1,4,3,4,137,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,3,6,
        147,8,6,1,6,1,6,1,6,3,6,152,8,6,1,6,1,6,3,6,156,8,6,1,6,1,6,5,6,
        160,8,6,10,6,12,6,163,9,6,1,6,1,6,3,6,167,8,6,1,7,1,7,3,7,171,8,
        7,1,7,1,7,1,7,3,7,176,8,7,1,7,1,7,3,7,180,8,7,1,8,1,8,1,8,5,8,185,
        8,8,10,8,12,8,188,9,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,5,10,198,
        8,10,10,10,12,10,201,9,10,1,11,1,11,3,11,205,8,11,1,12,1,12,1,12,
        3,12,210,8,12,1,13,1,13,1,14,1,14,1,15,1,15,4,15,218,8,15,11,15,
        12,15,219,1,15,1,15,1,15,3,15,225,8,15,1,16,3,16,228,8,16,1,16,1,
        16,1,16,1,16,3,16,234,8,16,1,16,3,16,237,8,16,1,17,1,17,1,17,3,17,
        242,8,17,1,18,1,18,1,18,4,18,247,8,18,11,18,12,18,248,1,19,1,19,
        1,19,1,20,1,20,1,20,1,20,5,20,258,8,20,10,20,12,20,261,9,20,1,20,
        1,20,1,21,1,21,3,21,267,8,21,1,22,1,22,1,22,1,22,1,22,1,22,3,22,
        275,8,22,1,23,1,23,1,23,1,23,3,23,281,8,23,1,24,1,24,1,24,1,24,1,
        25,1,25,1,25,5,25,290,8,25,10,25,12,25,293,9,25,1,25,1,25,1,26,1,
        26,1,26,1,26,1,26,3,26,302,8,26,1,26,3,26,305,8,26,1,27,1,27,1,27,
        1,27,1,27,5,27,312,8,27,10,27,12,27,315,9,27,3,27,317,8,27,1,27,
        1,27,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,5,30,
        332,8,30,10,30,12,30,335,9,30,1,30,1,30,1,31,1,31,1,31,3,31,342,
        8,31,1,31,1,31,3,31,346,8,31,1,31,3,31,349,8,31,1,32,1,32,1,32,1,
        32,1,32,1,32,3,32,357,8,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,
        32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,4,32,375,8,32,11,32,12,
        32,376,1,32,1,32,1,32,5,32,382,8,32,10,32,12,32,385,9,32,1,33,1,
        33,1,33,1,33,1,33,1,33,3,33,393,8,33,1,34,1,34,1,34,1,34,1,34,1,
        34,1,34,1,34,1,34,3,34,404,8,34,1,35,1,35,5,35,408,8,35,10,35,12,
        35,411,9,35,1,35,1,35,1,35,3,35,416,8,35,1,36,1,36,1,36,1,36,1,36,
        1,36,5,36,424,8,36,10,36,12,36,427,9,36,1,36,1,36,5,36,431,8,36,
        10,36,12,36,434,9,36,1,36,1,36,1,36,5,36,439,8,36,10,36,12,36,442,
        9,36,1,36,3,36,445,8,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,5,37,
        454,8,37,10,37,12,37,457,9,37,1,37,1,37,1,38,1,38,1,38,1,38,5,38,
        465,8,38,10,38,12,38,468,9,38,1,38,1,38,1,39,1,39,1,39,3,39,475,
        8,39,1,40,3,40,478,8,40,1,40,1,40,1,40,1,40,3,40,484,8,40,1,41,1,
        41,1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,43,1,43,1,43,1,44,1,
        44,3,44,501,8,44,1,44,1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,
        48,1,49,1,49,1,49,1,49,1,49,0,1,64,50,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,
        66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,0,7,2,0,54,54,
        59,62,1,0,12,15,2,0,1,1,63,63,1,0,35,37,1,0,24,28,1,0,29,34,1,0,
        39,43,545,0,101,1,0,0,0,2,113,1,0,0,0,4,118,1,0,0,0,6,120,1,0,0,
        0,8,123,1,0,0,0,10,138,1,0,0,0,12,144,1,0,0,0,14,170,1,0,0,0,16,
        181,1,0,0,0,18,189,1,0,0,0,20,194,1,0,0,0,22,202,1,0,0,0,24,209,
        1,0,0,0,26,211,1,0,0,0,28,213,1,0,0,0,30,215,1,0,0,0,32,227,1,0,
        0,0,34,238,1,0,0,0,36,246,1,0,0,0,38,250,1,0,0,0,40,253,1,0,0,0,
        42,266,1,0,0,0,44,268,1,0,0,0,46,276,1,0,0,0,48,282,1,0,0,0,50,286,
        1,0,0,0,52,296,1,0,0,0,54,306,1,0,0,0,56,320,1,0,0,0,58,324,1,0,
        0,0,60,328,1,0,0,0,62,338,1,0,0,0,64,356,1,0,0,0,66,392,1,0,0,0,
        68,403,1,0,0,0,70,405,1,0,0,0,72,417,1,0,0,0,74,446,1,0,0,0,76,460,
        1,0,0,0,78,474,1,0,0,0,80,477,1,0,0,0,82,485,1,0,0,0,84,492,1,0,
        0,0,86,495,1,0,0,0,88,498,1,0,0,0,90,504,1,0,0,0,92,506,1,0,0,0,
        94,508,1,0,0,0,96,510,1,0,0,0,98,512,1,0,0,0,100,102,3,68,34,0,101,
        100,1,0,0,0,102,103,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,
        105,1,0,0,0,105,106,5,0,0,1,106,1,1,0,0,0,107,114,3,12,6,0,108,114,
        3,8,4,0,109,114,3,10,5,0,110,114,3,32,16,0,111,114,3,48,24,0,112,
        114,3,58,29,0,113,107,1,0,0,0,113,108,1,0,0,0,113,109,1,0,0,0,113,
        110,1,0,0,0,113,111,1,0,0,0,113,112,1,0,0,0,114,3,1,0,0,0,115,119,
        3,30,15,0,116,119,3,46,23,0,117,119,3,44,22,0,118,115,1,0,0,0,118,
        116,1,0,0,0,118,117,1,0,0,0,119,5,1,0,0,0,120,121,3,14,7,0,121,7,
        1,0,0,0,122,124,5,17,0,0,123,122,1,0,0,0,123,124,1,0,0,0,124,125,
        1,0,0,0,125,133,5,63,0,0,126,129,3,28,14,0,127,128,5,38,0,0,128,
        130,3,64,32,0,129,127,1,0,0,0,129,130,1,0,0,0,130,134,1,0,0,0,131,
        132,5,38,0,0,132,134,3,64,32,0,133,126,1,0,0,0,133,131,1,0,0,0,134,
        136,1,0,0,0,135,137,5,53,0,0,136,135,1,0,0,0,136,137,1,0,0,0,137,
        9,1,0,0,0,138,139,5,16,0,0,139,140,5,63,0,0,140,141,5,38,0,0,141,
        142,3,64,32,0,142,143,5,53,0,0,143,11,1,0,0,0,144,146,5,8,0,0,145,
        147,3,18,9,0,146,145,1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,
        149,5,63,0,0,149,151,5,45,0,0,150,152,3,20,10,0,151,150,1,0,0,0,
        151,152,1,0,0,0,152,153,1,0,0,0,153,155,5,46,0,0,154,156,3,24,12,
        0,155,154,1,0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,161,5,47,0,
        0,158,160,3,68,34,0,159,158,1,0,0,0,160,163,1,0,0,0,161,159,1,0,
        0,0,161,162,1,0,0,0,162,164,1,0,0,0,163,161,1,0,0,0,164,166,5,48,
        0,0,165,167,5,53,0,0,166,165,1,0,0,0,166,167,1,0,0,0,167,13,1,0,
        0,0,168,169,5,63,0,0,169,171,5,44,0,0,170,168,1,0,0,0,170,171,1,
        0,0,0,171,172,1,0,0,0,172,173,5,63,0,0,173,175,5,45,0,0,174,176,
        3,16,8,0,175,174,1,0,0,0,175,176,1,0,0,0,176,177,1,0,0,0,177,179,
        5,46,0,0,178,180,5,53,0,0,179,178,1,0,0,0,179,180,1,0,0,0,180,15,
        1,0,0,0,181,186,3,64,32,0,182,183,5,51,0,0,183,185,3,64,32,0,184,
        182,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,
        17,1,0,0,0,188,186,1,0,0,0,189,190,5,45,0,0,190,191,5,63,0,0,191,
        192,5,63,0,0,192,193,5,46,0,0,193,19,1,0,0,0,194,199,3,22,11,0,195,
        196,5,51,0,0,196,198,3,22,11,0,197,195,1,0,0,0,198,201,1,0,0,0,199,
        197,1,0,0,0,199,200,1,0,0,0,200,21,1,0,0,0,201,199,1,0,0,0,202,204,
        5,63,0,0,203,205,3,24,12,0,204,203,1,0,0,0,204,205,1,0,0,0,205,23,
        1,0,0,0,206,210,3,28,14,0,207,210,3,34,17,0,208,210,5,63,0,0,209,
        206,1,0,0,0,209,207,1,0,0,0,209,208,1,0,0,0,210,25,1,0,0,0,211,212,
        7,0,0,0,212,27,1,0,0,0,213,214,7,1,0,0,214,29,1,0,0,0,215,217,5,
        63,0,0,216,218,3,98,49,0,217,216,1,0,0,0,218,219,1,0,0,0,219,217,
        1,0,0,0,219,220,1,0,0,0,220,221,1,0,0,0,221,222,5,38,0,0,222,224,
        3,64,32,0,223,225,5,53,0,0,224,223,1,0,0,0,224,225,1,0,0,0,225,31,
        1,0,0,0,226,228,5,17,0,0,227,226,1,0,0,0,227,228,1,0,0,0,228,229,
        1,0,0,0,229,233,5,63,0,0,230,234,3,34,17,0,231,232,5,38,0,0,232,
        234,3,38,19,0,233,230,1,0,0,0,233,231,1,0,0,0,234,236,1,0,0,0,235,
        237,5,53,0,0,236,235,1,0,0,0,236,237,1,0,0,0,237,33,1,0,0,0,238,
        241,3,36,18,0,239,242,3,28,14,0,240,242,5,63,0,0,241,239,1,0,0,0,
        241,240,1,0,0,0,242,35,1,0,0,0,243,244,5,49,0,0,244,245,5,54,0,0,
        245,247,5,50,0,0,246,243,1,0,0,0,247,248,1,0,0,0,248,246,1,0,0,0,
        248,249,1,0,0,0,249,37,1,0,0,0,250,251,3,34,17,0,251,252,3,40,20,
        0,252,39,1,0,0,0,253,254,5,47,0,0,254,259,3,42,21,0,255,256,5,51,
        0,0,256,258,3,42,21,0,257,255,1,0,0,0,258,261,1,0,0,0,259,257,1,
        0,0,0,259,260,1,0,0,0,260,262,1,0,0,0,261,259,1,0,0,0,262,263,5,
        48,0,0,263,41,1,0,0,0,264,267,3,40,20,0,265,267,3,26,13,0,266,264,
        1,0,0,0,266,265,1,0,0,0,267,43,1,0,0,0,268,269,5,63,0,0,269,270,
        5,44,0,0,270,271,5,63,0,0,271,272,5,38,0,0,272,274,3,64,32,0,273,
        275,5,53,0,0,274,273,1,0,0,0,274,275,1,0,0,0,275,45,1,0,0,0,276,
        277,5,63,0,0,277,278,5,38,0,0,278,280,3,54,27,0,279,281,5,53,0,0,
        280,279,1,0,0,0,280,281,1,0,0,0,281,47,1,0,0,0,282,283,5,9,0,0,283,
        284,5,63,0,0,284,285,3,50,25,0,285,49,1,0,0,0,286,287,5,10,0,0,287,
        291,5,47,0,0,288,290,3,52,26,0,289,288,1,0,0,0,290,293,1,0,0,0,291,
        289,1,0,0,0,291,292,1,0,0,0,292,294,1,0,0,0,293,291,1,0,0,0,294,
        295,5,48,0,0,295,51,1,0,0,0,296,301,5,63,0,0,297,302,3,28,14,0,298,
        302,3,34,17,0,299,302,3,50,25,0,300,302,5,63,0,0,301,297,1,0,0,0,
        301,298,1,0,0,0,301,299,1,0,0,0,301,300,1,0,0,0,302,304,1,0,0,0,
        303,305,5,53,0,0,304,303,1,0,0,0,304,305,1,0,0,0,305,53,1,0,0,0,
        306,307,5,63,0,0,307,316,5,47,0,0,308,313,3,56,28,0,309,310,5,51,
        0,0,310,312,3,56,28,0,311,309,1,0,0,0,312,315,1,0,0,0,313,311,1,
        0,0,0,313,314,1,0,0,0,314,317,1,0,0,0,315,313,1,0,0,0,316,308,1,
        0,0,0,316,317,1,0,0,0,317,318,1,0,0,0,318,319,5,48,0,0,319,55,1,
        0,0,0,320,321,5,63,0,0,321,322,5,52,0,0,322,323,3,64,32,0,323,57,
        1,0,0,0,324,325,5,9,0,0,325,326,5,63,0,0,326,327,3,60,30,0,327,59,
        1,0,0,0,328,329,5,11,0,0,329,333,5,47,0,0,330,332,3,62,31,0,331,
        330,1,0,0,0,332,335,1,0,0,0,333,331,1,0,0,0,333,334,1,0,0,0,334,
        336,1,0,0,0,335,333,1,0,0,0,336,337,5,48,0,0,337,61,1,0,0,0,338,
        339,5,63,0,0,339,341,5,45,0,0,340,342,3,20,10,0,341,340,1,0,0,0,
        341,342,1,0,0,0,342,343,1,0,0,0,343,345,5,46,0,0,344,346,3,24,12,
        0,345,344,1,0,0,0,345,346,1,0,0,0,346,348,1,0,0,0,347,349,5,53,0,
        0,348,347,1,0,0,0,348,349,1,0,0,0,349,63,1,0,0,0,350,351,6,32,-1,
        0,351,352,5,37,0,0,352,357,3,64,32,5,353,354,5,25,0,0,354,357,3,
        64,32,4,355,357,3,66,33,0,356,350,1,0,0,0,356,353,1,0,0,0,356,355,
        1,0,0,0,357,383,1,0,0,0,358,359,10,9,0,0,359,360,5,36,0,0,360,382,
        3,64,32,10,361,362,10,8,0,0,362,363,5,35,0,0,363,382,3,64,32,9,364,
        365,10,7,0,0,365,366,3,94,47,0,366,367,3,64,32,8,367,382,1,0,0,0,
        368,369,10,6,0,0,369,370,3,92,46,0,370,371,3,64,32,7,371,382,1,0,
        0,0,372,374,10,3,0,0,373,375,3,98,49,0,374,373,1,0,0,0,375,376,1,
        0,0,0,376,374,1,0,0,0,376,377,1,0,0,0,377,382,1,0,0,0,378,379,10,
        2,0,0,379,380,5,44,0,0,380,382,5,63,0,0,381,358,1,0,0,0,381,361,
        1,0,0,0,381,364,1,0,0,0,381,368,1,0,0,0,381,372,1,0,0,0,381,378,
        1,0,0,0,382,385,1,0,0,0,383,381,1,0,0,0,383,384,1,0,0,0,384,65,1,
        0,0,0,385,383,1,0,0,0,386,393,5,63,0,0,387,393,3,26,13,0,388,389,
        5,45,0,0,389,390,3,64,32,0,390,391,5,46,0,0,391,393,1,0,0,0,392,
        386,1,0,0,0,392,387,1,0,0,0,392,388,1,0,0,0,393,67,1,0,0,0,394,404,
        3,2,1,0,395,404,3,4,2,0,396,404,3,6,3,0,397,404,3,70,35,0,398,404,
        3,72,36,0,399,404,3,76,38,0,400,404,3,84,42,0,401,404,3,86,43,0,
        402,404,3,88,44,0,403,394,1,0,0,0,403,395,1,0,0,0,403,396,1,0,0,
        0,403,397,1,0,0,0,403,398,1,0,0,0,403,399,1,0,0,0,403,400,1,0,0,
        0,403,401,1,0,0,0,403,402,1,0,0,0,404,69,1,0,0,0,405,409,5,63,0,
        0,406,408,3,98,49,0,407,406,1,0,0,0,408,411,1,0,0,0,409,407,1,0,
        0,0,409,410,1,0,0,0,410,412,1,0,0,0,411,409,1,0,0,0,412,413,3,96,
        48,0,413,415,3,64,32,0,414,416,5,53,0,0,415,414,1,0,0,0,415,416,
        1,0,0,0,416,71,1,0,0,0,417,418,5,4,0,0,418,419,5,45,0,0,419,420,
        3,64,32,0,420,421,5,46,0,0,421,425,5,47,0,0,422,424,3,68,34,0,423,
        422,1,0,0,0,424,427,1,0,0,0,425,423,1,0,0,0,425,426,1,0,0,0,426,
        428,1,0,0,0,427,425,1,0,0,0,428,432,5,48,0,0,429,431,3,74,37,0,430,
        429,1,0,0,0,431,434,1,0,0,0,432,430,1,0,0,0,432,433,1,0,0,0,433,
        444,1,0,0,0,434,432,1,0,0,0,435,436,5,5,0,0,436,440,5,47,0,0,437,
        439,3,68,34,0,438,437,1,0,0,0,439,442,1,0,0,0,440,438,1,0,0,0,440,
        441,1,0,0,0,441,443,1,0,0,0,442,440,1,0,0,0,443,445,5,48,0,0,444,
        435,1,0,0,0,444,445,1,0,0,0,445,73,1,0,0,0,446,447,5,5,0,0,447,448,
        5,4,0,0,448,449,5,45,0,0,449,450,3,64,32,0,450,451,5,46,0,0,451,
        455,5,47,0,0,452,454,3,68,34,0,453,452,1,0,0,0,454,457,1,0,0,0,455,
        453,1,0,0,0,455,456,1,0,0,0,456,458,1,0,0,0,457,455,1,0,0,0,458,
        459,5,48,0,0,459,75,1,0,0,0,460,461,5,6,0,0,461,462,3,78,39,0,462,
        466,5,47,0,0,463,465,3,68,34,0,464,463,1,0,0,0,465,468,1,0,0,0,466,
        464,1,0,0,0,466,467,1,0,0,0,467,469,1,0,0,0,468,466,1,0,0,0,469,
        470,5,48,0,0,470,77,1,0,0,0,471,475,3,64,32,0,472,475,3,80,40,0,
        473,475,3,82,41,0,474,471,1,0,0,0,474,472,1,0,0,0,474,473,1,0,0,
        0,475,79,1,0,0,0,476,478,3,8,4,0,477,476,1,0,0,0,477,478,1,0,0,0,
        478,479,1,0,0,0,479,480,5,53,0,0,480,481,3,64,32,0,481,483,5,53,
        0,0,482,484,3,70,35,0,483,482,1,0,0,0,483,484,1,0,0,0,484,81,1,0,
        0,0,485,486,7,2,0,0,486,487,5,51,0,0,487,488,5,63,0,0,488,489,5,
        38,0,0,489,490,5,20,0,0,490,491,5,63,0,0,491,83,1,0,0,0,492,493,
        5,19,0,0,493,494,5,53,0,0,494,85,1,0,0,0,495,496,5,18,0,0,496,497,
        5,53,0,0,497,87,1,0,0,0,498,500,5,7,0,0,499,501,3,64,32,0,500,499,
        1,0,0,0,500,501,1,0,0,0,501,502,1,0,0,0,502,503,5,53,0,0,503,89,
        1,0,0,0,504,505,7,3,0,0,505,91,1,0,0,0,506,507,7,4,0,0,507,93,1,
        0,0,0,508,509,7,5,0,0,509,95,1,0,0,0,510,511,7,6,0,0,511,97,1,0,
        0,0,512,513,5,49,0,0,513,514,3,64,32,0,514,515,5,50,0,0,515,99,1,
        0,0,0,57,103,113,118,123,129,133,136,146,151,155,161,166,170,175,
        179,186,199,204,209,219,224,227,233,236,241,248,259,266,274,280,
        291,301,304,313,316,333,341,345,348,356,376,381,383,392,403,409,
        415,425,432,440,444,455,466,474,477,483,500
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'_'", "<INVALID>", "<INVALID>", "'if'", 
                     "'else'", "'for'", "'return'", "'func'", "'type'", 
                     "'struct'", "'interface'", "'string'", "'int'", "'float'", 
                     "'boolean'", "'const'", "'var'", "'continue'", "'break'", 
                     "'range'", "'nil'", "'true'", "'false'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'&&'", "'||'", "'!'", "<INVALID>", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "','", "':'", "';'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LINE_COMMENT", "COMMENT", 
                      "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                      "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", 
                      "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "EQ", "NEQ", "LT", "LE", "GT", "GE", "AND", "OR", 
                      "NOT", "ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", "MULT_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "LB", "RB", "LCB", 
                      "RCB", "LSB", "RSB", "COMMA", "COLON", "SEMICOLON", 
                      "INT_LITERAL", "DECIMAL_LITERAL", "BINARY_LITERAL", 
                      "OCTAL_LITERAL", "HEX_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
                      "BOOLEAN_LITERAL", "NIL_LITERAL", "IDENTIFIER", "NL", 
                      "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_assign = 2
    RULE_call = 3
    RULE_var_decl = 4
    RULE_const_decl = 5
    RULE_func_decl = 6
    RULE_func_call = 7
    RULE_args = 8
    RULE_method = 9
    RULE_param_list = 10
    RULE_param = 11
    RULE_types = 12
    RULE_literals = 13
    RULE_primitive_type = 14
    RULE_assign_array = 15
    RULE_array_decl = 16
    RULE_array_type = 17
    RULE_dimensions = 18
    RULE_array_literal = 19
    RULE_ele_list = 20
    RULE_ele = 21
    RULE_access_struct = 22
    RULE_assign_struct = 23
    RULE_struct_decl = 24
    RULE_struct_type = 25
    RULE_fields = 26
    RULE_struct_literal = 27
    RULE_field_lit = 28
    RULE_interface_decl = 29
    RULE_interface_type = 30
    RULE_method_decl = 31
    RULE_expr = 32
    RULE_primary_expr = 33
    RULE_stmt = 34
    RULE_asm_stmt = 35
    RULE_if_stmt = 36
    RULE_else_if_stmt = 37
    RULE_for_stmt = 38
    RULE_for_clause = 39
    RULE_fully_clause = 40
    RULE_range_clause = 41
    RULE_break_stmt = 42
    RULE_continue_stmt = 43
    RULE_return_stmt = 44
    RULE_boolean_ops = 45
    RULE_arithmetic_ops = 46
    RULE_relational_ops = 47
    RULE_assign_ops = 48
    RULE_index_ops = 49

    ruleNames =  [ "program", "decl", "assign", "call", "var_decl", "const_decl", 
                   "func_decl", "func_call", "args", "method", "param_list", 
                   "param", "types", "literals", "primitive_type", "assign_array", 
                   "array_decl", "array_type", "dimensions", "array_literal", 
                   "ele_list", "ele", "access_struct", "assign_struct", 
                   "struct_decl", "struct_type", "fields", "struct_literal", 
                   "field_lit", "interface_decl", "interface_type", "method_decl", 
                   "expr", "primary_expr", "stmt", "asm_stmt", "if_stmt", 
                   "else_if_stmt", "for_stmt", "for_clause", "fully_clause", 
                   "range_clause", "break_stmt", "continue_stmt", "return_stmt", 
                   "boolean_ops", "arithmetic_ops", "relational_ops", "assign_ops", 
                   "index_ops" ]

    EOF = Token.EOF
    T__0=1
    LINE_COMMENT=2
    COMMENT=3
    IF=4
    ELSE=5
    FOR=6
    RETURN=7
    FUNC=8
    TYPE=9
    STRUCT=10
    INTERFACE=11
    STRING=12
    INT=13
    FLOAT=14
    BOOLEAN=15
    CONST=16
    VAR=17
    CONTINUE=18
    BREAK=19
    RANGE=20
    NIL=21
    TRUE=22
    FALSE=23
    ADD=24
    SUB=25
    MUL=26
    DIV=27
    MOD=28
    EQ=29
    NEQ=30
    LT=31
    LE=32
    GT=33
    GE=34
    AND=35
    OR=36
    NOT=37
    ASSIGN=38
    PLUS_ASSIGN=39
    MINUS_ASSIGN=40
    MULT_ASSIGN=41
    DIV_ASSIGN=42
    MOD_ASSIGN=43
    DOT=44
    LB=45
    RB=46
    LCB=47
    RCB=48
    LSB=49
    RSB=50
    COMMA=51
    COLON=52
    SEMICOLON=53
    INT_LITERAL=54
    DECIMAL_LITERAL=55
    BINARY_LITERAL=56
    OCTAL_LITERAL=57
    HEX_LITERAL=58
    FLOAT_LITERAL=59
    STRING_LITERAL=60
    BOOLEAN_LITERAL=61
    NIL_LITERAL=62
    IDENTIFIER=63
    NL=64
    WS=65
    ERROR_CHAR=66
    ILLEGAL_ESCAPE=67
    UNCLOSE_STRING=68

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
            self.state = 101 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 100
                self.stmt()
                self.state = 103 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & -9223372036853791792) != 0)):
                    break

            self.state = 105
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


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declContext,0)


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
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.var_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.const_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 110
                self.array_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 111
                self.struct_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 112
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
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.assign_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.assign_struct()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
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
            self.state = 120
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

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 122
                self.match(MiniGoParser.VAR)


            self.state = 125
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13, 14, 15]:
                self.state = 126
                self.primitive_type()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==38:
                    self.state = 127
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 128
                    self.expr(0)


                pass
            elif token in [38]:
                self.state = 131
                self.match(MiniGoParser.ASSIGN)
                self.state = 132
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 135
                self.match(MiniGoParser.SEMICOLON)


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


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(MiniGoParser.CONST)
            self.state = 139
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 140
            self.match(MiniGoParser.ASSIGN)
            self.state = 141
            self.expr(0)
            self.state = 142
            self.match(MiniGoParser.SEMICOLON)
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


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(MiniGoParser.FUNC)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 145
                self.method()


            self.state = 148
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 149
            self.match(MiniGoParser.LB)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==63:
                self.state = 150
                self.param_list()


            self.state = 153
            self.match(MiniGoParser.RB)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -9222809086901293056) != 0):
                self.state = 154
                self.types()


            self.state = 157
            self.match(MiniGoParser.LCB)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223372036853791792) != 0):
                self.state = 158
                self.stmt()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self.match(MiniGoParser.RCB)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 165
                self.match(MiniGoParser.SEMICOLON)


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

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def args(self):
            return self.getTypedRuleContext(MiniGoParser.ArgsContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 168
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 169
                self.match(MiniGoParser.DOT)


            self.state = 172
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 173
            self.match(MiniGoParser.LB)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -558411031949344768) != 0):
                self.state = 174
                self.args()


            self.state = 177
            self.match(MiniGoParser.RB)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 178
                self.match(MiniGoParser.SEMICOLON)


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
        self.enterRule(localctx, 16, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.expr(0)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 182
                self.match(MiniGoParser.COMMA)
                self.state = 183
                self.expr(0)
                self.state = 188
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
        self.enterRule(localctx, 18, self.RULE_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(MiniGoParser.LB)
            self.state = 190
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 191
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 192
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
        self.enterRule(localctx, 20, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.param()
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 195
                self.match(MiniGoParser.COMMA)
                self.state = 196
                self.param()
                self.state = 201
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
        self.enterRule(localctx, 22, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -9222809086901293056) != 0):
                self.state = 203
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
        self.enterRule(localctx, 24, self.RULE_types)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13, 14, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.primitive_type()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.array_type()
                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
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
        self.enterRule(localctx, 26, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8664925683060834304) != 0)):
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
        self.enterRule(localctx, 28, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
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


        def index_ops(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Index_opsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Index_opsContext,i)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_array




    def assign_array(self):

        localctx = MiniGoParser.Assign_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assign_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 217 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 216
                self.index_ops()
                self.state = 219 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==49):
                    break

            self.state = 221
            self.match(MiniGoParser.ASSIGN)
            self.state = 222
            self.expr(0)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 223
                self.match(MiniGoParser.SEMICOLON)


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

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_decl




    def array_decl(self):

        localctx = MiniGoParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_array_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 226
                self.match(MiniGoParser.VAR)


            self.state = 229
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.state = 230
                self.array_type()
                pass
            elif token in [38]:
                self.state = 231
                self.match(MiniGoParser.ASSIGN)
                self.state = 232
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 235
                self.match(MiniGoParser.SEMICOLON)


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
        self.enterRule(localctx, 34, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.dimensions()
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13, 14, 15]:
                self.state = 239
                self.primitive_type()
                pass
            elif token in [63]:
                self.state = 240
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
        self.enterRule(localctx, 36, self.RULE_dimensions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 243
                self.match(MiniGoParser.LSB)
                self.state = 244
                self.match(MiniGoParser.INT_LITERAL)
                self.state = 245
                self.match(MiniGoParser.RSB)
                self.state = 248 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==49):
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
        self.enterRule(localctx, 38, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.array_type()
            self.state = 251
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
        self.enterRule(localctx, 40, self.RULE_ele_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(MiniGoParser.LCB)
            self.state = 254
            self.ele()
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 255
                self.match(MiniGoParser.COMMA)
                self.state = 256
                self.ele()
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 262
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
        self.enterRule(localctx, 42, self.RULE_ele)
        try:
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.ele_list()
                pass
            elif token in [54, 59, 60, 61, 62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
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


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_access_struct




    def access_struct(self):

        localctx = MiniGoParser.Access_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_access_struct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 269
            self.match(MiniGoParser.DOT)
            self.state = 270
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 271
            self.match(MiniGoParser.ASSIGN)
            self.state = 272
            self.expr(0)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 273
                self.match(MiniGoParser.SEMICOLON)


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

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_struct




    def assign_struct(self):

        localctx = MiniGoParser.Assign_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assign_struct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 277
            self.match(MiniGoParser.ASSIGN)
            self.state = 278
            self.struct_literal()
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 279
                self.match(MiniGoParser.SEMICOLON)


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


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(MiniGoParser.TYPE)
            self.state = 283
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 284
            self.struct_type()
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
        self.enterRule(localctx, 50, self.RULE_struct_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(MiniGoParser.STRUCT)
            self.state = 287
            self.match(MiniGoParser.LCB)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==63:
                self.state = 288
                self.fields()
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 294
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

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_fields




    def fields(self):

        localctx = MiniGoParser.FieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13, 14, 15]:
                self.state = 297
                self.primitive_type()
                pass
            elif token in [49]:
                self.state = 298
                self.array_type()
                pass
            elif token in [10]:
                self.state = 299
                self.struct_type()
                pass
            elif token in [63]:
                self.state = 300
                self.match(MiniGoParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 303
                self.match(MiniGoParser.SEMICOLON)


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
        self.enterRule(localctx, 54, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 307
            self.match(MiniGoParser.LCB)
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==63:
                self.state = 308
                self.field_lit()
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==51:
                    self.state = 309
                    self.match(MiniGoParser.COMMA)
                    self.state = 310
                    self.field_lit()
                    self.state = 315
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 318
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
        self.enterRule(localctx, 56, self.RULE_field_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 321
            self.match(MiniGoParser.COLON)
            self.state = 322
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(MiniGoParser.TYPE)
            self.state = 325
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 326
            self.interface_type()
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
        self.enterRule(localctx, 60, self.RULE_interface_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(MiniGoParser.INTERFACE)
            self.state = 329
            self.match(MiniGoParser.LCB)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==63:
                self.state = 330
                self.method_decl()
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 336
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

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 339
            self.match(MiniGoParser.LB)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==63:
                self.state = 340
                self.param_list()


            self.state = 343
            self.match(MiniGoParser.RB)
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 344
                self.types()


            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 347
                self.match(MiniGoParser.SEMICOLON)


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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.state = 351
                self.match(MiniGoParser.NOT)
                self.state = 352
                self.expr(5)
                pass
            elif token in [25]:
                self.state = 353
                self.match(MiniGoParser.SUB)
                self.state = 354
                self.expr(4)
                pass
            elif token in [45, 54, 59, 60, 61, 62, 63]:
                self.state = 355
                self.primary_expr()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 383
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 381
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 358
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 359
                        self.match(MiniGoParser.OR)
                        self.state = 360
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 361
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 362
                        self.match(MiniGoParser.AND)
                        self.state = 363
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 364
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 365
                        self.relational_ops()
                        self.state = 366
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 368
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 369
                        self.arithmetic_ops()
                        self.state = 370
                        self.expr(7)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 372
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 374 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 373
                                self.index_ops()

                            else:
                                raise NoViableAltException(self)
                            self.state = 376 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

                        pass

                    elif la_ == 6:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 378
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 379
                        self.match(MiniGoParser.DOT)
                        self.state = 380
                        self.match(MiniGoParser.IDENTIFIER)
                        pass

             
                self.state = 385
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
        self.enterRule(localctx, 66, self.RULE_primary_expr)
        try:
            self.state = 392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [63]:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [54, 59, 60, 61, 62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.literals()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 3)
                self.state = 388
                self.match(MiniGoParser.LB)
                self.state = 389
                self.expr(0)
                self.state = 390
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
        self.enterRule(localctx, 68, self.RULE_stmt)
        try:
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 396
                self.call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 397
                self.asm_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 398
                self.if_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 399
                self.for_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 400
                self.break_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 401
                self.continue_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 402
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


        def index_ops(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Index_opsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Index_opsContext,i)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_asm_stmt




    def asm_stmt(self):

        localctx = MiniGoParser.Asm_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_asm_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==49:
                self.state = 406
                self.index_ops()
                self.state = 411
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 412
            self.assign_ops()
            self.state = 413
            self.expr(0)
            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 414
                self.match(MiniGoParser.SEMICOLON)


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
        self.enterRule(localctx, 72, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(MiniGoParser.IF)
            self.state = 418
            self.match(MiniGoParser.LB)
            self.state = 419
            self.expr(0)
            self.state = 420
            self.match(MiniGoParser.RB)
            self.state = 421
            self.match(MiniGoParser.LCB)
            self.state = 425
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223372036853791792) != 0):
                self.state = 422
                self.stmt()
                self.state = 427
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 428
            self.match(MiniGoParser.RCB)
            self.state = 432
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 429
                    self.else_if_stmt() 
                self.state = 434
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

            self.state = 444
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 435
                self.match(MiniGoParser.ELSE)
                self.state = 436
                self.match(MiniGoParser.LCB)
                self.state = 440
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223372036853791792) != 0):
                    self.state = 437
                    self.stmt()
                    self.state = 442
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 443
                self.match(MiniGoParser.RCB)


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
        self.enterRule(localctx, 74, self.RULE_else_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(MiniGoParser.ELSE)
            self.state = 447
            self.match(MiniGoParser.IF)
            self.state = 448
            self.match(MiniGoParser.LB)
            self.state = 449
            self.expr(0)
            self.state = 450
            self.match(MiniGoParser.RB)
            self.state = 451
            self.match(MiniGoParser.LCB)
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223372036853791792) != 0):
                self.state = 452
                self.stmt()
                self.state = 457
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 458
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

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(MiniGoParser.FOR)
            self.state = 461
            self.for_clause()
            self.state = 462
            self.match(MiniGoParser.LCB)
            self.state = 466
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223372036853791792) != 0):
                self.state = 463
                self.stmt()
                self.state = 468
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 469
            self.match(MiniGoParser.RCB)
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
        self.enterRule(localctx, 78, self.RULE_for_clause)
        try:
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
                self.fully_clause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 473
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

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def asm_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Asm_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fully_clause




    def fully_clause(self):

        localctx = MiniGoParser.Fully_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_fully_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17 or _la==63:
                self.state = 476
                self.var_decl()


            self.state = 479
            self.match(MiniGoParser.SEMICOLON)
            self.state = 480
            self.expr(0)
            self.state = 481
            self.match(MiniGoParser.SEMICOLON)
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==63:
                self.state = 482
                self.asm_stmt()


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

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_range_clause




    def range_clause(self):

        localctx = MiniGoParser.Range_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_range_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            _la = self._input.LA(1)
            if not(_la==1 or _la==63):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 486
            self.match(MiniGoParser.COMMA)
            self.state = 487
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 488
            self.match(MiniGoParser.ASSIGN)
            self.state = 489
            self.match(MiniGoParser.RANGE)
            self.state = 490
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

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(MiniGoParser.BREAK)
            self.state = 493
            self.match(MiniGoParser.SEMICOLON)
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

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(MiniGoParser.CONTINUE)
            self.state = 496
            self.match(MiniGoParser.SEMICOLON)
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

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(MiniGoParser.RETURN)
            self.state = 500
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -558411031949344768) != 0):
                self.state = 499
                self.expr(0)


            self.state = 502
            self.match(MiniGoParser.SEMICOLON)
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
        self.enterRule(localctx, 90, self.RULE_boolean_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 240518168576) != 0)):
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
        self.enterRule(localctx, 92, self.RULE_arithmetic_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 520093696) != 0)):
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
        self.enterRule(localctx, 94, self.RULE_relational_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33822867456) != 0)):
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
        self.enterRule(localctx, 96, self.RULE_assign_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17042430230528) != 0)):
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
        self.enterRule(localctx, 98, self.RULE_index_ops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(MiniGoParser.LSB)
            self.state = 513
            self.expr(0)
            self.state = 514
            self.match(MiniGoParser.RSB)
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
        self._predicates[32] = self.expr_sempred
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
         




