# Generated from c:/Users/Huy/Documents/Tuan_Huy/CO3005_PPL/Assignment_2/initial/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
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
        4,1,69,648,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,71,2,72,
        7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,78,7,78,
        2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,3,1,174,8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,182,8,2,1,3,1,3,1,3,
        3,3,187,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,3,8,215,8,8,
        1,9,1,9,1,9,1,9,3,9,221,8,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,
        12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,3,13,239,8,13,1,14,1,
        14,1,14,1,14,3,14,245,8,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,
        16,1,16,1,16,1,17,1,17,1,17,1,17,3,17,261,8,17,1,18,1,18,1,18,1,
        19,1,19,1,19,1,19,3,19,270,8,19,1,20,1,20,1,20,3,20,275,8,20,1,20,
        1,20,1,21,1,21,1,21,1,21,1,21,3,21,284,8,21,1,22,1,22,1,22,1,22,
        1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,
        1,25,3,25,304,8,25,1,26,1,26,1,26,3,26,309,8,26,1,26,1,26,3,26,313,
        8,26,1,26,1,26,1,27,1,27,1,27,1,27,3,27,321,8,27,1,27,1,27,3,27,
        325,8,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,3,28,335,8,28,1,
        29,1,29,1,29,1,30,1,30,1,30,1,30,3,30,344,8,30,1,31,1,31,1,31,1,
        31,1,32,1,32,1,32,1,32,3,32,354,8,32,1,33,1,33,1,33,1,33,1,33,3,
        33,361,8,33,1,33,1,33,3,33,365,8,33,1,33,1,33,1,33,1,34,1,34,1,34,
        1,34,1,34,1,35,1,35,1,35,3,35,378,8,35,1,36,1,36,1,37,1,37,1,37,
        3,37,385,8,37,1,38,1,38,1,39,1,39,1,39,3,39,392,8,39,1,39,1,39,1,
        40,1,40,1,40,1,40,1,40,1,40,5,40,402,8,40,10,40,12,40,405,9,40,1,
        41,1,41,1,41,1,41,1,41,1,41,5,41,413,8,41,10,41,12,41,416,9,41,1,
        42,1,42,1,42,1,42,1,42,1,42,1,42,5,42,425,8,42,10,42,12,42,428,9,
        42,1,43,1,43,1,43,1,43,1,43,1,43,5,43,436,8,43,10,43,12,43,439,9,
        43,1,44,1,44,1,44,1,44,1,44,1,44,5,44,447,8,44,10,44,12,44,450,9,
        44,1,45,1,45,1,45,3,45,455,8,45,1,46,1,46,1,46,1,46,1,46,1,46,1,
        46,1,46,1,46,1,46,1,46,1,46,1,46,3,46,470,8,46,1,46,5,46,473,8,46,
        10,46,12,46,476,9,46,1,47,1,47,1,47,1,47,1,47,3,47,483,8,47,1,48,
        1,48,1,48,1,48,1,48,1,48,1,48,3,48,492,8,48,1,49,1,49,1,49,1,49,
        1,49,1,49,1,49,1,49,3,49,502,8,49,1,50,1,50,3,50,506,8,50,1,51,1,
        51,1,51,1,52,1,52,1,52,1,52,1,53,1,53,1,53,3,53,518,8,53,1,54,1,
        54,1,54,1,55,1,55,1,55,1,55,3,55,527,8,55,1,56,1,56,1,56,1,56,1,
        57,1,57,1,58,1,58,1,58,1,58,1,58,1,58,3,58,541,8,58,1,58,1,58,1,
        59,1,59,1,59,1,59,1,59,3,59,550,8,59,1,60,1,60,1,60,1,60,1,60,1,
        60,1,60,1,61,1,61,1,61,1,62,1,62,1,62,3,62,565,8,62,1,63,1,63,1,
        63,1,63,1,63,1,64,1,64,1,64,1,64,1,64,1,65,1,65,1,65,1,65,1,65,1,
        66,1,66,1,66,1,66,1,66,1,66,1,67,1,67,1,67,3,67,591,8,67,1,68,1,
        68,1,68,1,68,1,68,1,68,1,69,1,69,1,70,1,70,1,70,1,70,1,71,1,71,1,
        71,1,71,1,71,1,71,1,71,1,72,1,72,1,72,1,73,1,73,1,73,1,74,1,74,3,
        74,620,8,74,1,74,1,74,1,75,1,75,1,75,1,75,1,76,1,76,3,76,630,8,76,
        1,76,1,76,1,77,1,77,1,78,1,78,1,79,1,79,1,80,1,80,1,81,1,81,1,81,
        1,81,1,82,1,82,1,82,0,6,80,82,84,86,88,92,83,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,
        102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,
        134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,
        0,12,2,0,55,55,62,62,3,0,3,4,55,55,60,61,1,0,13,16,1,0,25,26,1,0,
        27,29,2,0,26,26,38,38,2,0,2,2,62,62,1,0,36,38,1,0,25,29,1,0,30,35,
        1,0,40,45,2,0,54,54,66,66,632,0,166,1,0,0,0,2,173,1,0,0,0,4,181,
        1,0,0,0,6,186,1,0,0,0,8,190,1,0,0,0,10,196,1,0,0,0,12,201,1,0,0,
        0,14,205,1,0,0,0,16,211,1,0,0,0,18,220,1,0,0,0,20,222,1,0,0,0,22,
        226,1,0,0,0,24,229,1,0,0,0,26,238,1,0,0,0,28,244,1,0,0,0,30,246,
        1,0,0,0,32,251,1,0,0,0,34,260,1,0,0,0,36,262,1,0,0,0,38,265,1,0,
        0,0,40,271,1,0,0,0,42,283,1,0,0,0,44,285,1,0,0,0,46,289,1,0,0,0,
        48,294,1,0,0,0,50,303,1,0,0,0,52,305,1,0,0,0,54,316,1,0,0,0,56,334,
        1,0,0,0,58,336,1,0,0,0,60,343,1,0,0,0,62,345,1,0,0,0,64,353,1,0,
        0,0,66,355,1,0,0,0,68,369,1,0,0,0,70,377,1,0,0,0,72,379,1,0,0,0,
        74,384,1,0,0,0,76,386,1,0,0,0,78,388,1,0,0,0,80,395,1,0,0,0,82,406,
        1,0,0,0,84,417,1,0,0,0,86,429,1,0,0,0,88,440,1,0,0,0,90,454,1,0,
        0,0,92,456,1,0,0,0,94,482,1,0,0,0,96,491,1,0,0,0,98,501,1,0,0,0,
        100,505,1,0,0,0,102,507,1,0,0,0,104,510,1,0,0,0,106,517,1,0,0,0,
        108,519,1,0,0,0,110,526,1,0,0,0,112,528,1,0,0,0,114,532,1,0,0,0,
        116,534,1,0,0,0,118,549,1,0,0,0,120,551,1,0,0,0,122,558,1,0,0,0,
        124,564,1,0,0,0,126,566,1,0,0,0,128,571,1,0,0,0,130,576,1,0,0,0,
        132,581,1,0,0,0,134,590,1,0,0,0,136,592,1,0,0,0,138,598,1,0,0,0,
        140,600,1,0,0,0,142,604,1,0,0,0,144,611,1,0,0,0,146,614,1,0,0,0,
        148,619,1,0,0,0,150,623,1,0,0,0,152,627,1,0,0,0,154,633,1,0,0,0,
        156,635,1,0,0,0,158,637,1,0,0,0,160,639,1,0,0,0,162,641,1,0,0,0,
        164,645,1,0,0,0,166,167,3,2,1,0,167,168,5,0,0,1,168,1,1,0,0,0,169,
        170,3,4,2,0,170,171,3,2,1,0,171,174,1,0,0,0,172,174,3,4,2,0,173,
        169,1,0,0,0,173,172,1,0,0,0,174,3,1,0,0,0,175,182,3,6,3,0,176,182,
        3,14,7,0,177,182,3,30,15,0,178,182,3,46,23,0,179,182,3,54,27,0,180,
        182,3,66,33,0,181,175,1,0,0,0,181,176,1,0,0,0,181,177,1,0,0,0,181,
        178,1,0,0,0,181,179,1,0,0,0,181,180,1,0,0,0,182,5,1,0,0,0,183,187,
        3,8,4,0,184,187,3,10,5,0,185,187,3,12,6,0,186,183,1,0,0,0,186,184,
        1,0,0,0,186,185,1,0,0,0,187,188,1,0,0,0,188,189,3,164,82,0,189,7,
        1,0,0,0,190,191,5,18,0,0,191,192,5,62,0,0,192,193,3,70,35,0,193,
        194,5,39,0,0,194,195,3,80,40,0,195,9,1,0,0,0,196,197,5,18,0,0,197,
        198,5,62,0,0,198,199,5,39,0,0,199,200,3,80,40,0,200,11,1,0,0,0,201,
        202,5,18,0,0,202,203,5,62,0,0,203,204,3,70,35,0,204,13,1,0,0,0,205,
        206,5,17,0,0,206,207,5,62,0,0,207,208,5,39,0,0,208,209,3,80,40,0,
        209,210,3,164,82,0,210,15,1,0,0,0,211,214,3,18,9,0,212,215,3,76,
        38,0,213,215,5,62,0,0,214,212,1,0,0,0,214,213,1,0,0,0,215,17,1,0,
        0,0,216,217,3,20,10,0,217,218,3,18,9,0,218,221,1,0,0,0,219,221,3,
        20,10,0,220,216,1,0,0,0,220,219,1,0,0,0,221,19,1,0,0,0,222,223,5,
        51,0,0,223,224,7,0,0,0,224,225,5,52,0,0,225,21,1,0,0,0,226,227,3,
        16,8,0,227,228,3,24,12,0,228,23,1,0,0,0,229,230,5,49,0,0,230,231,
        3,26,13,0,231,232,5,50,0,0,232,25,1,0,0,0,233,234,3,28,14,0,234,
        235,5,53,0,0,235,236,3,26,13,0,236,239,1,0,0,0,237,239,3,28,14,0,
        238,233,1,0,0,0,238,237,1,0,0,0,239,27,1,0,0,0,240,245,3,24,12,0,
        241,245,3,72,36,0,242,245,3,40,20,0,243,245,5,62,0,0,244,240,1,0,
        0,0,244,241,1,0,0,0,244,242,1,0,0,0,244,243,1,0,0,0,245,29,1,0,0,
        0,246,247,5,10,0,0,247,248,5,62,0,0,248,249,3,32,16,0,249,250,3,
        164,82,0,250,31,1,0,0,0,251,252,5,11,0,0,252,253,5,49,0,0,253,254,
        3,34,17,0,254,255,5,50,0,0,255,33,1,0,0,0,256,257,3,36,18,0,257,
        258,3,34,17,0,258,261,1,0,0,0,259,261,3,36,18,0,260,256,1,0,0,0,
        260,259,1,0,0,0,261,35,1,0,0,0,262,263,3,38,19,0,263,264,3,164,82,
        0,264,37,1,0,0,0,265,269,5,62,0,0,266,270,3,76,38,0,267,270,3,16,
        8,0,268,270,5,62,0,0,269,266,1,0,0,0,269,267,1,0,0,0,269,268,1,0,
        0,0,270,39,1,0,0,0,271,272,5,62,0,0,272,274,5,49,0,0,273,275,3,42,
        21,0,274,273,1,0,0,0,274,275,1,0,0,0,275,276,1,0,0,0,276,277,5,50,
        0,0,277,41,1,0,0,0,278,279,3,44,22,0,279,280,5,53,0,0,280,281,3,
        42,21,0,281,284,1,0,0,0,282,284,3,44,22,0,283,278,1,0,0,0,283,282,
        1,0,0,0,284,43,1,0,0,0,285,286,5,62,0,0,286,287,5,1,0,0,287,288,
        3,80,40,0,288,45,1,0,0,0,289,290,5,10,0,0,290,291,5,62,0,0,291,292,
        3,48,24,0,292,293,3,164,82,0,293,47,1,0,0,0,294,295,5,12,0,0,295,
        296,5,49,0,0,296,297,3,50,25,0,297,298,5,50,0,0,298,49,1,0,0,0,299,
        300,3,52,26,0,300,301,3,50,25,0,301,304,1,0,0,0,302,304,3,52,26,
        0,303,299,1,0,0,0,303,302,1,0,0,0,304,51,1,0,0,0,305,306,5,62,0,
        0,306,308,5,47,0,0,307,309,3,56,28,0,308,307,1,0,0,0,308,309,1,0,
        0,0,309,310,1,0,0,0,310,312,5,48,0,0,311,313,3,70,35,0,312,311,1,
        0,0,0,312,313,1,0,0,0,313,314,1,0,0,0,314,315,3,164,82,0,315,53,
        1,0,0,0,316,317,5,9,0,0,317,318,5,62,0,0,318,320,5,47,0,0,319,321,
        3,56,28,0,320,319,1,0,0,0,320,321,1,0,0,0,321,322,1,0,0,0,322,324,
        5,48,0,0,323,325,3,70,35,0,324,323,1,0,0,0,324,325,1,0,0,0,325,326,
        1,0,0,0,326,327,3,62,31,0,327,328,3,164,82,0,328,55,1,0,0,0,329,
        330,3,58,29,0,330,331,5,53,0,0,331,332,3,56,28,0,332,335,1,0,0,0,
        333,335,3,58,29,0,334,329,1,0,0,0,334,333,1,0,0,0,335,57,1,0,0,0,
        336,337,3,60,30,0,337,338,3,70,35,0,338,59,1,0,0,0,339,340,5,62,
        0,0,340,341,5,53,0,0,341,344,3,60,30,0,342,344,5,62,0,0,343,339,
        1,0,0,0,343,342,1,0,0,0,344,61,1,0,0,0,345,346,5,49,0,0,346,347,
        3,64,32,0,347,348,5,50,0,0,348,63,1,0,0,0,349,350,3,98,49,0,350,
        351,3,64,32,0,351,354,1,0,0,0,352,354,3,98,49,0,353,349,1,0,0,0,
        353,352,1,0,0,0,354,65,1,0,0,0,355,356,5,9,0,0,356,357,3,68,34,0,
        357,358,5,62,0,0,358,360,5,47,0,0,359,361,3,56,28,0,360,359,1,0,
        0,0,360,361,1,0,0,0,361,362,1,0,0,0,362,364,5,48,0,0,363,365,3,70,
        35,0,364,363,1,0,0,0,364,365,1,0,0,0,365,366,1,0,0,0,366,367,3,62,
        31,0,367,368,3,164,82,0,368,67,1,0,0,0,369,370,5,47,0,0,370,371,
        5,62,0,0,371,372,5,62,0,0,372,373,5,48,0,0,373,69,1,0,0,0,374,378,
        3,76,38,0,375,378,3,16,8,0,376,378,5,62,0,0,377,374,1,0,0,0,377,
        375,1,0,0,0,377,376,1,0,0,0,378,71,1,0,0,0,379,380,7,1,0,0,380,73,
        1,0,0,0,381,385,3,72,36,0,382,385,3,22,11,0,383,385,3,40,20,0,384,
        381,1,0,0,0,384,382,1,0,0,0,384,383,1,0,0,0,385,75,1,0,0,0,386,387,
        7,2,0,0,387,77,1,0,0,0,388,389,5,62,0,0,389,391,5,47,0,0,390,392,
        3,94,47,0,391,390,1,0,0,0,391,392,1,0,0,0,392,393,1,0,0,0,393,394,
        5,48,0,0,394,79,1,0,0,0,395,396,6,40,-1,0,396,397,3,82,41,0,397,
        403,1,0,0,0,398,399,10,2,0,0,399,400,5,37,0,0,400,402,3,82,41,0,
        401,398,1,0,0,0,402,405,1,0,0,0,403,401,1,0,0,0,403,404,1,0,0,0,
        404,81,1,0,0,0,405,403,1,0,0,0,406,407,6,41,-1,0,407,408,3,84,42,
        0,408,414,1,0,0,0,409,410,10,2,0,0,410,411,5,36,0,0,411,413,3,84,
        42,0,412,409,1,0,0,0,413,416,1,0,0,0,414,412,1,0,0,0,414,415,1,0,
        0,0,415,83,1,0,0,0,416,414,1,0,0,0,417,418,6,42,-1,0,418,419,3,86,
        43,0,419,426,1,0,0,0,420,421,10,2,0,0,421,422,3,158,79,0,422,423,
        3,86,43,0,423,425,1,0,0,0,424,420,1,0,0,0,425,428,1,0,0,0,426,424,
        1,0,0,0,426,427,1,0,0,0,427,85,1,0,0,0,428,426,1,0,0,0,429,430,6,
        43,-1,0,430,431,3,88,44,0,431,437,1,0,0,0,432,433,10,2,0,0,433,434,
        7,3,0,0,434,436,3,88,44,0,435,432,1,0,0,0,436,439,1,0,0,0,437,435,
        1,0,0,0,437,438,1,0,0,0,438,87,1,0,0,0,439,437,1,0,0,0,440,441,6,
        44,-1,0,441,442,3,90,45,0,442,448,1,0,0,0,443,444,10,2,0,0,444,445,
        7,4,0,0,445,447,3,90,45,0,446,443,1,0,0,0,447,450,1,0,0,0,448,446,
        1,0,0,0,448,449,1,0,0,0,449,89,1,0,0,0,450,448,1,0,0,0,451,452,7,
        5,0,0,452,455,3,90,45,0,453,455,3,92,46,0,454,451,1,0,0,0,454,453,
        1,0,0,0,455,91,1,0,0,0,456,457,6,46,-1,0,457,458,3,96,48,0,458,474,
        1,0,0,0,459,460,10,4,0,0,460,473,3,110,55,0,461,462,10,3,0,0,462,
        463,5,46,0,0,463,473,5,62,0,0,464,465,10,2,0,0,465,466,5,46,0,0,
        466,467,5,62,0,0,467,469,5,47,0,0,468,470,3,94,47,0,469,468,1,0,
        0,0,469,470,1,0,0,0,470,471,1,0,0,0,471,473,5,48,0,0,472,459,1,0,
        0,0,472,461,1,0,0,0,472,464,1,0,0,0,473,476,1,0,0,0,474,472,1,0,
        0,0,474,475,1,0,0,0,475,93,1,0,0,0,476,474,1,0,0,0,477,478,3,80,
        40,0,478,479,5,53,0,0,479,480,3,94,47,0,480,483,1,0,0,0,481,483,
        3,80,40,0,482,477,1,0,0,0,482,481,1,0,0,0,483,95,1,0,0,0,484,492,
        3,74,37,0,485,492,5,62,0,0,486,492,3,78,39,0,487,488,5,47,0,0,488,
        489,3,80,40,0,489,490,5,48,0,0,490,492,1,0,0,0,491,484,1,0,0,0,491,
        485,1,0,0,0,491,486,1,0,0,0,491,487,1,0,0,0,492,97,1,0,0,0,493,502,
        3,100,50,0,494,502,3,102,51,0,495,502,3,116,58,0,496,502,3,124,62,
        0,497,502,3,144,72,0,498,502,3,146,73,0,499,502,3,148,74,0,500,502,
        3,152,76,0,501,493,1,0,0,0,501,494,1,0,0,0,501,495,1,0,0,0,501,496,
        1,0,0,0,501,497,1,0,0,0,501,498,1,0,0,0,501,499,1,0,0,0,501,500,
        1,0,0,0,502,99,1,0,0,0,503,506,3,6,3,0,504,506,3,14,7,0,505,503,
        1,0,0,0,505,504,1,0,0,0,506,101,1,0,0,0,507,508,3,104,52,0,508,509,
        3,164,82,0,509,103,1,0,0,0,510,511,3,106,53,0,511,512,3,160,80,0,
        512,513,3,114,57,0,513,105,1,0,0,0,514,518,5,62,0,0,515,518,3,108,
        54,0,516,518,3,112,56,0,517,514,1,0,0,0,517,515,1,0,0,0,517,516,
        1,0,0,0,518,107,1,0,0,0,519,520,3,80,40,0,520,521,3,110,55,0,521,
        109,1,0,0,0,522,523,3,162,81,0,523,524,3,110,55,0,524,527,1,0,0,
        0,525,527,3,162,81,0,526,522,1,0,0,0,526,525,1,0,0,0,527,111,1,0,
        0,0,528,529,3,80,40,0,529,530,5,46,0,0,530,531,5,62,0,0,531,113,
        1,0,0,0,532,533,3,80,40,0,533,115,1,0,0,0,534,535,5,5,0,0,535,536,
        5,47,0,0,536,537,3,80,40,0,537,538,5,48,0,0,538,540,3,62,31,0,539,
        541,3,118,59,0,540,539,1,0,0,0,540,541,1,0,0,0,541,542,1,0,0,0,542,
        543,3,164,82,0,543,117,1,0,0,0,544,545,3,120,60,0,545,546,3,118,
        59,0,546,550,1,0,0,0,547,550,3,120,60,0,548,550,3,122,61,0,549,544,
        1,0,0,0,549,547,1,0,0,0,549,548,1,0,0,0,550,119,1,0,0,0,551,552,
        5,6,0,0,552,553,5,5,0,0,553,554,5,47,0,0,554,555,3,80,40,0,555,556,
        5,48,0,0,556,557,3,62,31,0,557,121,1,0,0,0,558,559,5,6,0,0,559,560,
        3,62,31,0,560,123,1,0,0,0,561,565,3,126,63,0,562,565,3,128,64,0,
        563,565,3,130,65,0,564,561,1,0,0,0,564,562,1,0,0,0,564,563,1,0,0,
        0,565,125,1,0,0,0,566,567,5,7,0,0,567,568,3,80,40,0,568,569,3,62,
        31,0,569,570,3,164,82,0,570,127,1,0,0,0,571,572,5,7,0,0,572,573,
        3,132,66,0,573,574,3,62,31,0,574,575,3,164,82,0,575,129,1,0,0,0,
        576,577,5,7,0,0,577,578,3,142,71,0,578,579,3,62,31,0,579,580,3,164,
        82,0,580,131,1,0,0,0,581,582,3,134,67,0,582,583,3,164,82,0,583,584,
        3,80,40,0,584,585,3,164,82,0,585,586,3,138,69,0,586,133,1,0,0,0,
        587,591,3,140,70,0,588,591,3,10,5,0,589,591,3,136,68,0,590,587,1,
        0,0,0,590,588,1,0,0,0,590,589,1,0,0,0,591,135,1,0,0,0,592,593,5,
        18,0,0,593,594,5,62,0,0,594,595,3,76,38,0,595,596,5,39,0,0,596,597,
        3,80,40,0,597,137,1,0,0,0,598,599,3,140,70,0,599,139,1,0,0,0,600,
        601,5,62,0,0,601,602,3,160,80,0,602,603,3,114,57,0,603,141,1,0,0,
        0,604,605,7,6,0,0,605,606,5,53,0,0,606,607,5,62,0,0,607,608,5,40,
        0,0,608,609,5,21,0,0,609,610,3,80,40,0,610,143,1,0,0,0,611,612,5,
        20,0,0,612,613,3,164,82,0,613,145,1,0,0,0,614,615,5,19,0,0,615,616,
        3,164,82,0,616,147,1,0,0,0,617,620,3,78,39,0,618,620,3,150,75,0,
        619,617,1,0,0,0,619,618,1,0,0,0,620,621,1,0,0,0,621,622,3,164,82,
        0,622,149,1,0,0,0,623,624,3,80,40,0,624,625,5,46,0,0,625,626,3,78,
        39,0,626,151,1,0,0,0,627,629,5,8,0,0,628,630,3,80,40,0,629,628,1,
        0,0,0,629,630,1,0,0,0,630,631,1,0,0,0,631,632,3,164,82,0,632,153,
        1,0,0,0,633,634,7,7,0,0,634,155,1,0,0,0,635,636,7,8,0,0,636,157,
        1,0,0,0,637,638,7,9,0,0,638,159,1,0,0,0,639,640,7,10,0,0,640,161,
        1,0,0,0,641,642,5,51,0,0,642,643,3,80,40,0,643,644,5,52,0,0,644,
        163,1,0,0,0,645,646,7,11,0,0,646,165,1,0,0,0,45,173,181,186,214,
        220,238,244,260,269,274,283,303,308,312,320,324,334,343,353,360,
        364,377,384,391,403,414,426,437,448,454,469,472,474,482,491,501,
        505,517,526,540,549,564,590,619,629
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
                      "OR", "NOT", "DECLARE_ASSIGN", "ASSIGN", "PLUS_ASSIGN", 
                      "MINUS_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "DOT", "LB", "RB", "LCB", "RCB", "LSB", "RSB", "COMMA", 
                      "SEMICOLON", "INT_LITERAL", "DECIMAL_LITERAL", "BINARY_LITERAL", 
                      "OCTAL_LITERAL", "HEX_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
                      "IDENTIFIER", "LINE_COMMENT", "COMMENT", "WS", "NL", 
                      "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_many_decl = 1
    RULE_decl = 2
    RULE_var_decl = 3
    RULE_decl_var_type_init = 4
    RULE_decl_var_init = 5
    RULE_decl_var_type = 6
    RULE_const_decl = 7
    RULE_array_type = 8
    RULE_dimensions = 9
    RULE_dim = 10
    RULE_array_literal = 11
    RULE_ele_list = 12
    RULE_many_ele = 13
    RULE_ele = 14
    RULE_struct_decl = 15
    RULE_struct_type = 16
    RULE_many_fields = 17
    RULE_fields = 18
    RULE_ele_field = 19
    RULE_struct_literal = 20
    RULE_struct_elements = 21
    RULE_struct_ele = 22
    RULE_interface_decl = 23
    RULE_interface_type = 24
    RULE_many_interface_field = 25
    RULE_interface_field = 26
    RULE_func_decl = 27
    RULE_param_list = 28
    RULE_param = 29
    RULE_id_list = 30
    RULE_block = 31
    RULE_many_stmt = 32
    RULE_method_decl = 33
    RULE_method = 34
    RULE_types = 35
    RULE_primitive_lit = 36
    RULE_literals = 37
    RULE_primitive_type = 38
    RULE_func_call = 39
    RULE_expr = 40
    RULE_expr1 = 41
    RULE_expr2 = 42
    RULE_expr3 = 43
    RULE_expr4 = 44
    RULE_expr5 = 45
    RULE_primary_expr = 46
    RULE_expr_list = 47
    RULE_operand = 48
    RULE_stmt = 49
    RULE_decl_stmt = 50
    RULE_asm_stmt = 51
    RULE_asm = 52
    RULE_lhs = 53
    RULE_array_elem = 54
    RULE_many_index_ops = 55
    RULE_struct_elem = 56
    RULE_rhs = 57
    RULE_if_stmt = 58
    RULE_if_tail = 59
    RULE_else_if_stmt = 60
    RULE_else_stmt = 61
    RULE_for_stmt = 62
    RULE_for_basic = 63
    RULE_for_step = 64
    RULE_for_each = 65
    RULE_fully_clause = 66
    RULE_init = 67
    RULE_decl_var_type_init_for = 68
    RULE_update = 69
    RULE_asm_for = 70
    RULE_range_clause = 71
    RULE_break_stmt = 72
    RULE_continue_stmt = 73
    RULE_call_stmt = 74
    RULE_method_call = 75
    RULE_return_stmt = 76
    RULE_boolean_ops = 77
    RULE_arithmetic_ops = 78
    RULE_relational_ops = 79
    RULE_assign_ops = 80
    RULE_index_ops = 81
    RULE_eos = 82

    ruleNames =  [ "program", "many_decl", "decl", "var_decl", "decl_var_type_init", 
                   "decl_var_init", "decl_var_type", "const_decl", "array_type", 
                   "dimensions", "dim", "array_literal", "ele_list", "many_ele", 
                   "ele", "struct_decl", "struct_type", "many_fields", "fields", 
                   "ele_field", "struct_literal", "struct_elements", "struct_ele", 
                   "interface_decl", "interface_type", "many_interface_field", 
                   "interface_field", "func_decl", "param_list", "param", 
                   "id_list", "block", "many_stmt", "method_decl", "method", 
                   "types", "primitive_lit", "literals", "primitive_type", 
                   "func_call", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "primary_expr", "expr_list", "operand", "stmt", 
                   "decl_stmt", "asm_stmt", "asm", "lhs", "array_elem", 
                   "many_index_ops", "struct_elem", "rhs", "if_stmt", "if_tail", 
                   "else_if_stmt", "else_stmt", "for_stmt", "for_basic", 
                   "for_step", "for_each", "fully_clause", "init", "decl_var_type_init_for", 
                   "update", "asm_for", "range_clause", "break_stmt", "continue_stmt", 
                   "call_stmt", "method_call", "return_stmt", "boolean_ops", 
                   "arithmetic_ops", "relational_ops", "assign_ops", "index_ops", 
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
    DECLARE_ASSIGN=39
    ASSIGN=40
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
    NL=66
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

        def many_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Many_declContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.many_decl()
            self.state = 167
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def many_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Many_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_many_decl




    def many_decl(self):

        localctx = MiniGoParser.Many_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_many_decl)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.decl()
                self.state = 170
                self.many_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.decl()
                pass


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

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
                self.struct_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 178
                self.interface_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 179
                self.func_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 180
                self.method_decl()
                pass


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

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def decl_var_type_init(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_var_type_initContext,0)


        def decl_var_init(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_var_initContext,0)


        def decl_var_type(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_var_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 183
                self.decl_var_type_init()
                pass

            elif la_ == 2:
                self.state = 184
                self.decl_var_init()
                pass

            elif la_ == 3:
                self.state = 185
                self.decl_var_type()
                pass


            self.state = 188
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_var_type_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_var_type_init




    def decl_var_type_init(self):

        localctx = MiniGoParser.Decl_var_type_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_decl_var_type_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(MiniGoParser.VAR)
            self.state = 191
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 192
            self.types()
            self.state = 193
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 194
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_var_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_var_init




    def decl_var_init(self):

        localctx = MiniGoParser.Decl_var_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_decl_var_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(MiniGoParser.VAR)
            self.state = 197
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 198
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 199
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_var_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_var_type




    def decl_var_type(self):

        localctx = MiniGoParser.Decl_var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_decl_var_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(MiniGoParser.VAR)
            self.state = 202
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 203
            self.types()
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

        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(MiniGoParser.CONST)
            self.state = 206
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 207
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 208
            self.expr(0)
            self.state = 209
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
        self.enterRule(localctx, 16, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.dimensions()
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.state = 212
                self.primitive_type()
                pass
            elif token in [62]:
                self.state = 213
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

        def dim(self):
            return self.getTypedRuleContext(MiniGoParser.DimContext,0)


        def dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dimensions




    def dimensions(self):

        localctx = MiniGoParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dimensions)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.dim()
                self.state = 217
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.dim()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def INT_LITERAL(self):
            return self.getToken(MiniGoParser.INT_LITERAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dim




    def dim(self):

        localctx = MiniGoParser.DimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_dim)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(MiniGoParser.LSB)
            self.state = 223
            _la = self._input.LA(1)
            if not(_la==55 or _la==62):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 224
            self.match(MiniGoParser.RSB)
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
        self.enterRule(localctx, 22, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.array_type()
            self.state = 227
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

        def many_ele(self):
            return self.getTypedRuleContext(MiniGoParser.Many_eleContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ele_list




    def ele_list(self):

        localctx = MiniGoParser.Ele_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ele_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(MiniGoParser.LCB)
            self.state = 230
            self.many_ele()
            self.state = 231
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ele(self):
            return self.getTypedRuleContext(MiniGoParser.EleContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def many_ele(self):
            return self.getTypedRuleContext(MiniGoParser.Many_eleContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_many_ele




    def many_ele(self):

        localctx = MiniGoParser.Many_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_many_ele)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.ele()
                self.state = 234
                self.match(MiniGoParser.COMMA)
                self.state = 235
                self.many_ele()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.ele()
                pass


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


        def primitive_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_litContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ele




    def ele(self):

        localctx = MiniGoParser.EleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ele)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.ele_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.primitive_lit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.struct_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 243
                self.match(MiniGoParser.IDENTIFIER)
                pass


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
        self.enterRule(localctx, 30, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(MiniGoParser.TYPE)
            self.state = 247
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 248
            self.struct_type()
            self.state = 249
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

        def many_fields(self):
            return self.getTypedRuleContext(MiniGoParser.Many_fieldsContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type




    def struct_type(self):

        localctx = MiniGoParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_struct_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(MiniGoParser.STRUCT)
            self.state = 252
            self.match(MiniGoParser.LCB)
            self.state = 253
            self.many_fields()
            self.state = 254
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_fieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fields(self):
            return self.getTypedRuleContext(MiniGoParser.FieldsContext,0)


        def many_fields(self):
            return self.getTypedRuleContext(MiniGoParser.Many_fieldsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_many_fields




    def many_fields(self):

        localctx = MiniGoParser.Many_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_many_fields)
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.fields()
                self.state = 257
                self.many_fields()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.fields()
                pass


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

        def ele_field(self):
            return self.getTypedRuleContext(MiniGoParser.Ele_fieldContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fields




    def fields(self):

        localctx = MiniGoParser.FieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.ele_field()
            self.state = 263
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ele_fieldContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_ele_field




    def ele_field(self):

        localctx = MiniGoParser.Ele_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ele_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.state = 266
                self.primitive_type()
                pass
            elif token in [51]:
                self.state = 267
                self.array_type()
                pass
            elif token in [62]:
                self.state = 268
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

        def struct_elements(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elementsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 272
            self.match(MiniGoParser.LCB)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 273
                self.struct_elements()


            self.state = 276
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_ele(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_eleContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def struct_elements(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elementsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_elements




    def struct_elements(self):

        localctx = MiniGoParser.Struct_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_struct_elements)
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.struct_ele()
                self.state = 279
                self.match(MiniGoParser.COMMA)
                self.state = 280
                self.struct_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.struct_ele()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_ele




    def struct_ele(self):

        localctx = MiniGoParser.Struct_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_struct_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 286
            self.match(MiniGoParser.T__0)
            self.state = 287
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
        self.enterRule(localctx, 46, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(MiniGoParser.TYPE)
            self.state = 290
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 291
            self.interface_type()
            self.state = 292
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

        def many_interface_field(self):
            return self.getTypedRuleContext(MiniGoParser.Many_interface_fieldContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type




    def interface_type(self):

        localctx = MiniGoParser.Interface_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_interface_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(MiniGoParser.INTERFACE)
            self.state = 295
            self.match(MiniGoParser.LCB)
            self.state = 296
            self.many_interface_field()
            self.state = 297
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_interface_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_field(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_fieldContext,0)


        def many_interface_field(self):
            return self.getTypedRuleContext(MiniGoParser.Many_interface_fieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_many_interface_field




    def many_interface_field(self):

        localctx = MiniGoParser.Many_interface_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_many_interface_field)
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.interface_field()
                self.state = 300
                self.many_interface_field()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.interface_field()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_fieldContext(ParserRuleContext):
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
            return MiniGoParser.RULE_interface_field




    def interface_field(self):

        localctx = MiniGoParser.Interface_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_interface_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 306
            self.match(MiniGoParser.LB)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 307
                self.param_list()


            self.state = 310
            self.match(MiniGoParser.RB)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4613937818241196032) != 0):
                self.state = 311
                self.types()


            self.state = 314
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

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(MiniGoParser.FUNC)
            self.state = 317
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 318
            self.match(MiniGoParser.LB)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 319
                self.param_list()


            self.state = 322
            self.match(MiniGoParser.RB)
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4613937818241196032) != 0):
                self.state = 323
                self.types()


            self.state = 326
            self.block()
            self.state = 327
            self.eos()
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

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_list




    def param_list(self):

        localctx = MiniGoParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_param_list)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.param()
                self.state = 330
                self.match(MiniGoParser.COMMA)
                self.state = 331
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.param()
                pass


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

        def id_list(self):
            return self.getTypedRuleContext(MiniGoParser.Id_listContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.id_list()
            self.state = 337
            self.types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def id_list(self):
            return self.getTypedRuleContext(MiniGoParser.Id_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_id_list




    def id_list(self):

        localctx = MiniGoParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_id_list)
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 340
                self.match(MiniGoParser.COMMA)
                self.state = 341
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.match(MiniGoParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def many_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Many_stmtContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_block




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(MiniGoParser.LCB)
            self.state = 346
            self.many_stmt()
            self.state = 347
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def many_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Many_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_many_stmt




    def many_stmt(self):

        localctx = MiniGoParser.Many_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_many_stmt)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.stmt()
                self.state = 350
                self.many_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.stmt()
                pass


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

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def method(self):
            return self.getTypedRuleContext(MiniGoParser.MethodContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


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
            self.state = 355
            self.match(MiniGoParser.FUNC)
            self.state = 356
            self.method()
            self.state = 357
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 358
            self.match(MiniGoParser.LB)
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 359
                self.param_list()


            self.state = 362
            self.match(MiniGoParser.RB)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4613937818241196032) != 0):
                self.state = 363
                self.types()


            self.state = 366
            self.block()
            self.state = 367
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
        self.enterRule(localctx, 68, self.RULE_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(MiniGoParser.LB)
            self.state = 370
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 371
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 372
            self.match(MiniGoParser.RB)
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
        self.enterRule(localctx, 70, self.RULE_types)
        try:
            self.state = 377
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.primitive_type()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.array_type()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 3)
                self.state = 376
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


    class Primitive_litContext(ParserRuleContext):
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
            return MiniGoParser.RULE_primitive_lit




    def primitive_lit(self):

        localctx = MiniGoParser.Primitive_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_primitive_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
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


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_litContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literals




    def literals(self):

        localctx = MiniGoParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_literals)
        try:
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 55, 60, 61]:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.primitive_lit()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.array_literal()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 3)
                self.state = 383
                self.struct_literal()
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
        self.enterRule(localctx, 76, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
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


    class Func_callContext(ParserRuleContext):
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

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 389
            self.match(MiniGoParser.LB)
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8108872141513949208) != 0):
                self.state = 390
                self.expr_list()


            self.state = 393
            self.match(MiniGoParser.RB)
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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 403
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 398
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 399
                    self.match(MiniGoParser.OR)
                    self.state = 400
                    self.expr1(0) 
                self.state = 405
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 414
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 409
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 410
                    self.match(MiniGoParser.AND)
                    self.state = 411
                    self.expr2(0) 
                self.state = 416
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 426
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 420
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 421
                    self.relational_ops()
                    self.state = 422
                    self.expr3(0) 
                self.state = 428
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 437
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 432
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 433
                    _la = self._input.LA(1)
                    if not(_la==25 or _la==26):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 434
                    self.expr4(0) 
                self.state = 439
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 448
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 443
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 444
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 445
                    self.expr5() 
                self.state = 450
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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

        def primary_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Primary_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 454
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                _la = self._input.LA(1)
                if not(_la==26 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 452
                self.expr5()
                pass
            elif token in [3, 4, 47, 51, 55, 60, 61, 62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.primary_expr(0)
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


    class Primary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def primary_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Primary_exprContext,0)


        def many_index_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Many_index_opsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primary_expr



    def primary_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Primary_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_primary_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 474
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 472
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 459
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 460
                        self.many_index_ops()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 461
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 462
                        self.match(MiniGoParser.DOT)
                        self.state = 463
                        self.match(MiniGoParser.IDENTIFIER)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 464
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 465
                        self.match(MiniGoParser.DOT)
                        self.state = 466
                        self.match(MiniGoParser.IDENTIFIER)
                        self.state = 467
                        self.match(MiniGoParser.LB)
                        self.state = 469
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8108872141513949208) != 0):
                            self.state = 468
                            self.expr_list()


                        self.state = 471
                        self.match(MiniGoParser.RB)
                        pass

             
                self.state = 476
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 94, self.RULE_expr_list)
        try:
            self.state = 482
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.expr(0)
                self.state = 478
                self.match(MiniGoParser.COMMA)
                self.state = 479
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
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

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


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
        self.enterRule(localctx, 96, self.RULE_operand)
        try:
            self.state = 491
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 484
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 486
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 487
                self.match(MiniGoParser.LB)
                self.state = 488
                self.expr(0)
                self.state = 489
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

        def decl_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_stmtContext,0)


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


        def call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_stmt)
        try:
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.decl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 494
                self.asm_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 495
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 496
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 497
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 498
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 499
                self.call_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 500
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_stmt




    def decl_stmt(self):

        localctx = MiniGoParser.Decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_decl_stmt)
        try:
            self.state = 505
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.var_decl()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 504
                self.const_decl()
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


    class Asm_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asm(self):
            return self.getTypedRuleContext(MiniGoParser.AsmContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_asm_stmt




    def asm_stmt(self):

        localctx = MiniGoParser.Asm_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_asm_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.asm()
            self.state = 508
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assign_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opsContext,0)


        def rhs(self):
            return self.getTypedRuleContext(MiniGoParser.RhsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_asm




    def asm(self):

        localctx = MiniGoParser.AsmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_asm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.lhs()
            self.state = 511
            self.assign_ops()
            self.state = 512
            self.rhs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def array_elem(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elemContext,0)


        def struct_elem(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elemContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_lhs)
        try:
            self.state = 517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 514
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.array_elem()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 516
                self.struct_elem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def many_index_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Many_index_opsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_elem




    def array_elem(self):

        localctx = MiniGoParser.Array_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_array_elem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.expr(0)
            self.state = 520
            self.many_index_ops()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_index_opsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Index_opsContext,0)


        def many_index_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Many_index_opsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_many_index_ops




    def many_index_ops(self):

        localctx = MiniGoParser.Many_index_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_many_index_ops)
        try:
            self.state = 526
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 522
                self.index_ops()
                self.state = 523
                self.many_index_ops()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 525
                self.index_ops()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_elemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_elem




    def struct_elem(self):

        localctx = MiniGoParser.Struct_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_struct_elem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.expr(0)
            self.state = 529
            self.match(MiniGoParser.DOT)
            self.state = 530
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_rhs




    def rhs(self):

        localctx = MiniGoParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.expr(0)
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

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def if_tail(self):
            return self.getTypedRuleContext(MiniGoParser.If_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.match(MiniGoParser.IF)
            self.state = 535
            self.match(MiniGoParser.LB)
            self.state = 536
            self.expr(0)
            self.state = 537
            self.match(MiniGoParser.RB)
            self.state = 538
            self.block()
            self.state = 540
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 539
                self.if_tail()


            self.state = 542
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_stmtContext,0)


        def if_tail(self):
            return self.getTypedRuleContext(MiniGoParser.If_tailContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_tail




    def if_tail(self):

        localctx = MiniGoParser.If_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_if_tail)
        try:
            self.state = 549
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 544
                self.else_if_stmt()
                self.state = 545
                self.if_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 547
                self.else_if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 548
                self.else_stmt()
                pass


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

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_stmt




    def else_if_stmt(self):

        localctx = MiniGoParser.Else_if_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_else_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.match(MiniGoParser.ELSE)
            self.state = 552
            self.match(MiniGoParser.IF)
            self.state = 553
            self.match(MiniGoParser.LB)
            self.state = 554
            self.expr(0)
            self.state = 555
            self.match(MiniGoParser.RB)
            self.state = 556
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_stmt




    def else_stmt(self):

        localctx = MiniGoParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.match(MiniGoParser.ELSE)
            self.state = 559
            self.block()
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

        def for_basic(self):
            return self.getTypedRuleContext(MiniGoParser.For_basicContext,0)


        def for_step(self):
            return self.getTypedRuleContext(MiniGoParser.For_stepContext,0)


        def for_each(self):
            return self.getTypedRuleContext(MiniGoParser.For_eachContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_for_stmt)
        try:
            self.state = 564
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 561
                self.for_basic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 562
                self.for_step()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 563
                self.for_each()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_basicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_basic




    def for_basic(self):

        localctx = MiniGoParser.For_basicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_for_basic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
            self.match(MiniGoParser.FOR)
            self.state = 567
            self.expr(0)
            self.state = 568
            self.block()
            self.state = 569
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def fully_clause(self):
            return self.getTypedRuleContext(MiniGoParser.Fully_clauseContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_step




    def for_step(self):

        localctx = MiniGoParser.For_stepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_for_step)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self.match(MiniGoParser.FOR)
            self.state = 572
            self.fully_clause()
            self.state = 573
            self.block()
            self.state = 574
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_eachContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def range_clause(self):
            return self.getTypedRuleContext(MiniGoParser.Range_clauseContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_each




    def for_each(self):

        localctx = MiniGoParser.For_eachContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_for_each)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.match(MiniGoParser.FOR)
            self.state = 577
            self.range_clause()
            self.state = 578
            self.block()
            self.state = 579
            self.eos()
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

        def init(self):
            return self.getTypedRuleContext(MiniGoParser.InitContext,0)


        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.EosContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.EosContext,i)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def update(self):
            return self.getTypedRuleContext(MiniGoParser.UpdateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fully_clause




    def fully_clause(self):

        localctx = MiniGoParser.Fully_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_fully_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.init()
            self.state = 582
            self.eos()
            self.state = 583
            self.expr(0)
            self.state = 584
            self.eos()
            self.state = 585
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

        def asm_for(self):
            return self.getTypedRuleContext(MiniGoParser.Asm_forContext,0)


        def decl_var_init(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_var_initContext,0)


        def decl_var_type_init_for(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_var_type_init_forContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init




    def init(self):

        localctx = MiniGoParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_init)
        try:
            self.state = 590
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 587
                self.asm_for()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 588
                self.decl_var_init()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 589
                self.decl_var_type_init_for()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_var_type_init_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_var_type_init_for




    def decl_var_type_init_for(self):

        localctx = MiniGoParser.Decl_var_type_init_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_decl_var_type_init_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(MiniGoParser.VAR)
            self.state = 593
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 594
            self.primitive_type()
            self.state = 595
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 596
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

        def asm_for(self):
            return self.getTypedRuleContext(MiniGoParser.Asm_forContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_update




    def update(self):

        localctx = MiniGoParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 598
            self.asm_for()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asm_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def assign_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_opsContext,0)


        def rhs(self):
            return self.getTypedRuleContext(MiniGoParser.RhsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_asm_for




    def asm_for(self):

        localctx = MiniGoParser.Asm_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_asm_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 601
            self.assign_ops()
            self.state = 602
            self.rhs()
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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_range_clause




    def range_clause(self):

        localctx = MiniGoParser.Range_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_range_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            _la = self._input.LA(1)
            if not(_la==2 or _la==62):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 605
            self.match(MiniGoParser.COMMA)
            self.state = 606
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 607
            self.match(MiniGoParser.ASSIGN)
            self.state = 608
            self.match(MiniGoParser.RANGE)
            self.state = 609
            self.expr(0)
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
        self.enterRule(localctx, 144, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            self.match(MiniGoParser.BREAK)
            self.state = 612
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
        self.enterRule(localctx, 146, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self.match(MiniGoParser.CONTINUE)
            self.state = 615
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_stmt




    def call_stmt(self):

        localctx = MiniGoParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 617
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 618
                self.method_call()
                pass


            self.state = 621
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            self.expr(0)
            self.state = 624
            self.match(MiniGoParser.DOT)
            self.state = 625
            self.func_call()
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
        self.enterRule(localctx, 152, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 627
            self.match(MiniGoParser.RETURN)
            self.state = 629
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8108872141513949208) != 0):
                self.state = 628
                self.expr(0)


            self.state = 631
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
        self.enterRule(localctx, 154, self.RULE_boolean_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
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
        self.enterRule(localctx, 156, self.RULE_arithmetic_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
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
        self.enterRule(localctx, 158, self.RULE_relational_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
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

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

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
        self.enterRule(localctx, 160, self.RULE_assign_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 639
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 69269232549888) != 0)):
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
        self.enterRule(localctx, 162, self.RULE_index_ops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
            self.match(MiniGoParser.LSB)
            self.state = 642
            self.expr(0)
            self.state = 643
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

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_eos




    def eos(self):

        localctx = MiniGoParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_eos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
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
        self._predicates[40] = self.expr_sempred
        self._predicates[41] = self.expr1_sempred
        self._predicates[42] = self.expr2_sempred
        self._predicates[43] = self.expr3_sempred
        self._predicates[44] = self.expr4_sempred
        self._predicates[46] = self.primary_expr_sempred
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
         

    def primary_expr_sempred(self, localctx:Primary_exprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         




