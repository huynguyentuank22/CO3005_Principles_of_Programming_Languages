# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u020d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u00a6")
        buf.write("\n\3\f\3\16\3\u00a9\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\7")
        buf.write("\4\u00b2\n\4\f\4\16\4\u00b5\13\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3")
        buf.write("$\3$\3$\3%\3%\3%\3&\3&\3\'\5\'\u0154\n\'\3\'\3\'\3(\3")
        buf.write("(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\3\67\3\67\5\67\u017f\n")
        buf.write("\67\38\38\39\39\39\69\u0186\n9\r9\169\u0187\3:\3:\3:\6")
        buf.write(":\u018d\n:\r:\16:\u018e\3;\3;\3;\6;\u0194\n;\r;\16;\u0195")
        buf.write("\3<\3<\3=\3=\3>\3>\3?\3?\3?\3?\3?\5?\u01a3\n?\3?\3?\5")
        buf.write("?\u01a7\n?\3@\3@\7@\u01ab\n@\f@\16@\u01ae\13@\3@\5@\u01b1")
        buf.write("\n@\3A\3A\7A\u01b5\nA\fA\16A\u01b8\13A\3B\3B\5B\u01bc")
        buf.write("\nB\3B\6B\u01bf\nB\rB\16B\u01c0\3C\3C\7C\u01c5\nC\fC\16")
        buf.write("C\u01c8\13C\3C\3C\3D\3D\5D\u01ce\nD\3E\3E\3E\3F\3F\3F")
        buf.write("\3G\3G\5G\u01d8\nG\3H\3H\3I\3I\5I\u01de\nI\3I\3I\3I\7")
        buf.write("I\u01e3\nI\fI\16I\u01e6\13I\3J\3J\3K\3K\3K\3K\3L\6L\u01ef")
        buf.write("\nL\rL\16L\u01f0\3L\3L\3M\3M\3M\3N\3N\7N\u01fa\nN\fN\16")
        buf.write("N\u01fd\13N\3N\3N\3N\3O\3O\7O\u0204\nO\fO\16O\u0207\13")
        buf.write("O\3O\5O\u020a\nO\3O\3O\3\u00b3\2P\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w\2y\2{\2}=\177\2\u0081")
        buf.write("\2\u0083\2\u0085>\u0087\2\u0089\2\u008b\2\u008d?\u008f")
        buf.write("@\u0091A\u0093\2\u0095B\u0097C\u0099D\u009bE\u009dF\3")
        buf.write("\2\22\4\2\f\f\17\17\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629")
        buf.write("\4\2ZZzz\5\2\62;CHch\3\2\62;\3\2\63;\4\2C\\c|\4\2GGgg")
        buf.write("\4\2--//\6\2\f\f\17\17$$^^\7\2$$^^ppttvv\5\2\13\f\16\17")
        buf.write("\"\"\4\3\f\f\17\17\2\u021d\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\u0085\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\3\u009f")
        buf.write("\3\2\2\2\5\u00a1\3\2\2\2\7\u00ac\3\2\2\2\t\u00bb\3\2\2")
        buf.write("\2\13\u00be\3\2\2\2\r\u00c3\3\2\2\2\17\u00c7\3\2\2\2\21")
        buf.write("\u00ce\3\2\2\2\23\u00d3\3\2\2\2\25\u00d8\3\2\2\2\27\u00df")
        buf.write("\3\2\2\2\31\u00e9\3\2\2\2\33\u00f0\3\2\2\2\35\u00f4\3")
        buf.write("\2\2\2\37\u00fa\3\2\2\2!\u0102\3\2\2\2#\u0108\3\2\2\2")
        buf.write("%\u010c\3\2\2\2\'\u0115\3\2\2\2)\u011b\3\2\2\2+\u0121")
        buf.write("\3\2\2\2-\u0125\3\2\2\2/\u012a\3\2\2\2\61\u0130\3\2\2")
        buf.write("\2\63\u0132\3\2\2\2\65\u0134\3\2\2\2\67\u0136\3\2\2\2")
        buf.write("9\u0138\3\2\2\2;\u013a\3\2\2\2=\u013d\3\2\2\2?\u0140\3")
        buf.write("\2\2\2A\u0142\3\2\2\2C\u0145\3\2\2\2E\u0147\3\2\2\2G\u014a")
        buf.write("\3\2\2\2I\u014d\3\2\2\2K\u0150\3\2\2\2M\u0153\3\2\2\2")
        buf.write("O\u0157\3\2\2\2Q\u015a\3\2\2\2S\u015d\3\2\2\2U\u0160\3")
        buf.write("\2\2\2W\u0163\3\2\2\2Y\u0166\3\2\2\2[\u0168\3\2\2\2]\u016a")
        buf.write("\3\2\2\2_\u016c\3\2\2\2a\u016e\3\2\2\2c\u0170\3\2\2\2")
        buf.write("e\u0172\3\2\2\2g\u0174\3\2\2\2i\u0176\3\2\2\2k\u0178\3")
        buf.write("\2\2\2m\u017e\3\2\2\2o\u0180\3\2\2\2q\u0182\3\2\2\2s\u0189")
        buf.write("\3\2\2\2u\u0190\3\2\2\2w\u0197\3\2\2\2y\u0199\3\2\2\2")
        buf.write("{\u019b\3\2\2\2}\u01a6\3\2\2\2\177\u01b0\3\2\2\2\u0081")
        buf.write("\u01b2\3\2\2\2\u0083\u01b9\3\2\2\2\u0085\u01c2\3\2\2\2")
        buf.write("\u0087\u01cd\3\2\2\2\u0089\u01cf\3\2\2\2\u008b\u01d2\3")
        buf.write("\2\2\2\u008d\u01d7\3\2\2\2\u008f\u01d9\3\2\2\2\u0091\u01dd")
        buf.write("\3\2\2\2\u0093\u01e7\3\2\2\2\u0095\u01e9\3\2\2\2\u0097")
        buf.write("\u01ee\3\2\2\2\u0099\u01f4\3\2\2\2\u009b\u01f7\3\2\2\2")
        buf.write("\u009d\u0201\3\2\2\2\u009f\u00a0\7a\2\2\u00a0\4\3\2\2")
        buf.write("\2\u00a1\u00a2\7\61\2\2\u00a2\u00a3\7\61\2\2\u00a3\u00a7")
        buf.write("\3\2\2\2\u00a4\u00a6\n\2\2\2\u00a5\u00a4\3\2\2\2\u00a6")
        buf.write("\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2")
        buf.write("\u00a8\u00aa\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ab\b")
        buf.write("\3\2\2\u00ab\6\3\2\2\2\u00ac\u00ad\7\61\2\2\u00ad\u00ae")
        buf.write("\7,\2\2\u00ae\u00b3\3\2\2\2\u00af\u00b2\5\7\4\2\u00b0")
        buf.write("\u00b2\13\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2")
        buf.write("\2\u00b2\u00b5\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b3\u00b1")
        buf.write("\3\2\2\2\u00b4\u00b6\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6")
        buf.write("\u00b7\7,\2\2\u00b7\u00b8\7\61\2\2\u00b8\u00b9\3\2\2\2")
        buf.write("\u00b9\u00ba\b\4\2\2\u00ba\b\3\2\2\2\u00bb\u00bc\7k\2")
        buf.write("\2\u00bc\u00bd\7h\2\2\u00bd\n\3\2\2\2\u00be\u00bf\7g\2")
        buf.write("\2\u00bf\u00c0\7n\2\2\u00c0\u00c1\7u\2\2\u00c1\u00c2\7")
        buf.write("g\2\2\u00c2\f\3\2\2\2\u00c3\u00c4\7h\2\2\u00c4\u00c5\7")
        buf.write("q\2\2\u00c5\u00c6\7t\2\2\u00c6\16\3\2\2\2\u00c7\u00c8")
        buf.write("\7t\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb")
        buf.write("\7w\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd\7p\2\2\u00cd\20")
        buf.write("\3\2\2\2\u00ce\u00cf\7h\2\2\u00cf\u00d0\7w\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\u00d2\7e\2\2\u00d2\22\3\2\2\2\u00d3\u00d4")
        buf.write("\7v\2\2\u00d4\u00d5\7{\2\2\u00d5\u00d6\7r\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7\24\3\2\2\2\u00d8\u00d9\7u\2\2\u00d9\u00da")
        buf.write("\7v\2\2\u00da\u00db\7t\2\2\u00db\u00dc\7w\2\2\u00dc\u00dd")
        buf.write("\7e\2\2\u00dd\u00de\7v\2\2\u00de\26\3\2\2\2\u00df\u00e0")
        buf.write("\7k\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3")
        buf.write("\7g\2\2\u00e3\u00e4\7t\2\2\u00e4\u00e5\7h\2\2\u00e5\u00e6")
        buf.write("\7c\2\2\u00e6\u00e7\7e\2\2\u00e7\u00e8\7g\2\2\u00e8\30")
        buf.write("\3\2\2\2\u00e9\u00ea\7u\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec")
        buf.write("\7t\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef")
        buf.write("\7i\2\2\u00ef\32\3\2\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2")
        buf.write("\7p\2\2\u00f2\u00f3\7v\2\2\u00f3\34\3\2\2\2\u00f4\u00f5")
        buf.write("\7h\2\2\u00f5\u00f6\7n\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8")
        buf.write("\7c\2\2\u00f8\u00f9\7v\2\2\u00f9\36\3\2\2\2\u00fa\u00fb")
        buf.write("\7d\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe")
        buf.write("\7n\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100\7c\2\2\u0100\u0101")
        buf.write("\7p\2\2\u0101 \3\2\2\2\u0102\u0103\7e\2\2\u0103\u0104")
        buf.write("\7q\2\2\u0104\u0105\7p\2\2\u0105\u0106\7u\2\2\u0106\u0107")
        buf.write("\7v\2\2\u0107\"\3\2\2\2\u0108\u0109\7x\2\2\u0109\u010a")
        buf.write("\7c\2\2\u010a\u010b\7t\2\2\u010b$\3\2\2\2\u010c\u010d")
        buf.write("\7e\2\2\u010d\u010e\7q\2\2\u010e\u010f\7p\2\2\u010f\u0110")
        buf.write("\7v\2\2\u0110\u0111\7k\2\2\u0111\u0112\7p\2\2\u0112\u0113")
        buf.write("\7w\2\2\u0113\u0114\7g\2\2\u0114&\3\2\2\2\u0115\u0116")
        buf.write("\7d\2\2\u0116\u0117\7t\2\2\u0117\u0118\7g\2\2\u0118\u0119")
        buf.write("\7c\2\2\u0119\u011a\7m\2\2\u011a(\3\2\2\2\u011b\u011c")
        buf.write("\7t\2\2\u011c\u011d\7c\2\2\u011d\u011e\7p\2\2\u011e\u011f")
        buf.write("\7i\2\2\u011f\u0120\7g\2\2\u0120*\3\2\2\2\u0121\u0122")
        buf.write("\7p\2\2\u0122\u0123\7k\2\2\u0123\u0124\7n\2\2\u0124,\3")
        buf.write("\2\2\2\u0125\u0126\7v\2\2\u0126\u0127\7t\2\2\u0127\u0128")
        buf.write("\7w\2\2\u0128\u0129\7g\2\2\u0129.\3\2\2\2\u012a\u012b")
        buf.write("\7h\2\2\u012b\u012c\7c\2\2\u012c\u012d\7n\2\2\u012d\u012e")
        buf.write("\7u\2\2\u012e\u012f\7g\2\2\u012f\60\3\2\2\2\u0130\u0131")
        buf.write("\7-\2\2\u0131\62\3\2\2\2\u0132\u0133\7/\2\2\u0133\64\3")
        buf.write("\2\2\2\u0134\u0135\7,\2\2\u0135\66\3\2\2\2\u0136\u0137")
        buf.write("\7\61\2\2\u01378\3\2\2\2\u0138\u0139\7\'\2\2\u0139:\3")
        buf.write("\2\2\2\u013a\u013b\7?\2\2\u013b\u013c\7?\2\2\u013c<\3")
        buf.write("\2\2\2\u013d\u013e\7#\2\2\u013e\u013f\7?\2\2\u013f>\3")
        buf.write("\2\2\2\u0140\u0141\7>\2\2\u0141@\3\2\2\2\u0142\u0143\7")
        buf.write(">\2\2\u0143\u0144\7?\2\2\u0144B\3\2\2\2\u0145\u0146\7")
        buf.write("@\2\2\u0146D\3\2\2\2\u0147\u0148\7@\2\2\u0148\u0149\7")
        buf.write("?\2\2\u0149F\3\2\2\2\u014a\u014b\7(\2\2\u014b\u014c\7")
        buf.write("(\2\2\u014cH\3\2\2\2\u014d\u014e\7~\2\2\u014e\u014f\7")
        buf.write("~\2\2\u014fJ\3\2\2\2\u0150\u0151\7#\2\2\u0151L\3\2\2\2")
        buf.write("\u0152\u0154\7<\2\2\u0153\u0152\3\2\2\2\u0153\u0154\3")
        buf.write("\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156\7?\2\2\u0156N\3")
        buf.write("\2\2\2\u0157\u0158\7-\2\2\u0158\u0159\7?\2\2\u0159P\3")
        buf.write("\2\2\2\u015a\u015b\7/\2\2\u015b\u015c\7?\2\2\u015cR\3")
        buf.write("\2\2\2\u015d\u015e\7,\2\2\u015e\u015f\7?\2\2\u015fT\3")
        buf.write("\2\2\2\u0160\u0161\7\61\2\2\u0161\u0162\7?\2\2\u0162V")
        buf.write("\3\2\2\2\u0163\u0164\7\'\2\2\u0164\u0165\7?\2\2\u0165")
        buf.write("X\3\2\2\2\u0166\u0167\7\60\2\2\u0167Z\3\2\2\2\u0168\u0169")
        buf.write("\7*\2\2\u0169\\\3\2\2\2\u016a\u016b\7+\2\2\u016b^\3\2")
        buf.write("\2\2\u016c\u016d\7}\2\2\u016d`\3\2\2\2\u016e\u016f\7\177")
        buf.write("\2\2\u016fb\3\2\2\2\u0170\u0171\7]\2\2\u0171d\3\2\2\2")
        buf.write("\u0172\u0173\7_\2\2\u0173f\3\2\2\2\u0174\u0175\7.\2\2")
        buf.write("\u0175h\3\2\2\2\u0176\u0177\7<\2\2\u0177j\3\2\2\2\u0178")
        buf.write("\u0179\7=\2\2\u0179l\3\2\2\2\u017a\u017f\5o8\2\u017b\u017f")
        buf.write("\5q9\2\u017c\u017f\5s:\2\u017d\u017f\5u;\2\u017e\u017a")
        buf.write("\3\2\2\2\u017e\u017b\3\2\2\2\u017e\u017c\3\2\2\2\u017e")
        buf.write("\u017d\3\2\2\2\u017fn\3\2\2\2\u0180\u0181\5\177@\2\u0181")
        buf.write("p\3\2\2\2\u0182\u0183\7\62\2\2\u0183\u0185\t\3\2\2\u0184")
        buf.write("\u0186\t\4\2\2\u0185\u0184\3\2\2\2\u0186\u0187\3\2\2\2")
        buf.write("\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188r\3\2\2")
        buf.write("\2\u0189\u018a\7\62\2\2\u018a\u018c\t\5\2\2\u018b\u018d")
        buf.write("\t\6\2\2\u018c\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write("\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018ft\3\2\2\2\u0190")
        buf.write("\u0191\7\62\2\2\u0191\u0193\t\7\2\2\u0192\u0194\t\b\2")
        buf.write("\2\u0193\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0193")
        buf.write("\3\2\2\2\u0195\u0196\3\2\2\2\u0196v\3\2\2\2\u0197\u0198")
        buf.write("\t\t\2\2\u0198x\3\2\2\2\u0199\u019a\t\n\2\2\u019az\3\2")
        buf.write("\2\2\u019b\u019c\t\13\2\2\u019c|\3\2\2\2\u019d\u019e\5")
        buf.write("\177@\2\u019e\u019f\5\u0081A\2\u019f\u01a7\3\2\2\2\u01a0")
        buf.write("\u01a2\5\177@\2\u01a1\u01a3\5\u0081A\2\u01a2\u01a1\3\2")
        buf.write("\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5")
        buf.write("\5\u0083B\2\u01a5\u01a7\3\2\2\2\u01a6\u019d\3\2\2\2\u01a6")
        buf.write("\u01a0\3\2\2\2\u01a7~\3\2\2\2\u01a8\u01ac\5y=\2\u01a9")
        buf.write("\u01ab\5w<\2\u01aa\u01a9\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01b1\3\2\2\2")
        buf.write("\u01ae\u01ac\3\2\2\2\u01af\u01b1\7\62\2\2\u01b0\u01a8")
        buf.write("\3\2\2\2\u01b0\u01af\3\2\2\2\u01b1\u0080\3\2\2\2\u01b2")
        buf.write("\u01b6\7\60\2\2\u01b3\u01b5\5w<\2\u01b4\u01b3\3\2\2\2")
        buf.write("\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3")
        buf.write("\2\2\2\u01b7\u0082\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01bb")
        buf.write("\t\f\2\2\u01ba\u01bc\t\r\2\2\u01bb\u01ba\3\2\2\2\u01bb")
        buf.write("\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bf\5w<\2\u01be")
        buf.write("\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01be\3\2\2\2")
        buf.write("\u01c0\u01c1\3\2\2\2\u01c1\u0084\3\2\2\2\u01c2\u01c6\7")
        buf.write("$\2\2\u01c3\u01c5\5\u0087D\2\u01c4\u01c3\3\2\2\2\u01c5")
        buf.write("\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2")
        buf.write("\u01c7\u01c9\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9\u01ca\7")
        buf.write("$\2\2\u01ca\u0086\3\2\2\2\u01cb\u01ce\5\u0089E\2\u01cc")
        buf.write("\u01ce\n\16\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01cc\3\2\2")
        buf.write("\2\u01ce\u0088\3\2\2\2\u01cf\u01d0\7^\2\2\u01d0\u01d1")
        buf.write("\t\17\2\2\u01d1\u008a\3\2\2\2\u01d2\u01d3\7^\2\2\u01d3")
        buf.write("\u01d4\n\17\2\2\u01d4\u008c\3\2\2\2\u01d5\u01d8\5-\27")
        buf.write("\2\u01d6\u01d8\5/\30\2\u01d7\u01d5\3\2\2\2\u01d7\u01d6")
        buf.write("\3\2\2\2\u01d8\u008e\3\2\2\2\u01d9\u01da\5+\26\2\u01da")
        buf.write("\u0090\3\2\2\2\u01db\u01de\5{>\2\u01dc\u01de\5\u0093J")
        buf.write("\2\u01dd\u01db\3\2\2\2\u01dd\u01dc\3\2\2\2\u01de\u01e4")
        buf.write("\3\2\2\2\u01df\u01e3\5{>\2\u01e0\u01e3\5\u0093J\2\u01e1")
        buf.write("\u01e3\5w<\2\u01e2\u01df\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2")
        buf.write("\u01e1\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2")
        buf.write("\u01e4\u01e5\3\2\2\2\u01e5\u0092\3\2\2\2\u01e6\u01e4\3")
        buf.write("\2\2\2\u01e7\u01e8\7a\2\2\u01e8\u0094\3\2\2\2\u01e9\u01ea")
        buf.write("\7\f\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ec\bK\2\2\u01ec")
        buf.write("\u0096\3\2\2\2\u01ed\u01ef\t\20\2\2\u01ee\u01ed\3\2\2")
        buf.write("\2\u01ef\u01f0\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01f1")
        buf.write("\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\bL\2\2\u01f3")
        buf.write("\u0098\3\2\2\2\u01f4\u01f5\13\2\2\2\u01f5\u01f6\bM\3\2")
        buf.write("\u01f6\u009a\3\2\2\2\u01f7\u01fb\7$\2\2\u01f8\u01fa\5")
        buf.write("\u0087D\2\u01f9\u01f8\3\2\2\2\u01fa\u01fd\3\2\2\2\u01fb")
        buf.write("\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fe\3\2\2\2")
        buf.write("\u01fd\u01fb\3\2\2\2\u01fe\u01ff\5\u008bF\2\u01ff\u0200")
        buf.write("\bN\4\2\u0200\u009c\3\2\2\2\u0201\u0205\7$\2\2\u0202\u0204")
        buf.write("\5\u0087D\2\u0203\u0202\3\2\2\2\u0204\u0207\3\2\2\2\u0205")
        buf.write("\u0203\3\2\2\2\u0205\u0206\3\2\2\2\u0206\u0209\3\2\2\2")
        buf.write("\u0207\u0205\3\2\2\2\u0208\u020a\t\21\2\2\u0209\u0208")
        buf.write("\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020c\bO\5\2\u020c")
        buf.write("\u009e\3\2\2\2\34\2\u00a7\u00b1\u00b3\u0153\u017e\u0187")
        buf.write("\u018e\u0195\u01a2\u01a6\u01ac\u01b0\u01b6\u01bb\u01c0")
        buf.write("\u01c6\u01cd\u01d7\u01dd\u01e2\u01e4\u01f0\u01fb\u0205")
        buf.write("\u0209\6\b\2\2\3M\2\3N\3\3O\4")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    LINE_COMMENT = 2
    COMMENT = 3
    IF = 4
    ELSE = 5
    FOR = 6
    RETURN = 7
    FUNC = 8
    TYPE = 9
    STRUCT = 10
    INTERFACE = 11
    STRING = 12
    INT = 13
    FLOAT = 14
    BOOLEAN = 15
    CONST = 16
    VAR = 17
    CONTINUE = 18
    BREAK = 19
    RANGE = 20
    NIL = 21
    TRUE = 22
    FALSE = 23
    ADD = 24
    SUB = 25
    MUL = 26
    DIV = 27
    MOD = 28
    EQ = 29
    NEQ = 30
    LT = 31
    LE = 32
    GT = 33
    GE = 34
    AND = 35
    OR = 36
    NOT = 37
    ASSIGN = 38
    PLUS_ASSIGN = 39
    MINUS_ASSIGN = 40
    MULT_ASSIGN = 41
    DIV_ASSIGN = 42
    MOD_ASSIGN = 43
    DOT = 44
    LB = 45
    RB = 46
    LCB = 47
    RCB = 48
    LSB = 49
    RSB = 50
    COMMA = 51
    COLON = 52
    SEMICOLON = 53
    INT_LITERAL = 54
    DECIMAL_LITERAL = 55
    BINARY_LITERAL = 56
    OCTAL_LITERAL = 57
    HEX_LITERAL = 58
    FLOAT_LITERAL = 59
    STRING_LITERAL = 60
    BOOLEAN_LITERAL = 61
    NIL_LITERAL = 62
    IDENTIFIER = 63
    NL = 64
    WS = 65
    ERROR_CHAR = 66
    ILLEGAL_ESCAPE = 67
    UNCLOSE_STRING = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'_'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "'('", "')'", 
            "'{'", "'}'", "'['", "']'", "','", "':'", "';'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "LINE_COMMENT", "COMMENT", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
            "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
            "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
            "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", 
            "LE", "GT", "GE", "AND", "OR", "NOT", "ASSIGN", "PLUS_ASSIGN", 
            "MINUS_ASSIGN", "MULT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", 
            "LB", "RB", "LCB", "RCB", "LSB", "RSB", "COMMA", "COLON", "SEMICOLON", 
            "INT_LITERAL", "DECIMAL_LITERAL", "BINARY_LITERAL", "OCTAL_LITERAL", 
            "HEX_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
            "NIL_LITERAL", "IDENTIFIER", "NL", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "LINE_COMMENT", "COMMENT", "IF", "ELSE", "FOR", 
                  "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", 
                  "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
                  "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", "LE", "GT", "GE", 
                  "AND", "OR", "NOT", "ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", 
                  "MULT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "LB", 
                  "RB", "LCB", "RCB", "LSB", "RSB", "COMMA", "COLON", "SEMICOLON", 
                  "INT_LITERAL", "DECIMAL_LITERAL", "BINARY_LITERAL", "OCTAL_LITERAL", 
                  "HEX_LITERAL", "DIGIT", "NONZERO_DIGIT", "LETTER", "FLOAT_LITERAL", 
                  "INT_PART", "DEC_PART", "EXP_PART", "STRING_LITERAL", 
                  "CHAR", "ESC", "INVALID_ESC", "BOOLEAN_LITERAL", "NIL_LITERAL", 
                  "IDENTIFIER", "UNDERSCORE", "NL", "WS", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[75] = self.ERROR_CHAR_action 
            actions[76] = self.ILLEGAL_ESCAPE_action 
            actions[77] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                illegal_string = str(self.text) 
                raise IllegalEscape(illegal_string[1:])
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                ESC = ['\r', '\n']
                text = str(self.text)
                if text[-1] in ESC:
                    raise UncloseString(text[1:-1])
                else:
                    raise UncloseString(text[1:])
                
     


