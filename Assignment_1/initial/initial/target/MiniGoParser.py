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
        buf.write("\u0276\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\6\2\u0094\n\2\r\2")
        buf.write("\16\2\u0095\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00a1")
        buf.write("\n\3\3\4\3\4\3\4\5\4\u00a6\n\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u00b9")
        buf.write("\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\5\t\u00c3\n\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\5\13\u00ce\n\13\3")
        buf.write("\f\3\f\3\f\6\f\u00d3\n\f\r\f\16\f\u00d4\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\7\17\u00e3\n")
        buf.write("\17\f\17\16\17\u00e6\13\17\5\17\u00e8\n\17\3\17\3\17\3")
        buf.write("\20\3\20\5\20\u00ee\n\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\6\22\u00f8\n\22\r\22\16\22\u00f9\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\5\23\u0103\n\23\3\23\3\23\3")
        buf.write("\24\3\24\3\24\5\24\u010a\n\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\7\25\u0111\n\25\f\25\16\25\u0114\13\25\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\6\30\u0122")
        buf.write("\n\30\r\30\16\30\u0123\3\30\3\30\3\31\3\31\3\31\5\31\u012b")
        buf.write("\n\31\3\31\3\31\5\31\u012f\n\31\3\31\3\31\3\32\3\32\3")
        buf.write("\32\3\32\5\32\u0137\n\32\3\32\3\32\5\32\u013b\n\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\7\33\u0143\n\33\f\33\16\33\u0146")
        buf.write("\13\33\3\34\3\34\3\34\3\35\3\35\3\35\7\35\u014e\n\35\f")
        buf.write("\35\16\35\u0151\13\35\3\36\3\36\6\36\u0155\n\36\r\36\16")
        buf.write("\36\u0156\3\36\3\36\3\37\3\37\3\37\3\37\3\37\5\37\u0160")
        buf.write("\n\37\3\37\3\37\5\37\u0164\n\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\5!\u0171\n!\3\"\3\"\3#\3#\3#\5#\u0178")
        buf.write("\n#\3$\3$\3%\3%\3%\5%\u017f\n%\3%\3%\3&\3&\3&\3&\3&\3")
        buf.write("&\7&\u0189\n&\f&\16&\u018c\13&\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\7\'\u0194\n\'\f\'\16\'\u0197\13\'\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\7(\u01a0\n(\f(\16(\u01a3\13(\3)\3)\3)\3)\3)\3)\7)\u01ab")
        buf.write("\n)\f)\16)\u01ae\13)\3*\3*\3*\3*\3*\3*\7*\u01b6\n*\f*")
        buf.write("\16*\u01b9\13*\3+\3+\3+\5+\u01be\n+\3,\3,\3,\3,\5,\u01c4")
        buf.write("\n,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u01d0\n,\3,\7,\u01d3")
        buf.write("\n,\f,\16,\u01d6\13,\3-\3-\3-\7-\u01db\n-\f-\16-\u01de")
        buf.write("\13-\3.\3.\3.\3.\3.\3.\3.\5.\u01e7\n.\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\5/\u01f1\n/\3\60\3\60\3\60\5\60\u01f6\n\60\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\5\63\u0202")
        buf.write("\n\63\3\64\3\64\6\64\u0206\n\64\r\64\16\64\u0207\3\65")
        buf.write("\3\65\5\65\u020c\n\65\3\65\6\65\u020f\n\65\r\65\16\65")
        buf.write("\u0210\3\66\3\66\3\66\3\66\5\66\u0217\n\66\3\67\3\67\3")
        buf.write("8\38\38\38\38\38\78\u0221\n8\f8\168\u0224\138\38\38\5")
        buf.write("8\u0228\n8\38\38\39\39\39\39\39\39\39\3:\3:\3:\3:\3:\3")
        buf.write(";\3;\3;\5;\u023b\n;\3<\5<\u023e\n<\3<\3<\5<\u0242\n<\3")
        buf.write("<\3<\5<\u0246\n<\3=\3=\5=\u024a\n=\3>\3>\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\3B\5B\u025e\nB\3B\3B\3")
        buf.write("C\3C\5C\u0264\nC\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3")
        buf.write("H\3H\3I\3I\3I\2\bJLNPRVJ\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("dfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c")
        buf.write("\u008e\u0090\2\16\4\299@@\5\2\5\699>?\3\2\17\22\3\2\33")
        buf.write("\34\3\2\35\37\4\2\34\34((\4\2\4\4@@\3\2&(\3\2\33\37\3")
        buf.write("\2 %\3\2*/\4\288DD\2\u027c\2\u0093\3\2\2\2\4\u00a0\3\2")
        buf.write("\2\2\6\u00a5\3\2\2\2\b\u00a9\3\2\2\2\n\u00af\3\2\2\2\f")
        buf.write("\u00b4\3\2\2\2\16\u00ba\3\2\2\2\20\u00c2\3\2\2\2\22\u00c6")
        buf.write("\3\2\2\2\24\u00ca\3\2\2\2\26\u00d2\3\2\2\2\30\u00d6\3")
        buf.write("\2\2\2\32\u00db\3\2\2\2\34\u00de\3\2\2\2\36\u00ed\3\2")
        buf.write("\2\2 \u00ef\3\2\2\2\"\u00f4\3\2\2\2$\u00fd\3\2\2\2&\u0106")
        buf.write("\3\2\2\2(\u010d\3\2\2\2*\u0115\3\2\2\2,\u0119\3\2\2\2")
        buf.write(".\u011e\3\2\2\2\60\u0127\3\2\2\2\62\u0132\3\2\2\2\64\u013f")
        buf.write("\3\2\2\2\66\u0147\3\2\2\28\u014a\3\2\2\2:\u0152\3\2\2")
        buf.write("\2<\u015a\3\2\2\2>\u0168\3\2\2\2@\u0170\3\2\2\2B\u0172")
        buf.write("\3\2\2\2D\u0177\3\2\2\2F\u0179\3\2\2\2H\u017b\3\2\2\2")
        buf.write("J\u0182\3\2\2\2L\u018d\3\2\2\2N\u0198\3\2\2\2P\u01a4\3")
        buf.write("\2\2\2R\u01af\3\2\2\2T\u01bd\3\2\2\2V\u01c3\3\2\2\2X\u01d7")
        buf.write("\3\2\2\2Z\u01e6\3\2\2\2\\\u01f0\3\2\2\2^\u01f5\3\2\2\2")
        buf.write("`\u01f7\3\2\2\2b\u01fa\3\2\2\2d\u0201\3\2\2\2f\u0203\3")
        buf.write("\2\2\2h\u020b\3\2\2\2j\u0212\3\2\2\2l\u0218\3\2\2\2n\u021a")
        buf.write("\3\2\2\2p\u022b\3\2\2\2r\u0232\3\2\2\2t\u023a\3\2\2\2")
        buf.write("v\u023d\3\2\2\2x\u0249\3\2\2\2z\u024b\3\2\2\2|\u024d\3")
        buf.write("\2\2\2~\u0254\3\2\2\2\u0080\u0257\3\2\2\2\u0082\u025d")
        buf.write("\3\2\2\2\u0084\u0261\3\2\2\2\u0086\u0267\3\2\2\2\u0088")
        buf.write("\u0269\3\2\2\2\u008a\u026b\3\2\2\2\u008c\u026d\3\2\2\2")
        buf.write("\u008e\u026f\3\2\2\2\u0090\u0273\3\2\2\2\u0092\u0094\5")
        buf.write("\4\3\2\u0093\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0093")
        buf.write("\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write("\u0098\7\2\2\3\u0098\3\3\2\2\2\u0099\u00a1\5\6\4\2\u009a")
        buf.write("\u00a1\5\16\b\2\u009b\u00a1\5\20\t\2\u009c\u00a1\5 \21")
        buf.write("\2\u009d\u00a1\5,\27\2\u009e\u00a1\5\62\32\2\u009f\u00a1")
        buf.write("\5<\37\2\u00a0\u0099\3\2\2\2\u00a0\u009a\3\2\2\2\u00a0")
        buf.write("\u009b\3\2\2\2\u00a0\u009c\3\2\2\2\u00a0\u009d\3\2\2\2")
        buf.write("\u00a0\u009e\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\5\3\2\2")
        buf.write("\2\u00a2\u00a6\5\b\5\2\u00a3\u00a6\5\n\6\2\u00a4\u00a6")
        buf.write("\5\f\7\2\u00a5\u00a2\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8\5\u0090")
        buf.write("I\2\u00a8\7\3\2\2\2\u00a9\u00aa\7\24\2\2\u00aa\u00ab\7")
        buf.write("@\2\2\u00ab\u00ac\5F$\2\u00ac\u00ad\7)\2\2\u00ad\u00ae")
        buf.write("\5J&\2\u00ae\t\3\2\2\2\u00af\u00b0\7\24\2\2\u00b0\u00b1")
        buf.write("\7@\2\2\u00b1\u00b2\7)\2\2\u00b2\u00b3\5J&\2\u00b3\13")
        buf.write("\3\2\2\2\u00b4\u00b5\7\24\2\2\u00b5\u00b8\7@\2\2\u00b6")
        buf.write("\u00b9\5F$\2\u00b7\u00b9\7@\2\2\u00b8\u00b6\3\2\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b9\r\3\2\2\2\u00ba\u00bb\7\23\2\2\u00bb")
        buf.write("\u00bc\7@\2\2\u00bc\u00bd\7)\2\2\u00bd\u00be\5J&\2\u00be")
        buf.write("\u00bf\5\u0090I\2\u00bf\17\3\2\2\2\u00c0\u00c3\5\22\n")
        buf.write("\2\u00c1\u00c3\5\30\r\2\u00c2\u00c0\3\2\2\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\5\u0090I\2\u00c5")
        buf.write("\21\3\2\2\2\u00c6\u00c7\7\24\2\2\u00c7\u00c8\7@\2\2\u00c8")
        buf.write("\u00c9\5\24\13\2\u00c9\23\3\2\2\2\u00ca\u00cd\5\26\f\2")
        buf.write("\u00cb\u00ce\5F$\2\u00cc\u00ce\7@\2\2\u00cd\u00cb\3\2")
        buf.write("\2\2\u00cd\u00cc\3\2\2\2\u00ce\25\3\2\2\2\u00cf\u00d0")
        buf.write("\7\65\2\2\u00d0\u00d1\t\2\2\2\u00d1\u00d3\7\66\2\2\u00d2")
        buf.write("\u00cf\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d2\3\2\2\2")
        buf.write("\u00d4\u00d5\3\2\2\2\u00d5\27\3\2\2\2\u00d6\u00d7\7\24")
        buf.write("\2\2\u00d7\u00d8\7@\2\2\u00d8\u00d9\7)\2\2\u00d9\u00da")
        buf.write("\5\32\16\2\u00da\31\3\2\2\2\u00db\u00dc\5\24\13\2\u00dc")
        buf.write("\u00dd\5\34\17\2\u00dd\33\3\2\2\2\u00de\u00e7\7\63\2\2")
        buf.write("\u00df\u00e4\5\36\20\2\u00e0\u00e1\7\67\2\2\u00e1\u00e3")
        buf.write("\5\36\20\2\u00e2\u00e0\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4")
        buf.write("\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e8\3\2\2\2")
        buf.write("\u00e6\u00e4\3\2\2\2\u00e7\u00df\3\2\2\2\u00e7\u00e8\3")
        buf.write("\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\7\64\2\2\u00ea")
        buf.write("\35\3\2\2\2\u00eb\u00ee\5\34\17\2\u00ec\u00ee\5B\"\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ed\u00ec\3\2\2\2\u00ee\37\3\2\2\2\u00ef")
        buf.write("\u00f0\7\f\2\2\u00f0\u00f1\7@\2\2\u00f1\u00f2\5\"\22\2")
        buf.write("\u00f2\u00f3\5\u0090I\2\u00f3!\3\2\2\2\u00f4\u00f5\7\r")
        buf.write("\2\2\u00f5\u00f7\7\63\2\2\u00f6\u00f8\5$\23\2\u00f7\u00f6")
        buf.write("\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9")
        buf.write("\u00fa\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fc\7\64\2")
        buf.write("\2\u00fc#\3\2\2\2\u00fd\u0102\7@\2\2\u00fe\u0103\5F$\2")
        buf.write("\u00ff\u0103\5\24\13\2\u0100\u0103\5\"\22\2\u0101\u0103")
        buf.write("\7@\2\2\u0102\u00fe\3\2\2\2\u0102\u00ff\3\2\2\2\u0102")
        buf.write("\u0100\3\2\2\2\u0102\u0101\3\2\2\2\u0103\u0104\3\2\2\2")
        buf.write("\u0104\u0105\5\u0090I\2\u0105%\3\2\2\2\u0106\u0107\7@")
        buf.write("\2\2\u0107\u0109\7\63\2\2\u0108\u010a\5(\25\2\u0109\u0108")
        buf.write("\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b\3\2\2\2\u010b")
        buf.write("\u010c\7\64\2\2\u010c\'\3\2\2\2\u010d\u0112\5*\26\2\u010e")
        buf.write("\u010f\7\67\2\2\u010f\u0111\5*\26\2\u0110\u010e\3\2\2")
        buf.write("\2\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113")
        buf.write("\3\2\2\2\u0113)\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0116")
        buf.write("\7@\2\2\u0116\u0117\7\3\2\2\u0117\u0118\5J&\2\u0118+\3")
        buf.write("\2\2\2\u0119\u011a\7\f\2\2\u011a\u011b\7@\2\2\u011b\u011c")
        buf.write("\5.\30\2\u011c\u011d\5\u0090I\2\u011d-\3\2\2\2\u011e\u011f")
        buf.write("\7\16\2\2\u011f\u0121\7\63\2\2\u0120\u0122\5\60\31\2\u0121")
        buf.write("\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0121\3\2\2\2")
        buf.write("\u0123\u0124\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0126\7")
        buf.write("\64\2\2\u0126/\3\2\2\2\u0127\u0128\7@\2\2\u0128\u012a")
        buf.write("\7\61\2\2\u0129\u012b\5\64\33\2\u012a\u0129\3\2\2\2\u012a")
        buf.write("\u012b\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012e\7\62\2")
        buf.write("\2\u012d\u012f\5@!\2\u012e\u012d\3\2\2\2\u012e\u012f\3")
        buf.write("\2\2\2\u012f\u0130\3\2\2\2\u0130\u0131\5\u0090I\2\u0131")
        buf.write("\61\3\2\2\2\u0132\u0133\7\13\2\2\u0133\u0134\7@\2\2\u0134")
        buf.write("\u0136\7\61\2\2\u0135\u0137\5\64\33\2\u0136\u0135\3\2")
        buf.write("\2\2\u0136\u0137\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013a")
        buf.write("\7\62\2\2\u0139\u013b\5@!\2\u013a\u0139\3\2\2\2\u013a")
        buf.write("\u013b\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\5:\36\2")
        buf.write("\u013d\u013e\5\u0090I\2\u013e\63\3\2\2\2\u013f\u0144\5")
        buf.write("\66\34\2\u0140\u0141\7\67\2\2\u0141\u0143\5\66\34\2\u0142")
        buf.write("\u0140\3\2\2\2\u0143\u0146\3\2\2\2\u0144\u0142\3\2\2\2")
        buf.write("\u0144\u0145\3\2\2\2\u0145\65\3\2\2\2\u0146\u0144\3\2")
        buf.write("\2\2\u0147\u0148\58\35\2\u0148\u0149\5@!\2\u0149\67\3")
        buf.write("\2\2\2\u014a\u014f\7@\2\2\u014b\u014c\7\67\2\2\u014c\u014e")
        buf.write("\7@\2\2\u014d\u014b\3\2\2\2\u014e\u0151\3\2\2\2\u014f")
        buf.write("\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u01509\3\2\2\2\u0151")
        buf.write("\u014f\3\2\2\2\u0152\u0154\7\63\2\2\u0153\u0155\5\\/\2")
        buf.write("\u0154\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0154\3")
        buf.write("\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0159")
        buf.write("\7\64\2\2\u0159;\3\2\2\2\u015a\u015b\7\13\2\2\u015b\u015c")
        buf.write("\5> \2\u015c\u015d\7@\2\2\u015d\u015f\7\61\2\2\u015e\u0160")
        buf.write("\5\64\33\2\u015f\u015e\3\2\2\2\u015f\u0160\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\u0163\7\62\2\2\u0162\u0164\5@!\2")
        buf.write("\u0163\u0162\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\3")
        buf.write("\2\2\2\u0165\u0166\5:\36\2\u0166\u0167\5\u0090I\2\u0167")
        buf.write("=\3\2\2\2\u0168\u0169\7\61\2\2\u0169\u016a\7@\2\2\u016a")
        buf.write("\u016b\7@\2\2\u016b\u016c\7\62\2\2\u016c?\3\2\2\2\u016d")
        buf.write("\u0171\5F$\2\u016e\u0171\5\24\13\2\u016f\u0171\7@\2\2")
        buf.write("\u0170\u016d\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u016f\3")
        buf.write("\2\2\2\u0171A\3\2\2\2\u0172\u0173\t\3\2\2\u0173C\3\2\2")
        buf.write("\2\u0174\u0178\5B\"\2\u0175\u0178\5\32\16\2\u0176\u0178")
        buf.write("\5&\24\2\u0177\u0174\3\2\2\2\u0177\u0175\3\2\2\2\u0177")
        buf.write("\u0176\3\2\2\2\u0178E\3\2\2\2\u0179\u017a\t\4\2\2\u017a")
        buf.write("G\3\2\2\2\u017b\u017c\7@\2\2\u017c\u017e\7\61\2\2\u017d")
        buf.write("\u017f\5X-\2\u017e\u017d\3\2\2\2\u017e\u017f\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180\u0181\7\62\2\2\u0181I\3\2\2\2\u0182")
        buf.write("\u0183\b&\1\2\u0183\u0184\5L\'\2\u0184\u018a\3\2\2\2\u0185")
        buf.write("\u0186\f\4\2\2\u0186\u0187\7\'\2\2\u0187\u0189\5L\'\2")
        buf.write("\u0188\u0185\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188\3")
        buf.write("\2\2\2\u018a\u018b\3\2\2\2\u018bK\3\2\2\2\u018c\u018a")
        buf.write("\3\2\2\2\u018d\u018e\b\'\1\2\u018e\u018f\5N(\2\u018f\u0195")
        buf.write("\3\2\2\2\u0190\u0191\f\4\2\2\u0191\u0192\7&\2\2\u0192")
        buf.write("\u0194\5N(\2\u0193\u0190\3\2\2\2\u0194\u0197\3\2\2\2\u0195")
        buf.write("\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196M\3\2\2\2\u0197")
        buf.write("\u0195\3\2\2\2\u0198\u0199\b(\1\2\u0199\u019a\5P)\2\u019a")
        buf.write("\u01a1\3\2\2\2\u019b\u019c\f\4\2\2\u019c\u019d\5\u008a")
        buf.write("F\2\u019d\u019e\5P)\2\u019e\u01a0\3\2\2\2\u019f\u019b")
        buf.write("\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2O\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4")
        buf.write("\u01a5\b)\1\2\u01a5\u01a6\5R*\2\u01a6\u01ac\3\2\2\2\u01a7")
        buf.write("\u01a8\f\4\2\2\u01a8\u01a9\t\5\2\2\u01a9\u01ab\5R*\2\u01aa")
        buf.write("\u01a7\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2")
        buf.write("\u01ac\u01ad\3\2\2\2\u01adQ\3\2\2\2\u01ae\u01ac\3\2\2")
        buf.write("\2\u01af\u01b0\b*\1\2\u01b0\u01b1\5T+\2\u01b1\u01b7\3")
        buf.write("\2\2\2\u01b2\u01b3\f\4\2\2\u01b3\u01b4\t\6\2\2\u01b4\u01b6")
        buf.write("\5T+\2\u01b5\u01b2\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5")
        buf.write("\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8S\3\2\2\2\u01b9\u01b7")
        buf.write("\3\2\2\2\u01ba\u01bb\t\7\2\2\u01bb\u01be\5T+\2\u01bc\u01be")
        buf.write("\5V,\2\u01bd\u01ba\3\2\2\2\u01bd\u01bc\3\2\2\2\u01beU")
        buf.write("\3\2\2\2\u01bf\u01c0\b,\1\2\u01c0\u01c1\7@\2\2\u01c1\u01c4")
        buf.write("\5\u008eH\2\u01c2\u01c4\5Z.\2\u01c3\u01bf\3\2\2\2\u01c3")
        buf.write("\u01c2\3\2\2\2\u01c4\u01d4\3\2\2\2\u01c5\u01c6\f\6\2\2")
        buf.write("\u01c6\u01d3\5\u008eH\2\u01c7\u01c8\f\5\2\2\u01c8\u01c9")
        buf.write("\7\60\2\2\u01c9\u01d3\7@\2\2\u01ca\u01cb\f\4\2\2\u01cb")
        buf.write("\u01cc\7\60\2\2\u01cc\u01cd\7@\2\2\u01cd\u01cf\7\61\2")
        buf.write("\2\u01ce\u01d0\5X-\2\u01cf\u01ce\3\2\2\2\u01cf\u01d0\3")
        buf.write("\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d3\7\62\2\2\u01d2")
        buf.write("\u01c5\3\2\2\2\u01d2\u01c7\3\2\2\2\u01d2\u01ca\3\2\2\2")
        buf.write("\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3")
        buf.write("\2\2\2\u01d5W\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7\u01dc")
        buf.write("\5J&\2\u01d8\u01d9\7\67\2\2\u01d9\u01db\5X-\2\u01da\u01d8")
        buf.write("\3\2\2\2\u01db\u01de\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc")
        buf.write("\u01dd\3\2\2\2\u01ddY\3\2\2\2\u01de\u01dc\3\2\2\2\u01df")
        buf.write("\u01e7\5D#\2\u01e0\u01e7\7@\2\2\u01e1\u01e7\5H%\2\u01e2")
        buf.write("\u01e3\7\61\2\2\u01e3\u01e4\5J&\2\u01e4\u01e5\7\62\2\2")
        buf.write("\u01e5\u01e7\3\2\2\2\u01e6\u01df\3\2\2\2\u01e6\u01e0\3")
        buf.write("\2\2\2\u01e6\u01e1\3\2\2\2\u01e6\u01e2\3\2\2\2\u01e7[")
        buf.write("\3\2\2\2\u01e8\u01f1\5^\60\2\u01e9\u01f1\5`\61\2\u01ea")
        buf.write("\u01f1\5n8\2\u01eb\u01f1\5r:\2\u01ec\u01f1\5~@\2\u01ed")
        buf.write("\u01f1\5\u0080A\2\u01ee\u01f1\5\u0082B\2\u01ef\u01f1\5")
        buf.write("\u0084C\2\u01f0\u01e8\3\2\2\2\u01f0\u01e9\3\2\2\2\u01f0")
        buf.write("\u01ea\3\2\2\2\u01f0\u01eb\3\2\2\2\u01f0\u01ec\3\2\2\2")
        buf.write("\u01f0\u01ed\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01ef\3")
        buf.write("\2\2\2\u01f1]\3\2\2\2\u01f2\u01f6\5\6\4\2\u01f3\u01f6")
        buf.write("\5\16\b\2\u01f4\u01f6\5\20\t\2\u01f5\u01f2\3\2\2\2\u01f5")
        buf.write("\u01f3\3\2\2\2\u01f5\u01f4\3\2\2\2\u01f6_\3\2\2\2\u01f7")
        buf.write("\u01f8\5b\62\2\u01f8\u01f9\5\u0090I\2\u01f9a\3\2\2\2\u01fa")
        buf.write("\u01fb\5d\63\2\u01fb\u01fc\5\u008cG\2\u01fc\u01fd\5l\67")
        buf.write("\2\u01fdc\3\2\2\2\u01fe\u0202\7@\2\2\u01ff\u0202\5f\64")
        buf.write("\2\u0200\u0202\5h\65\2\u0201\u01fe\3\2\2\2\u0201\u01ff")
        buf.write("\3\2\2\2\u0201\u0200\3\2\2\2\u0202e\3\2\2\2\u0203\u0205")
        buf.write("\7@\2\2\u0204\u0206\5\u008eH\2\u0205\u0204\3\2\2\2\u0206")
        buf.write("\u0207\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2\2")
        buf.write("\u0208g\3\2\2\2\u0209\u020c\7@\2\2\u020a\u020c\5f\64\2")
        buf.write("\u020b\u0209\3\2\2\2\u020b\u020a\3\2\2\2\u020c\u020e\3")
        buf.write("\2\2\2\u020d\u020f\5j\66\2\u020e\u020d\3\2\2\2\u020f\u0210")
        buf.write("\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211")
        buf.write("i\3\2\2\2\u0212\u0216\7\60\2\2\u0213\u0217\7@\2\2\u0214")
        buf.write("\u0217\5f\64\2\u0215\u0217\5H%\2\u0216\u0213\3\2\2\2\u0216")
        buf.write("\u0214\3\2\2\2\u0216\u0215\3\2\2\2\u0217k\3\2\2\2\u0218")
        buf.write("\u0219\5J&\2\u0219m\3\2\2\2\u021a\u021b\7\7\2\2\u021b")
        buf.write("\u021c\7\61\2\2\u021c\u021d\5J&\2\u021d\u021e\7\62\2\2")
        buf.write("\u021e\u0222\5:\36\2\u021f\u0221\5p9\2\u0220\u021f\3\2")
        buf.write("\2\2\u0221\u0224\3\2\2\2\u0222\u0220\3\2\2\2\u0222\u0223")
        buf.write("\3\2\2\2\u0223\u0227\3\2\2\2\u0224\u0222\3\2\2\2\u0225")
        buf.write("\u0226\7\b\2\2\u0226\u0228\5:\36\2\u0227\u0225\3\2\2\2")
        buf.write("\u0227\u0228\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u022a\5")
        buf.write("\u0090I\2\u022ao\3\2\2\2\u022b\u022c\7\b\2\2\u022c\u022d")
        buf.write("\7\7\2\2\u022d\u022e\7\61\2\2\u022e\u022f\5J&\2\u022f")
        buf.write("\u0230\7\62\2\2\u0230\u0231\5:\36\2\u0231q\3\2\2\2\u0232")
        buf.write("\u0233\7\t\2\2\u0233\u0234\5t;\2\u0234\u0235\5:\36\2\u0235")
        buf.write("\u0236\5\u0090I\2\u0236s\3\2\2\2\u0237\u023b\5J&\2\u0238")
        buf.write("\u023b\5v<\2\u0239\u023b\5|?\2\u023a\u0237\3\2\2\2\u023a")
        buf.write("\u0238\3\2\2\2\u023a\u0239\3\2\2\2\u023bu\3\2\2\2\u023c")
        buf.write("\u023e\5x=\2\u023d\u023c\3\2\2\2\u023d\u023e\3\2\2\2\u023e")
        buf.write("\u023f\3\2\2\2\u023f\u0241\5\u0090I\2\u0240\u0242\5J&")
        buf.write("\2\u0241\u0240\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0243")
        buf.write("\3\2\2\2\u0243\u0245\5\u0090I\2\u0244\u0246\5z>\2\u0245")
        buf.write("\u0244\3\2\2\2\u0245\u0246\3\2\2\2\u0246w\3\2\2\2\u0247")
        buf.write("\u024a\5b\62\2\u0248\u024a\5\n\6\2\u0249\u0247\3\2\2\2")
        buf.write("\u0249\u0248\3\2\2\2\u024ay\3\2\2\2\u024b\u024c\5b\62")
        buf.write("\2\u024c{\3\2\2\2\u024d\u024e\t\b\2\2\u024e\u024f\7\67")
        buf.write("\2\2\u024f\u0250\7@\2\2\u0250\u0251\7*\2\2\u0251\u0252")
        buf.write("\7\27\2\2\u0252\u0253\7@\2\2\u0253}\3\2\2\2\u0254\u0255")
        buf.write("\7\26\2\2\u0255\u0256\5\u0090I\2\u0256\177\3\2\2\2\u0257")
        buf.write("\u0258\7\25\2\2\u0258\u0259\5\u0090I\2\u0259\u0081\3\2")
        buf.write("\2\2\u025a\u025e\5H%\2\u025b\u025e\5h\65\2\u025c\u025e")
        buf.write("\5f\64\2\u025d\u025a\3\2\2\2\u025d\u025b\3\2\2\2\u025d")
        buf.write("\u025c\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u0260\5\u0090")
        buf.write("I\2\u0260\u0083\3\2\2\2\u0261\u0263\7\n\2\2\u0262\u0264")
        buf.write("\5J&\2\u0263\u0262\3\2\2\2\u0263\u0264\3\2\2\2\u0264\u0265")
        buf.write("\3\2\2\2\u0265\u0266\5\u0090I\2\u0266\u0085\3\2\2\2\u0267")
        buf.write("\u0268\t\t\2\2\u0268\u0087\3\2\2\2\u0269\u026a\t\n\2\2")
        buf.write("\u026a\u0089\3\2\2\2\u026b\u026c\t\13\2\2\u026c\u008b")
        buf.write("\3\2\2\2\u026d\u026e\t\f\2\2\u026e\u008d\3\2\2\2\u026f")
        buf.write("\u0270\7\65\2\2\u0270\u0271\5J&\2\u0271\u0272\7\66\2\2")
        buf.write("\u0272\u008f\3\2\2\2\u0273\u0274\t\r\2\2\u0274\u0091\3")
        buf.write("\2\2\29\u0095\u00a0\u00a5\u00b8\u00c2\u00cd\u00d4\u00e4")
        buf.write("\u00e7\u00ed\u00f9\u0102\u0109\u0112\u0123\u012a\u012e")
        buf.write("\u0136\u013a\u0144\u014f\u0156\u015f\u0163\u0170\u0177")
        buf.write("\u017e\u018a\u0195\u01a1\u01ac\u01b7\u01bd\u01c3\u01cf")
        buf.write("\u01d2\u01d4\u01dc\u01e6\u01f0\u01f5\u0201\u0207\u020b")
        buf.write("\u0210\u0216\u0222\u0227\u023a\u023d\u0241\u0245\u0249")
        buf.write("\u025d\u0263")
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
                      "IDENTIFIER", "LINE_COMMENT", "COMMENT", "WS", "EOS", 
                      "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_var_decl = 2
    RULE_decl_var_type_init = 3
    RULE_decl_var_init = 4
    RULE_decl_var_type = 5
    RULE_const_decl = 6
    RULE_array_decl = 7
    RULE_decl_arr = 8
    RULE_array_type = 9
    RULE_dimensions = 10
    RULE_decl_arr_init = 11
    RULE_array_literal = 12
    RULE_ele_list = 13
    RULE_ele = 14
    RULE_struct_decl = 15
    RULE_struct_type = 16
    RULE_fields = 17
    RULE_struct_literal = 18
    RULE_struct_elements = 19
    RULE_struct_ele = 20
    RULE_interface_decl = 21
    RULE_interface_type = 22
    RULE_interface_field = 23
    RULE_func_decl = 24
    RULE_param_list = 25
    RULE_param = 26
    RULE_id_list = 27
    RULE_block = 28
    RULE_method_decl = 29
    RULE_method = 30
    RULE_types = 31
    RULE_primitive_lit = 32
    RULE_literals = 33
    RULE_primitive_type = 34
    RULE_func_call = 35
    RULE_expr = 36
    RULE_expr1 = 37
    RULE_expr2 = 38
    RULE_expr3 = 39
    RULE_expr4 = 40
    RULE_expr5 = 41
    RULE_primary_expr = 42
    RULE_expr_list = 43
    RULE_operand = 44
    RULE_stmt = 45
    RULE_decl_stmt = 46
    RULE_asm_stmt = 47
    RULE_asm = 48
    RULE_lhs = 49
    RULE_array_elem = 50
    RULE_struct_elem = 51
    RULE_struct_ops = 52
    RULE_rhs = 53
    RULE_if_stmt = 54
    RULE_else_if_stmt = 55
    RULE_for_stmt = 56
    RULE_for_clause = 57
    RULE_fully_clause = 58
    RULE_init = 59
    RULE_update = 60
    RULE_range_clause = 61
    RULE_break_stmt = 62
    RULE_continue_stmt = 63
    RULE_call_stmt = 64
    RULE_return_stmt = 65
    RULE_boolean_ops = 66
    RULE_arithmetic_ops = 67
    RULE_relational_ops = 68
    RULE_assign_ops = 69
    RULE_index_ops = 70
    RULE_eos = 71

    ruleNames =  [ "program", "decl", "var_decl", "decl_var_type_init", 
                   "decl_var_init", "decl_var_type", "const_decl", "array_decl", 
                   "decl_arr", "array_type", "dimensions", "decl_arr_init", 
                   "array_literal", "ele_list", "ele", "struct_decl", "struct_type", 
                   "fields", "struct_literal", "struct_elements", "struct_ele", 
                   "interface_decl", "interface_type", "interface_field", 
                   "func_decl", "param_list", "param", "id_list", "block", 
                   "method_decl", "method", "types", "primitive_lit", "literals", 
                   "primitive_type", "func_call", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "primary_expr", "expr_list", 
                   "operand", "stmt", "decl_stmt", "asm_stmt", "asm", "lhs", 
                   "array_elem", "struct_elem", "struct_ops", "rhs", "if_stmt", 
                   "else_if_stmt", "for_stmt", "for_clause", "fully_clause", 
                   "init", "update", "range_clause", "break_stmt", "continue_stmt", 
                   "call_stmt", "return_stmt", "boolean_ops", "arithmetic_ops", 
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
    EOS=66
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

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 144
                self.decl()
                self.state = 147 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 149
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.array_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.struct_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 155
                self.interface_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 156
                self.func_decl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 157
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
        self.enterRule(localctx, 4, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 160
                self.decl_var_type_init()
                pass

            elif la_ == 2:
                self.state = 161
                self.decl_var_init()
                pass

            elif la_ == 3:
                self.state = 162
                self.decl_var_type()
                pass


            self.state = 165
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

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


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
        self.enterRule(localctx, 6, self.RULE_decl_var_type_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(MiniGoParser.VAR)
            self.state = 168
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 169
            self.primitive_type()
            self.state = 170
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 171
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
        self.enterRule(localctx, 8, self.RULE_decl_var_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(MiniGoParser.VAR)
            self.state = 174
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 175
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 176
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_var_type" ):
                return visitor.visitDecl_var_type(self)
            else:
                return visitor.visitChildren(self)




    def decl_var_type(self):

        localctx = MiniGoParser.Decl_var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_decl_var_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(MiniGoParser.VAR)
            self.state = 179
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 180
                self.primitive_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.state = 181
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(MiniGoParser.CONST)
            self.state = 185
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 186
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 187
            self.expr(0)
            self.state = 188
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

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def decl_arr(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_arrContext,0)


        def decl_arr_init(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_arr_initContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = MiniGoParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 190
                self.decl_arr()
                pass

            elif la_ == 2:
                self.state = 191
                self.decl_arr_init()
                pass


            self.state = 194
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_arr" ):
                return visitor.visitDecl_arr(self)
            else:
                return visitor.visitChildren(self)




    def decl_arr(self):

        localctx = MiniGoParser.Decl_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_decl_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(MiniGoParser.VAR)
            self.state = 197
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 198
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.dimensions()
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 201
                self.primitive_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.state = 202
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

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RSB)
            else:
                return self.getToken(MiniGoParser.RSB, i)

        def INT_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INT_LITERAL)
            else:
                return self.getToken(MiniGoParser.INT_LITERAL, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




    def dimensions(self):

        localctx = MiniGoParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_dimensions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 205
                self.match(MiniGoParser.LSB)
                self.state = 206
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.INT_LITERAL or _la==MiniGoParser.IDENTIFIER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 207
                self.match(MiniGoParser.RSB)
                self.state = 210 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LSB):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_arr_initContext(ParserRuleContext):
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

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_arr_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_arr_init" ):
                return visitor.visitDecl_arr_init(self)
            else:
                return visitor.visitChildren(self)




    def decl_arr_init(self):

        localctx = MiniGoParser.Decl_arr_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_decl_arr_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(MiniGoParser.VAR)
            self.state = 213
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 214
            self.match(MiniGoParser.DECLARE_ASSIGN)
            self.state = 215
            self.array_literal()
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
        self.enterRule(localctx, 24, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.array_type()
            self.state = 218
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

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def ele(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.EleContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.EleContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ele_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEle_list" ):
                return visitor.visitEle_list(self)
            else:
                return visitor.visitChildren(self)




    def ele_list(self):

        localctx = MiniGoParser.Ele_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ele_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(MiniGoParser.LCB)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.LCB) | (1 << MiniGoParser.INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL))) != 0):
                self.state = 221
                self.ele()
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 222
                    self.match(MiniGoParser.COMMA)
                    self.state = 223
                    self.ele()
                    self.state = 228
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 231
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
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LCB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.ele_list()
                pass
            elif token in [MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.NIL_LITERAL, MiniGoParser.INT_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
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
            self.state = 237
            self.match(MiniGoParser.TYPE)
            self.state = 238
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 239
            self.struct_type()
            self.state = 240
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type" ):
                return visitor.visitStruct_type(self)
            else:
                return visitor.visitChildren(self)




    def struct_type(self):

        localctx = MiniGoParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_struct_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(MiniGoParser.STRUCT)
            self.state = 243
            self.match(MiniGoParser.LCB)
            self.state = 245 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 244
                self.fields()
                self.state = 247 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.IDENTIFIER):
                    break

            self.state = 249
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFields" ):
                return visitor.visitFields(self)
            else:
                return visitor.visitChildren(self)




    def fields(self):

        localctx = MiniGoParser.FieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 252
                self.primitive_type()
                pass
            elif token in [MiniGoParser.LSB]:
                self.state = 253
                self.array_type()
                pass
            elif token in [MiniGoParser.STRUCT]:
                self.state = 254
                self.struct_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.state = 255
                self.match(MiniGoParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 258
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 261
            self.match(MiniGoParser.LCB)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 262
                self.struct_elements()


            self.state = 265
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

        def struct_ele(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_eleContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_eleContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_elements" ):
                return visitor.visitStruct_elements(self)
            else:
                return visitor.visitChildren(self)




    def struct_elements(self):

        localctx = MiniGoParser.Struct_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_struct_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.struct_ele()
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 268
                self.match(MiniGoParser.COMMA)
                self.state = 269
                self.struct_ele()
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 40, self.RULE_struct_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 276
            self.match(MiniGoParser.T__0)
            self.state = 277
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
        self.enterRule(localctx, 42, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(MiniGoParser.TYPE)
            self.state = 280
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 281
            self.interface_type()
            self.state = 282
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

        def interface_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Interface_fieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Interface_fieldContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_type" ):
                return visitor.visitInterface_type(self)
            else:
                return visitor.visitChildren(self)




    def interface_type(self):

        localctx = MiniGoParser.Interface_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_interface_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(MiniGoParser.INTERFACE)
            self.state = 285
            self.match(MiniGoParser.LCB)
            self.state = 287 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 286
                self.interface_field()
                self.state = 289 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.IDENTIFIER):
                    break

            self.state = 291
            self.match(MiniGoParser.RCB)
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
        self.enterRule(localctx, 46, self.RULE_interface_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 294
            self.match(MiniGoParser.LB)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 295
                self.param_list()


            self.state = 298
            self.match(MiniGoParser.RB)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 299
                self.types()


            self.state = 302
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
        self.enterRule(localctx, 48, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(MiniGoParser.FUNC)
            self.state = 305
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 306
            self.match(MiniGoParser.LB)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 307
                self.param_list()


            self.state = 310
            self.match(MiniGoParser.RB)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 311
                self.types()


            self.state = 314
            self.block()
            self.state = 315
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = MiniGoParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.param()
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 318
                self.match(MiniGoParser.COMMA)
                self.state = 319
                self.param()
                self.state = 324
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
        self.enterRule(localctx, 52, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.id_list()
            self.state = 326
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = MiniGoParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 329
                self.match(MiniGoParser.COMMA)
                self.state = 330
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(MiniGoParser.LCB)
            self.state = 338 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 337
                self.stmt()
                self.state = 340 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                    break

            self.state = 342
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
        self.enterRule(localctx, 58, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(MiniGoParser.FUNC)
            self.state = 345
            self.method()
            self.state = 346
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 347
            self.match(MiniGoParser.LB)
            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 348
                self.param_list()


            self.state = 351
            self.match(MiniGoParser.RB)
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 352
                self.types()


            self.state = 355
            self.block()
            self.state = 356
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
        self.enterRule(localctx, 60, self.RULE_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(MiniGoParser.LB)
            self.state = 359
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 360
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 361
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
        self.enterRule(localctx, 62, self.RULE_types)
        try:
            self.state = 366
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.primitive_type()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.array_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 365
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
        self.enterRule(localctx, 64, self.RULE_primitive_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
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
        self.enterRule(localctx, 66, self.RULE_literals)
        try:
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.NIL_LITERAL, MiniGoParser.INT_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.primitive_lit()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.array_literal()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 372
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
        self.enterRule(localctx, 68, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
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
        self.enterRule(localctx, 70, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 378
            self.match(MiniGoParser.LB)
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 379
                self.expr_list()


            self.state = 382
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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 392
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 387
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 388
                    self.match(MiniGoParser.OR)
                    self.state = 389
                    self.expr1(0) 
                self.state = 394
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 403
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 398
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 399
                    self.match(MiniGoParser.AND)
                    self.state = 400
                    self.expr2(0) 
                self.state = 405
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 415
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 409
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 410
                    self.relational_ops()
                    self.state = 411
                    self.expr3(0) 
                self.state = 417
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 426
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 421
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 422
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 423
                    self.expr4(0) 
                self.state = 428
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 437
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 432
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 433
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 434
                    self.expr5() 
                self.state = 439
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        self.enterRule(localctx, 82, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 441
                self.expr5()
                pass
            elif token in [MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.NIL_LITERAL, MiniGoParser.LB, MiniGoParser.LSB, MiniGoParser.INT_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_primary_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 446
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 447
                self.index_ops()
                pass

            elif la_ == 2:
                self.state = 448
                self.operand()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 466
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 464
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 451
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 452
                        self.index_ops()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 453
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 454
                        self.match(MiniGoParser.DOT)
                        self.state = 455
                        self.match(MiniGoParser.IDENTIFIER)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Primary_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primary_expr)
                        self.state = 456
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 457
                        self.match(MiniGoParser.DOT)
                        self.state = 458
                        self.match(MiniGoParser.IDENTIFIER)
                        self.state = 459
                        self.match(MiniGoParser.LB)
                        self.state = 461
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                            self.state = 460
                            self.expr_list()


                        self.state = 463
                        self.match(MiniGoParser.RB)
                        pass

             
                self.state = 468
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def expr_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Expr_listContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Expr_listContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = MiniGoParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.expr(0)
            self.state = 474
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 470
                    self.match(MiniGoParser.COMMA)
                    self.state = 471
                    self.expr_list() 
                self.state = 476
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

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
        self.enterRule(localctx, 88, self.RULE_operand)
        try:
            self.state = 484
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 479
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 480
                self.match(MiniGoParser.LB)
                self.state = 481
                self.expr(0)
                self.state = 482
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
        self.enterRule(localctx, 90, self.RULE_stmt)
        try:
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.decl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.asm_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 488
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 489
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 490
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 491
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 492
                self.call_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 493
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_stmt" ):
                return visitor.visitDecl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def decl_stmt(self):

        localctx = MiniGoParser.Decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_decl_stmt)
        try:
            self.state = 499
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 498
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsm_stmt" ):
                return visitor.visitAsm_stmt(self)
            else:
                return visitor.visitChildren(self)




    def asm_stmt(self):

        localctx = MiniGoParser.Asm_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_asm_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.asm()
            self.state = 502
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
        self.enterRule(localctx, 96, self.RULE_asm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.lhs()
            self.state = 505
            self.assign_ops()
            self.state = 506
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
        self.enterRule(localctx, 98, self.RULE_lhs)
        try:
            self.state = 511
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
                self.array_elem()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 510
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

        def index_ops(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Index_opsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Index_opsContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_elem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_elem" ):
                return visitor.visitArray_elem(self)
            else:
                return visitor.visitChildren(self)




    def array_elem(self):

        localctx = MiniGoParser.Array_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_array_elem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 515 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 514
                self.index_ops()
                self.state = 517 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LSB):
                    break

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

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def array_elem(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elemContext,0)


        def struct_ops(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_opsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_opsContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_elem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_elem" ):
                return visitor.visitStruct_elem(self)
            else:
                return visitor.visitChildren(self)




    def struct_elem(self):

        localctx = MiniGoParser.Struct_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_struct_elem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 519
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 520
                self.array_elem()
                pass


            self.state = 524 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 523
                self.struct_ops()
                self.state = 526 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.DOT):
                    break

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


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_ops

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_ops" ):
                return visitor.visitStruct_ops(self)
            else:
                return visitor.visitChildren(self)




    def struct_ops(self):

        localctx = MiniGoParser.Struct_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_struct_ops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(MiniGoParser.DOT)
            self.state = 532
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 529
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 530
                self.array_elem()
                pass

            elif la_ == 3:
                self.state = 531
                self.func_call()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhs" ):
                return visitor.visitRhs(self)
            else:
                return visitor.visitChildren(self)




    def rhs(self):

        localctx = MiniGoParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
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


        def else_if_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Else_if_stmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Else_if_stmtContext,i)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(MiniGoParser.IF)
            self.state = 537
            self.match(MiniGoParser.LB)
            self.state = 538
            self.expr(0)
            self.state = 539
            self.match(MiniGoParser.RB)
            self.state = 540
            self.block()
            self.state = 544
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 541
                    self.else_if_stmt() 
                self.state = 546
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

            self.state = 549
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 547
                self.match(MiniGoParser.ELSE)
                self.state = 548
                self.block()


            self.state = 551
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
        self.enterRule(localctx, 110, self.RULE_else_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.match(MiniGoParser.ELSE)
            self.state = 554
            self.match(MiniGoParser.IF)
            self.state = 555
            self.match(MiniGoParser.LB)
            self.state = 556
            self.expr(0)
            self.state = 557
            self.match(MiniGoParser.RB)
            self.state = 558
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.match(MiniGoParser.FOR)
            self.state = 561
            self.for_clause()
            self.state = 562
            self.block()
            self.state = 563
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_clause" ):
                return visitor.visitFor_clause(self)
            else:
                return visitor.visitChildren(self)




    def for_clause(self):

        localctx = MiniGoParser.For_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_for_clause)
        try:
            self.state = 568
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 565
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.fully_clause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 567
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFully_clause" ):
                return visitor.visitFully_clause(self)
            else:
                return visitor.visitChildren(self)




    def fully_clause(self):

        localctx = MiniGoParser.Fully_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_fully_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.VAR or _la==MiniGoParser.IDENTIFIER:
                self.state = 570
                self.init()


            self.state = 573
            self.eos()
            self.state = 575
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 574
                self.expr(0)


            self.state = 577
            self.eos()
            self.state = 579
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 578
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

        def asm(self):
            return self.getTypedRuleContext(MiniGoParser.AsmContext,0)


        def decl_var_init(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_var_initContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = MiniGoParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_init)
        try:
            self.state = 583
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 581
                self.asm()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 582
                self.decl_var_init()
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


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asm(self):
            return self.getTypedRuleContext(MiniGoParser.AsmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate" ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = MiniGoParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.asm()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_clause" ):
                return visitor.visitRange_clause(self)
            else:
                return visitor.visitChildren(self)




    def range_clause(self):

        localctx = MiniGoParser.Range_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_range_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__1 or _la==MiniGoParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 588
            self.match(MiniGoParser.COMMA)
            self.state = 589
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 590
            self.match(MiniGoParser.ASSIGN)
            self.state = 591
            self.match(MiniGoParser.RANGE)
            self.state = 592
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(MiniGoParser.BREAK)
            self.state = 595
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
        self.enterRule(localctx, 126, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.match(MiniGoParser.CONTINUE)
            self.state = 598
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


        def struct_elem(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_elemContext,0)


        def array_elem(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elemContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = MiniGoParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 600
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 601
                self.struct_elem()
                pass

            elif la_ == 3:
                self.state = 602
                self.array_elem()
                pass


            self.state = 605
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.match(MiniGoParser.RETURN)
            self.state = 609
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 608
                self.expr(0)


            self.state = 611
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
        self.enterRule(localctx, 132, self.RULE_boolean_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 613
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
        self.enterRule(localctx, 134, self.RULE_arithmetic_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
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
        self.enterRule(localctx, 136, self.RULE_relational_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
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
        self.enterRule(localctx, 138, self.RULE_assign_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
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
        self.enterRule(localctx, 140, self.RULE_index_ops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self.match(MiniGoParser.LSB)
            self.state = 622
            self.expr(0)
            self.state = 623
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEos" ):
                return visitor.visitEos(self)
            else:
                return visitor.visitChildren(self)




    def eos(self):

        localctx = MiniGoParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_eos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 625
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.EOS):
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
        self._predicates[36] = self.expr_sempred
        self._predicates[37] = self.expr1_sempred
        self._predicates[38] = self.expr2_sempred
        self._predicates[39] = self.expr3_sempred
        self._predicates[40] = self.expr4_sempred
        self._predicates[42] = self.primary_expr_sempred
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
         




