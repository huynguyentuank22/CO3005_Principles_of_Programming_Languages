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
        4,1,69,686,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
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
        2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,84,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,3,1,178,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,187,8,2,1,3,1,3,1,3,3,3,192,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,211,8,6,1,7,1,7,1,7,
        1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,229,
        8,10,1,11,1,11,1,11,1,11,3,11,235,8,11,1,12,1,12,1,12,1,12,1,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,3,15,253,
        8,15,1,16,1,16,1,16,1,16,3,16,259,8,16,1,17,1,17,1,17,1,17,1,17,
        1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,3,19,275,8,19,1,20,
        1,20,1,20,1,20,3,20,281,8,20,1,20,1,20,1,21,1,21,1,21,3,21,288,8,
        21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,3,22,297,8,22,1,23,1,23,1,
        23,1,23,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,
        26,1,26,1,26,3,26,317,8,26,1,27,1,27,1,27,3,27,322,8,27,1,27,1,27,
        3,27,326,8,27,1,27,1,27,1,28,1,28,1,28,1,28,3,28,334,8,28,1,28,1,
        28,3,28,338,8,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,3,29,348,
        8,29,1,30,1,30,1,30,1,31,1,31,1,31,1,31,3,31,357,8,31,1,32,1,32,
        1,32,1,32,1,33,1,33,1,33,1,33,3,33,367,8,33,1,34,1,34,1,34,1,34,
        1,34,3,34,374,8,34,1,34,1,34,3,34,378,8,34,1,34,1,34,1,34,1,35,1,
        35,1,35,1,35,1,35,1,36,1,36,1,36,3,36,391,8,36,1,37,1,37,1,38,1,
        38,1,38,3,38,398,8,38,1,39,1,39,1,40,1,40,1,40,3,40,405,8,40,1,40,
        1,40,1,41,1,41,1,41,1,41,1,41,1,41,5,41,415,8,41,10,41,12,41,418,
        9,41,1,42,1,42,1,42,1,42,1,42,1,42,5,42,426,8,42,10,42,12,42,429,
        9,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,5,43,438,8,43,10,43,12,43,
        441,9,43,1,44,1,44,1,44,1,44,1,44,1,44,5,44,449,8,44,10,44,12,44,
        452,9,44,1,45,1,45,1,45,1,45,1,45,1,45,5,45,460,8,45,10,45,12,45,
        463,9,45,1,46,1,46,1,46,3,46,468,8,46,1,47,1,47,1,47,1,47,3,47,474,
        8,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,3,47,486,
        8,47,1,47,5,47,489,8,47,10,47,12,47,492,9,47,1,48,1,48,1,48,1,48,
        1,48,3,48,499,8,48,1,49,1,49,1,49,1,49,1,49,1,49,1,49,3,49,508,8,
        49,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,50,3,50,518,8,50,1,51,1,
        51,1,51,3,51,523,8,51,1,52,1,52,1,52,1,53,1,53,1,53,1,53,1,54,1,
        54,1,54,3,54,535,8,54,1,55,1,55,1,55,1,56,1,56,1,56,1,56,3,56,544,
        8,56,1,57,1,57,3,57,548,8,57,1,57,1,57,1,58,1,58,1,58,1,58,3,58,
        556,8,58,1,59,1,59,1,59,3,59,561,8,59,1,60,1,60,1,61,1,61,1,61,1,
        61,1,61,1,61,3,61,571,8,61,1,61,1,61,3,61,575,8,61,1,61,1,61,1,62,
        1,62,1,62,1,62,3,62,583,8,62,1,63,1,63,1,63,1,63,1,63,1,63,1,63,
        1,64,1,64,1,64,1,64,1,64,1,65,1,65,1,65,3,65,600,8,65,1,66,1,66,
        1,66,1,66,1,66,1,66,1,67,1,67,1,67,3,67,611,8,67,1,68,1,68,1,68,
        1,68,1,68,1,68,1,69,1,69,1,70,1,70,1,70,1,70,1,71,1,71,1,71,1,71,
        1,71,1,71,1,71,1,72,1,72,1,72,1,73,1,73,1,73,1,74,1,74,3,74,640,
        8,74,1,74,1,74,1,75,1,75,3,75,646,8,75,1,75,3,75,649,8,75,1,75,1,
        75,1,75,1,76,1,76,1,76,1,76,3,76,658,8,76,1,77,1,77,1,77,1,77,3,
        77,664,8,77,1,78,1,78,3,78,668,8,78,1,78,1,78,1,79,1,79,1,80,1,80,
        1,81,1,81,1,82,1,82,1,83,1,83,1,83,1,83,1,84,1,84,1,84,0,6,82,84,
        86,88,90,94,85,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,
        80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,
        118,120,122,124,126,128,130,132,134,136,138,140,142,144,146,148,
        150,152,154,156,158,160,162,164,166,168,0,12,2,0,55,55,62,62,3,0,
        3,4,55,55,60,61,1,0,13,16,1,0,25,26,1,0,27,29,2,0,26,26,38,38,2,
        0,2,2,62,62,1,0,36,38,1,0,25,29,1,0,30,35,1,0,40,45,2,0,54,54,66,
        66,680,0,170,1,0,0,0,2,177,1,0,0,0,4,186,1,0,0,0,6,191,1,0,0,0,8,
        195,1,0,0,0,10,201,1,0,0,0,12,206,1,0,0,0,14,212,1,0,0,0,16,218,
        1,0,0,0,18,221,1,0,0,0,20,225,1,0,0,0,22,234,1,0,0,0,24,236,1,0,
        0,0,26,240,1,0,0,0,28,243,1,0,0,0,30,252,1,0,0,0,32,258,1,0,0,0,
        34,260,1,0,0,0,36,265,1,0,0,0,38,274,1,0,0,0,40,276,1,0,0,0,42,284,
        1,0,0,0,44,296,1,0,0,0,46,298,1,0,0,0,48,302,1,0,0,0,50,307,1,0,
        0,0,52,316,1,0,0,0,54,318,1,0,0,0,56,329,1,0,0,0,58,347,1,0,0,0,
        60,349,1,0,0,0,62,356,1,0,0,0,64,358,1,0,0,0,66,366,1,0,0,0,68,368,
        1,0,0,0,70,382,1,0,0,0,72,390,1,0,0,0,74,392,1,0,0,0,76,397,1,0,
        0,0,78,399,1,0,0,0,80,401,1,0,0,0,82,408,1,0,0,0,84,419,1,0,0,0,
        86,430,1,0,0,0,88,442,1,0,0,0,90,453,1,0,0,0,92,467,1,0,0,0,94,473,
        1,0,0,0,96,498,1,0,0,0,98,507,1,0,0,0,100,517,1,0,0,0,102,522,1,
        0,0,0,104,524,1,0,0,0,106,527,1,0,0,0,108,534,1,0,0,0,110,536,1,
        0,0,0,112,543,1,0,0,0,114,547,1,0,0,0,116,555,1,0,0,0,118,557,1,
        0,0,0,120,562,1,0,0,0,122,564,1,0,0,0,124,582,1,0,0,0,126,584,1,
        0,0,0,128,591,1,0,0,0,130,599,1,0,0,0,132,601,1,0,0,0,134,610,1,
        0,0,0,136,612,1,0,0,0,138,618,1,0,0,0,140,620,1,0,0,0,142,624,1,
        0,0,0,144,631,1,0,0,0,146,634,1,0,0,0,148,639,1,0,0,0,150,645,1,
        0,0,0,152,657,1,0,0,0,154,659,1,0,0,0,156,665,1,0,0,0,158,671,1,
        0,0,0,160,673,1,0,0,0,162,675,1,0,0,0,164,677,1,0,0,0,166,679,1,
        0,0,0,168,683,1,0,0,0,170,171,3,2,1,0,171,172,5,0,0,1,172,1,1,0,
        0,0,173,174,3,4,2,0,174,175,3,2,1,0,175,178,1,0,0,0,176,178,3,4,
        2,0,177,173,1,0,0,0,177,176,1,0,0,0,178,3,1,0,0,0,179,187,3,6,3,
        0,180,187,3,14,7,0,181,187,3,16,8,0,182,187,3,34,17,0,183,187,3,
        48,24,0,184,187,3,56,28,0,185,187,3,68,34,0,186,179,1,0,0,0,186,
        180,1,0,0,0,186,181,1,0,0,0,186,182,1,0,0,0,186,183,1,0,0,0,186,
        184,1,0,0,0,186,185,1,0,0,0,187,5,1,0,0,0,188,192,3,8,4,0,189,192,
        3,10,5,0,190,192,3,12,6,0,191,188,1,0,0,0,191,189,1,0,0,0,191,190,
        1,0,0,0,192,193,1,0,0,0,193,194,3,168,84,0,194,7,1,0,0,0,195,196,
        5,18,0,0,196,197,5,62,0,0,197,198,3,72,36,0,198,199,5,39,0,0,199,
        200,3,82,41,0,200,9,1,0,0,0,201,202,5,18,0,0,202,203,5,62,0,0,203,
        204,5,39,0,0,204,205,3,82,41,0,205,11,1,0,0,0,206,207,5,18,0,0,207,
        210,5,62,0,0,208,211,3,78,39,0,209,211,5,62,0,0,210,208,1,0,0,0,
        210,209,1,0,0,0,211,13,1,0,0,0,212,213,5,17,0,0,213,214,5,62,0,0,
        214,215,5,39,0,0,215,216,3,82,41,0,216,217,3,168,84,0,217,15,1,0,
        0,0,218,219,3,18,9,0,219,220,3,168,84,0,220,17,1,0,0,0,221,222,5,
        18,0,0,222,223,5,62,0,0,223,224,3,20,10,0,224,19,1,0,0,0,225,228,
        3,22,11,0,226,229,3,78,39,0,227,229,5,62,0,0,228,226,1,0,0,0,228,
        227,1,0,0,0,229,21,1,0,0,0,230,231,3,24,12,0,231,232,3,22,11,0,232,
        235,1,0,0,0,233,235,3,24,12,0,234,230,1,0,0,0,234,233,1,0,0,0,235,
        23,1,0,0,0,236,237,5,51,0,0,237,238,7,0,0,0,238,239,5,52,0,0,239,
        25,1,0,0,0,240,241,3,20,10,0,241,242,3,28,14,0,242,27,1,0,0,0,243,
        244,5,49,0,0,244,245,3,30,15,0,245,246,5,50,0,0,246,29,1,0,0,0,247,
        248,3,32,16,0,248,249,5,53,0,0,249,250,3,30,15,0,250,253,1,0,0,0,
        251,253,3,32,16,0,252,247,1,0,0,0,252,251,1,0,0,0,253,31,1,0,0,0,
        254,259,3,28,14,0,255,259,3,74,37,0,256,259,5,62,0,0,257,259,3,42,
        21,0,258,254,1,0,0,0,258,255,1,0,0,0,258,256,1,0,0,0,258,257,1,0,
        0,0,259,33,1,0,0,0,260,261,5,10,0,0,261,262,5,62,0,0,262,263,3,36,
        18,0,263,264,3,168,84,0,264,35,1,0,0,0,265,266,5,11,0,0,266,267,
        5,49,0,0,267,268,3,38,19,0,268,269,5,50,0,0,269,37,1,0,0,0,270,271,
        3,40,20,0,271,272,3,38,19,0,272,275,1,0,0,0,273,275,3,40,20,0,274,
        270,1,0,0,0,274,273,1,0,0,0,275,39,1,0,0,0,276,280,5,62,0,0,277,
        281,3,78,39,0,278,281,3,20,10,0,279,281,5,62,0,0,280,277,1,0,0,0,
        280,278,1,0,0,0,280,279,1,0,0,0,281,282,1,0,0,0,282,283,3,168,84,
        0,283,41,1,0,0,0,284,285,5,62,0,0,285,287,5,49,0,0,286,288,3,44,
        22,0,287,286,1,0,0,0,287,288,1,0,0,0,288,289,1,0,0,0,289,290,5,50,
        0,0,290,43,1,0,0,0,291,292,3,46,23,0,292,293,5,53,0,0,293,294,3,
        44,22,0,294,297,1,0,0,0,295,297,3,46,23,0,296,291,1,0,0,0,296,295,
        1,0,0,0,297,45,1,0,0,0,298,299,5,62,0,0,299,300,5,1,0,0,300,301,
        3,82,41,0,301,47,1,0,0,0,302,303,5,10,0,0,303,304,5,62,0,0,304,305,
        3,50,25,0,305,306,3,168,84,0,306,49,1,0,0,0,307,308,5,12,0,0,308,
        309,5,49,0,0,309,310,3,52,26,0,310,311,5,50,0,0,311,51,1,0,0,0,312,
        313,3,54,27,0,313,314,3,52,26,0,314,317,1,0,0,0,315,317,3,54,27,
        0,316,312,1,0,0,0,316,315,1,0,0,0,317,53,1,0,0,0,318,319,5,62,0,
        0,319,321,5,47,0,0,320,322,3,58,29,0,321,320,1,0,0,0,321,322,1,0,
        0,0,322,323,1,0,0,0,323,325,5,48,0,0,324,326,3,72,36,0,325,324,1,
        0,0,0,325,326,1,0,0,0,326,327,1,0,0,0,327,328,3,168,84,0,328,55,
        1,0,0,0,329,330,5,9,0,0,330,331,5,62,0,0,331,333,5,47,0,0,332,334,
        3,58,29,0,333,332,1,0,0,0,333,334,1,0,0,0,334,335,1,0,0,0,335,337,
        5,48,0,0,336,338,3,72,36,0,337,336,1,0,0,0,337,338,1,0,0,0,338,339,
        1,0,0,0,339,340,3,64,32,0,340,341,3,168,84,0,341,57,1,0,0,0,342,
        343,3,60,30,0,343,344,5,53,0,0,344,345,3,58,29,0,345,348,1,0,0,0,
        346,348,3,60,30,0,347,342,1,0,0,0,347,346,1,0,0,0,348,59,1,0,0,0,
        349,350,3,62,31,0,350,351,3,72,36,0,351,61,1,0,0,0,352,353,5,62,
        0,0,353,354,5,53,0,0,354,357,3,62,31,0,355,357,5,62,0,0,356,352,
        1,0,0,0,356,355,1,0,0,0,357,63,1,0,0,0,358,359,5,49,0,0,359,360,
        3,66,33,0,360,361,5,50,0,0,361,65,1,0,0,0,362,363,3,100,50,0,363,
        364,3,66,33,0,364,367,1,0,0,0,365,367,3,100,50,0,366,362,1,0,0,0,
        366,365,1,0,0,0,367,67,1,0,0,0,368,369,5,9,0,0,369,370,3,70,35,0,
        370,371,5,62,0,0,371,373,5,47,0,0,372,374,3,58,29,0,373,372,1,0,
        0,0,373,374,1,0,0,0,374,375,1,0,0,0,375,377,5,48,0,0,376,378,3,72,
        36,0,377,376,1,0,0,0,377,378,1,0,0,0,378,379,1,0,0,0,379,380,3,64,
        32,0,380,381,3,168,84,0,381,69,1,0,0,0,382,383,5,47,0,0,383,384,
        5,62,0,0,384,385,5,62,0,0,385,386,5,48,0,0,386,71,1,0,0,0,387,391,
        3,78,39,0,388,391,3,20,10,0,389,391,5,62,0,0,390,387,1,0,0,0,390,
        388,1,0,0,0,390,389,1,0,0,0,391,73,1,0,0,0,392,393,7,1,0,0,393,75,
        1,0,0,0,394,398,3,74,37,0,395,398,3,26,13,0,396,398,3,42,21,0,397,
        394,1,0,0,0,397,395,1,0,0,0,397,396,1,0,0,0,398,77,1,0,0,0,399,400,
        7,2,0,0,400,79,1,0,0,0,401,402,5,62,0,0,402,404,5,47,0,0,403,405,
        3,96,48,0,404,403,1,0,0,0,404,405,1,0,0,0,405,406,1,0,0,0,406,407,
        5,48,0,0,407,81,1,0,0,0,408,409,6,41,-1,0,409,410,3,84,42,0,410,
        416,1,0,0,0,411,412,10,2,0,0,412,413,5,37,0,0,413,415,3,84,42,0,
        414,411,1,0,0,0,415,418,1,0,0,0,416,414,1,0,0,0,416,417,1,0,0,0,
        417,83,1,0,0,0,418,416,1,0,0,0,419,420,6,42,-1,0,420,421,3,86,43,
        0,421,427,1,0,0,0,422,423,10,2,0,0,423,424,5,36,0,0,424,426,3,86,
        43,0,425,422,1,0,0,0,426,429,1,0,0,0,427,425,1,0,0,0,427,428,1,0,
        0,0,428,85,1,0,0,0,429,427,1,0,0,0,430,431,6,43,-1,0,431,432,3,88,
        44,0,432,439,1,0,0,0,433,434,10,2,0,0,434,435,3,162,81,0,435,436,
        3,88,44,0,436,438,1,0,0,0,437,433,1,0,0,0,438,441,1,0,0,0,439,437,
        1,0,0,0,439,440,1,0,0,0,440,87,1,0,0,0,441,439,1,0,0,0,442,443,6,
        44,-1,0,443,444,3,90,45,0,444,450,1,0,0,0,445,446,10,2,0,0,446,447,
        7,3,0,0,447,449,3,90,45,0,448,445,1,0,0,0,449,452,1,0,0,0,450,448,
        1,0,0,0,450,451,1,0,0,0,451,89,1,0,0,0,452,450,1,0,0,0,453,454,6,
        45,-1,0,454,455,3,92,46,0,455,461,1,0,0,0,456,457,10,2,0,0,457,458,
        7,4,0,0,458,460,3,92,46,0,459,456,1,0,0,0,460,463,1,0,0,0,461,459,
        1,0,0,0,461,462,1,0,0,0,462,91,1,0,0,0,463,461,1,0,0,0,464,465,7,
        5,0,0,465,468,3,92,46,0,466,468,3,94,47,0,467,464,1,0,0,0,467,466,
        1,0,0,0,468,93,1,0,0,0,469,470,6,47,-1,0,470,471,5,62,0,0,471,474,
        3,166,83,0,472,474,3,98,49,0,473,469,1,0,0,0,473,472,1,0,0,0,474,
        490,1,0,0,0,475,476,10,4,0,0,476,489,3,166,83,0,477,478,10,3,0,0,
        478,479,5,46,0,0,479,489,5,62,0,0,480,481,10,2,0,0,481,482,5,46,
        0,0,482,483,5,62,0,0,483,485,5,47,0,0,484,486,3,96,48,0,485,484,
        1,0,0,0,485,486,1,0,0,0,486,487,1,0,0,0,487,489,5,48,0,0,488,475,
        1,0,0,0,488,477,1,0,0,0,488,480,1,0,0,0,489,492,1,0,0,0,490,488,
        1,0,0,0,490,491,1,0,0,0,491,95,1,0,0,0,492,490,1,0,0,0,493,494,3,
        82,41,0,494,495,5,53,0,0,495,496,3,96,48,0,496,499,1,0,0,0,497,499,
        3,82,41,0,498,493,1,0,0,0,498,497,1,0,0,0,499,97,1,0,0,0,500,508,
        3,76,38,0,501,508,5,62,0,0,502,508,3,80,40,0,503,504,5,47,0,0,504,
        505,3,82,41,0,505,506,5,48,0,0,506,508,1,0,0,0,507,500,1,0,0,0,507,
        501,1,0,0,0,507,502,1,0,0,0,507,503,1,0,0,0,508,99,1,0,0,0,509,518,
        3,102,51,0,510,518,3,104,52,0,511,518,3,122,61,0,512,518,3,128,64,
        0,513,518,3,144,72,0,514,518,3,146,73,0,515,518,3,148,74,0,516,518,
        3,156,78,0,517,509,1,0,0,0,517,510,1,0,0,0,517,511,1,0,0,0,517,512,
        1,0,0,0,517,513,1,0,0,0,517,514,1,0,0,0,517,515,1,0,0,0,517,516,
        1,0,0,0,518,101,1,0,0,0,519,523,3,6,3,0,520,523,3,14,7,0,521,523,
        3,16,8,0,522,519,1,0,0,0,522,520,1,0,0,0,522,521,1,0,0,0,523,103,
        1,0,0,0,524,525,3,106,53,0,525,526,3,168,84,0,526,105,1,0,0,0,527,
        528,3,108,54,0,528,529,3,164,82,0,529,530,3,120,60,0,530,107,1,0,
        0,0,531,535,5,62,0,0,532,535,3,110,55,0,533,535,3,114,57,0,534,531,
        1,0,0,0,534,532,1,0,0,0,534,533,1,0,0,0,535,109,1,0,0,0,536,537,
        5,62,0,0,537,538,3,112,56,0,538,111,1,0,0,0,539,540,3,166,83,0,540,
        541,3,112,56,0,541,544,1,0,0,0,542,544,3,166,83,0,543,539,1,0,0,
        0,543,542,1,0,0,0,544,113,1,0,0,0,545,548,5,62,0,0,546,548,3,110,
        55,0,547,545,1,0,0,0,547,546,1,0,0,0,548,549,1,0,0,0,549,550,3,116,
        58,0,550,115,1,0,0,0,551,552,3,118,59,0,552,553,3,116,58,0,553,556,
        1,0,0,0,554,556,3,118,59,0,555,551,1,0,0,0,555,554,1,0,0,0,556,117,
        1,0,0,0,557,560,5,46,0,0,558,561,5,62,0,0,559,561,3,110,55,0,560,
        558,1,0,0,0,560,559,1,0,0,0,561,119,1,0,0,0,562,563,3,82,41,0,563,
        121,1,0,0,0,564,565,5,5,0,0,565,566,5,47,0,0,566,567,3,82,41,0,567,
        568,5,48,0,0,568,570,3,64,32,0,569,571,3,124,62,0,570,569,1,0,0,
        0,570,571,1,0,0,0,571,574,1,0,0,0,572,573,5,6,0,0,573,575,3,64,32,
        0,574,572,1,0,0,0,574,575,1,0,0,0,575,576,1,0,0,0,576,577,3,168,
        84,0,577,123,1,0,0,0,578,579,3,126,63,0,579,580,3,124,62,0,580,583,
        1,0,0,0,581,583,3,126,63,0,582,578,1,0,0,0,582,581,1,0,0,0,583,125,
        1,0,0,0,584,585,5,6,0,0,585,586,5,5,0,0,586,587,5,47,0,0,587,588,
        3,82,41,0,588,589,5,48,0,0,589,590,3,64,32,0,590,127,1,0,0,0,591,
        592,5,7,0,0,592,593,3,130,65,0,593,594,3,64,32,0,594,595,3,168,84,
        0,595,129,1,0,0,0,596,600,3,82,41,0,597,600,3,132,66,0,598,600,3,
        142,71,0,599,596,1,0,0,0,599,597,1,0,0,0,599,598,1,0,0,0,600,131,
        1,0,0,0,601,602,3,134,67,0,602,603,3,168,84,0,603,604,3,82,41,0,
        604,605,3,168,84,0,605,606,3,138,69,0,606,133,1,0,0,0,607,611,3,
        140,70,0,608,611,3,10,5,0,609,611,3,136,68,0,610,607,1,0,0,0,610,
        608,1,0,0,0,610,609,1,0,0,0,611,135,1,0,0,0,612,613,5,18,0,0,613,
        614,5,62,0,0,614,615,3,78,39,0,615,616,5,39,0,0,616,617,3,82,41,
        0,617,137,1,0,0,0,618,619,3,140,70,0,619,139,1,0,0,0,620,621,5,62,
        0,0,621,622,3,164,82,0,622,623,3,120,60,0,623,141,1,0,0,0,624,625,
        7,6,0,0,625,626,5,53,0,0,626,627,5,62,0,0,627,628,5,40,0,0,628,629,
        5,21,0,0,629,630,3,82,41,0,630,143,1,0,0,0,631,632,5,20,0,0,632,
        633,3,168,84,0,633,145,1,0,0,0,634,635,5,19,0,0,635,636,3,168,84,
        0,636,147,1,0,0,0,637,640,3,80,40,0,638,640,3,150,75,0,639,637,1,
        0,0,0,639,638,1,0,0,0,640,641,1,0,0,0,641,642,3,168,84,0,642,149,
        1,0,0,0,643,646,5,62,0,0,644,646,3,110,55,0,645,643,1,0,0,0,645,
        644,1,0,0,0,646,648,1,0,0,0,647,649,3,152,76,0,648,647,1,0,0,0,648,
        649,1,0,0,0,649,650,1,0,0,0,650,651,5,46,0,0,651,652,3,80,40,0,652,
        151,1,0,0,0,653,654,3,154,77,0,654,655,3,152,76,0,655,658,1,0,0,
        0,656,658,3,154,77,0,657,653,1,0,0,0,657,656,1,0,0,0,658,153,1,0,
        0,0,659,663,5,46,0,0,660,664,5,62,0,0,661,664,3,110,55,0,662,664,
        3,80,40,0,663,660,1,0,0,0,663,661,1,0,0,0,663,662,1,0,0,0,664,155,
        1,0,0,0,665,667,5,8,0,0,666,668,3,82,41,0,667,666,1,0,0,0,667,668,
        1,0,0,0,668,669,1,0,0,0,669,670,3,168,84,0,670,157,1,0,0,0,671,672,
        7,7,0,0,672,159,1,0,0,0,673,674,7,8,0,0,674,161,1,0,0,0,675,676,
        7,9,0,0,676,163,1,0,0,0,677,678,7,10,0,0,678,165,1,0,0,0,679,680,
        5,51,0,0,680,681,3,82,41,0,681,682,5,52,0,0,682,167,1,0,0,0,683,
        684,7,11,0,0,684,169,1,0,0,0,55,177,186,191,210,228,234,252,258,
        274,280,287,296,316,321,325,333,337,347,356,366,373,377,390,397,
        404,416,427,439,450,461,467,473,485,488,490,498,507,517,522,534,
        543,547,555,560,570,574,582,599,610,639,645,648,657,663,667
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
    RULE_array_decl = 8
    RULE_decl_arr = 9
    RULE_array_type = 10
    RULE_dimensions = 11
    RULE_dim = 12
    RULE_array_literal = 13
    RULE_ele_list = 14
    RULE_many_ele = 15
    RULE_ele = 16
    RULE_struct_decl = 17
    RULE_struct_type = 18
    RULE_many_fields = 19
    RULE_fields = 20
    RULE_struct_literal = 21
    RULE_struct_elements = 22
    RULE_struct_ele = 23
    RULE_interface_decl = 24
    RULE_interface_type = 25
    RULE_many_interface_field = 26
    RULE_interface_field = 27
    RULE_func_decl = 28
    RULE_param_list = 29
    RULE_param = 30
    RULE_id_list = 31
    RULE_block = 32
    RULE_many_stmt = 33
    RULE_method_decl = 34
    RULE_method = 35
    RULE_types = 36
    RULE_primitive_lit = 37
    RULE_literals = 38
    RULE_primitive_type = 39
    RULE_func_call = 40
    RULE_expr = 41
    RULE_expr1 = 42
    RULE_expr2 = 43
    RULE_expr3 = 44
    RULE_expr4 = 45
    RULE_expr5 = 46
    RULE_primary_expr = 47
    RULE_expr_list = 48
    RULE_operand = 49
    RULE_stmt = 50
    RULE_decl_stmt = 51
    RULE_asm_stmt = 52
    RULE_asm = 53
    RULE_lhs = 54
    RULE_array_elem = 55
    RULE_many_index_ops = 56
    RULE_struct_elem = 57
    RULE_many_struct_ops = 58
    RULE_struct_ops = 59
    RULE_rhs = 60
    RULE_if_stmt = 61
    RULE_many_else_if_stmt = 62
    RULE_else_if_stmt = 63
    RULE_for_stmt = 64
    RULE_for_clause = 65
    RULE_fully_clause = 66
    RULE_init = 67
    RULE_decl_var_type_init_for = 68
    RULE_update = 69
    RULE_asm_for = 70
    RULE_range_clause = 71
    RULE_break_stmt = 72
    RULE_continue_stmt = 73
    RULE_call_stmt = 74
    RULE_struct_elem_call = 75
    RULE_many_struct_ops_call = 76
    RULE_struct_ops_call = 77
    RULE_return_stmt = 78
    RULE_boolean_ops = 79
    RULE_arithmetic_ops = 80
    RULE_relational_ops = 81
    RULE_assign_ops = 82
    RULE_index_ops = 83
    RULE_eos = 84

    ruleNames =  [ "program", "many_decl", "decl", "var_decl", "decl_var_type_init", 
                   "decl_var_init", "decl_var_type", "const_decl", "array_decl", 
                   "decl_arr", "array_type", "dimensions", "dim", "array_literal", 
                   "ele_list", "many_ele", "ele", "struct_decl", "struct_type", 
                   "many_fields", "fields", "struct_literal", "struct_elements", 
                   "struct_ele", "interface_decl", "interface_type", "many_interface_field", 
                   "interface_field", "func_decl", "param_list", "param", 
                   "id_list", "block", "many_stmt", "method_decl", "method", 
                   "types", "primitive_lit", "literals", "primitive_type", 
                   "func_call", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "primary_expr", "expr_list", "operand", "stmt", 
                   "decl_stmt", "asm_stmt", "asm", "lhs", "array_elem", 
                   "many_index_ops", "struct_elem", "many_struct_ops", "struct_ops", 
                   "rhs", "if_stmt", "many_else_if_stmt", "else_if_stmt", 
                   "for_stmt", "for_clause", "fully_clause", "init", "decl_var_type_init_for", 
                   "update", "asm_for", "range_clause", "break_stmt", "continue_stmt", 
                   "call_stmt", "struct_elem_call", "many_struct_ops_call", 
                   "struct_ops_call", "return_stmt", "boolean_ops", "arithmetic_ops", 
                   "relational_ops", "assign_ops", "index_ops", "eos" ]

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
            self.state = 170
            self.many_decl()
            self.state = 171
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
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.decl()
                self.state = 174
                self.many_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
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


        def array_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declContext,0)


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
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self.array_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 182
                self.struct_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 183
                self.interface_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 184
                self.func_decl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 185
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
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 188
                self.decl_var_type_init()
                pass

            elif la_ == 2:
                self.state = 189
                self.decl_var_init()
                pass

            elif la_ == 3:
                self.state = 190
                self.decl_var_type()
                pass


            self.state = 193
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
            self.state = 195
            self.match(MiniGoParser.VAR)
            self.state = 196
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 197
            self.types()
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
            self.state = 201
            self.match(MiniGoParser.VAR)
            self.state = 202
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 203
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 204
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_var_type




    def decl_var_type(self):

        localctx = MiniGoParser.Decl_var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_decl_var_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(MiniGoParser.VAR)
            self.state = 207
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.state = 208
                self.primitive_type()
                pass
            elif token in [62]:
                self.state = 209
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
            self.state = 212
            self.match(MiniGoParser.CONST)
            self.state = 213
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 214
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 215
            self.expr(0)
            self.state = 216
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

        def decl_arr(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_arrContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_decl




    def array_decl(self):

        localctx = MiniGoParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.decl_arr()
            self.state = 219
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_arr




    def decl_arr(self):

        localctx = MiniGoParser.Decl_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_decl_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(MiniGoParser.VAR)
            self.state = 222
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 223
            self.array_type()
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
        self.enterRule(localctx, 20, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.dimensions()
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.state = 226
                self.primitive_type()
                pass
            elif token in [62]:
                self.state = 227
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
        self.enterRule(localctx, 22, self.RULE_dimensions)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.dim()
                self.state = 231
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
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

        def INT_LITERAL(self):
            return self.getToken(MiniGoParser.INT_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dim




    def dim(self):

        localctx = MiniGoParser.DimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dim)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(MiniGoParser.LSB)
            self.state = 237
            _la = self._input.LA(1)
            if not(_la==55 or _la==62):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 238
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
        self.enterRule(localctx, 26, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.array_type()
            self.state = 241
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
        self.enterRule(localctx, 28, self.RULE_ele_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(MiniGoParser.LCB)
            self.state = 244
            self.many_ele()
            self.state = 245
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
        self.enterRule(localctx, 30, self.RULE_many_ele)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.ele()
                self.state = 248
                self.match(MiniGoParser.COMMA)
                self.state = 249
                self.many_ele()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
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


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ele




    def ele(self):

        localctx = MiniGoParser.EleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ele)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.ele_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.primitive_lit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 256
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 257
                self.struct_literal()
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
        self.enterRule(localctx, 34, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(MiniGoParser.TYPE)
            self.state = 261
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 262
            self.struct_type()
            self.state = 263
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
        self.enterRule(localctx, 36, self.RULE_struct_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(MiniGoParser.STRUCT)
            self.state = 266
            self.match(MiniGoParser.LCB)
            self.state = 267
            self.many_fields()
            self.state = 268
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
        self.enterRule(localctx, 38, self.RULE_many_fields)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.fields()
                self.state = 271
                self.many_fields()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_fields




    def fields(self):

        localctx = MiniGoParser.FieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.state = 277
                self.primitive_type()
                pass
            elif token in [51]:
                self.state = 278
                self.array_type()
                pass
            elif token in [62]:
                self.state = 279
                self.match(MiniGoParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 282
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

        def struct_elements(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elementsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 285
            self.match(MiniGoParser.LCB)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 286
                self.struct_elements()


            self.state = 289
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
        self.enterRule(localctx, 44, self.RULE_struct_elements)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.struct_ele()
                self.state = 292
                self.match(MiniGoParser.COMMA)
                self.state = 293
                self.struct_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
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
        self.enterRule(localctx, 46, self.RULE_struct_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 299
            self.match(MiniGoParser.T__0)
            self.state = 300
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
        self.enterRule(localctx, 48, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(MiniGoParser.TYPE)
            self.state = 303
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 304
            self.interface_type()
            self.state = 305
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
        self.enterRule(localctx, 50, self.RULE_interface_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(MiniGoParser.INTERFACE)
            self.state = 308
            self.match(MiniGoParser.LCB)
            self.state = 309
            self.many_interface_field()
            self.state = 310
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
        self.enterRule(localctx, 52, self.RULE_many_interface_field)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.interface_field()
                self.state = 313
                self.many_interface_field()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
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
        self.enterRule(localctx, 54, self.RULE_interface_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 319
            self.match(MiniGoParser.LB)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 320
                self.param_list()


            self.state = 323
            self.match(MiniGoParser.RB)
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4613937818241196032) != 0):
                self.state = 324
                self.types()


            self.state = 327
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
        self.enterRule(localctx, 56, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(MiniGoParser.FUNC)
            self.state = 330
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 331
            self.match(MiniGoParser.LB)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 332
                self.param_list()


            self.state = 335
            self.match(MiniGoParser.RB)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4613937818241196032) != 0):
                self.state = 336
                self.types()


            self.state = 339
            self.block()
            self.state = 340
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
        self.enterRule(localctx, 58, self.RULE_param_list)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.param()
                self.state = 343
                self.match(MiniGoParser.COMMA)
                self.state = 344
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
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
        self.enterRule(localctx, 60, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.id_list()
            self.state = 350
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
        self.enterRule(localctx, 62, self.RULE_id_list)
        try:
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 353
                self.match(MiniGoParser.COMMA)
                self.state = 354
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
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
        self.enterRule(localctx, 64, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(MiniGoParser.LCB)
            self.state = 359
            self.many_stmt()
            self.state = 360
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
        self.enterRule(localctx, 66, self.RULE_many_stmt)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.stmt()
                self.state = 363
                self.many_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
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
        self.enterRule(localctx, 68, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(MiniGoParser.FUNC)
            self.state = 369
            self.method()
            self.state = 370
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 371
            self.match(MiniGoParser.LB)
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 372
                self.param_list()


            self.state = 375
            self.match(MiniGoParser.RB)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4613937818241196032) != 0):
                self.state = 376
                self.types()


            self.state = 379
            self.block()
            self.state = 380
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
        self.enterRule(localctx, 70, self.RULE_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(MiniGoParser.LB)
            self.state = 383
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 384
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 385
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
        self.enterRule(localctx, 72, self.RULE_types)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.primitive_type()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.array_type()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 3)
                self.state = 389
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
        self.enterRule(localctx, 74, self.RULE_primitive_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
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
        self.enterRule(localctx, 76, self.RULE_literals)
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 55, 60, 61]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.primitive_lit()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.array_literal()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 3)
                self.state = 396
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
        self.enterRule(localctx, 78, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
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
        self.enterRule(localctx, 80, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 402
            self.match(MiniGoParser.LB)
            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8108872141513949208) != 0):
                self.state = 403
                self.expr_list()


            self.state = 406
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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 416
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 411
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 412
                    self.match(MiniGoParser.OR)
                    self.state = 413
                    self.expr1(0) 
                self.state = 418
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 422
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 423
                    self.match(MiniGoParser.AND)
                    self.state = 424
                    self.expr2(0) 
                self.state = 429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 439
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 433
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 434
                    self.relational_ops()
                    self.state = 435
                    self.expr3(0) 
                self.state = 441
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 450
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 445
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 446
                    _la = self._input.LA(1)
                    if not(_la==25 or _la==26):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 447
                    self.expr4(0) 
                self.state = 452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 461
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 456
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 457
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 458
                    self.expr5() 
                self.state = 463
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        self.enterRule(localctx, 92, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 467
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                _la = self._input.LA(1)
                if not(_la==26 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 465
                self.expr5()
                pass
            elif token in [3, 4, 47, 51, 55, 60, 61, 62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
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

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def index_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Index_opsContext,0)


        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def primary_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Primary_exprContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_primary_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 470
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 471
                self.index_ops()
                pass

            elif la_ == 2:
                self.state = 472
                self.operand()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 490
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 488
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 475
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 476
                        self.index_ops()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 477
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 478
                        self.match(MiniGoParser.DOT)
                        self.state = 479
                        self.match(MiniGoParser.IDENTIFIER)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 480
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 481
                        self.match(MiniGoParser.DOT)
                        self.state = 482
                        self.match(MiniGoParser.IDENTIFIER)
                        self.state = 483
                        self.match(MiniGoParser.LB)
                        self.state = 485
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8108872141513949208) != 0):
                            self.state = 484
                            self.expr_list()


                        self.state = 487
                        self.match(MiniGoParser.RB)
                        pass

             
                self.state = 492
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        self.enterRule(localctx, 96, self.RULE_expr_list)
        try:
            self.state = 498
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.expr(0)
                self.state = 494
                self.match(MiniGoParser.COMMA)
                self.state = 495
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
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
        self.enterRule(localctx, 98, self.RULE_operand)
        try:
            self.state = 507
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 502
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 503
                self.match(MiniGoParser.LB)
                self.state = 504
                self.expr(0)
                self.state = 505
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
        self.enterRule(localctx, 100, self.RULE_stmt)
        try:
            self.state = 517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.decl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 510
                self.asm_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 511
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 512
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 513
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 514
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 515
                self.call_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 516
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


        def array_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_stmt




    def decl_stmt(self):

        localctx = MiniGoParser.Decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_decl_stmt)
        try:
            self.state = 522
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 519
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 521
                self.array_decl()
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

        def asm(self):
            return self.getTypedRuleContext(MiniGoParser.AsmContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_asm_stmt




    def asm_stmt(self):

        localctx = MiniGoParser.Asm_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_asm_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.asm()
            self.state = 525
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
        self.enterRule(localctx, 106, self.RULE_asm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.lhs()
            self.state = 528
            self.assign_ops()
            self.state = 529
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
        self.enterRule(localctx, 108, self.RULE_lhs)
        try:
            self.state = 534
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 532
                self.array_elem()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 533
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

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def many_index_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Many_index_opsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_elem




    def array_elem(self):

        localctx = MiniGoParser.Array_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_array_elem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 537
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
        self.enterRule(localctx, 112, self.RULE_many_index_ops)
        try:
            self.state = 543
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 539
                self.index_ops()
                self.state = 540
                self.many_index_ops()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 542
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

        def many_struct_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Many_struct_opsContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def array_elem(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elemContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_elem




    def struct_elem(self):

        localctx = MiniGoParser.Struct_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_struct_elem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 545
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 546
                self.array_elem()
                pass


            self.state = 549
            self.many_struct_ops()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_struct_opsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_opsContext,0)


        def many_struct_ops(self):
            return self.getTypedRuleContext(MiniGoParser.Many_struct_opsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_many_struct_ops




    def many_struct_ops(self):

        localctx = MiniGoParser.Many_struct_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_many_struct_ops)
        try:
            self.state = 555
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.struct_ops()
                self.state = 552
                self.many_struct_ops()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 554
                self.struct_ops()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_opsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def array_elem(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elemContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_ops




    def struct_ops(self):

        localctx = MiniGoParser.Struct_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_struct_ops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self.match(MiniGoParser.DOT)
            self.state = 560
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 558
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 559
                self.array_elem()
                pass


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
        self.enterRule(localctx, 120, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
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

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def many_else_if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Many_else_if_stmtContext,0)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.match(MiniGoParser.IF)
            self.state = 565
            self.match(MiniGoParser.LB)
            self.state = 566
            self.expr(0)
            self.state = 567
            self.match(MiniGoParser.RB)
            self.state = 568
            self.block()
            self.state = 570
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 569
                self.many_else_if_stmt()


            self.state = 574
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 572
                self.match(MiniGoParser.ELSE)
                self.state = 573
                self.block()


            self.state = 576
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_else_if_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_stmtContext,0)


        def many_else_if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Many_else_if_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_many_else_if_stmt




    def many_else_if_stmt(self):

        localctx = MiniGoParser.Many_else_if_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_many_else_if_stmt)
        try:
            self.state = 582
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 578
                self.else_if_stmt()
                self.state = 579
                self.many_else_if_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 581
                self.else_if_stmt()
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
        self.enterRule(localctx, 126, self.RULE_else_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            self.match(MiniGoParser.ELSE)
            self.state = 585
            self.match(MiniGoParser.IF)
            self.state = 586
            self.match(MiniGoParser.LB)
            self.state = 587
            self.expr(0)
            self.state = 588
            self.match(MiniGoParser.RB)
            self.state = 589
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

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def for_clause(self):
            return self.getTypedRuleContext(MiniGoParser.For_clauseContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.match(MiniGoParser.FOR)
            self.state = 592
            self.for_clause()
            self.state = 593
            self.block()
            self.state = 594
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
        self.enterRule(localctx, 130, self.RULE_for_clause)
        try:
            self.state = 599
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 596
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 597
                self.fully_clause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 598
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
            self.state = 601
            self.init()
            self.state = 602
            self.eos()
            self.state = 603
            self.expr(0)
            self.state = 604
            self.eos()
            self.state = 605
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
            self.state = 610
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 607
                self.asm_for()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 608
                self.decl_var_init()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 609
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
            self.state = 612
            self.match(MiniGoParser.VAR)
            self.state = 613
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 614
            self.primitive_type()
            self.state = 615
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 616
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
            self.state = 618
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
            self.state = 620
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 621
            self.assign_ops()
            self.state = 622
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
            self.state = 624
            _la = self._input.LA(1)
            if not(_la==2 or _la==62):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 625
            self.match(MiniGoParser.COMMA)
            self.state = 626
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 627
            self.match(MiniGoParser.ASSIGN)
            self.state = 628
            self.match(MiniGoParser.RANGE)
            self.state = 629
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
            self.state = 631
            self.match(MiniGoParser.BREAK)
            self.state = 632
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
            self.state = 634
            self.match(MiniGoParser.CONTINUE)
            self.state = 635
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


        def struct_elem_call(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elem_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_stmt




    def call_stmt(self):

        localctx = MiniGoParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 639
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 637
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 638
                self.struct_elem_call()
                pass


            self.state = 641
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_elem_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def array_elem(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elemContext,0)


        def many_struct_ops_call(self):
            return self.getTypedRuleContext(MiniGoParser.Many_struct_ops_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_elem_call




    def struct_elem_call(self):

        localctx = MiniGoParser.Struct_elem_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_struct_elem_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 643
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 644
                self.array_elem()
                pass


            self.state = 648
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 647
                self.many_struct_ops_call()


            self.state = 650
            self.match(MiniGoParser.DOT)
            self.state = 651
            self.func_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_struct_ops_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_ops_call(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_ops_callContext,0)


        def many_struct_ops_call(self):
            return self.getTypedRuleContext(MiniGoParser.Many_struct_ops_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_many_struct_ops_call




    def many_struct_ops_call(self):

        localctx = MiniGoParser.Many_struct_ops_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_many_struct_ops_call)
        try:
            self.state = 657
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 653
                self.struct_ops_call()
                self.state = 654
                self.many_struct_ops_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 656
                self.struct_ops_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_ops_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def array_elem(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elemContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_ops_call




    def struct_ops_call(self):

        localctx = MiniGoParser.Struct_ops_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_struct_ops_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 659
            self.match(MiniGoParser.DOT)
            self.state = 663
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 660
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 661
                self.array_elem()
                pass

            elif la_ == 3:
                self.state = 662
                self.func_call()
                pass


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
        self.enterRule(localctx, 156, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 665
            self.match(MiniGoParser.RETURN)
            self.state = 667
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8108872141513949208) != 0):
                self.state = 666
                self.expr(0)


            self.state = 669
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
        self.enterRule(localctx, 158, self.RULE_boolean_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 671
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
        self.enterRule(localctx, 160, self.RULE_arithmetic_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 673
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
        self.enterRule(localctx, 162, self.RULE_relational_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 675
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
        self.enterRule(localctx, 164, self.RULE_assign_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 677
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
        self.enterRule(localctx, 166, self.RULE_index_ops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 679
            self.match(MiniGoParser.LSB)
            self.state = 680
            self.expr(0)
            self.state = 681
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
        self.enterRule(localctx, 168, self.RULE_eos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 683
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
        self._predicates[41] = self.expr_sempred
        self._predicates[42] = self.expr1_sempred
        self._predicates[43] = self.expr2_sempred
        self._predicates[44] = self.expr3_sempred
        self._predicates[45] = self.expr4_sempred
        self._predicates[47] = self.primary_expr_sempred
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
         




