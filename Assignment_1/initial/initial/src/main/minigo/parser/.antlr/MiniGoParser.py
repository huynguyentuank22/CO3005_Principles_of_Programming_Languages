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
        4,1,69,614,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,1,0,4,0,128,8,0,11,0,12,0,129,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,142,8,1,1,2,1,2,1,2,
        3,2,147,8,2,1,3,1,3,1,4,3,4,152,8,4,1,4,1,4,1,4,1,4,3,4,158,8,4,
        1,4,1,4,3,4,162,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,7,1,7,3,7,179,8,7,1,7,1,7,1,7,3,7,184,8,7,1,7,1,7,3,7,
        188,8,7,1,7,1,7,5,7,192,8,7,10,7,12,7,195,9,7,1,7,1,7,1,7,1,8,1,
        8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,5,10,211,8,10,10,10,12,
        10,214,9,10,1,11,1,11,3,11,218,8,11,1,12,1,12,1,12,3,12,223,8,12,
        1,13,1,13,1,14,1,14,1,15,1,15,4,15,231,8,15,11,15,12,15,232,1,15,
        1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,3,16,244,8,16,1,16,1,16,
        1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,3,18,256,8,18,1,19,1,19,
        1,19,4,19,261,8,19,11,19,12,19,262,1,20,1,20,1,20,1,21,1,21,1,21,
        1,21,5,21,272,8,21,10,21,12,21,275,9,21,1,21,1,21,1,22,1,22,3,22,
        281,8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,
        1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,5,26,303,8,26,10,26,
        12,26,306,9,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,3,27,315,8,27,
        1,27,1,27,1,28,1,28,1,28,1,28,1,28,5,28,324,8,28,10,28,12,28,327,
        9,28,3,28,329,8,28,1,28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,
        1,30,1,30,1,31,1,31,1,31,5,31,345,8,31,10,31,12,31,348,9,31,1,31,
        1,31,1,32,1,32,1,32,3,32,355,8,32,1,32,1,32,3,32,359,8,32,1,32,1,
        32,1,33,1,33,1,33,1,33,1,33,1,33,5,33,369,8,33,10,33,12,33,372,9,
        33,1,34,1,34,1,34,1,34,1,34,1,34,5,34,380,8,34,10,34,12,34,383,9,
        34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,5,35,392,8,35,10,35,12,35,
        395,9,35,1,36,1,36,1,36,1,36,1,36,1,36,5,36,403,8,36,10,36,12,36,
        406,9,36,1,37,1,37,1,37,1,37,1,37,1,37,5,37,414,8,37,10,37,12,37,
        417,9,37,1,38,1,38,1,38,3,38,422,8,38,1,39,1,39,1,39,1,39,1,39,1,
        39,1,39,3,39,431,8,39,5,39,433,8,39,10,39,12,39,436,9,39,1,40,1,
        40,1,40,1,40,1,40,3,40,443,8,40,1,41,1,41,1,41,1,41,1,41,3,41,450,
        8,41,1,42,1,42,1,42,1,42,1,42,1,42,1,42,3,42,459,8,42,1,43,1,43,
        1,43,1,43,1,43,1,43,1,43,1,43,1,43,3,43,470,8,43,1,44,1,44,5,44,
        474,8,44,10,44,12,44,477,9,44,1,44,1,44,1,44,1,44,1,45,1,45,1,45,
        1,45,1,45,1,45,5,45,489,8,45,10,45,12,45,492,9,45,1,45,1,45,5,45,
        496,8,45,10,45,12,45,499,9,45,1,45,1,45,1,45,5,45,504,8,45,10,45,
        12,45,507,9,45,1,45,3,45,510,8,45,1,45,1,45,1,46,1,46,1,46,1,46,
        1,46,1,46,1,46,5,46,521,8,46,10,46,12,46,524,9,46,1,46,1,46,1,47,
        1,47,1,47,1,47,5,47,532,8,47,10,47,12,47,535,9,47,1,47,1,47,1,47,
        1,48,1,48,1,48,3,48,543,8,48,1,49,3,49,546,8,49,1,49,1,49,3,49,550,
        8,49,1,49,1,49,3,49,554,8,49,1,50,1,50,1,50,1,50,1,51,1,51,5,51,
        562,8,51,10,51,12,51,565,9,51,1,51,1,51,1,51,1,52,1,52,1,52,1,52,
        1,52,1,52,1,52,1,53,1,53,1,53,1,54,1,54,1,54,1,55,1,55,3,55,585,
        8,55,1,55,1,55,1,56,1,56,1,57,1,57,1,58,1,58,1,59,1,59,1,60,1,60,
        1,60,1,60,1,61,1,61,3,61,603,8,61,1,61,1,61,1,61,3,61,608,8,61,1,
        61,1,61,1,62,1,62,1,62,0,6,66,68,70,72,74,78,63,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,
        102,104,106,108,110,112,114,116,118,120,122,124,0,12,3,0,3,4,55,
        55,60,61,1,0,13,16,1,0,25,26,1,0,27,29,2,0,26,26,38,38,1,0,39,40,
        2,0,2,2,62,62,1,0,36,38,1,0,25,29,1,0,30,35,1,0,41,45,2,0,54,54,
        66,66,623,0,127,1,0,0,0,2,141,1,0,0,0,4,146,1,0,0,0,6,148,1,0,0,
        0,8,151,1,0,0,0,10,165,1,0,0,0,12,170,1,0,0,0,14,176,1,0,0,0,16,
        199,1,0,0,0,18,202,1,0,0,0,20,207,1,0,0,0,22,215,1,0,0,0,24,222,
        1,0,0,0,26,224,1,0,0,0,28,226,1,0,0,0,30,228,1,0,0,0,32,238,1,0,
        0,0,34,247,1,0,0,0,36,252,1,0,0,0,38,260,1,0,0,0,40,264,1,0,0,0,
        42,267,1,0,0,0,44,280,1,0,0,0,46,282,1,0,0,0,48,289,1,0,0,0,50,294,
        1,0,0,0,52,299,1,0,0,0,54,309,1,0,0,0,56,318,1,0,0,0,58,332,1,0,
        0,0,60,336,1,0,0,0,62,341,1,0,0,0,64,351,1,0,0,0,66,362,1,0,0,0,
        68,373,1,0,0,0,70,384,1,0,0,0,72,396,1,0,0,0,74,407,1,0,0,0,76,421,
        1,0,0,0,78,423,1,0,0,0,80,442,1,0,0,0,82,449,1,0,0,0,84,458,1,0,
        0,0,86,469,1,0,0,0,88,471,1,0,0,0,90,482,1,0,0,0,92,513,1,0,0,0,
        94,527,1,0,0,0,96,542,1,0,0,0,98,545,1,0,0,0,100,555,1,0,0,0,102,
        559,1,0,0,0,104,569,1,0,0,0,106,576,1,0,0,0,108,579,1,0,0,0,110,
        582,1,0,0,0,112,588,1,0,0,0,114,590,1,0,0,0,116,592,1,0,0,0,118,
        594,1,0,0,0,120,596,1,0,0,0,122,602,1,0,0,0,124,611,1,0,0,0,126,
        128,3,86,43,0,127,126,1,0,0,0,128,129,1,0,0,0,129,127,1,0,0,0,129,
        130,1,0,0,0,130,131,1,0,0,0,131,132,5,0,0,1,132,1,1,0,0,0,133,142,
        3,14,7,0,134,142,3,8,4,0,135,142,3,10,5,0,136,142,3,12,6,0,137,142,
        3,32,16,0,138,142,3,34,17,0,139,142,3,50,25,0,140,142,3,60,30,0,
        141,133,1,0,0,0,141,134,1,0,0,0,141,135,1,0,0,0,141,136,1,0,0,0,
        141,137,1,0,0,0,141,138,1,0,0,0,141,139,1,0,0,0,141,140,1,0,0,0,
        142,3,1,0,0,0,143,147,3,30,15,0,144,147,3,48,24,0,145,147,3,46,23,
        0,146,143,1,0,0,0,146,144,1,0,0,0,146,145,1,0,0,0,147,5,1,0,0,0,
        148,149,3,16,8,0,149,7,1,0,0,0,150,152,5,18,0,0,151,150,1,0,0,0,
        151,152,1,0,0,0,152,153,1,0,0,0,153,161,5,62,0,0,154,157,3,28,14,
        0,155,156,5,39,0,0,156,158,3,66,33,0,157,155,1,0,0,0,157,158,1,0,
        0,0,158,162,1,0,0,0,159,160,5,39,0,0,160,162,3,66,33,0,161,154,1,
        0,0,0,161,159,1,0,0,0,162,163,1,0,0,0,163,164,3,124,62,0,164,9,1,
        0,0,0,165,166,5,62,0,0,166,167,5,40,0,0,167,168,3,66,33,0,168,169,
        3,124,62,0,169,11,1,0,0,0,170,171,5,17,0,0,171,172,5,62,0,0,172,
        173,5,39,0,0,173,174,3,66,33,0,174,175,3,124,62,0,175,13,1,0,0,0,
        176,178,5,9,0,0,177,179,3,18,9,0,178,177,1,0,0,0,178,179,1,0,0,0,
        179,180,1,0,0,0,180,181,5,62,0,0,181,183,5,47,0,0,182,184,3,20,10,
        0,183,182,1,0,0,0,183,184,1,0,0,0,184,185,1,0,0,0,185,187,5,48,0,
        0,186,188,3,24,12,0,187,186,1,0,0,0,187,188,1,0,0,0,188,189,1,0,
        0,0,189,193,5,49,0,0,190,192,3,86,43,0,191,190,1,0,0,0,192,195,1,
        0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,196,1,0,0,0,195,193,1,
        0,0,0,196,197,5,50,0,0,197,198,3,124,62,0,198,15,1,0,0,0,199,200,
        3,122,61,0,200,201,3,124,62,0,201,17,1,0,0,0,202,203,5,47,0,0,203,
        204,5,62,0,0,204,205,5,62,0,0,205,206,5,48,0,0,206,19,1,0,0,0,207,
        212,3,22,11,0,208,209,5,53,0,0,209,211,3,22,11,0,210,208,1,0,0,0,
        211,214,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,213,21,1,0,0,0,214,
        212,1,0,0,0,215,217,5,62,0,0,216,218,3,24,12,0,217,216,1,0,0,0,217,
        218,1,0,0,0,218,23,1,0,0,0,219,223,3,28,14,0,220,223,3,36,18,0,221,
        223,5,62,0,0,222,219,1,0,0,0,222,220,1,0,0,0,222,221,1,0,0,0,223,
        25,1,0,0,0,224,225,7,0,0,0,225,27,1,0,0,0,226,227,7,1,0,0,227,29,
        1,0,0,0,228,230,5,62,0,0,229,231,3,120,60,0,230,229,1,0,0,0,231,
        232,1,0,0,0,232,230,1,0,0,0,232,233,1,0,0,0,233,234,1,0,0,0,234,
        235,5,39,0,0,235,236,3,66,33,0,236,237,3,124,62,0,237,31,1,0,0,0,
        238,239,5,18,0,0,239,243,5,62,0,0,240,244,3,36,18,0,241,242,5,39,
        0,0,242,244,3,40,20,0,243,240,1,0,0,0,243,241,1,0,0,0,244,245,1,
        0,0,0,245,246,3,124,62,0,246,33,1,0,0,0,247,248,5,62,0,0,248,249,
        5,40,0,0,249,250,3,40,20,0,250,251,3,124,62,0,251,35,1,0,0,0,252,
        255,3,38,19,0,253,256,3,28,14,0,254,256,5,62,0,0,255,253,1,0,0,0,
        255,254,1,0,0,0,256,37,1,0,0,0,257,258,5,51,0,0,258,259,5,55,0,0,
        259,261,5,52,0,0,260,257,1,0,0,0,261,262,1,0,0,0,262,260,1,0,0,0,
        262,263,1,0,0,0,263,39,1,0,0,0,264,265,3,36,18,0,265,266,3,42,21,
        0,266,41,1,0,0,0,267,268,5,49,0,0,268,273,3,44,22,0,269,270,5,53,
        0,0,270,272,3,44,22,0,271,269,1,0,0,0,272,275,1,0,0,0,273,271,1,
        0,0,0,273,274,1,0,0,0,274,276,1,0,0,0,275,273,1,0,0,0,276,277,5,
        50,0,0,277,43,1,0,0,0,278,281,3,42,21,0,279,281,3,26,13,0,280,278,
        1,0,0,0,280,279,1,0,0,0,281,45,1,0,0,0,282,283,5,62,0,0,283,284,
        5,46,0,0,284,285,5,62,0,0,285,286,5,39,0,0,286,287,3,66,33,0,287,
        288,3,124,62,0,288,47,1,0,0,0,289,290,5,62,0,0,290,291,5,40,0,0,
        291,292,3,56,28,0,292,293,3,124,62,0,293,49,1,0,0,0,294,295,5,10,
        0,0,295,296,5,62,0,0,296,297,3,52,26,0,297,298,3,124,62,0,298,51,
        1,0,0,0,299,300,5,11,0,0,300,304,5,49,0,0,301,303,3,54,27,0,302,
        301,1,0,0,0,303,306,1,0,0,0,304,302,1,0,0,0,304,305,1,0,0,0,305,
        307,1,0,0,0,306,304,1,0,0,0,307,308,5,50,0,0,308,53,1,0,0,0,309,
        314,5,62,0,0,310,315,3,28,14,0,311,315,3,36,18,0,312,315,3,52,26,
        0,313,315,5,62,0,0,314,310,1,0,0,0,314,311,1,0,0,0,314,312,1,0,0,
        0,314,313,1,0,0,0,315,316,1,0,0,0,316,317,3,124,62,0,317,55,1,0,
        0,0,318,319,5,62,0,0,319,328,5,49,0,0,320,325,3,58,29,0,321,322,
        5,53,0,0,322,324,3,58,29,0,323,321,1,0,0,0,324,327,1,0,0,0,325,323,
        1,0,0,0,325,326,1,0,0,0,326,329,1,0,0,0,327,325,1,0,0,0,328,320,
        1,0,0,0,328,329,1,0,0,0,329,330,1,0,0,0,330,331,5,50,0,0,331,57,
        1,0,0,0,332,333,5,62,0,0,333,334,5,1,0,0,334,335,3,66,33,0,335,59,
        1,0,0,0,336,337,5,10,0,0,337,338,5,62,0,0,338,339,3,62,31,0,339,
        340,3,124,62,0,340,61,1,0,0,0,341,342,5,12,0,0,342,346,5,49,0,0,
        343,345,3,64,32,0,344,343,1,0,0,0,345,348,1,0,0,0,346,344,1,0,0,
        0,346,347,1,0,0,0,347,349,1,0,0,0,348,346,1,0,0,0,349,350,5,50,0,
        0,350,63,1,0,0,0,351,352,5,62,0,0,352,354,5,47,0,0,353,355,3,20,
        10,0,354,353,1,0,0,0,354,355,1,0,0,0,355,356,1,0,0,0,356,358,5,48,
        0,0,357,359,3,24,12,0,358,357,1,0,0,0,358,359,1,0,0,0,359,360,1,
        0,0,0,360,361,3,124,62,0,361,65,1,0,0,0,362,363,6,33,-1,0,363,364,
        3,68,34,0,364,370,1,0,0,0,365,366,10,2,0,0,366,367,5,37,0,0,367,
        369,3,68,34,0,368,365,1,0,0,0,369,372,1,0,0,0,370,368,1,0,0,0,370,
        371,1,0,0,0,371,67,1,0,0,0,372,370,1,0,0,0,373,374,6,34,-1,0,374,
        375,3,70,35,0,375,381,1,0,0,0,376,377,10,2,0,0,377,378,5,36,0,0,
        378,380,3,70,35,0,379,376,1,0,0,0,380,383,1,0,0,0,381,379,1,0,0,
        0,381,382,1,0,0,0,382,69,1,0,0,0,383,381,1,0,0,0,384,385,6,35,-1,
        0,385,386,3,72,36,0,386,393,1,0,0,0,387,388,10,2,0,0,388,389,3,116,
        58,0,389,390,3,72,36,0,390,392,1,0,0,0,391,387,1,0,0,0,392,395,1,
        0,0,0,393,391,1,0,0,0,393,394,1,0,0,0,394,71,1,0,0,0,395,393,1,0,
        0,0,396,397,6,36,-1,0,397,398,3,74,37,0,398,404,1,0,0,0,399,400,
        10,2,0,0,400,401,7,2,0,0,401,403,3,74,37,0,402,399,1,0,0,0,403,406,
        1,0,0,0,404,402,1,0,0,0,404,405,1,0,0,0,405,73,1,0,0,0,406,404,1,
        0,0,0,407,408,6,37,-1,0,408,409,3,76,38,0,409,415,1,0,0,0,410,411,
        10,2,0,0,411,412,7,3,0,0,412,414,3,76,38,0,413,410,1,0,0,0,414,417,
        1,0,0,0,415,413,1,0,0,0,415,416,1,0,0,0,416,75,1,0,0,0,417,415,1,
        0,0,0,418,419,7,4,0,0,419,422,3,76,38,0,420,422,3,78,39,0,421,418,
        1,0,0,0,421,420,1,0,0,0,422,77,1,0,0,0,423,424,6,39,-1,0,424,425,
        3,80,40,0,425,434,1,0,0,0,426,430,10,2,0,0,427,428,5,46,0,0,428,
        431,5,62,0,0,429,431,3,120,60,0,430,427,1,0,0,0,430,429,1,0,0,0,
        431,433,1,0,0,0,432,426,1,0,0,0,433,436,1,0,0,0,434,432,1,0,0,0,
        434,435,1,0,0,0,435,79,1,0,0,0,436,434,1,0,0,0,437,438,5,47,0,0,
        438,439,3,82,41,0,439,440,5,48,0,0,440,443,1,0,0,0,441,443,3,84,
        42,0,442,437,1,0,0,0,442,441,1,0,0,0,443,81,1,0,0,0,444,445,3,66,
        33,0,445,446,5,53,0,0,446,447,3,82,41,0,447,450,1,0,0,0,448,450,
        3,66,33,0,449,444,1,0,0,0,449,448,1,0,0,0,450,83,1,0,0,0,451,459,
        3,26,13,0,452,459,5,62,0,0,453,459,3,122,61,0,454,455,5,47,0,0,455,
        456,3,66,33,0,456,457,5,48,0,0,457,459,1,0,0,0,458,451,1,0,0,0,458,
        452,1,0,0,0,458,453,1,0,0,0,458,454,1,0,0,0,459,85,1,0,0,0,460,470,
        3,2,1,0,461,470,3,4,2,0,462,470,3,6,3,0,463,470,3,88,44,0,464,470,
        3,90,45,0,465,470,3,94,47,0,466,470,3,106,53,0,467,470,3,108,54,
        0,468,470,3,110,55,0,469,460,1,0,0,0,469,461,1,0,0,0,469,462,1,0,
        0,0,469,463,1,0,0,0,469,464,1,0,0,0,469,465,1,0,0,0,469,466,1,0,
        0,0,469,467,1,0,0,0,469,468,1,0,0,0,470,87,1,0,0,0,471,475,5,62,
        0,0,472,474,3,120,60,0,473,472,1,0,0,0,474,477,1,0,0,0,475,473,1,
        0,0,0,475,476,1,0,0,0,476,478,1,0,0,0,477,475,1,0,0,0,478,479,3,
        118,59,0,479,480,3,66,33,0,480,481,3,124,62,0,481,89,1,0,0,0,482,
        483,5,5,0,0,483,484,5,47,0,0,484,485,3,66,33,0,485,486,5,48,0,0,
        486,490,5,49,0,0,487,489,3,86,43,0,488,487,1,0,0,0,489,492,1,0,0,
        0,490,488,1,0,0,0,490,491,1,0,0,0,491,493,1,0,0,0,492,490,1,0,0,
        0,493,497,5,50,0,0,494,496,3,92,46,0,495,494,1,0,0,0,496,499,1,0,
        0,0,497,495,1,0,0,0,497,498,1,0,0,0,498,509,1,0,0,0,499,497,1,0,
        0,0,500,501,5,6,0,0,501,505,5,49,0,0,502,504,3,86,43,0,503,502,1,
        0,0,0,504,507,1,0,0,0,505,503,1,0,0,0,505,506,1,0,0,0,506,508,1,
        0,0,0,507,505,1,0,0,0,508,510,5,50,0,0,509,500,1,0,0,0,509,510,1,
        0,0,0,510,511,1,0,0,0,511,512,3,124,62,0,512,91,1,0,0,0,513,514,
        5,6,0,0,514,515,5,5,0,0,515,516,5,47,0,0,516,517,3,66,33,0,517,518,
        5,48,0,0,518,522,5,49,0,0,519,521,3,86,43,0,520,519,1,0,0,0,521,
        524,1,0,0,0,522,520,1,0,0,0,522,523,1,0,0,0,523,525,1,0,0,0,524,
        522,1,0,0,0,525,526,5,50,0,0,526,93,1,0,0,0,527,528,5,7,0,0,528,
        529,3,96,48,0,529,533,5,49,0,0,530,532,3,86,43,0,531,530,1,0,0,0,
        532,535,1,0,0,0,533,531,1,0,0,0,533,534,1,0,0,0,534,536,1,0,0,0,
        535,533,1,0,0,0,536,537,5,50,0,0,537,538,3,124,62,0,538,95,1,0,0,
        0,539,543,3,66,33,0,540,543,3,98,49,0,541,543,3,104,52,0,542,539,
        1,0,0,0,542,540,1,0,0,0,542,541,1,0,0,0,543,97,1,0,0,0,544,546,3,
        100,50,0,545,544,1,0,0,0,545,546,1,0,0,0,546,547,1,0,0,0,547,549,
        3,124,62,0,548,550,3,66,33,0,549,548,1,0,0,0,549,550,1,0,0,0,550,
        551,1,0,0,0,551,553,3,124,62,0,552,554,3,102,51,0,553,552,1,0,0,
        0,553,554,1,0,0,0,554,99,1,0,0,0,555,556,5,62,0,0,556,557,7,5,0,
        0,557,558,3,66,33,0,558,101,1,0,0,0,559,563,5,62,0,0,560,562,3,120,
        60,0,561,560,1,0,0,0,562,565,1,0,0,0,563,561,1,0,0,0,563,564,1,0,
        0,0,564,566,1,0,0,0,565,563,1,0,0,0,566,567,3,118,59,0,567,568,3,
        66,33,0,568,103,1,0,0,0,569,570,7,6,0,0,570,571,5,53,0,0,571,572,
        5,62,0,0,572,573,5,40,0,0,573,574,5,21,0,0,574,575,5,62,0,0,575,
        105,1,0,0,0,576,577,5,20,0,0,577,578,3,124,62,0,578,107,1,0,0,0,
        579,580,5,19,0,0,580,581,3,124,62,0,581,109,1,0,0,0,582,584,5,8,
        0,0,583,585,3,66,33,0,584,583,1,0,0,0,584,585,1,0,0,0,585,586,1,
        0,0,0,586,587,3,124,62,0,587,111,1,0,0,0,588,589,7,7,0,0,589,113,
        1,0,0,0,590,591,7,8,0,0,591,115,1,0,0,0,592,593,7,9,0,0,593,117,
        1,0,0,0,594,595,7,10,0,0,595,119,1,0,0,0,596,597,5,51,0,0,597,598,
        3,66,33,0,598,599,5,52,0,0,599,121,1,0,0,0,600,601,5,62,0,0,601,
        603,5,46,0,0,602,600,1,0,0,0,602,603,1,0,0,0,603,604,1,0,0,0,604,
        605,5,62,0,0,605,607,5,47,0,0,606,608,3,82,41,0,607,606,1,0,0,0,
        607,608,1,0,0,0,608,609,1,0,0,0,609,610,5,48,0,0,610,123,1,0,0,0,
        611,612,7,11,0,0,612,125,1,0,0,0,53,129,141,146,151,157,161,178,
        183,187,193,212,217,222,232,243,255,262,273,280,304,314,325,328,
        346,354,358,370,381,393,404,415,421,430,434,442,449,458,469,475,
        490,497,505,509,522,533,542,545,549,553,563,584,602,607
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'_'", "<INVALID>", "<INVALID>", 
                     "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
                     "'struct'", "'interface'", "'string'", "'int'", "'float'", 
                     "'boolean'", "'const'", "'var'", "'continue'", "'break'", 
                     "'range'", "'nil'", "'true'", "'false'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'&&'", "'||'", "'!'", "'='", "':='", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "BOOLEAN_LITERAL", 
                      "NIL_LITERAL", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQ", "NEQ", "LT", "LE", "GT", "GE", "AND", 
                      "OR", "NOT", "ASSIGN", "DECLARE_ASSIGN", "PLUS_ASSIGN", 
                      "MINUS_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "DOT", "LB", "RB", "LCB", "RCB", "LSB", "RSB", "COMMA", 
                      "SEMICOLON", "INT_LITERAL", "DECIMAL_LITERAL", "BINARY_LITERAL", 
                      "OCTAL_LITERAL", "HEX_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
                      "IDENTIFIER", "LINE_COMMENT", "COMMENT", "WS", "EOS", 
                      "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_assign = 2
    RULE_call = 3
    RULE_var_decl = 4
    RULE_short_var_decl = 5
    RULE_const_decl = 6
    RULE_func_decl = 7
    RULE_func_call = 8
    RULE_method = 9
    RULE_param_list = 10
    RULE_param = 11
    RULE_types = 12
    RULE_literals = 13
    RULE_primitive_type = 14
    RULE_assign_array = 15
    RULE_array_decl = 16
    RULE_short_array_decl = 17
    RULE_array_type = 18
    RULE_dimensions = 19
    RULE_array_literal = 20
    RULE_ele_list = 21
    RULE_ele = 22
    RULE_access_struct = 23
    RULE_assign_struct = 24
    RULE_struct_decl = 25
    RULE_struct_type = 26
    RULE_fields = 27
    RULE_struct_literal = 28
    RULE_field_lit = 29
    RULE_interface_decl = 30
    RULE_interface_type = 31
    RULE_method_decl = 32
    RULE_expr = 33
    RULE_expr1 = 34
    RULE_expr2 = 35
    RULE_expr3 = 36
    RULE_expr4 = 37
    RULE_expr5 = 38
    RULE_expr6 = 39
    RULE_expr7 = 40
    RULE_expr_list = 41
    RULE_operand = 42
    RULE_stmt = 43
    RULE_asm_stmt = 44
    RULE_if_stmt = 45
    RULE_else_if_stmt = 46
    RULE_for_stmt = 47
    RULE_for_clause = 48
    RULE_fully_clause = 49
    RULE_init = 50
    RULE_update = 51
    RULE_range_clause = 52
    RULE_break_stmt = 53
    RULE_continue_stmt = 54
    RULE_return_stmt = 55
    RULE_boolean_ops = 56
    RULE_arithmetic_ops = 57
    RULE_relational_ops = 58
    RULE_assign_ops = 59
    RULE_index_ops = 60
    RULE_call_expr = 61
    RULE_eos = 62

    ruleNames =  [ "program", "decl", "assign", "call", "var_decl", "short_var_decl", 
                   "const_decl", "func_decl", "func_call", "method", "param_list", 
                   "param", "types", "literals", "primitive_type", "assign_array", 
                   "array_decl", "short_array_decl", "array_type", "dimensions", 
                   "array_literal", "ele_list", "ele", "access_struct", 
                   "assign_struct", "struct_decl", "struct_type", "fields", 
                   "struct_literal", "field_lit", "interface_decl", "interface_type", 
                   "method_decl", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "expr_list", "operand", "stmt", 
                   "asm_stmt", "if_stmt", "else_if_stmt", "for_stmt", "for_clause", 
                   "fully_clause", "init", "update", "range_clause", "break_stmt", 
                   "continue_stmt", "return_stmt", "boolean_ops", "arithmetic_ops", 
                   "relational_ops", "assign_ops", "index_ops", "call_expr", 
                   "eos" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    BOOLEAN_LITERAL=3
    NIL_LITERAL=4
    IF=5
    ELSE=6
    FOR=7
    RETURN=8
    FUNC=9
    TYPE=10
    STRUCT=11
    INTERFACE=12
    STRING=13
    INT=14
    FLOAT=15
    BOOLEAN=16
    CONST=17
    VAR=18
    CONTINUE=19
    BREAK=20
    RANGE=21
    NIL=22
    TRUE=23
    FALSE=24
    ADD=25
    SUB=26
    MUL=27
    DIV=28
    MOD=29
    EQ=30
    NEQ=31
    LT=32
    LE=33
    GT=34
    GE=35
    AND=36
    OR=37
    NOT=38
    ASSIGN=39
    DECLARE_ASSIGN=40
    PLUS_ASSIGN=41
    MINUS_ASSIGN=42
    MULT_ASSIGN=43
    DIV_ASSIGN=44
    MOD_ASSIGN=45
    DOT=46
    LB=47
    RB=48
    LCB=49
    RCB=50
    LSB=51
    RSB=52
    COMMA=53
    SEMICOLON=54
    INT_LITERAL=55
    DECIMAL_LITERAL=56
    BINARY_LITERAL=57
    OCTAL_LITERAL=58
    HEX_LITERAL=59
    FLOAT_LITERAL=60
    STRING_LITERAL=61
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
            self.state = 127 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 126
                self.stmt()
                self.state = 129 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018429355936) != 0)):
                    break

            self.state = 131
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
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.func_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.var_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.short_var_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.const_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 137
                self.array_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 138
                self.short_array_decl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 139
                self.struct_decl()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 140
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
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.assign_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.assign_struct()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
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
            self.state = 148
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
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 150
                self.match(MiniGoParser.VAR)


            self.state = 153
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.state = 154
                self.primitive_type()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 155
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 156
                    self.expr(0)


                pass
            elif token in [39]:
                self.state = 159
                self.match(MiniGoParser.ASSIGN)
                self.state = 160
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 163
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
            self.state = 165
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 166
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 167
            self.expr(0)
            self.state = 168
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
            self.state = 170
            self.match(MiniGoParser.CONST)
            self.state = 171
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 172
            self.match(MiniGoParser.ASSIGN)
            self.state = 173
            self.expr(0)
            self.state = 174
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
            self.state = 176
            self.match(MiniGoParser.FUNC)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 177
                self.method()


            self.state = 180
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 181
            self.match(MiniGoParser.LB)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 182
                self.param_list()


            self.state = 185
            self.match(MiniGoParser.RB)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4613937818241196032) != 0):
                self.state = 186
                self.types()


            self.state = 189
            self.match(MiniGoParser.LCB)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018429355936) != 0):
                self.state = 190
                self.stmt()
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 196
            self.match(MiniGoParser.RCB)
            self.state = 197
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

        def call_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Call_exprContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.call_expr()
            self.state = 200
            self.eos()
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
            self.state = 202
            self.match(MiniGoParser.LB)
            self.state = 203
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 204
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 205
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
            self.state = 207
            self.param()
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 208
                self.match(MiniGoParser.COMMA)
                self.state = 209
                self.param()
                self.state = 214
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
            self.state = 215
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4613937818241196032) != 0):
                self.state = 216
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
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.primitive_type()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.array_type()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
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
            self.state = 224
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3494793310839504920) != 0)):
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
            self.state = 226
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
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
        self.enterRule(localctx, 30, self.RULE_assign_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 230 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 229
                self.index_ops()
                self.state = 232 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==51):
                    break

            self.state = 234
            self.match(MiniGoParser.ASSIGN)
            self.state = 235
            self.expr(0)
            self.state = 236
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
        self.enterRule(localctx, 32, self.RULE_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MiniGoParser.VAR)
            self.state = 239
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.state = 240
                self.array_type()
                pass
            elif token in [39]:
                self.state = 241
                self.match(MiniGoParser.ASSIGN)
                self.state = 242
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 245
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
        self.enterRule(localctx, 34, self.RULE_short_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 248
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 249
            self.array_literal()
            self.state = 250
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
        self.enterRule(localctx, 36, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.dimensions()
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.state = 253
                self.primitive_type()
                pass
            elif token in [62]:
                self.state = 254
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
        self.enterRule(localctx, 38, self.RULE_dimensions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 257
                self.match(MiniGoParser.LSB)
                self.state = 258
                self.match(MiniGoParser.INT_LITERAL)
                self.state = 259
                self.match(MiniGoParser.RSB)
                self.state = 262 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==51):
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
        self.enterRule(localctx, 40, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.array_type()
            self.state = 265
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
        self.enterRule(localctx, 42, self.RULE_ele_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(MiniGoParser.LCB)
            self.state = 268
            self.ele()
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 269
                self.match(MiniGoParser.COMMA)
                self.state = 270
                self.ele()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 276
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
        self.enterRule(localctx, 44, self.RULE_ele)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.ele_list()
                pass
            elif token in [3, 4, 55, 60, 61]:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
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
        self.enterRule(localctx, 46, self.RULE_access_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 283
            self.match(MiniGoParser.DOT)
            self.state = 284
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 285
            self.match(MiniGoParser.ASSIGN)
            self.state = 286
            self.expr(0)
            self.state = 287
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
        self.enterRule(localctx, 48, self.RULE_assign_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 290
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 291
            self.struct_literal()
            self.state = 292
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
        self.enterRule(localctx, 50, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(MiniGoParser.TYPE)
            self.state = 295
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 296
            self.struct_type()
            self.state = 297
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
        self.enterRule(localctx, 52, self.RULE_struct_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(MiniGoParser.STRUCT)
            self.state = 300
            self.match(MiniGoParser.LCB)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 301
                self.fields()
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 307
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
        self.enterRule(localctx, 54, self.RULE_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.state = 310
                self.primitive_type()
                pass
            elif token in [51]:
                self.state = 311
                self.array_type()
                pass
            elif token in [11]:
                self.state = 312
                self.struct_type()
                pass
            elif token in [62]:
                self.state = 313
                self.match(MiniGoParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 316
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
        self.enterRule(localctx, 56, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 319
            self.match(MiniGoParser.LCB)
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 320
                self.field_lit()
                self.state = 325
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==53:
                    self.state = 321
                    self.match(MiniGoParser.COMMA)
                    self.state = 322
                    self.field_lit()
                    self.state = 327
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 330
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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_lit




    def field_lit(self):

        localctx = MiniGoParser.Field_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_field_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 333
            self.match(MiniGoParser.T__0)
            self.state = 334
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
        self.enterRule(localctx, 60, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(MiniGoParser.TYPE)
            self.state = 337
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 338
            self.interface_type()
            self.state = 339
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
        self.enterRule(localctx, 62, self.RULE_interface_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(MiniGoParser.INTERFACE)
            self.state = 342
            self.match(MiniGoParser.LCB)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 343
                self.method_decl()
                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 349
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
        self.enterRule(localctx, 64, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 352
            self.match(MiniGoParser.LB)
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 353
                self.param_list()


            self.state = 356
            self.match(MiniGoParser.RB)
            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4613937818241196032) != 0):
                self.state = 357
                self.types()


            self.state = 360
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

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 365
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 366
                    self.match(MiniGoParser.OR)
                    self.state = 367
                    self.expr1(0) 
                self.state = 372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 376
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 377
                    self.match(MiniGoParser.AND)
                    self.state = 378
                    self.expr2(0) 
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def relational_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Relational_opsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 393
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 387
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 388
                    self.relational_ops()
                    self.state = 389
                    self.expr3(0) 
                self.state = 395
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 404
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 399
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 400
                    _la = self._input.LA(1)
                    if not(_la==25 or _la==26):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 401
                    self.expr4(0) 
                self.state = 406
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 415
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 410
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 411
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 412
                    self.expr5() 
                self.state = 417
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 421
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                _la = self._input.LA(1)
                if not(_la==26 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 419
                self.expr5()
                pass
            elif token in [3, 4, 47, 55, 60, 61, 62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.expr6(0)
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def index_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Index_opsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 434
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 426
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 430
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [46]:
                        self.state = 427
                        self.match(MiniGoParser.DOT)
                        self.state = 428
                        self.match(MiniGoParser.IDENTIFIER)
                        pass
                    elif token in [51]:
                        self.state = 429
                        self.index_ops()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 436
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr7)
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.match(MiniGoParser.LB)
                self.state = 438
                self.expr_list()
                self.state = 439
                self.match(MiniGoParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_list




    def expr_list(self):

        localctx = MiniGoParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr_list)
        try:
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.expr(0)
                self.state = 445
                self.match(MiniGoParser.COMMA)
                self.state = 446
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralsContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def call_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Call_exprContext,0)


        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_operand




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_operand)
        try:
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 453
                self.call_expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 454
                self.match(MiniGoParser.LB)
                self.state = 455
                self.expr(0)
                self.state = 456
                self.match(MiniGoParser.RB)
                pass


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
        self.enterRule(localctx, 86, self.RULE_stmt)
        try:
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 462
                self.call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 463
                self.asm_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 464
                self.if_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 465
                self.for_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 466
                self.break_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 467
                self.continue_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 468
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
        self.enterRule(localctx, 88, self.RULE_asm_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 475
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 472
                self.index_ops()
                self.state = 477
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 478
            self.assign_ops()
            self.state = 479
            self.expr(0)
            self.state = 480
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
        self.enterRule(localctx, 90, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(MiniGoParser.IF)
            self.state = 483
            self.match(MiniGoParser.LB)
            self.state = 484
            self.expr(0)
            self.state = 485
            self.match(MiniGoParser.RB)
            self.state = 486
            self.match(MiniGoParser.LCB)
            self.state = 490
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018429355936) != 0):
                self.state = 487
                self.stmt()
                self.state = 492
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 493
            self.match(MiniGoParser.RCB)
            self.state = 497
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 494
                    self.else_if_stmt() 
                self.state = 499
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

            self.state = 509
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 500
                self.match(MiniGoParser.ELSE)
                self.state = 501
                self.match(MiniGoParser.LCB)
                self.state = 505
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018429355936) != 0):
                    self.state = 502
                    self.stmt()
                    self.state = 507
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 508
                self.match(MiniGoParser.RCB)


            self.state = 511
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
        self.enterRule(localctx, 92, self.RULE_else_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(MiniGoParser.ELSE)
            self.state = 514
            self.match(MiniGoParser.IF)
            self.state = 515
            self.match(MiniGoParser.LB)
            self.state = 516
            self.expr(0)
            self.state = 517
            self.match(MiniGoParser.RB)
            self.state = 518
            self.match(MiniGoParser.LCB)
            self.state = 522
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018429355936) != 0):
                self.state = 519
                self.stmt()
                self.state = 524
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 525
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
        self.enterRule(localctx, 94, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(MiniGoParser.FOR)
            self.state = 528
            self.for_clause()
            self.state = 529
            self.match(MiniGoParser.LCB)
            self.state = 533
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018429355936) != 0):
                self.state = 530
                self.stmt()
                self.state = 535
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 536
            self.match(MiniGoParser.RCB)
            self.state = 537
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
        self.enterRule(localctx, 96, self.RULE_for_clause)
        try:
            self.state = 542
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 539
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 540
                self.fully_clause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 541
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
        self.enterRule(localctx, 98, self.RULE_fully_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 544
                self.init()


            self.state = 547
            self.eos()
            self.state = 549
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8106620341700263960) != 0):
                self.state = 548
                self.expr(0)


            self.state = 551
            self.eos()
            self.state = 553
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 552
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
        self.enterRule(localctx, 100, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 556
            _la = self._input.LA(1)
            if not(_la==39 or _la==40):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 557
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
        self.enterRule(localctx, 102, self.RULE_update)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 563
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 560
                self.index_ops()
                self.state = 565
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 566
            self.assign_ops()
            self.state = 567
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
        self.enterRule(localctx, 104, self.RULE_range_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            _la = self._input.LA(1)
            if not(_la==2 or _la==62):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 570
            self.match(MiniGoParser.COMMA)
            self.state = 571
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 572
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 573
            self.match(MiniGoParser.RANGE)
            self.state = 574
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
        self.enterRule(localctx, 106, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.match(MiniGoParser.BREAK)
            self.state = 577
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
        self.enterRule(localctx, 108, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            self.match(MiniGoParser.CONTINUE)
            self.state = 580
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
        self.enterRule(localctx, 110, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 582
            self.match(MiniGoParser.RETURN)
            self.state = 584
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8106620341700263960) != 0):
                self.state = 583
                self.expr(0)


            self.state = 586
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
        self.enterRule(localctx, 112, self.RULE_boolean_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 481036337152) != 0)):
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
        self.enterRule(localctx, 114, self.RULE_arithmetic_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1040187392) != 0)):
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
        self.enterRule(localctx, 116, self.RULE_relational_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67645734912) != 0)):
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
        self.enterRule(localctx, 118, self.RULE_assign_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 68169720922112) != 0)):
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
        self.enterRule(localctx, 120, self.RULE_index_ops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self.match(MiniGoParser.LSB)
            self.state = 597
            self.expr(0)
            self.state = 598
            self.match(MiniGoParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_exprContext(ParserRuleContext):
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

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_expr




    def call_expr(self):

        localctx = MiniGoParser.Call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_call_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 600
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 601
                self.match(MiniGoParser.DOT)


            self.state = 604
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 605
            self.match(MiniGoParser.LB)
            self.state = 607
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8106620341700263960) != 0):
                self.state = 606
                self.expr_list()


            self.state = 609
            self.match(MiniGoParser.RB)
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
        self.enterRule(localctx, 124, self.RULE_eos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            _la = self._input.LA(1)
            if not(_la==54 or _la==66):
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
        self._predicates[33] = self.expr_sempred
        self._predicates[34] = self.expr1_sempred
        self._predicates[35] = self.expr2_sempred
        self._predicates[36] = self.expr3_sempred
        self._predicates[37] = self.expr4_sempred
        self._predicates[39] = self.expr6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




