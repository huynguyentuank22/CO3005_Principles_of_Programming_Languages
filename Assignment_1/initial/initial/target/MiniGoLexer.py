# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


# Nguyen Tuan Huy - 2211253
# fix như tam, sua expression
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u0218\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\3\3\3\3\4\3\4\5\4")
        buf.write("\u00a8\n\4\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3")
        buf.write(")\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\38\58\u016d\n")
        buf.write("8\39\39\79\u0171\n9\f9\169\u0174\139\39\59\u0177\n9\3")
        buf.write(":\3:\3:\6:\u017c\n:\r:\16:\u017d\3;\3;\3;\6;\u0183\n;")
        buf.write("\r;\16;\u0184\3<\3<\3<\6<\u018a\n<\r<\16<\u018b\3=\3=")
        buf.write("\3>\3>\3?\3?\3@\3@\3@\3@\3@\3@\3@\5@\u019b\n@\3A\6A\u019e")
        buf.write("\nA\rA\16A\u019f\3B\3B\7B\u01a4\nB\fB\16B\u01a7\13B\3")
        buf.write("C\3C\5C\u01ab\nC\3C\6C\u01ae\nC\rC\16C\u01af\3D\3D\7D")
        buf.write("\u01b4\nD\fD\16D\u01b7\13D\3D\3D\3E\3E\5E\u01bd\nE\3F")
        buf.write("\3F\3F\3G\3G\3G\3H\3H\5H\u01c7\nH\3H\3H\3H\7H\u01cc\n")
        buf.write("H\fH\16H\u01cf\13H\3I\3I\3J\3J\3J\3J\7J\u01d7\nJ\fJ\16")
        buf.write("J\u01da\13J\3J\3J\3K\3K\3K\3K\3K\7K\u01e3\nK\fK\16K\u01e6")
        buf.write("\13K\3K\3K\3K\3K\3K\3L\6L\u01ee\nL\rL\16L\u01ef\3L\3L")
        buf.write("\3M\6M\u01f5\nM\rM\16M\u01f6\3M\3M\3N\3N\3N\3O\3O\7O\u0200")
        buf.write("\nO\fO\16O\u0203\13O\3O\3O\3O\3P\3P\7P\u020a\nP\fP\16")
        buf.write("P\u020d\13P\3P\6P\u0210\nP\rP\16P\u0211\3P\5P\u0215\n")
        buf.write("P\3P\3P\3\u01e4\2Q\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g")
        buf.write("\65i\66k\67m8o9q:s;u<w=y\2{\2}\2\177>\u0081\2\u0083\2")
        buf.write("\u0085\2\u0087?\u0089\2\u008b\2\u008d\2\u008f@\u0091\2")
        buf.write("\u0093A\u0095B\u0097C\u0099D\u009bE\u009dF\u009fG\3\2")
        buf.write("\21\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;")
        buf.write("CHch\3\2\62;\3\2\63;\4\2C\\c|\4\2GGgg\4\2--//\6\2\f\f")
        buf.write("\17\17$$^^\7\2$$^^ppttvv\4\2\f\f\17\17\5\2\13\13\16\17")
        buf.write("\"\"\2\u022a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0087\3\2\2\2\2\u008f\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\3\u00a1")
        buf.write("\3\2\2\2\5\u00a3\3\2\2\2\7\u00a7\3\2\2\2\t\u00a9\3\2\2")
        buf.write("\2\13\u00ab\3\2\2\2\r\u00ae\3\2\2\2\17\u00b3\3\2\2\2\21")
        buf.write("\u00b7\3\2\2\2\23\u00be\3\2\2\2\25\u00c3\3\2\2\2\27\u00c8")
        buf.write("\3\2\2\2\31\u00cf\3\2\2\2\33\u00d9\3\2\2\2\35\u00e0\3")
        buf.write("\2\2\2\37\u00e4\3\2\2\2!\u00ea\3\2\2\2#\u00f2\3\2\2\2")
        buf.write("%\u00f8\3\2\2\2\'\u00fc\3\2\2\2)\u0105\3\2\2\2+\u010b")
        buf.write("\3\2\2\2-\u0111\3\2\2\2/\u0115\3\2\2\2\61\u011a\3\2\2")
        buf.write("\2\63\u0120\3\2\2\2\65\u0122\3\2\2\2\67\u0124\3\2\2\2")
        buf.write("9\u0126\3\2\2\2;\u0128\3\2\2\2=\u012a\3\2\2\2?\u012d\3")
        buf.write("\2\2\2A\u0130\3\2\2\2C\u0132\3\2\2\2E\u0135\3\2\2\2G\u0137")
        buf.write("\3\2\2\2I\u013a\3\2\2\2K\u013d\3\2\2\2M\u0140\3\2\2\2")
        buf.write("O\u0142\3\2\2\2Q\u0144\3\2\2\2S\u0147\3\2\2\2U\u014a\3")
        buf.write("\2\2\2W\u014d\3\2\2\2Y\u0150\3\2\2\2[\u0153\3\2\2\2]\u0156")
        buf.write("\3\2\2\2_\u0158\3\2\2\2a\u015a\3\2\2\2c\u015c\3\2\2\2")
        buf.write("e\u015e\3\2\2\2g\u0160\3\2\2\2i\u0162\3\2\2\2k\u0164\3")
        buf.write("\2\2\2m\u0166\3\2\2\2o\u016c\3\2\2\2q\u0176\3\2\2\2s\u0178")
        buf.write("\3\2\2\2u\u017f\3\2\2\2w\u0186\3\2\2\2y\u018d\3\2\2\2")
        buf.write("{\u018f\3\2\2\2}\u0191\3\2\2\2\177\u019a\3\2\2\2\u0081")
        buf.write("\u019d\3\2\2\2\u0083\u01a1\3\2\2\2\u0085\u01a8\3\2\2\2")
        buf.write("\u0087\u01b1\3\2\2\2\u0089\u01bc\3\2\2\2\u008b\u01be\3")
        buf.write("\2\2\2\u008d\u01c1\3\2\2\2\u008f\u01c6\3\2\2\2\u0091\u01d0")
        buf.write("\3\2\2\2\u0093\u01d2\3\2\2\2\u0095\u01dd\3\2\2\2\u0097")
        buf.write("\u01ed\3\2\2\2\u0099\u01f4\3\2\2\2\u009b\u01fa\3\2\2\2")
        buf.write("\u009d\u01fd\3\2\2\2\u009f\u0207\3\2\2\2\u00a1\u00a2\7")
        buf.write("<\2\2\u00a2\4\3\2\2\2\u00a3\u00a4\7a\2\2\u00a4\6\3\2\2")
        buf.write("\2\u00a5\u00a8\5/\30\2\u00a6\u00a8\5\61\31\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\b\3\2\2\2\u00a9\u00aa")
        buf.write("\5-\27\2\u00aa\n\3\2\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad")
        buf.write("\7h\2\2\u00ad\f\3\2\2\2\u00ae\u00af\7g\2\2\u00af\u00b0")
        buf.write("\7n\2\2\u00b0\u00b1\7u\2\2\u00b1\u00b2\7g\2\2\u00b2\16")
        buf.write("\3\2\2\2\u00b3\u00b4\7h\2\2\u00b4\u00b5\7q\2\2\u00b5\u00b6")
        buf.write("\7t\2\2\u00b6\20\3\2\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9")
        buf.write("\7g\2\2\u00b9\u00ba\7v\2\2\u00ba\u00bb\7w\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\u00bd\7p\2\2\u00bd\22\3\2\2\2\u00be\u00bf")
        buf.write("\7h\2\2\u00bf\u00c0\7w\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2")
        buf.write("\7e\2\2\u00c2\24\3\2\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5")
        buf.write("\7{\2\2\u00c5\u00c6\7r\2\2\u00c6\u00c7\7g\2\2\u00c7\26")
        buf.write("\3\2\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb")
        buf.write("\7t\2\2\u00cb\u00cc\7w\2\2\u00cc\u00cd\7e\2\2\u00cd\u00ce")
        buf.write("\7v\2\2\u00ce\30\3\2\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4")
        buf.write("\7t\2\2\u00d4\u00d5\7h\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7")
        buf.write("\7e\2\2\u00d7\u00d8\7g\2\2\u00d8\32\3\2\2\2\u00d9\u00da")
        buf.write("\7u\2\2\u00da\u00db\7v\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd")
        buf.write("\7k\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7i\2\2\u00df\34")
        buf.write("\3\2\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3")
        buf.write("\7v\2\2\u00e3\36\3\2\2\2\u00e4\u00e5\7h\2\2\u00e5\u00e6")
        buf.write("\7n\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9")
        buf.write("\7v\2\2\u00e9 \3\2\2\2\u00ea\u00eb\7d\2\2\u00eb\u00ec")
        buf.write("\7q\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef")
        buf.write("\7g\2\2\u00ef\u00f0\7c\2\2\u00f0\u00f1\7p\2\2\u00f1\"")
        buf.write("\3\2\2\2\u00f2\u00f3\7e\2\2\u00f3\u00f4\7q\2\2\u00f4\u00f5")
        buf.write("\7p\2\2\u00f5\u00f6\7u\2\2\u00f6\u00f7\7v\2\2\u00f7$\3")
        buf.write("\2\2\2\u00f8\u00f9\7x\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb")
        buf.write("\7t\2\2\u00fb&\3\2\2\2\u00fc\u00fd\7e\2\2\u00fd\u00fe")
        buf.write("\7q\2\2\u00fe\u00ff\7p\2\2\u00ff\u0100\7v\2\2\u0100\u0101")
        buf.write("\7k\2\2\u0101\u0102\7p\2\2\u0102\u0103\7w\2\2\u0103\u0104")
        buf.write("\7g\2\2\u0104(\3\2\2\2\u0105\u0106\7d\2\2\u0106\u0107")
        buf.write("\7t\2\2\u0107\u0108\7g\2\2\u0108\u0109\7c\2\2\u0109\u010a")
        buf.write("\7m\2\2\u010a*\3\2\2\2\u010b\u010c\7t\2\2\u010c\u010d")
        buf.write("\7c\2\2\u010d\u010e\7p\2\2\u010e\u010f\7i\2\2\u010f\u0110")
        buf.write("\7g\2\2\u0110,\3\2\2\2\u0111\u0112\7p\2\2\u0112\u0113")
        buf.write("\7k\2\2\u0113\u0114\7n\2\2\u0114.\3\2\2\2\u0115\u0116")
        buf.write("\7v\2\2\u0116\u0117\7t\2\2\u0117\u0118\7w\2\2\u0118\u0119")
        buf.write("\7g\2\2\u0119\60\3\2\2\2\u011a\u011b\7h\2\2\u011b\u011c")
        buf.write("\7c\2\2\u011c\u011d\7n\2\2\u011d\u011e\7u\2\2\u011e\u011f")
        buf.write("\7g\2\2\u011f\62\3\2\2\2\u0120\u0121\7-\2\2\u0121\64\3")
        buf.write("\2\2\2\u0122\u0123\7/\2\2\u0123\66\3\2\2\2\u0124\u0125")
        buf.write("\7,\2\2\u01258\3\2\2\2\u0126\u0127\7\61\2\2\u0127:\3\2")
        buf.write("\2\2\u0128\u0129\7\'\2\2\u0129<\3\2\2\2\u012a\u012b\7")
        buf.write("?\2\2\u012b\u012c\7?\2\2\u012c>\3\2\2\2\u012d\u012e\7")
        buf.write("#\2\2\u012e\u012f\7?\2\2\u012f@\3\2\2\2\u0130\u0131\7")
        buf.write(">\2\2\u0131B\3\2\2\2\u0132\u0133\7>\2\2\u0133\u0134\7")
        buf.write("?\2\2\u0134D\3\2\2\2\u0135\u0136\7@\2\2\u0136F\3\2\2\2")
        buf.write("\u0137\u0138\7@\2\2\u0138\u0139\7?\2\2\u0139H\3\2\2\2")
        buf.write("\u013a\u013b\7(\2\2\u013b\u013c\7(\2\2\u013cJ\3\2\2\2")
        buf.write("\u013d\u013e\7~\2\2\u013e\u013f\7~\2\2\u013fL\3\2\2\2")
        buf.write("\u0140\u0141\7#\2\2\u0141N\3\2\2\2\u0142\u0143\7?\2\2")
        buf.write("\u0143P\3\2\2\2\u0144\u0145\7<\2\2\u0145\u0146\7?\2\2")
        buf.write("\u0146R\3\2\2\2\u0147\u0148\7-\2\2\u0148\u0149\7?\2\2")
        buf.write("\u0149T\3\2\2\2\u014a\u014b\7/\2\2\u014b\u014c\7?\2\2")
        buf.write("\u014cV\3\2\2\2\u014d\u014e\7,\2\2\u014e\u014f\7?\2\2")
        buf.write("\u014fX\3\2\2\2\u0150\u0151\7\61\2\2\u0151\u0152\7?\2")
        buf.write("\2\u0152Z\3\2\2\2\u0153\u0154\7\'\2\2\u0154\u0155\7?\2")
        buf.write("\2\u0155\\\3\2\2\2\u0156\u0157\7\60\2\2\u0157^\3\2\2\2")
        buf.write("\u0158\u0159\7*\2\2\u0159`\3\2\2\2\u015a\u015b\7+\2\2")
        buf.write("\u015bb\3\2\2\2\u015c\u015d\7}\2\2\u015dd\3\2\2\2\u015e")
        buf.write("\u015f\7\177\2\2\u015ff\3\2\2\2\u0160\u0161\7]\2\2\u0161")
        buf.write("h\3\2\2\2\u0162\u0163\7_\2\2\u0163j\3\2\2\2\u0164\u0165")
        buf.write("\7.\2\2\u0165l\3\2\2\2\u0166\u0167\7=\2\2\u0167n\3\2\2")
        buf.write("\2\u0168\u016d\5q9\2\u0169\u016d\5s:\2\u016a\u016d\5u")
        buf.write(";\2\u016b\u016d\5w<\2\u016c\u0168\3\2\2\2\u016c\u0169")
        buf.write("\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016b\3\2\2\2\u016d")
        buf.write("p\3\2\2\2\u016e\u0172\5{>\2\u016f\u0171\5y=\2\u0170\u016f")
        buf.write("\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0172")
        buf.write("\u0173\3\2\2\2\u0173\u0177\3\2\2\2\u0174\u0172\3\2\2\2")
        buf.write("\u0175\u0177\7\62\2\2\u0176\u016e\3\2\2\2\u0176\u0175")
        buf.write("\3\2\2\2\u0177r\3\2\2\2\u0178\u0179\7\62\2\2\u0179\u017b")
        buf.write("\t\2\2\2\u017a\u017c\t\3\2\2\u017b\u017a\3\2\2\2\u017c")
        buf.write("\u017d\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017et\3\2\2\2\u017f\u0180\7\62\2\2\u0180\u0182\t\4\2")
        buf.write("\2\u0181\u0183\t\5\2\2\u0182\u0181\3\2\2\2\u0183\u0184")
        buf.write("\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185")
        buf.write("v\3\2\2\2\u0186\u0187\7\62\2\2\u0187\u0189\t\6\2\2\u0188")
        buf.write("\u018a\t\7\2\2\u0189\u0188\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write("\u018b\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018cx\3\2\2")
        buf.write("\2\u018d\u018e\t\b\2\2\u018ez\3\2\2\2\u018f\u0190\t\t")
        buf.write("\2\2\u0190|\3\2\2\2\u0191\u0192\t\n\2\2\u0192~\3\2\2\2")
        buf.write("\u0193\u0194\5\u0081A\2\u0194\u0195\5\u0083B\2\u0195\u019b")
        buf.write("\3\2\2\2\u0196\u0197\5\u0081A\2\u0197\u0198\5\u0083B\2")
        buf.write("\u0198\u0199\5\u0085C\2\u0199\u019b\3\2\2\2\u019a\u0193")
        buf.write("\3\2\2\2\u019a\u0196\3\2\2\2\u019b\u0080\3\2\2\2\u019c")
        buf.write("\u019e\5y=\2\u019d\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f")
        buf.write("\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u0082\3\2\2\2")
        buf.write("\u01a1\u01a5\7\60\2\2\u01a2\u01a4\5y=\2\u01a3\u01a2\3")
        buf.write("\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6")
        buf.write("\3\2\2\2\u01a6\u0084\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8")
        buf.write("\u01aa\t\13\2\2\u01a9\u01ab\t\f\2\2\u01aa\u01a9\3\2\2")
        buf.write("\2\u01aa\u01ab\3\2\2\2\u01ab\u01ad\3\2\2\2\u01ac\u01ae")
        buf.write("\5y=\2\u01ad\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u0086\3\2\2\2\u01b1")
        buf.write("\u01b5\7$\2\2\u01b2\u01b4\5\u0089E\2\u01b3\u01b2\3\2\2")
        buf.write("\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6")
        buf.write("\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8")
        buf.write("\u01b9\7$\2\2\u01b9\u0088\3\2\2\2\u01ba\u01bd\5\u008b")
        buf.write("F\2\u01bb\u01bd\n\r\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bb")
        buf.write("\3\2\2\2\u01bd\u008a\3\2\2\2\u01be\u01bf\7^\2\2\u01bf")
        buf.write("\u01c0\t\16\2\2\u01c0\u008c\3\2\2\2\u01c1\u01c2\7^\2\2")
        buf.write("\u01c2\u01c3\n\16\2\2\u01c3\u008e\3\2\2\2\u01c4\u01c7")
        buf.write("\5}?\2\u01c5\u01c7\5\u0091I\2\u01c6\u01c4\3\2\2\2\u01c6")
        buf.write("\u01c5\3\2\2\2\u01c7\u01cd\3\2\2\2\u01c8\u01cc\5}?\2\u01c9")
        buf.write("\u01cc\5\u0091I\2\u01ca\u01cc\5y=\2\u01cb\u01c8\3\2\2")
        buf.write("\2\u01cb\u01c9\3\2\2\2\u01cb\u01ca\3\2\2\2\u01cc\u01cf")
        buf.write("\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce")
        buf.write("\u0090\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01d1\7a\2\2")
        buf.write("\u01d1\u0092\3\2\2\2\u01d2\u01d3\7\61\2\2\u01d3\u01d4")
        buf.write("\7\61\2\2\u01d4\u01d8\3\2\2\2\u01d5\u01d7\n\17\2\2\u01d6")
        buf.write("\u01d5\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2")
        buf.write("\u01d8\u01d9\3\2\2\2\u01d9\u01db\3\2\2\2\u01da\u01d8\3")
        buf.write("\2\2\2\u01db\u01dc\bJ\2\2\u01dc\u0094\3\2\2\2\u01dd\u01de")
        buf.write("\7\61\2\2\u01de\u01df\7,\2\2\u01df\u01e4\3\2\2\2\u01e0")
        buf.write("\u01e3\5\u0095K\2\u01e1\u01e3\13\2\2\2\u01e2\u01e0\3\2")
        buf.write("\2\2\u01e2\u01e1\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4\u01e5")
        buf.write("\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5\u01e7\3\2\2\2\u01e6")
        buf.write("\u01e4\3\2\2\2\u01e7\u01e8\7,\2\2\u01e8\u01e9\7\61\2\2")
        buf.write("\u01e9\u01ea\3\2\2\2\u01ea\u01eb\bK\2\2\u01eb\u0096\3")
        buf.write("\2\2\2\u01ec\u01ee\t\20\2\2\u01ed\u01ec\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2")
        buf.write("\u01f0\u01f1\3\2\2\2\u01f1\u01f2\bL\2\2\u01f2\u0098\3")
        buf.write("\2\2\2\u01f3\u01f5\t\17\2\2\u01f4\u01f3\3\2\2\2\u01f5")
        buf.write("\u01f6\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2")
        buf.write("\u01f7\u01f8\3\2\2\2\u01f8\u01f9\bM\3\2\u01f9\u009a\3")
        buf.write("\2\2\2\u01fa\u01fb\13\2\2\2\u01fb\u01fc\bN\4\2\u01fc\u009c")
        buf.write("\3\2\2\2\u01fd\u0201\7$\2\2\u01fe\u0200\5\u0089E\2\u01ff")
        buf.write("\u01fe\3\2\2\2\u0200\u0203\3\2\2\2\u0201\u01ff\3\2\2\2")
        buf.write("\u0201\u0202\3\2\2\2\u0202\u0204\3\2\2\2\u0203\u0201\3")
        buf.write("\2\2\2\u0204\u0205\5\u008dG\2\u0205\u0206\bO\5\2\u0206")
        buf.write("\u009e\3\2\2\2\u0207\u020b\7$\2\2\u0208\u020a\5\u0089")
        buf.write("E\2\u0209\u0208\3\2\2\2\u020a\u020d\3\2\2\2\u020b\u0209")
        buf.write("\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u0214\3\2\2\2\u020d")
        buf.write("\u020b\3\2\2\2\u020e\u0210\t\17\2\2\u020f\u020e\3\2\2")
        buf.write("\2\u0210\u0211\3\2\2\2\u0211\u020f\3\2\2\2\u0211\u0212")
        buf.write("\3\2\2\2\u0212\u0215\3\2\2\2\u0213\u0215\7\2\2\3\u0214")
        buf.write("\u020f\3\2\2\2\u0214\u0213\3\2\2\2\u0215\u0216\3\2\2\2")
        buf.write("\u0216\u0217\bP\6\2\u0217\u00a0\3\2\2\2\35\2\u00a7\u016c")
        buf.write("\u0172\u0176\u017d\u0184\u018b\u019a\u019f\u01a5\u01aa")
        buf.write("\u01af\u01b5\u01bc\u01c6\u01cb\u01cd\u01d8\u01e2\u01e4")
        buf.write("\u01ef\u01f6\u0201\u020b\u0211\u0214\7\b\2\2\3M\2\3N\3")
        buf.write("\3O\4\3P\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    BOOLEAN_LITERAL = 3
    NIL_LITERAL = 4
    IF = 5
    ELSE = 6
    FOR = 7
    RETURN = 8
    FUNC = 9
    TYPE = 10
    STRUCT = 11
    INTERFACE = 12
    STRING = 13
    INT = 14
    FLOAT = 15
    BOOLEAN = 16
    CONST = 17
    VAR = 18
    CONTINUE = 19
    BREAK = 20
    RANGE = 21
    NIL = 22
    TRUE = 23
    FALSE = 24
    ADD = 25
    SUB = 26
    MUL = 27
    DIV = 28
    MOD = 29
    EQ = 30
    NEQ = 31
    LT = 32
    LE = 33
    GT = 34
    GE = 35
    AND = 36
    OR = 37
    NOT = 38
    DECLARE_ASSIGN = 39
    ASSIGN = 40
    PLUS_ASSIGN = 41
    MINUS_ASSIGN = 42
    MULT_ASSIGN = 43
    DIV_ASSIGN = 44
    MOD_ASSIGN = 45
    DOT = 46
    LB = 47
    RB = 48
    LCB = 49
    RCB = 50
    LSB = 51
    RSB = 52
    COMMA = 53
    SEMICOLON = 54
    INT_LITERAL = 55
    DECIMAL_LITERAL = 56
    BINARY_LITERAL = 57
    OCTAL_LITERAL = 58
    HEX_LITERAL = 59
    FLOAT_LITERAL = 60
    STRING_LITERAL = 61
    IDENTIFIER = 62
    LINE_COMMENT = 63
    COMMENT = 64
    WS = 65
    EOS = 66
    ERROR_CHAR = 67
    ILLEGAL_ESCAPE = 68
    UNCLOSE_STRING = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'_'", "'if'", "'else'", "'for'", "'return'", "'func'", 
            "'type'", "'struct'", "'interface'", "'string'", "'int'", "'float'", 
            "'boolean'", "'const'", "'var'", "'continue'", "'break'", "'range'", 
            "'nil'", "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
            "'!'", "'='", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", 
            "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEAN_LITERAL", "NIL_LITERAL", "IF", "ELSE", "FOR", "RETURN", 
            "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
            "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", 
            "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", 
            "LT", "LE", "GT", "GE", "AND", "OR", "NOT", "DECLARE_ASSIGN", 
            "ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", 
            "MOD_ASSIGN", "DOT", "LB", "RB", "LCB", "RCB", "LSB", "RSB", 
            "COMMA", "SEMICOLON", "INT_LITERAL", "DECIMAL_LITERAL", "BINARY_LITERAL", 
            "OCTAL_LITERAL", "HEX_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
            "IDENTIFIER", "LINE_COMMENT", "COMMENT", "WS", "EOS", "ERROR_CHAR", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "BOOLEAN_LITERAL", "NIL_LITERAL", "IF", 
                  "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
                  "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
                  "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", "LE", "GT", "GE", 
                  "AND", "OR", "NOT", "DECLARE_ASSIGN", "ASSIGN", "PLUS_ASSIGN", 
                  "MINUS_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                  "DOT", "LB", "RB", "LCB", "RCB", "LSB", "RSB", "COMMA", 
                  "SEMICOLON", "INT_LITERAL", "DECIMAL_LITERAL", "BINARY_LITERAL", 
                  "OCTAL_LITERAL", "HEX_LITERAL", "DIGIT", "NONZERO_DIGIT", 
                  "LETTER", "FLOAT_LITERAL", "INT_PART", "DEC_PART", "EXP_PART", 
                  "STRING_LITERAL", "CHAR", "ESC", "INVALID_ESC", "IDENTIFIER", 
                  "UNDERSCORE", "LINE_COMMENT", "COMMENT", "WS", "EOS", 
                  "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def __init__(self, input):
        super().__init__(input)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
        self.prev_token = None

    def check_EOS(self):
        if not self.prev_token:
            return False
        tokens = [
            self.IDENTIFIER,
            self.INT_LITERAL, self.FLOAT_LITERAL, self.STRING_LITERAL, self.BOOLEAN_LITERAL, self.NIL_LITERAL,
            self.INT, self.FLOAT, self.STRING, self.BOOLEAN,
            self.RETURN, self.BREAK, self.CONTINUE,
            self.RB, self.RCB, self.RSB
        ]
        return self.prev_token.type in tokens

    def emit(self):
        tk = self.type
        token = super().emit()
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        elif tk != '\n':
            self.prev_token = token
        return token


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[75] = self.EOS_action 
            actions[76] = self.ERROR_CHAR_action 
            actions[77] = self.ILLEGAL_ESCAPE_action 
            actions[78] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def EOS_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                if self.check_EOS():
                    self.text = ';'
                else:
                    self.skip()

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             raise IllegalEscape(self.text) 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                ESC = ['\r', '\n']
                text = str(self.text)
                while text[-1] in ESC:
                    text = text[:-1]
                raise UncloseString(text[:])

     


