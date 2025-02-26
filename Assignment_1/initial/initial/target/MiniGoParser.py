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
        buf.write("\u02b0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u00b4\n\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\5\4\u00bd\n\4\3\5\3\5\3\5\5\5\u00c2")
        buf.write("\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\5\b\u00d5\n\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\5\f\u00e7")
        buf.write("\n\f\3\r\3\r\3\r\3\r\5\r\u00ed\n\r\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\5\21\u00ff\n\21\3\22\3\22\3\22\3\22\5\22\u0105\n")
        buf.write("\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u0115\n\25\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u011b\n\26\3\26\3\26\3\27\3\27\3\27\5\27\u0122")
        buf.write("\n\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\5\30\u012b\n")
        buf.write("\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u013f\n")
        buf.write("\34\3\35\3\35\3\35\5\35\u0144\n\35\3\35\3\35\5\35\u0148")
        buf.write("\n\35\3\35\3\35\3\36\3\36\3\36\3\36\5\36\u0150\n\36\3")
        buf.write("\36\3\36\5\36\u0154\n\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\5\37\u015e\n\37\3 \3 \3 \3!\3!\3!\3!\5!\u0167")
        buf.write("\n!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\5#\u0171\n#\3$\3$\3$\3")
        buf.write("$\3$\5$\u0178\n$\3$\3$\5$\u017c\n$\3$\3$\3$\3%\3%\3%\3")
        buf.write("%\3%\3&\3&\3&\5&\u0189\n&\3\'\3\'\3(\3(\3(\5(\u0190\n")
        buf.write("(\3)\3)\3*\3*\3*\5*\u0197\n*\3*\3*\3+\3+\3+\3+\3+\3+\7")
        buf.write("+\u01a1\n+\f+\16+\u01a4\13+\3,\3,\3,\3,\3,\3,\7,\u01ac")
        buf.write("\n,\f,\16,\u01af\13,\3-\3-\3-\3-\3-\3-\3-\7-\u01b8\n-")
        buf.write("\f-\16-\u01bb\13-\3.\3.\3.\3.\3.\3.\7.\u01c3\n.\f.\16")
        buf.write(".\u01c6\13.\3/\3/\3/\3/\3/\3/\7/\u01ce\n/\f/\16/\u01d1")
        buf.write("\13/\3\60\3\60\3\60\5\60\u01d6\n\60\3\61\3\61\3\61\3\61")
        buf.write("\5\61\u01dc\n\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\5\61\u01e8\n\61\3\61\7\61\u01eb\n\61\f\61")
        buf.write("\16\61\u01ee\13\61\3\62\3\62\3\62\3\62\3\62\5\62\u01f5")
        buf.write("\n\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u01fe\n")
        buf.write("\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u0208")
        buf.write("\n\64\3\65\3\65\3\65\5\65\u020d\n\65\3\66\3\66\3\66\3")
        buf.write("\67\3\67\3\67\3\67\38\38\38\58\u0219\n8\39\39\39\3:\3")
        buf.write(":\3:\3:\5:\u0222\n:\3;\3;\5;\u0226\n;\3;\3;\3<\3<\3<\3")
        buf.write("<\5<\u022e\n<\3=\3=\3=\5=\u0233\n=\3>\3>\3?\3?\3?\3?\3")
        buf.write("?\3?\5?\u023d\n?\3?\3?\5?\u0241\n?\3?\3?\3@\3@\3@\3@\5")
        buf.write("@\u0249\n@\3A\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3C\3C\3")
        buf.write("C\5C\u025a\nC\3D\3D\3D\3D\3D\3D\3E\3E\3E\5E\u0265\nE\3")
        buf.write("F\3F\3F\3F\3F\3F\3G\3G\3H\3H\3H\3H\3I\3I\3I\3I\3I\3I\3")
        buf.write("I\3J\3J\3J\3K\3K\3K\3L\3L\5L\u0282\nL\3L\3L\3M\3M\5M\u0288")
        buf.write("\nM\3M\5M\u028b\nM\3M\3M\3M\3N\3N\3N\3N\5N\u0294\nN\3")
        buf.write("O\3O\3O\3O\5O\u029a\nO\3P\3P\5P\u029e\nP\3P\3P\3Q\3Q\3")
        buf.write("R\3R\3S\3S\3T\3T\3U\3U\3U\3U\3V\3V\3V\2\bTVXZ\\`W\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096")
        buf.write("\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8")
        buf.write("\u00aa\2\16\4\299@@\5\2\5\699>?\3\2\17\22\3\2\33\34\3")
        buf.write("\2\35\37\4\2\34\34((\4\2\4\4@@\3\2&(\3\2\33\37\3\2 %\3")
        buf.write("\2*/\4\288DD\2\u02aa\2\u00ac\3\2\2\2\4\u00b3\3\2\2\2\6")
        buf.write("\u00bc\3\2\2\2\b\u00c1\3\2\2\2\n\u00c5\3\2\2\2\f\u00cb")
        buf.write("\3\2\2\2\16\u00d0\3\2\2\2\20\u00d6\3\2\2\2\22\u00dc\3")
        buf.write("\2\2\2\24\u00df\3\2\2\2\26\u00e3\3\2\2\2\30\u00ec\3\2")
        buf.write("\2\2\32\u00ee\3\2\2\2\34\u00f2\3\2\2\2\36\u00f5\3\2\2")
        buf.write("\2 \u00fe\3\2\2\2\"\u0104\3\2\2\2$\u0106\3\2\2\2&\u010b")
        buf.write("\3\2\2\2(\u0114\3\2\2\2*\u0116\3\2\2\2,\u011e\3\2\2\2")
        buf.write(".\u012a\3\2\2\2\60\u012c\3\2\2\2\62\u0130\3\2\2\2\64\u0135")
        buf.write("\3\2\2\2\66\u013e\3\2\2\28\u0140\3\2\2\2:\u014b\3\2\2")
        buf.write("\2<\u015d\3\2\2\2>\u015f\3\2\2\2@\u0166\3\2\2\2B\u0168")
        buf.write("\3\2\2\2D\u0170\3\2\2\2F\u0172\3\2\2\2H\u0180\3\2\2\2")
        buf.write("J\u0188\3\2\2\2L\u018a\3\2\2\2N\u018f\3\2\2\2P\u0191\3")
        buf.write("\2\2\2R\u0193\3\2\2\2T\u019a\3\2\2\2V\u01a5\3\2\2\2X\u01b0")
        buf.write("\3\2\2\2Z\u01bc\3\2\2\2\\\u01c7\3\2\2\2^\u01d5\3\2\2\2")
        buf.write("`\u01db\3\2\2\2b\u01f4\3\2\2\2d\u01fd\3\2\2\2f\u0207\3")
        buf.write("\2\2\2h\u020c\3\2\2\2j\u020e\3\2\2\2l\u0211\3\2\2\2n\u0218")
        buf.write("\3\2\2\2p\u021a\3\2\2\2r\u0221\3\2\2\2t\u0225\3\2\2\2")
        buf.write("v\u022d\3\2\2\2x\u022f\3\2\2\2z\u0234\3\2\2\2|\u0236\3")
        buf.write("\2\2\2~\u0248\3\2\2\2\u0080\u024a\3\2\2\2\u0082\u0251")
        buf.write("\3\2\2\2\u0084\u0259\3\2\2\2\u0086\u025b\3\2\2\2\u0088")
        buf.write("\u0264\3\2\2\2\u008a\u0266\3\2\2\2\u008c\u026c\3\2\2\2")
        buf.write("\u008e\u026e\3\2\2\2\u0090\u0272\3\2\2\2\u0092\u0279\3")
        buf.write("\2\2\2\u0094\u027c\3\2\2\2\u0096\u0281\3\2\2\2\u0098\u0287")
        buf.write("\3\2\2\2\u009a\u0293\3\2\2\2\u009c\u0295\3\2\2\2\u009e")
        buf.write("\u029b\3\2\2\2\u00a0\u02a1\3\2\2\2\u00a2\u02a3\3\2\2\2")
        buf.write("\u00a4\u02a5\3\2\2\2\u00a6\u02a7\3\2\2\2\u00a8\u02a9\3")
        buf.write("\2\2\2\u00aa\u02ad\3\2\2\2\u00ac\u00ad\5\4\3\2\u00ad\u00ae")
        buf.write("\7\2\2\3\u00ae\3\3\2\2\2\u00af\u00b0\5\6\4\2\u00b0\u00b1")
        buf.write("\5\4\3\2\u00b1\u00b4\3\2\2\2\u00b2\u00b4\5\6\4\2\u00b3")
        buf.write("\u00af\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\5\3\2\2\2\u00b5")
        buf.write("\u00bd\5\b\5\2\u00b6\u00bd\5\20\t\2\u00b7\u00bd\5\22\n")
        buf.write("\2\u00b8\u00bd\5$\23\2\u00b9\u00bd\5\62\32\2\u00ba\u00bd")
        buf.write("\5:\36\2\u00bb\u00bd\5F$\2\u00bc\u00b5\3\2\2\2\u00bc\u00b6")
        buf.write("\3\2\2\2\u00bc\u00b7\3\2\2\2\u00bc\u00b8\3\2\2\2\u00bc")
        buf.write("\u00b9\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb\3\2\2\2")
        buf.write("\u00bd\7\3\2\2\2\u00be\u00c2\5\n\6\2\u00bf\u00c2\5\f\7")
        buf.write("\2\u00c0\u00c2\5\16\b\2\u00c1\u00be\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write("\u00c4\5\u00aaV\2\u00c4\t\3\2\2\2\u00c5\u00c6\7\24\2\2")
        buf.write("\u00c6\u00c7\7@\2\2\u00c7\u00c8\5J&\2\u00c8\u00c9\7)\2")
        buf.write("\2\u00c9\u00ca\5T+\2\u00ca\13\3\2\2\2\u00cb\u00cc\7\24")
        buf.write("\2\2\u00cc\u00cd\7@\2\2\u00cd\u00ce\7)\2\2\u00ce\u00cf")
        buf.write("\5T+\2\u00cf\r\3\2\2\2\u00d0\u00d1\7\24\2\2\u00d1\u00d4")
        buf.write("\7@\2\2\u00d2\u00d5\5P)\2\u00d3\u00d5\7@\2\2\u00d4\u00d2")
        buf.write("\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5\17\3\2\2\2\u00d6\u00d7")
        buf.write("\7\23\2\2\u00d7\u00d8\7@\2\2\u00d8\u00d9\7)\2\2\u00d9")
        buf.write("\u00da\5T+\2\u00da\u00db\5\u00aaV\2\u00db\21\3\2\2\2\u00dc")
        buf.write("\u00dd\5\24\13\2\u00dd\u00de\5\u00aaV\2\u00de\23\3\2\2")
        buf.write("\2\u00df\u00e0\7\24\2\2\u00e0\u00e1\7@\2\2\u00e1\u00e2")
        buf.write("\5\26\f\2\u00e2\25\3\2\2\2\u00e3\u00e6\5\30\r\2\u00e4")
        buf.write("\u00e7\5P)\2\u00e5\u00e7\7@\2\2\u00e6\u00e4\3\2\2\2\u00e6")
        buf.write("\u00e5\3\2\2\2\u00e7\27\3\2\2\2\u00e8\u00e9\5\32\16\2")
        buf.write("\u00e9\u00ea\5\30\r\2\u00ea\u00ed\3\2\2\2\u00eb\u00ed")
        buf.write("\5\32\16\2\u00ec\u00e8\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed")
        buf.write("\31\3\2\2\2\u00ee\u00ef\7\65\2\2\u00ef\u00f0\t\2\2\2\u00f0")
        buf.write("\u00f1\7\66\2\2\u00f1\33\3\2\2\2\u00f2\u00f3\5\26\f\2")
        buf.write("\u00f3\u00f4\5\36\20\2\u00f4\35\3\2\2\2\u00f5\u00f6\7")
        buf.write("\63\2\2\u00f6\u00f7\5 \21\2\u00f7\u00f8\7\64\2\2\u00f8")
        buf.write("\37\3\2\2\2\u00f9\u00fa\5\"\22\2\u00fa\u00fb\7\67\2\2")
        buf.write("\u00fb\u00fc\5 \21\2\u00fc\u00ff\3\2\2\2\u00fd\u00ff\5")
        buf.write("\"\22\2\u00fe\u00f9\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff")
        buf.write("!\3\2\2\2\u0100\u0105\5\36\20\2\u0101\u0105\5L\'\2\u0102")
        buf.write("\u0105\7@\2\2\u0103\u0105\5,\27\2\u0104\u0100\3\2\2\2")
        buf.write("\u0104\u0101\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0103\3")
        buf.write("\2\2\2\u0105#\3\2\2\2\u0106\u0107\7\f\2\2\u0107\u0108")
        buf.write("\7@\2\2\u0108\u0109\5&\24\2\u0109\u010a\5\u00aaV\2\u010a")
        buf.write("%\3\2\2\2\u010b\u010c\7\r\2\2\u010c\u010d\7\63\2\2\u010d")
        buf.write("\u010e\5(\25\2\u010e\u010f\7\64\2\2\u010f\'\3\2\2\2\u0110")
        buf.write("\u0111\5*\26\2\u0111\u0112\5(\25\2\u0112\u0115\3\2\2\2")
        buf.write("\u0113\u0115\5*\26\2\u0114\u0110\3\2\2\2\u0114\u0113\3")
        buf.write("\2\2\2\u0115)\3\2\2\2\u0116\u011a\7@\2\2\u0117\u011b\5")
        buf.write("P)\2\u0118\u011b\5\26\f\2\u0119\u011b\7@\2\2\u011a\u0117")
        buf.write("\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u0119\3\2\2\2\u011b")
        buf.write("\u011c\3\2\2\2\u011c\u011d\5\u00aaV\2\u011d+\3\2\2\2\u011e")
        buf.write("\u011f\7@\2\2\u011f\u0121\7\63\2\2\u0120\u0122\5.\30\2")
        buf.write("\u0121\u0120\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123\3")
        buf.write("\2\2\2\u0123\u0124\7\64\2\2\u0124-\3\2\2\2\u0125\u0126")
        buf.write("\5\60\31\2\u0126\u0127\7\67\2\2\u0127\u0128\5.\30\2\u0128")
        buf.write("\u012b\3\2\2\2\u0129\u012b\5\60\31\2\u012a\u0125\3\2\2")
        buf.write("\2\u012a\u0129\3\2\2\2\u012b/\3\2\2\2\u012c\u012d\7@\2")
        buf.write("\2\u012d\u012e\7\3\2\2\u012e\u012f\5T+\2\u012f\61\3\2")
        buf.write("\2\2\u0130\u0131\7\f\2\2\u0131\u0132\7@\2\2\u0132\u0133")
        buf.write("\5\64\33\2\u0133\u0134\5\u00aaV\2\u0134\63\3\2\2\2\u0135")
        buf.write("\u0136\7\16\2\2\u0136\u0137\7\63\2\2\u0137\u0138\5\66")
        buf.write("\34\2\u0138\u0139\7\64\2\2\u0139\65\3\2\2\2\u013a\u013b")
        buf.write("\58\35\2\u013b\u013c\5\66\34\2\u013c\u013f\3\2\2\2\u013d")
        buf.write("\u013f\58\35\2\u013e\u013a\3\2\2\2\u013e\u013d\3\2\2\2")
        buf.write("\u013f\67\3\2\2\2\u0140\u0141\7@\2\2\u0141\u0143\7\61")
        buf.write("\2\2\u0142\u0144\5<\37\2\u0143\u0142\3\2\2\2\u0143\u0144")
        buf.write("\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0147\7\62\2\2\u0146")
        buf.write("\u0148\5J&\2\u0147\u0146\3\2\2\2\u0147\u0148\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149\u014a\5\u00aaV\2\u014a9\3\2\2\2\u014b")
        buf.write("\u014c\7\13\2\2\u014c\u014d\7@\2\2\u014d\u014f\7\61\2")
        buf.write("\2\u014e\u0150\5<\37\2\u014f\u014e\3\2\2\2\u014f\u0150")
        buf.write("\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0153\7\62\2\2\u0152")
        buf.write("\u0154\5J&\2\u0153\u0152\3\2\2\2\u0153\u0154\3\2\2\2\u0154")
        buf.write("\u0155\3\2\2\2\u0155\u0156\5B\"\2\u0156\u0157\5\u00aa")
        buf.write("V\2\u0157;\3\2\2\2\u0158\u0159\5> \2\u0159\u015a\7\67")
        buf.write("\2\2\u015a\u015b\5<\37\2\u015b\u015e\3\2\2\2\u015c\u015e")
        buf.write("\5> \2\u015d\u0158\3\2\2\2\u015d\u015c\3\2\2\2\u015e=")
        buf.write("\3\2\2\2\u015f\u0160\5@!\2\u0160\u0161\5J&\2\u0161?\3")
        buf.write("\2\2\2\u0162\u0163\7@\2\2\u0163\u0164\7\67\2\2\u0164\u0167")
        buf.write("\5@!\2\u0165\u0167\7@\2\2\u0166\u0162\3\2\2\2\u0166\u0165")
        buf.write("\3\2\2\2\u0167A\3\2\2\2\u0168\u0169\7\63\2\2\u0169\u016a")
        buf.write("\5D#\2\u016a\u016b\7\64\2\2\u016bC\3\2\2\2\u016c\u016d")
        buf.write("\5f\64\2\u016d\u016e\5D#\2\u016e\u0171\3\2\2\2\u016f\u0171")
        buf.write("\5f\64\2\u0170\u016c\3\2\2\2\u0170\u016f\3\2\2\2\u0171")
        buf.write("E\3\2\2\2\u0172\u0173\7\13\2\2\u0173\u0174\5H%\2\u0174")
        buf.write("\u0175\7@\2\2\u0175\u0177\7\61\2\2\u0176\u0178\5<\37\2")
        buf.write("\u0177\u0176\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u0179\3")
        buf.write("\2\2\2\u0179\u017b\7\62\2\2\u017a\u017c\5J&\2\u017b\u017a")
        buf.write("\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017d\3\2\2\2\u017d")
        buf.write("\u017e\5B\"\2\u017e\u017f\5\u00aaV\2\u017fG\3\2\2\2\u0180")
        buf.write("\u0181\7\61\2\2\u0181\u0182\7@\2\2\u0182\u0183\7@\2\2")
        buf.write("\u0183\u0184\7\62\2\2\u0184I\3\2\2\2\u0185\u0189\5P)\2")
        buf.write("\u0186\u0189\5\26\f\2\u0187\u0189\7@\2\2\u0188\u0185\3")
        buf.write("\2\2\2\u0188\u0186\3\2\2\2\u0188\u0187\3\2\2\2\u0189K")
        buf.write("\3\2\2\2\u018a\u018b\t\3\2\2\u018bM\3\2\2\2\u018c\u0190")
        buf.write("\5L\'\2\u018d\u0190\5\34\17\2\u018e\u0190\5,\27\2\u018f")
        buf.write("\u018c\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u018e\3\2\2\2")
        buf.write("\u0190O\3\2\2\2\u0191\u0192\t\4\2\2\u0192Q\3\2\2\2\u0193")
        buf.write("\u0194\7@\2\2\u0194\u0196\7\61\2\2\u0195\u0197\5b\62\2")
        buf.write("\u0196\u0195\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198\3")
        buf.write("\2\2\2\u0198\u0199\7\62\2\2\u0199S\3\2\2\2\u019a\u019b")
        buf.write("\b+\1\2\u019b\u019c\5V,\2\u019c\u01a2\3\2\2\2\u019d\u019e")
        buf.write("\f\4\2\2\u019e\u019f\7\'\2\2\u019f\u01a1\5V,\2\u01a0\u019d")
        buf.write("\3\2\2\2\u01a1\u01a4\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a3\3\2\2\2\u01a3U\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5")
        buf.write("\u01a6\b,\1\2\u01a6\u01a7\5X-\2\u01a7\u01ad\3\2\2\2\u01a8")
        buf.write("\u01a9\f\4\2\2\u01a9\u01aa\7&\2\2\u01aa\u01ac\5X-\2\u01ab")
        buf.write("\u01a8\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01aeW\3\2\2\2\u01af\u01ad\3\2\2")
        buf.write("\2\u01b0\u01b1\b-\1\2\u01b1\u01b2\5Z.\2\u01b2\u01b9\3")
        buf.write("\2\2\2\u01b3\u01b4\f\4\2\2\u01b4\u01b5\5\u00a4S\2\u01b5")
        buf.write("\u01b6\5Z.\2\u01b6\u01b8\3\2\2\2\u01b7\u01b3\3\2\2\2\u01b8")
        buf.write("\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2")
        buf.write("\u01baY\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bc\u01bd\b.\1\2")
        buf.write("\u01bd\u01be\5\\/\2\u01be\u01c4\3\2\2\2\u01bf\u01c0\f")
        buf.write("\4\2\2\u01c0\u01c1\t\5\2\2\u01c1\u01c3\5\\/\2\u01c2\u01bf")
        buf.write("\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c5\3\2\2\2\u01c5[\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7")
        buf.write("\u01c8\b/\1\2\u01c8\u01c9\5^\60\2\u01c9\u01cf\3\2\2\2")
        buf.write("\u01ca\u01cb\f\4\2\2\u01cb\u01cc\t\6\2\2\u01cc\u01ce\5")
        buf.write("^\60\2\u01cd\u01ca\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01cd")
        buf.write("\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0]\3\2\2\2\u01d1\u01cf")
        buf.write("\3\2\2\2\u01d2\u01d3\t\7\2\2\u01d3\u01d6\5^\60\2\u01d4")
        buf.write("\u01d6\5`\61\2\u01d5\u01d2\3\2\2\2\u01d5\u01d4\3\2\2\2")
        buf.write("\u01d6_\3\2\2\2\u01d7\u01d8\b\61\1\2\u01d8\u01d9\7@\2")
        buf.write("\2\u01d9\u01dc\5\u00a8U\2\u01da\u01dc\5d\63\2\u01db\u01d7")
        buf.write("\3\2\2\2\u01db\u01da\3\2\2\2\u01dc\u01ec\3\2\2\2\u01dd")
        buf.write("\u01de\f\6\2\2\u01de\u01eb\5\u00a8U\2\u01df\u01e0\f\5")
        buf.write("\2\2\u01e0\u01e1\7\60\2\2\u01e1\u01eb\7@\2\2\u01e2\u01e3")
        buf.write("\f\4\2\2\u01e3\u01e4\7\60\2\2\u01e4\u01e5\7@\2\2\u01e5")
        buf.write("\u01e7\7\61\2\2\u01e6\u01e8\5b\62\2\u01e7\u01e6\3\2\2")
        buf.write("\2\u01e7\u01e8\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01eb")
        buf.write("\7\62\2\2\u01ea\u01dd\3\2\2\2\u01ea\u01df\3\2\2\2\u01ea")
        buf.write("\u01e2\3\2\2\2\u01eb\u01ee\3\2\2\2\u01ec\u01ea\3\2\2\2")
        buf.write("\u01ec\u01ed\3\2\2\2\u01eda\3\2\2\2\u01ee\u01ec\3\2\2")
        buf.write("\2\u01ef\u01f0\5T+\2\u01f0\u01f1\7\67\2\2\u01f1\u01f2")
        buf.write("\5b\62\2\u01f2\u01f5\3\2\2\2\u01f3\u01f5\5T+\2\u01f4\u01ef")
        buf.write("\3\2\2\2\u01f4\u01f3\3\2\2\2\u01f5c\3\2\2\2\u01f6\u01fe")
        buf.write("\5N(\2\u01f7\u01fe\7@\2\2\u01f8\u01fe\5R*\2\u01f9\u01fa")
        buf.write("\7\61\2\2\u01fa\u01fb\5T+\2\u01fb\u01fc\7\62\2\2\u01fc")
        buf.write("\u01fe\3\2\2\2\u01fd\u01f6\3\2\2\2\u01fd\u01f7\3\2\2\2")
        buf.write("\u01fd\u01f8\3\2\2\2\u01fd\u01f9\3\2\2\2\u01fee\3\2\2")
        buf.write("\2\u01ff\u0208\5h\65\2\u0200\u0208\5j\66\2\u0201\u0208")
        buf.write("\5|?\2\u0202\u0208\5\u0082B\2\u0203\u0208\5\u0092J\2\u0204")
        buf.write("\u0208\5\u0094K\2\u0205\u0208\5\u0096L\2\u0206\u0208\5")
        buf.write("\u009eP\2\u0207\u01ff\3\2\2\2\u0207\u0200\3\2\2\2\u0207")
        buf.write("\u0201\3\2\2\2\u0207\u0202\3\2\2\2\u0207\u0203\3\2\2\2")
        buf.write("\u0207\u0204\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0206\3")
        buf.write("\2\2\2\u0208g\3\2\2\2\u0209\u020d\5\b\5\2\u020a\u020d")
        buf.write("\5\20\t\2\u020b\u020d\5\22\n\2\u020c\u0209\3\2\2\2\u020c")
        buf.write("\u020a\3\2\2\2\u020c\u020b\3\2\2\2\u020di\3\2\2\2\u020e")
        buf.write("\u020f\5l\67\2\u020f\u0210\5\u00aaV\2\u0210k\3\2\2\2\u0211")
        buf.write("\u0212\5n8\2\u0212\u0213\5\u00a6T\2\u0213\u0214\5z>\2")
        buf.write("\u0214m\3\2\2\2\u0215\u0219\7@\2\2\u0216\u0219\5p9\2\u0217")
        buf.write("\u0219\5t;\2\u0218\u0215\3\2\2\2\u0218\u0216\3\2\2\2\u0218")
        buf.write("\u0217\3\2\2\2\u0219o\3\2\2\2\u021a\u021b\7@\2\2\u021b")
        buf.write("\u021c\5r:\2\u021cq\3\2\2\2\u021d\u021e\5\u00a8U\2\u021e")
        buf.write("\u021f\5r:\2\u021f\u0222\3\2\2\2\u0220\u0222\5\u00a8U")
        buf.write("\2\u0221\u021d\3\2\2\2\u0221\u0220\3\2\2\2\u0222s\3\2")
        buf.write("\2\2\u0223\u0226\7@\2\2\u0224\u0226\5p9\2\u0225\u0223")
        buf.write("\3\2\2\2\u0225\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227")
        buf.write("\u0228\5v<\2\u0228u\3\2\2\2\u0229\u022a\5x=\2\u022a\u022b")
        buf.write("\5v<\2\u022b\u022e\3\2\2\2\u022c\u022e\5x=\2\u022d\u0229")
        buf.write("\3\2\2\2\u022d\u022c\3\2\2\2\u022ew\3\2\2\2\u022f\u0232")
        buf.write("\7\60\2\2\u0230\u0233\7@\2\2\u0231\u0233\5p9\2\u0232\u0230")
        buf.write("\3\2\2\2\u0232\u0231\3\2\2\2\u0233y\3\2\2\2\u0234\u0235")
        buf.write("\5T+\2\u0235{\3\2\2\2\u0236\u0237\7\7\2\2\u0237\u0238")
        buf.write("\7\61\2\2\u0238\u0239\5T+\2\u0239\u023a\7\62\2\2\u023a")
        buf.write("\u023c\5B\"\2\u023b\u023d\5~@\2\u023c\u023b\3\2\2\2\u023c")
        buf.write("\u023d\3\2\2\2\u023d\u0240\3\2\2\2\u023e\u023f\7\b\2\2")
        buf.write("\u023f\u0241\5B\"\2\u0240\u023e\3\2\2\2\u0240\u0241\3")
        buf.write("\2\2\2\u0241\u0242\3\2\2\2\u0242\u0243\5\u00aaV\2\u0243")
        buf.write("}\3\2\2\2\u0244\u0245\5\u0080A\2\u0245\u0246\5~@\2\u0246")
        buf.write("\u0249\3\2\2\2\u0247\u0249\5\u0080A\2\u0248\u0244\3\2")
        buf.write("\2\2\u0248\u0247\3\2\2\2\u0249\177\3\2\2\2\u024a\u024b")
        buf.write("\7\b\2\2\u024b\u024c\7\7\2\2\u024c\u024d\7\61\2\2\u024d")
        buf.write("\u024e\5T+\2\u024e\u024f\7\62\2\2\u024f\u0250\5B\"\2\u0250")
        buf.write("\u0081\3\2\2\2\u0251\u0252\7\t\2\2\u0252\u0253\5\u0084")
        buf.write("C\2\u0253\u0254\5B\"\2\u0254\u0255\5\u00aaV\2\u0255\u0083")
        buf.write("\3\2\2\2\u0256\u025a\5T+\2\u0257\u025a\5\u0086D\2\u0258")
        buf.write("\u025a\5\u0090I\2\u0259\u0256\3\2\2\2\u0259\u0257\3\2")
        buf.write("\2\2\u0259\u0258\3\2\2\2\u025a\u0085\3\2\2\2\u025b\u025c")
        buf.write("\5\u0088E\2\u025c\u025d\5\u00aaV\2\u025d\u025e\5T+\2\u025e")
        buf.write("\u025f\5\u00aaV\2\u025f\u0260\5\u008cG\2\u0260\u0087\3")
        buf.write("\2\2\2\u0261\u0265\5\u008eH\2\u0262\u0265\5\f\7\2\u0263")
        buf.write("\u0265\5\u008aF\2\u0264\u0261\3\2\2\2\u0264\u0262\3\2")
        buf.write("\2\2\u0264\u0263\3\2\2\2\u0265\u0089\3\2\2\2\u0266\u0267")
        buf.write("\7\24\2\2\u0267\u0268\7@\2\2\u0268\u0269\5P)\2\u0269\u026a")
        buf.write("\7)\2\2\u026a\u026b\5T+\2\u026b\u008b\3\2\2\2\u026c\u026d")
        buf.write("\5\u008eH\2\u026d\u008d\3\2\2\2\u026e\u026f\7@\2\2\u026f")
        buf.write("\u0270\5\u00a6T\2\u0270\u0271\5z>\2\u0271\u008f\3\2\2")
        buf.write("\2\u0272\u0273\t\b\2\2\u0273\u0274\7\67\2\2\u0274\u0275")
        buf.write("\7@\2\2\u0275\u0276\7*\2\2\u0276\u0277\7\27\2\2\u0277")
        buf.write("\u0278\5T+\2\u0278\u0091\3\2\2\2\u0279\u027a\7\26\2\2")
        buf.write("\u027a\u027b\5\u00aaV\2\u027b\u0093\3\2\2\2\u027c\u027d")
        buf.write("\7\25\2\2\u027d\u027e\5\u00aaV\2\u027e\u0095\3\2\2\2\u027f")
        buf.write("\u0282\5R*\2\u0280\u0282\5\u0098M\2\u0281\u027f\3\2\2")
        buf.write("\2\u0281\u0280\3\2\2\2\u0282\u0283\3\2\2\2\u0283\u0284")
        buf.write("\5\u00aaV\2\u0284\u0097\3\2\2\2\u0285\u0288\7@\2\2\u0286")
        buf.write("\u0288\5p9\2\u0287\u0285\3\2\2\2\u0287\u0286\3\2\2\2\u0288")
        buf.write("\u028a\3\2\2\2\u0289\u028b\5\u009aN\2\u028a\u0289\3\2")
        buf.write("\2\2\u028a\u028b\3\2\2\2\u028b\u028c\3\2\2\2\u028c\u028d")
        buf.write("\7\60\2\2\u028d\u028e\5R*\2\u028e\u0099\3\2\2\2\u028f")
        buf.write("\u0290\5\u009cO\2\u0290\u0291\5\u009aN\2\u0291\u0294\3")
        buf.write("\2\2\2\u0292\u0294\5\u009cO\2\u0293\u028f\3\2\2\2\u0293")
        buf.write("\u0292\3\2\2\2\u0294\u009b\3\2\2\2\u0295\u0299\7\60\2")
        buf.write("\2\u0296\u029a\7@\2\2\u0297\u029a\5p9\2\u0298\u029a\5")
        buf.write("R*\2\u0299\u0296\3\2\2\2\u0299\u0297\3\2\2\2\u0299\u0298")
        buf.write("\3\2\2\2\u029a\u009d\3\2\2\2\u029b\u029d\7\n\2\2\u029c")
        buf.write("\u029e\5T+\2\u029d\u029c\3\2\2\2\u029d\u029e\3\2\2\2\u029e")
        buf.write("\u029f\3\2\2\2\u029f\u02a0\5\u00aaV\2\u02a0\u009f\3\2")
        buf.write("\2\2\u02a1\u02a2\t\t\2\2\u02a2\u00a1\3\2\2\2\u02a3\u02a4")
        buf.write("\t\n\2\2\u02a4\u00a3\3\2\2\2\u02a5\u02a6\t\13\2\2\u02a6")
        buf.write("\u00a5\3\2\2\2\u02a7\u02a8\t\f\2\2\u02a8\u00a7\3\2\2\2")
        buf.write("\u02a9\u02aa\7\65\2\2\u02aa\u02ab\5T+\2\u02ab\u02ac\7")
        buf.write("\66\2\2\u02ac\u00a9\3\2\2\2\u02ad\u02ae\t\r\2\2\u02ae")
        buf.write("\u00ab\3\2\2\29\u00b3\u00bc\u00c1\u00d4\u00e6\u00ec\u00fe")
        buf.write("\u0104\u0114\u011a\u0121\u012a\u013e\u0143\u0147\u014f")
        buf.write("\u0153\u015d\u0166\u0170\u0177\u017b\u0188\u018f\u0196")
        buf.write("\u01a2\u01ad\u01b9\u01c4\u01cf\u01d5\u01db\u01e7\u01ea")
        buf.write("\u01ec\u01f4\u01fd\u0207\u020c\u0218\u0221\u0225\u022d")
        buf.write("\u0232\u023c\u0240\u0248\u0259\u0264\u0281\u0287\u028a")
        buf.write("\u0293\u0299\u029d")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_decl" ):
                return visitor.visitMany_decl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




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
            self.state = 206
            self.match(MiniGoParser.VAR)
            self.state = 207
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 208
                self.primitive_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_arr" ):
                return visitor.visitDecl_arr(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




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
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 226
                self.primitive_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDim" ):
                return visitor.visitDim(self)
            else:
                return visitor.visitChildren(self)




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
            if not(_la==MiniGoParser.INT_LITERAL or _la==MiniGoParser.IDENTIFIER):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEle_list" ):
                return visitor.visitEle_list(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_ele" ):
                return visitor.visitMany_ele(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEle" ):
                return visitor.visitEle(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type" ):
                return visitor.visitStruct_type(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_fields" ):
                return visitor.visitMany_fields(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFields" ):
                return visitor.visitFields(self)
            else:
                return visitor.visitChildren(self)




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
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 277
                self.primitive_type()
                pass
            elif token in [MiniGoParser.LSB]:
                self.state = 278
                self.array_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.IDENTIFIER:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_elements" ):
                return visitor.visitStruct_elements(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_ele" ):
                return visitor.visitStruct_ele(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_type" ):
                return visitor.visitInterface_type(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_interface_field" ):
                return visitor.visitMany_interface_field(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_field" ):
                return visitor.visitInterface_field(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 320
                self.param_list()


            self.state = 323
            self.match(MiniGoParser.RB)
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 332
                self.param_list()


            self.state = 335
            self.match(MiniGoParser.RB)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_stmt" ):
                return visitor.visitMany_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 372
                self.param_list()


            self.state = 375
            self.match(MiniGoParser.RB)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = MiniGoParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_types)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.primitive_type()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.array_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_lit" ):
                return visitor.visitPrimitive_lit(self)
            else:
                return visitor.visitChildren(self)




    def primitive_lit(self):

        localctx = MiniGoParser.Primitive_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_primitive_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
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
        self.enterRule(localctx, 76, self.RULE_literals)
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.NIL_LITERAL, MiniGoParser.INT_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.primitive_lit()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.array_literal()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 467
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 465
                self.expr5()
                pass
            elif token in [MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.NIL_LITERAL, MiniGoParser.LB, MiniGoParser.LSB, MiniGoParser.INT_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.IDENTIFIER]:
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
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_stmt" ):
                return visitor.visitDecl_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsm_stmt" ):
                return visitor.visitAsm_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsm" ):
                return visitor.visitAsm(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_elem" ):
                return visitor.visitArray_elem(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_index_ops" ):
                return visitor.visitMany_index_ops(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_elem" ):
                return visitor.visitStruct_elem(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_struct_ops" ):
                return visitor.visitMany_struct_ops(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_ops" ):
                return visitor.visitStruct_ops(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhs" ):
                return visitor.visitRhs(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.ELSE:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_else_if_stmt" ):
                return visitor.visitMany_else_if_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_stmt" ):
                return visitor.visitElse_if_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_clause" ):
                return visitor.visitFor_clause(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




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
            self.state = 624
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__1 or _la==MiniGoParser.IDENTIFIER):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_elem_call" ):
                return visitor.visitStruct_elem_call(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_struct_ops_call" ):
                return visitor.visitMany_struct_ops_call(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_ops_call" ):
                return visitor.visitStruct_ops_call(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_ops" ):
                return visitor.visitBoolean_ops(self)
            else:
                return visitor.visitChildren(self)




    def boolean_ops(self):

        localctx = MiniGoParser.Boolean_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_boolean_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 671
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
        self.enterRule(localctx, 160, self.RULE_arithmetic_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 673
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
        self.enterRule(localctx, 162, self.RULE_relational_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 675
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
        self.enterRule(localctx, 164, self.RULE_assign_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 677
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEos" ):
                return visitor.visitEos(self)
            else:
                return visitor.visitChildren(self)




    def eos(self):

        localctx = MiniGoParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_eos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 683
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
         




