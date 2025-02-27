# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3G")
        buf.write("\u0288\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\5\3\u00b0\n\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4\u00b8\n\4\3\5\3\5\3\5\5\5\u00bd\n\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\5\n\u00d9\n\n\3")
        buf.write("\13\3\13\3\13\3\13\5\13\u00df\n\13\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u00f1\n\17\3\20\3\20\5\20\u00f5\n\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u0105\n\23\3\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\25\5\25\u010e\n\25\3\26\3\26\3\26\5\26\u0113\n\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\5\27\u011c\n\27\3\30\3")
        buf.write("\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\5\33\u0130\n\33\3\34\3")
        buf.write("\34\3\34\5\34\u0135\n\34\3\34\3\34\5\34\u0139\n\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\5\35\u0141\n\35\3\35\3\35\5")
        buf.write("\35\u0145\n\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u014f\n\36\3\37\3\37\3\37\3 \3 \3 \3 \5 \u0158\n")
        buf.write(" \3!\3!\3!\3!\3\"\3\"\3\"\3\"\5\"\u0162\n\"\3#\3#\3#\3")
        buf.write("#\3#\5#\u0169\n#\3#\3#\5#\u016d\n#\3#\3#\3#\3$\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\5%\u017a\n%\3&\3&\3\'\3\'\3\'\5\'\u0181")
        buf.write("\n\'\3(\3(\3)\3)\3)\5)\u0188\n)\3)\3)\3*\3*\3*\3*\3*\3")
        buf.write("*\7*\u0192\n*\f*\16*\u0195\13*\3+\3+\3+\3+\3+\3+\7+\u019d")
        buf.write("\n+\f+\16+\u01a0\13+\3,\3,\3,\3,\3,\3,\3,\7,\u01a9\n,")
        buf.write("\f,\16,\u01ac\13,\3-\3-\3-\3-\3-\3-\7-\u01b4\n-\f-\16")
        buf.write("-\u01b7\13-\3.\3.\3.\3.\3.\3.\7.\u01bf\n.\f.\16.\u01c2")
        buf.write("\13.\3/\3/\3/\5/\u01c7\n/\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01d6\n\60\3")
        buf.write("\60\7\60\u01d9\n\60\f\60\16\60\u01dc\13\60\3\61\3\61\3")
        buf.write("\61\3\61\3\61\5\61\u01e3\n\61\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\5\62\u01ec\n\62\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\5\63\u01f6\n\63\3\64\3\64\5\64\u01fa\n\64")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\5\67")
        buf.write("\u0206\n\67\38\38\38\39\39\39\39\59\u020f\n9\3:\3:\3:")
        buf.write("\3:\3;\3;\3<\3<\3<\3<\3<\3<\5<\u021d\n<\3<\3<\3=\3=\3")
        buf.write("=\3=\3=\5=\u0226\n=\3>\3>\3>\3>\3>\3>\3>\3?\3?\3?\3@\3")
        buf.write("@\3@\5@\u0235\n@\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3C\3C\3")
        buf.write("C\3C\3C\3D\3D\3D\3D\3D\3D\3E\3E\3E\5E\u024f\nE\3F\3F\3")
        buf.write("F\3F\3F\3F\3G\3G\3H\3H\3H\3H\3I\3I\3I\3I\3I\3I\3I\3J\3")
        buf.write("J\3J\3K\3K\3K\3L\3L\5L\u026c\nL\3L\3L\3M\3M\3M\3M\3N\3")
        buf.write("N\5N\u0276\nN\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3S\3")
        buf.write("S\3T\3T\3T\2\bRTVXZ^U\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh")
        buf.write("jlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c")
        buf.write("\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c\u009e")
        buf.write("\u00a0\u00a2\u00a4\u00a6\2\r\5\2\5\699>?\3\2\17\22\3\2")
        buf.write("\33\34\3\2\35\37\4\2\34\34((\4\2\4\4@@\3\2&(\3\2\33\37")
        buf.write("\3\2 %\3\2*/\4\288DD\2\u0276\2\u00a8\3\2\2\2\4\u00af\3")
        buf.write("\2\2\2\6\u00b7\3\2\2\2\b\u00bc\3\2\2\2\n\u00c0\3\2\2\2")
        buf.write("\f\u00c6\3\2\2\2\16\u00cb\3\2\2\2\20\u00cf\3\2\2\2\22")
        buf.write("\u00d5\3\2\2\2\24\u00de\3\2\2\2\26\u00e0\3\2\2\2\30\u00e4")
        buf.write("\3\2\2\2\32\u00e7\3\2\2\2\34\u00f0\3\2\2\2\36\u00f4\3")
        buf.write("\2\2\2 \u00f6\3\2\2\2\"\u00fb\3\2\2\2$\u0104\3\2\2\2&")
        buf.write("\u0106\3\2\2\2(\u0109\3\2\2\2*\u010f\3\2\2\2,\u011b\3")
        buf.write("\2\2\2.\u011d\3\2\2\2\60\u0121\3\2\2\2\62\u0126\3\2\2")
        buf.write("\2\64\u012f\3\2\2\2\66\u0131\3\2\2\28\u013c\3\2\2\2:\u014e")
        buf.write("\3\2\2\2<\u0150\3\2\2\2>\u0157\3\2\2\2@\u0159\3\2\2\2")
        buf.write("B\u0161\3\2\2\2D\u0163\3\2\2\2F\u0171\3\2\2\2H\u0179\3")
        buf.write("\2\2\2J\u017b\3\2\2\2L\u0180\3\2\2\2N\u0182\3\2\2\2P\u0184")
        buf.write("\3\2\2\2R\u018b\3\2\2\2T\u0196\3\2\2\2V\u01a1\3\2\2\2")
        buf.write("X\u01ad\3\2\2\2Z\u01b8\3\2\2\2\\\u01c6\3\2\2\2^\u01c8")
        buf.write("\3\2\2\2`\u01e2\3\2\2\2b\u01eb\3\2\2\2d\u01f5\3\2\2\2")
        buf.write("f\u01f9\3\2\2\2h\u01fb\3\2\2\2j\u01fe\3\2\2\2l\u0205\3")
        buf.write("\2\2\2n\u0207\3\2\2\2p\u020e\3\2\2\2r\u0210\3\2\2\2t\u0214")
        buf.write("\3\2\2\2v\u0216\3\2\2\2x\u0225\3\2\2\2z\u0227\3\2\2\2")
        buf.write("|\u022e\3\2\2\2~\u0234\3\2\2\2\u0080\u0236\3\2\2\2\u0082")
        buf.write("\u023b\3\2\2\2\u0084\u0240\3\2\2\2\u0086\u0245\3\2\2\2")
        buf.write("\u0088\u024e\3\2\2\2\u008a\u0250\3\2\2\2\u008c\u0256\3")
        buf.write("\2\2\2\u008e\u0258\3\2\2\2\u0090\u025c\3\2\2\2\u0092\u0263")
        buf.write("\3\2\2\2\u0094\u0266\3\2\2\2\u0096\u026b\3\2\2\2\u0098")
        buf.write("\u026f\3\2\2\2\u009a\u0273\3\2\2\2\u009c\u0279\3\2\2\2")
        buf.write("\u009e\u027b\3\2\2\2\u00a0\u027d\3\2\2\2\u00a2\u027f\3")
        buf.write("\2\2\2\u00a4\u0281\3\2\2\2\u00a6\u0285\3\2\2\2\u00a8\u00a9")
        buf.write("\5\4\3\2\u00a9\u00aa\7\2\2\3\u00aa\3\3\2\2\2\u00ab\u00ac")
        buf.write("\5\6\4\2\u00ac\u00ad\5\4\3\2\u00ad\u00b0\3\2\2\2\u00ae")
        buf.write("\u00b0\5\6\4\2\u00af\u00ab\3\2\2\2\u00af\u00ae\3\2\2\2")
        buf.write("\u00b0\5\3\2\2\2\u00b1\u00b8\5\b\5\2\u00b2\u00b8\5\20")
        buf.write("\t\2\u00b3\u00b8\5 \21\2\u00b4\u00b8\5\60\31\2\u00b5\u00b8")
        buf.write("\58\35\2\u00b6\u00b8\5D#\2\u00b7\u00b1\3\2\2\2\u00b7\u00b2")
        buf.write("\3\2\2\2\u00b7\u00b3\3\2\2\2\u00b7\u00b4\3\2\2\2\u00b7")
        buf.write("\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\7\3\2\2\2\u00b9")
        buf.write("\u00bd\5\n\6\2\u00ba\u00bd\5\f\7\2\u00bb\u00bd\5\16\b")
        buf.write("\2\u00bc\u00b9\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb")
        buf.write("\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\5\u00a6T\2\u00bf")
        buf.write("\t\3\2\2\2\u00c0\u00c1\7\24\2\2\u00c1\u00c2\7@\2\2\u00c2")
        buf.write("\u00c3\5H%\2\u00c3\u00c4\7)\2\2\u00c4\u00c5\5R*\2\u00c5")
        buf.write("\13\3\2\2\2\u00c6\u00c7\7\24\2\2\u00c7\u00c8\7@\2\2\u00c8")
        buf.write("\u00c9\7)\2\2\u00c9\u00ca\5R*\2\u00ca\r\3\2\2\2\u00cb")
        buf.write("\u00cc\7\24\2\2\u00cc\u00cd\7@\2\2\u00cd\u00ce\5H%\2\u00ce")
        buf.write("\17\3\2\2\2\u00cf\u00d0\7\23\2\2\u00d0\u00d1\7@\2\2\u00d1")
        buf.write("\u00d2\7)\2\2\u00d2\u00d3\5R*\2\u00d3\u00d4\5\u00a6T\2")
        buf.write("\u00d4\21\3\2\2\2\u00d5\u00d8\5\24\13\2\u00d6\u00d9\5")
        buf.write("N(\2\u00d7\u00d9\7@\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7")
        buf.write("\3\2\2\2\u00d9\23\3\2\2\2\u00da\u00db\5\26\f\2\u00db\u00dc")
        buf.write("\5\24\13\2\u00dc\u00df\3\2\2\2\u00dd\u00df\5\26\f\2\u00de")
        buf.write("\u00da\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\25\3\2\2\2\u00e0")
        buf.write("\u00e1\7\65\2\2\u00e1\u00e2\5R*\2\u00e2\u00e3\7\66\2\2")
        buf.write("\u00e3\27\3\2\2\2\u00e4\u00e5\5\22\n\2\u00e5\u00e6\5\32")
        buf.write("\16\2\u00e6\31\3\2\2\2\u00e7\u00e8\7\63\2\2\u00e8\u00e9")
        buf.write("\5\34\17\2\u00e9\u00ea\7\64\2\2\u00ea\33\3\2\2\2\u00eb")
        buf.write("\u00ec\5\36\20\2\u00ec\u00ed\7\67\2\2\u00ed\u00ee\5\34")
        buf.write("\17\2\u00ee\u00f1\3\2\2\2\u00ef\u00f1\5\36\20\2\u00f0")
        buf.write("\u00eb\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1\35\3\2\2\2\u00f2")
        buf.write("\u00f5\5\32\16\2\u00f3\u00f5\5J&\2\u00f4\u00f2\3\2\2\2")
        buf.write("\u00f4\u00f3\3\2\2\2\u00f5\37\3\2\2\2\u00f6\u00f7\7\f")
        buf.write("\2\2\u00f7\u00f8\7@\2\2\u00f8\u00f9\5\"\22\2\u00f9\u00fa")
        buf.write("\5\u00a6T\2\u00fa!\3\2\2\2\u00fb\u00fc\7\r\2\2\u00fc\u00fd")
        buf.write("\7\63\2\2\u00fd\u00fe\5$\23\2\u00fe\u00ff\7\64\2\2\u00ff")
        buf.write("#\3\2\2\2\u0100\u0101\5&\24\2\u0101\u0102\5$\23\2\u0102")
        buf.write("\u0105\3\2\2\2\u0103\u0105\5&\24\2\u0104\u0100\3\2\2\2")
        buf.write("\u0104\u0103\3\2\2\2\u0105%\3\2\2\2\u0106\u0107\5(\25")
        buf.write("\2\u0107\u0108\5\u00a6T\2\u0108\'\3\2\2\2\u0109\u010d")
        buf.write("\7@\2\2\u010a\u010e\5N(\2\u010b\u010e\5\22\n\2\u010c\u010e")
        buf.write("\7@\2\2\u010d\u010a\3\2\2\2\u010d\u010b\3\2\2\2\u010d")
        buf.write("\u010c\3\2\2\2\u010e)\3\2\2\2\u010f\u0110\7@\2\2\u0110")
        buf.write("\u0112\7\63\2\2\u0111\u0113\5,\27\2\u0112\u0111\3\2\2")
        buf.write("\2\u0112\u0113\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115")
        buf.write("\7\64\2\2\u0115+\3\2\2\2\u0116\u0117\5.\30\2\u0117\u0118")
        buf.write("\7\67\2\2\u0118\u0119\5,\27\2\u0119\u011c\3\2\2\2\u011a")
        buf.write("\u011c\5.\30\2\u011b\u0116\3\2\2\2\u011b\u011a\3\2\2\2")
        buf.write("\u011c-\3\2\2\2\u011d\u011e\7@\2\2\u011e\u011f\7\3\2\2")
        buf.write("\u011f\u0120\5R*\2\u0120/\3\2\2\2\u0121\u0122\7\f\2\2")
        buf.write("\u0122\u0123\7@\2\2\u0123\u0124\5\62\32\2\u0124\u0125")
        buf.write("\5\u00a6T\2\u0125\61\3\2\2\2\u0126\u0127\7\16\2\2\u0127")
        buf.write("\u0128\7\63\2\2\u0128\u0129\5\64\33\2\u0129\u012a\7\64")
        buf.write("\2\2\u012a\63\3\2\2\2\u012b\u012c\5\66\34\2\u012c\u012d")
        buf.write("\5\64\33\2\u012d\u0130\3\2\2\2\u012e\u0130\5\66\34\2\u012f")
        buf.write("\u012b\3\2\2\2\u012f\u012e\3\2\2\2\u0130\65\3\2\2\2\u0131")
        buf.write("\u0132\7@\2\2\u0132\u0134\7\61\2\2\u0133\u0135\5:\36\2")
        buf.write("\u0134\u0133\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\3")
        buf.write("\2\2\2\u0136\u0138\7\62\2\2\u0137\u0139\5H%\2\u0138\u0137")
        buf.write("\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("\u013b\5\u00a6T\2\u013b\67\3\2\2\2\u013c\u013d\7\13\2")
        buf.write("\2\u013d\u013e\7@\2\2\u013e\u0140\7\61\2\2\u013f\u0141")
        buf.write("\5:\36\2\u0140\u013f\3\2\2\2\u0140\u0141\3\2\2\2\u0141")
        buf.write("\u0142\3\2\2\2\u0142\u0144\7\62\2\2\u0143\u0145\5H%\2")
        buf.write("\u0144\u0143\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146\3")
        buf.write("\2\2\2\u0146\u0147\5@!\2\u0147\u0148\5\u00a6T\2\u0148")
        buf.write("9\3\2\2\2\u0149\u014a\5<\37\2\u014a\u014b\7\67\2\2\u014b")
        buf.write("\u014c\5:\36\2\u014c\u014f\3\2\2\2\u014d\u014f\5<\37\2")
        buf.write("\u014e\u0149\3\2\2\2\u014e\u014d\3\2\2\2\u014f;\3\2\2")
        buf.write("\2\u0150\u0151\5> \2\u0151\u0152\5H%\2\u0152=\3\2\2\2")
        buf.write("\u0153\u0154\7@\2\2\u0154\u0155\7\67\2\2\u0155\u0158\5")
        buf.write("> \2\u0156\u0158\7@\2\2\u0157\u0153\3\2\2\2\u0157\u0156")
        buf.write("\3\2\2\2\u0158?\3\2\2\2\u0159\u015a\7\63\2\2\u015a\u015b")
        buf.write("\5B\"\2\u015b\u015c\7\64\2\2\u015cA\3\2\2\2\u015d\u015e")
        buf.write("\5d\63\2\u015e\u015f\5B\"\2\u015f\u0162\3\2\2\2\u0160")
        buf.write("\u0162\5d\63\2\u0161\u015d\3\2\2\2\u0161\u0160\3\2\2\2")
        buf.write("\u0162C\3\2\2\2\u0163\u0164\7\13\2\2\u0164\u0165\5F$\2")
        buf.write("\u0165\u0166\7@\2\2\u0166\u0168\7\61\2\2\u0167\u0169\5")
        buf.write(":\36\2\u0168\u0167\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a")
        buf.write("\3\2\2\2\u016a\u016c\7\62\2\2\u016b\u016d\5H%\2\u016c")
        buf.write("\u016b\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016e\3\2\2\2")
        buf.write("\u016e\u016f\5@!\2\u016f\u0170\5\u00a6T\2\u0170E\3\2\2")
        buf.write("\2\u0171\u0172\7\61\2\2\u0172\u0173\7@\2\2\u0173\u0174")
        buf.write("\7@\2\2\u0174\u0175\7\62\2\2\u0175G\3\2\2\2\u0176\u017a")
        buf.write("\5N(\2\u0177\u017a\5\22\n\2\u0178\u017a\7@\2\2\u0179\u0176")
        buf.write("\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u0178\3\2\2\2\u017a")
        buf.write("I\3\2\2\2\u017b\u017c\t\2\2\2\u017cK\3\2\2\2\u017d\u0181")
        buf.write("\5J&\2\u017e\u0181\5\30\r\2\u017f\u0181\5*\26\2\u0180")
        buf.write("\u017d\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u017f\3\2\2\2")
        buf.write("\u0181M\3\2\2\2\u0182\u0183\t\3\2\2\u0183O\3\2\2\2\u0184")
        buf.write("\u0185\7@\2\2\u0185\u0187\7\61\2\2\u0186\u0188\5`\61\2")
        buf.write("\u0187\u0186\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\3")
        buf.write("\2\2\2\u0189\u018a\7\62\2\2\u018aQ\3\2\2\2\u018b\u018c")
        buf.write("\b*\1\2\u018c\u018d\5T+\2\u018d\u0193\3\2\2\2\u018e\u018f")
        buf.write("\f\4\2\2\u018f\u0190\7\'\2\2\u0190\u0192\5T+\2\u0191\u018e")
        buf.write("\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194S\3\2\2\2\u0195\u0193\3\2\2\2\u0196")
        buf.write("\u0197\b+\1\2\u0197\u0198\5V,\2\u0198\u019e\3\2\2\2\u0199")
        buf.write("\u019a\f\4\2\2\u019a\u019b\7&\2\2\u019b\u019d\5V,\2\u019c")
        buf.write("\u0199\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2")
        buf.write("\u019e\u019f\3\2\2\2\u019fU\3\2\2\2\u01a0\u019e\3\2\2")
        buf.write("\2\u01a1\u01a2\b,\1\2\u01a2\u01a3\5X-\2\u01a3\u01aa\3")
        buf.write("\2\2\2\u01a4\u01a5\f\4\2\2\u01a5\u01a6\5\u00a0Q\2\u01a6")
        buf.write("\u01a7\5X-\2\u01a7\u01a9\3\2\2\2\u01a8\u01a4\3\2\2\2\u01a9")
        buf.write("\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2")
        buf.write("\u01abW\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01ae\b-\1\2")
        buf.write("\u01ae\u01af\5Z.\2\u01af\u01b5\3\2\2\2\u01b0\u01b1\f\4")
        buf.write("\2\2\u01b1\u01b2\t\4\2\2\u01b2\u01b4\5Z.\2\u01b3\u01b0")
        buf.write("\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5")
        buf.write("\u01b6\3\2\2\2\u01b6Y\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8")
        buf.write("\u01b9\b.\1\2\u01b9\u01ba\5\\/\2\u01ba\u01c0\3\2\2\2\u01bb")
        buf.write("\u01bc\f\4\2\2\u01bc\u01bd\t\5\2\2\u01bd\u01bf\5\\/\2")
        buf.write("\u01be\u01bb\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be\3")
        buf.write("\2\2\2\u01c0\u01c1\3\2\2\2\u01c1[\3\2\2\2\u01c2\u01c0")
        buf.write("\3\2\2\2\u01c3\u01c4\t\6\2\2\u01c4\u01c7\5\\/\2\u01c5")
        buf.write("\u01c7\5^\60\2\u01c6\u01c3\3\2\2\2\u01c6\u01c5\3\2\2\2")
        buf.write("\u01c7]\3\2\2\2\u01c8\u01c9\b\60\1\2\u01c9\u01ca\5b\62")
        buf.write("\2\u01ca\u01da\3\2\2\2\u01cb\u01cc\f\6\2\2\u01cc\u01d9")
        buf.write("\5p9\2\u01cd\u01ce\f\5\2\2\u01ce\u01cf\7\60\2\2\u01cf")
        buf.write("\u01d9\7@\2\2\u01d0\u01d1\f\4\2\2\u01d1\u01d2\7\60\2\2")
        buf.write("\u01d2\u01d3\7@\2\2\u01d3\u01d5\7\61\2\2\u01d4\u01d6\5")
        buf.write("`\61\2\u01d5\u01d4\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7\u01d9\7\62\2\2\u01d8\u01cb\3\2\2\2\u01d8")
        buf.write("\u01cd\3\2\2\2\u01d8\u01d0\3\2\2\2\u01d9\u01dc\3\2\2\2")
        buf.write("\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db_\3\2\2")
        buf.write("\2\u01dc\u01da\3\2\2\2\u01dd\u01de\5R*\2\u01de\u01df\7")
        buf.write("\67\2\2\u01df\u01e0\5`\61\2\u01e0\u01e3\3\2\2\2\u01e1")
        buf.write("\u01e3\5R*\2\u01e2\u01dd\3\2\2\2\u01e2\u01e1\3\2\2\2\u01e3")
        buf.write("a\3\2\2\2\u01e4\u01ec\5L\'\2\u01e5\u01ec\7@\2\2\u01e6")
        buf.write("\u01ec\5P)\2\u01e7\u01e8\7\61\2\2\u01e8\u01e9\5R*\2\u01e9")
        buf.write("\u01ea\7\62\2\2\u01ea\u01ec\3\2\2\2\u01eb\u01e4\3\2\2")
        buf.write("\2\u01eb\u01e5\3\2\2\2\u01eb\u01e6\3\2\2\2\u01eb\u01e7")
        buf.write("\3\2\2\2\u01ecc\3\2\2\2\u01ed\u01f6\5f\64\2\u01ee\u01f6")
        buf.write("\5h\65\2\u01ef\u01f6\5v<\2\u01f0\u01f6\5~@\2\u01f1\u01f6")
        buf.write("\5\u0092J\2\u01f2\u01f6\5\u0094K\2\u01f3\u01f6\5\u0096")
        buf.write("L\2\u01f4\u01f6\5\u009aN\2\u01f5\u01ed\3\2\2\2\u01f5\u01ee")
        buf.write("\3\2\2\2\u01f5\u01ef\3\2\2\2\u01f5\u01f0\3\2\2\2\u01f5")
        buf.write("\u01f1\3\2\2\2\u01f5\u01f2\3\2\2\2\u01f5\u01f3\3\2\2\2")
        buf.write("\u01f5\u01f4\3\2\2\2\u01f6e\3\2\2\2\u01f7\u01fa\5\b\5")
        buf.write("\2\u01f8\u01fa\5\20\t\2\u01f9\u01f7\3\2\2\2\u01f9\u01f8")
        buf.write("\3\2\2\2\u01fag\3\2\2\2\u01fb\u01fc\5j\66\2\u01fc\u01fd")
        buf.write("\5\u00a6T\2\u01fdi\3\2\2\2\u01fe\u01ff\5l\67\2\u01ff\u0200")
        buf.write("\5\u00a2R\2\u0200\u0201\5t;\2\u0201k\3\2\2\2\u0202\u0206")
        buf.write("\7@\2\2\u0203\u0206\5n8\2\u0204\u0206\5r:\2\u0205\u0202")
        buf.write("\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0204\3\2\2\2\u0206")
        buf.write("m\3\2\2\2\u0207\u0208\5R*\2\u0208\u0209\5p9\2\u0209o\3")
        buf.write("\2\2\2\u020a\u020b\5\u00a4S\2\u020b\u020c\5p9\2\u020c")
        buf.write("\u020f\3\2\2\2\u020d\u020f\5\u00a4S\2\u020e\u020a\3\2")
        buf.write("\2\2\u020e\u020d\3\2\2\2\u020fq\3\2\2\2\u0210\u0211\5")
        buf.write("R*\2\u0211\u0212\7\60\2\2\u0212\u0213\7@\2\2\u0213s\3")
        buf.write("\2\2\2\u0214\u0215\5R*\2\u0215u\3\2\2\2\u0216\u0217\7")
        buf.write("\7\2\2\u0217\u0218\7\61\2\2\u0218\u0219\5R*\2\u0219\u021a")
        buf.write("\7\62\2\2\u021a\u021c\5@!\2\u021b\u021d\5x=\2\u021c\u021b")
        buf.write("\3\2\2\2\u021c\u021d\3\2\2\2\u021d\u021e\3\2\2\2\u021e")
        buf.write("\u021f\5\u00a6T\2\u021fw\3\2\2\2\u0220\u0221\5z>\2\u0221")
        buf.write("\u0222\5x=\2\u0222\u0226\3\2\2\2\u0223\u0226\5z>\2\u0224")
        buf.write("\u0226\5|?\2\u0225\u0220\3\2\2\2\u0225\u0223\3\2\2\2\u0225")
        buf.write("\u0224\3\2\2\2\u0226y\3\2\2\2\u0227\u0228\7\b\2\2\u0228")
        buf.write("\u0229\7\7\2\2\u0229\u022a\7\61\2\2\u022a\u022b\5R*\2")
        buf.write("\u022b\u022c\7\62\2\2\u022c\u022d\5@!\2\u022d{\3\2\2\2")
        buf.write("\u022e\u022f\7\b\2\2\u022f\u0230\5@!\2\u0230}\3\2\2\2")
        buf.write("\u0231\u0235\5\u0080A\2\u0232\u0235\5\u0082B\2\u0233\u0235")
        buf.write("\5\u0084C\2\u0234\u0231\3\2\2\2\u0234\u0232\3\2\2\2\u0234")
        buf.write("\u0233\3\2\2\2\u0235\177\3\2\2\2\u0236\u0237\7\t\2\2\u0237")
        buf.write("\u0238\5R*\2\u0238\u0239\5@!\2\u0239\u023a\5\u00a6T\2")
        buf.write("\u023a\u0081\3\2\2\2\u023b\u023c\7\t\2\2\u023c\u023d\5")
        buf.write("\u0086D\2\u023d\u023e\5@!\2\u023e\u023f\5\u00a6T\2\u023f")
        buf.write("\u0083\3\2\2\2\u0240\u0241\7\t\2\2\u0241\u0242\5\u0090")
        buf.write("I\2\u0242\u0243\5@!\2\u0243\u0244\5\u00a6T\2\u0244\u0085")
        buf.write("\3\2\2\2\u0245\u0246\5\u0088E\2\u0246\u0247\5\u00a6T\2")
        buf.write("\u0247\u0248\5R*\2\u0248\u0249\5\u00a6T\2\u0249\u024a")
        buf.write("\5\u008cG\2\u024a\u0087\3\2\2\2\u024b\u024f\5\u008eH\2")
        buf.write("\u024c\u024f\5\f\7\2\u024d\u024f\5\u008aF\2\u024e\u024b")
        buf.write("\3\2\2\2\u024e\u024c\3\2\2\2\u024e\u024d\3\2\2\2\u024f")
        buf.write("\u0089\3\2\2\2\u0250\u0251\7\24\2\2\u0251\u0252\7@\2\2")
        buf.write("\u0252\u0253\5N(\2\u0253\u0254\7)\2\2\u0254\u0255\5R*")
        buf.write("\2\u0255\u008b\3\2\2\2\u0256\u0257\5\u008eH\2\u0257\u008d")
        buf.write("\3\2\2\2\u0258\u0259\7@\2\2\u0259\u025a\5\u00a2R\2\u025a")
        buf.write("\u025b\5t;\2\u025b\u008f\3\2\2\2\u025c\u025d\t\7\2\2\u025d")
        buf.write("\u025e\7\67\2\2\u025e\u025f\7@\2\2\u025f\u0260\7*\2\2")
        buf.write("\u0260\u0261\7\27\2\2\u0261\u0262\5R*\2\u0262\u0091\3")
        buf.write("\2\2\2\u0263\u0264\7\26\2\2\u0264\u0265\5\u00a6T\2\u0265")
        buf.write("\u0093\3\2\2\2\u0266\u0267\7\25\2\2\u0267\u0268\5\u00a6")
        buf.write("T\2\u0268\u0095\3\2\2\2\u0269\u026c\5P)\2\u026a\u026c")
        buf.write("\5\u0098M\2\u026b\u0269\3\2\2\2\u026b\u026a\3\2\2\2\u026c")
        buf.write("\u026d\3\2\2\2\u026d\u026e\5\u00a6T\2\u026e\u0097\3\2")
        buf.write("\2\2\u026f\u0270\5R*\2\u0270\u0271\7\60\2\2\u0271\u0272")
        buf.write("\5P)\2\u0272\u0099\3\2\2\2\u0273\u0275\7\n\2\2\u0274\u0276")
        buf.write("\5R*\2\u0275\u0274\3\2\2\2\u0275\u0276\3\2\2\2\u0276\u0277")
        buf.write("\3\2\2\2\u0277\u0278\5\u00a6T\2\u0278\u009b\3\2\2\2\u0279")
        buf.write("\u027a\t\b\2\2\u027a\u009d\3\2\2\2\u027b\u027c\t\t\2\2")
        buf.write("\u027c\u009f\3\2\2\2\u027d\u027e\t\n\2\2\u027e\u00a1\3")
        buf.write("\2\2\2\u027f\u0280\t\13\2\2\u0280\u00a3\3\2\2\2\u0281")
        buf.write("\u0282\7\65\2\2\u0282\u0283\5R*\2\u0283\u0284\7\66\2\2")
        buf.write("\u0284\u00a5\3\2\2\2\u0285\u0286\t\f\2\2\u0286\u00a7\3")
        buf.write("\2\2\2/\u00af\u00b7\u00bc\u00d8\u00de\u00f0\u00f4\u0104")
        buf.write("\u010d\u0112\u011b\u012f\u0134\u0138\u0140\u0144\u014e")
        buf.write("\u0157\u0161\u0168\u016c\u0179\u0180\u0187\u0193\u019e")
        buf.write("\u01aa\u01b5\u01c0\u01c6\u01d5\u01d8\u01da\u01e2\u01eb")
        buf.write("\u01f5\u01f9\u0205\u020e\u021c\u0225\u0234\u024e\u026b")
        buf.write("\u0275")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_decl" ):
                return visitor.visitMany_decl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_var_type_init" ):
                return visitor.visitDecl_var_type_init(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_var_init" ):
                return visitor.visitDecl_var_init(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_var_type" ):
                return visitor.visitDecl_var_type(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




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
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 212
                self.primitive_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDim" ):
                return visitor.visitDim(self)
            else:
                return visitor.visitChildren(self)




    def dim(self):

        localctx = MiniGoParser.DimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_dim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(MiniGoParser.LSB)
            self.state = 223
            self.expr(0)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEle_list" ):
                return visitor.visitEle_list(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_ele" ):
                return visitor.visitMany_ele(self)
            else:
                return visitor.visitChildren(self)




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


        def getRuleIndex(self):
            return MiniGoParser.RULE_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEle" ):
                return visitor.visitEle(self)
            else:
                return visitor.visitChildren(self)




    def ele(self):

        localctx = MiniGoParser.EleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ele)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LCB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.ele_list()
                pass
            elif token in [MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.NIL_LITERAL, MiniGoParser.INT_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.primitive_lit()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(MiniGoParser.TYPE)
            self.state = 245
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 246
            self.struct_type()
            self.state = 247
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type" ):
                return visitor.visitStruct_type(self)
            else:
                return visitor.visitChildren(self)




    def struct_type(self):

        localctx = MiniGoParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_struct_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(MiniGoParser.STRUCT)
            self.state = 250
            self.match(MiniGoParser.LCB)
            self.state = 251
            self.many_fields()
            self.state = 252
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_fields" ):
                return visitor.visitMany_fields(self)
            else:
                return visitor.visitChildren(self)




    def many_fields(self):

        localctx = MiniGoParser.Many_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_many_fields)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.fields()
                self.state = 255
                self.many_fields()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFields" ):
                return visitor.visitFields(self)
            else:
                return visitor.visitChildren(self)




    def fields(self):

        localctx = MiniGoParser.FieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.ele_field()
            self.state = 261
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEle_field" ):
                return visitor.visitEle_field(self)
            else:
                return visitor.visitChildren(self)




    def ele_field(self):

        localctx = MiniGoParser.Ele_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ele_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 264
                self.primitive_type()
                pass
            elif token in [MiniGoParser.LSB]:
                self.state = 265
                self.array_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.state = 266
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 270
            self.match(MiniGoParser.LCB)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 271
                self.struct_elements()


            self.state = 274
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_elements" ):
                return visitor.visitStruct_elements(self)
            else:
                return visitor.visitChildren(self)




    def struct_elements(self):

        localctx = MiniGoParser.Struct_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_struct_elements)
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.struct_ele()
                self.state = 277
                self.match(MiniGoParser.COMMA)
                self.state = 278
                self.struct_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_ele" ):
                return visitor.visitStruct_ele(self)
            else:
                return visitor.visitChildren(self)




    def struct_ele(self):

        localctx = MiniGoParser.Struct_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_struct_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 284
            self.match(MiniGoParser.T__0)
            self.state = 285
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(MiniGoParser.TYPE)
            self.state = 288
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 289
            self.interface_type()
            self.state = 290
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_type" ):
                return visitor.visitInterface_type(self)
            else:
                return visitor.visitChildren(self)




    def interface_type(self):

        localctx = MiniGoParser.Interface_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_interface_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(MiniGoParser.INTERFACE)
            self.state = 293
            self.match(MiniGoParser.LCB)
            self.state = 294
            self.many_interface_field()
            self.state = 295
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_interface_field" ):
                return visitor.visitMany_interface_field(self)
            else:
                return visitor.visitChildren(self)




    def many_interface_field(self):

        localctx = MiniGoParser.Many_interface_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_many_interface_field)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.interface_field()
                self.state = 298
                self.many_interface_field()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_field" ):
                return visitor.visitInterface_field(self)
            else:
                return visitor.visitChildren(self)




    def interface_field(self):

        localctx = MiniGoParser.Interface_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_interface_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 304
            self.match(MiniGoParser.LB)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 305
                self.param_list()


            self.state = 308
            self.match(MiniGoParser.RB)
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 309
                self.types()


            self.state = 312
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(MiniGoParser.FUNC)
            self.state = 315
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 316
            self.match(MiniGoParser.LB)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 317
                self.param_list()


            self.state = 320
            self.match(MiniGoParser.RB)
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 321
                self.types()


            self.state = 324
            self.block()
            self.state = 325
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = MiniGoParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_param_list)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.param()
                self.state = 328
                self.match(MiniGoParser.COMMA)
                self.state = 329
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.id_list()
            self.state = 335
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = MiniGoParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_id_list)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 338
                self.match(MiniGoParser.COMMA)
                self.state = 339
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(MiniGoParser.LCB)
            self.state = 344
            self.many_stmt()
            self.state = 345
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_stmt" ):
                return visitor.visitMany_stmt(self)
            else:
                return visitor.visitChildren(self)




    def many_stmt(self):

        localctx = MiniGoParser.Many_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_many_stmt)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.stmt()
                self.state = 348
                self.many_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(MiniGoParser.FUNC)
            self.state = 354
            self.method()
            self.state = 355
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 356
            self.match(MiniGoParser.LB)
            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 357
                self.param_list()


            self.state = 360
            self.match(MiniGoParser.RB)
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 361
                self.types()


            self.state = 364
            self.block()
            self.state = 365
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = MiniGoParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(MiniGoParser.LB)
            self.state = 368
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 369
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 370
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = MiniGoParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_types)
        try:
            self.state = 375
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.primitive_type()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.array_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 374
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_lit" ):
                return visitor.visitPrimitive_lit(self)
            else:
                return visitor.visitChildren(self)




    def primitive_lit(self):

        localctx = MiniGoParser.Primitive_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_primitive_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = MiniGoParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_literals)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.NIL_LITERAL, MiniGoParser.INT_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.primitive_lit()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.array_literal()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 381
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 387
            self.match(MiniGoParser.LB)
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 388
                self.expr_list()


            self.state = 391
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 401
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 396
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 397
                    self.match(MiniGoParser.OR)
                    self.state = 398
                    self.expr1(0) 
                self.state = 403
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 412
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 407
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 408
                    self.match(MiniGoParser.AND)
                    self.state = 409
                    self.expr2(0) 
                self.state = 414
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 424
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 418
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 419
                    self.relational_ops()
                    self.state = 420
                    self.expr3(0) 
                self.state = 426
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 428
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 435
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 430
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 431
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 432
                    self.expr4(0) 
                self.state = 437
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 439
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 446
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 441
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 442
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 443
                    self.expr5() 
                self.state = 448
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 452
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 450
                self.expr5()
                pass
            elif token in [MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.NIL_LITERAL, MiniGoParser.LB, MiniGoParser.LSB, MiniGoParser.INT_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expr" ):
                return visitor.visitPrimary_expr(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 455
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 472
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 470
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 457
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 458
                        self.many_index_ops()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 459
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 460
                        self.match(MiniGoParser.DOT)
                        self.state = 461
                        self.match(MiniGoParser.IDENTIFIER)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 462
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 463
                        self.match(MiniGoParser.DOT)
                        self.state = 464
                        self.match(MiniGoParser.IDENTIFIER)
                        self.state = 465
                        self.match(MiniGoParser.LB)
                        self.state = 467
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                            self.state = 466
                            self.expr_list()


                        self.state = 469
                        self.match(MiniGoParser.RB)
                        pass

             
                self.state = 474
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = MiniGoParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr_list)
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self.expr(0)
                self.state = 476
                self.match(MiniGoParser.COMMA)
                self.state = 477
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_operand)
        try:
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 484
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 485
                self.match(MiniGoParser.LB)
                self.state = 486
                self.expr(0)
                self.state = 487
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_stmt)
        try:
            self.state = 499
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.decl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 492
                self.asm_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 493
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 494
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 495
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 496
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 497
                self.call_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 498
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_stmt" ):
                return visitor.visitDecl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def decl_stmt(self):

        localctx = MiniGoParser.Decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_decl_stmt)
        try:
            self.state = 503
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.var_decl()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsm_stmt" ):
                return visitor.visitAsm_stmt(self)
            else:
                return visitor.visitChildren(self)




    def asm_stmt(self):

        localctx = MiniGoParser.Asm_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_asm_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.asm()
            self.state = 506
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsm" ):
                return visitor.visitAsm(self)
            else:
                return visitor.visitChildren(self)




    def asm(self):

        localctx = MiniGoParser.AsmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_asm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.lhs()
            self.state = 509
            self.assign_ops()
            self.state = 510
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_lhs)
        try:
            self.state = 515
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 512
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
                self.array_elem()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 514
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_elem" ):
                return visitor.visitArray_elem(self)
            else:
                return visitor.visitChildren(self)




    def array_elem(self):

        localctx = MiniGoParser.Array_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_array_elem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.expr(0)
            self.state = 518
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_index_ops" ):
                return visitor.visitMany_index_ops(self)
            else:
                return visitor.visitChildren(self)




    def many_index_ops(self):

        localctx = MiniGoParser.Many_index_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_many_index_ops)
        try:
            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 520
                self.index_ops()
                self.state = 521
                self.many_index_ops()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 523
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_elem" ):
                return visitor.visitStruct_elem(self)
            else:
                return visitor.visitChildren(self)




    def struct_elem(self):

        localctx = MiniGoParser.Struct_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_struct_elem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.expr(0)
            self.state = 527
            self.match(MiniGoParser.DOT)
            self.state = 528
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhs" ):
                return visitor.visitRhs(self)
            else:
                return visitor.visitChildren(self)




    def rhs(self):

        localctx = MiniGoParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(MiniGoParser.IF)
            self.state = 533
            self.match(MiniGoParser.LB)
            self.state = 534
            self.expr(0)
            self.state = 535
            self.match(MiniGoParser.RB)
            self.state = 536
            self.block()
            self.state = 538
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 537
                self.if_tail()


            self.state = 540
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_tail" ):
                return visitor.visitIf_tail(self)
            else:
                return visitor.visitChildren(self)




    def if_tail(self):

        localctx = MiniGoParser.If_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_if_tail)
        try:
            self.state = 547
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 542
                self.else_if_stmt()
                self.state = 543
                self.if_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 545
                self.else_if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 546
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_stmt" ):
                return visitor.visitElse_if_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_if_stmt(self):

        localctx = MiniGoParser.Else_if_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_else_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(MiniGoParser.ELSE)
            self.state = 550
            self.match(MiniGoParser.IF)
            self.state = 551
            self.match(MiniGoParser.LB)
            self.state = 552
            self.expr(0)
            self.state = 553
            self.match(MiniGoParser.RB)
            self.state = 554
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = MiniGoParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.match(MiniGoParser.ELSE)
            self.state = 557
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_for_stmt)
        try:
            self.state = 562
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 559
                self.for_basic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 560
                self.for_step()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 561
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_basic" ):
                return visitor.visitFor_basic(self)
            else:
                return visitor.visitChildren(self)




    def for_basic(self):

        localctx = MiniGoParser.For_basicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_for_basic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.match(MiniGoParser.FOR)
            self.state = 565
            self.expr(0)
            self.state = 566
            self.block()
            self.state = 567
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_step" ):
                return visitor.visitFor_step(self)
            else:
                return visitor.visitChildren(self)




    def for_step(self):

        localctx = MiniGoParser.For_stepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_for_step)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(MiniGoParser.FOR)
            self.state = 570
            self.fully_clause()
            self.state = 571
            self.block()
            self.state = 572
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_each" ):
                return visitor.visitFor_each(self)
            else:
                return visitor.visitChildren(self)




    def for_each(self):

        localctx = MiniGoParser.For_eachContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_for_each)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.match(MiniGoParser.FOR)
            self.state = 575
            self.range_clause()
            self.state = 576
            self.block()
            self.state = 577
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFully_clause" ):
                return visitor.visitFully_clause(self)
            else:
                return visitor.visitChildren(self)




    def fully_clause(self):

        localctx = MiniGoParser.Fully_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_fully_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            self.init()
            self.state = 580
            self.eos()
            self.state = 581
            self.expr(0)
            self.state = 582
            self.eos()
            self.state = 583
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = MiniGoParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_init)
        try:
            self.state = 588
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 585
                self.asm_for()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 586
                self.decl_var_init()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 587
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_var_type_init_for" ):
                return visitor.visitDecl_var_type_init_for(self)
            else:
                return visitor.visitChildren(self)




    def decl_var_type_init_for(self):

        localctx = MiniGoParser.Decl_var_type_init_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_decl_var_type_init_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            self.match(MiniGoParser.VAR)
            self.state = 591
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 592
            self.primitive_type()
            self.state = 593
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 594
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate" ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = MiniGoParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsm_for" ):
                return visitor.visitAsm_for(self)
            else:
                return visitor.visitChildren(self)




    def asm_for(self):

        localctx = MiniGoParser.Asm_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_asm_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 598
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 599
            self.assign_ops()
            self.state = 600
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_clause" ):
                return visitor.visitRange_clause(self)
            else:
                return visitor.visitChildren(self)




    def range_clause(self):

        localctx = MiniGoParser.Range_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_range_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__1 or _la==MiniGoParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 603
            self.match(MiniGoParser.COMMA)
            self.state = 604
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 605
            self.match(MiniGoParser.ASSIGN)
            self.state = 606
            self.match(MiniGoParser.RANGE)
            self.state = 607
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            self.match(MiniGoParser.BREAK)
            self.state = 610
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self.match(MiniGoParser.CONTINUE)
            self.state = 613
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = MiniGoParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 615
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 616
                self.method_call()
                pass


            self.state = 619
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self.expr(0)
            self.state = 622
            self.match(MiniGoParser.DOT)
            self.state = 623
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 625
            self.match(MiniGoParser.RETURN)
            self.state = 627
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 626
                self.expr(0)


            self.state = 629
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_ops" ):
                return visitor.visitBoolean_ops(self)
            else:
                return visitor.visitChildren(self)




    def boolean_ops(self):

        localctx = MiniGoParser.Boolean_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_boolean_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 631
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.AND) | (1 << MiniGoParser.OR) | (1 << MiniGoParser.NOT))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic_ops" ):
                return visitor.visitArithmetic_ops(self)
            else:
                return visitor.visitChildren(self)




    def arithmetic_ops(self):

        localctx = MiniGoParser.Arithmetic_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_arithmetic_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ADD) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_ops" ):
                return visitor.visitRelational_ops(self)
            else:
                return visitor.visitChildren(self)




    def relational_ops(self):

        localctx = MiniGoParser.Relational_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_relational_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_ops" ):
                return visitor.visitAssign_ops(self)
            else:
                return visitor.visitChildren(self)




    def assign_ops(self):

        localctx = MiniGoParser.Assign_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_assign_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.PLUS_ASSIGN) | (1 << MiniGoParser.MINUS_ASSIGN) | (1 << MiniGoParser.MULT_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_ops" ):
                return visitor.visitIndex_ops(self)
            else:
                return visitor.visitChildren(self)




    def index_ops(self):

        localctx = MiniGoParser.Index_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_index_ops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 639
            self.match(MiniGoParser.LSB)
            self.state = 640
            self.expr(0)
            self.state = 641
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEos" ):
                return visitor.visitEos(self)
            else:
                return visitor.visitChildren(self)




    def eos(self):

        localctx = MiniGoParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_eos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
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
         




