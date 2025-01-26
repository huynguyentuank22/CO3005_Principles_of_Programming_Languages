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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u0207\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\6\2h")
        buf.write("\n\2\r\2\16\2i\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3t\n")
        buf.write("\3\3\4\3\4\3\4\5\4y\n\4\3\5\3\5\3\6\5\6~\n\6\3\6\3\6\3")
        buf.write("\6\3\6\5\6\u0084\n\6\3\6\3\6\5\6\u0088\n\6\3\6\5\6\u008b")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\5\b\u0095\n\b\3\b")
        buf.write("\3\b\3\b\5\b\u009a\n\b\3\b\3\b\5\b\u009e\n\b\3\b\3\b\7")
        buf.write("\b\u00a2\n\b\f\b\16\b\u00a5\13\b\3\b\3\b\5\b\u00a9\n\b")
        buf.write("\3\t\3\t\5\t\u00ad\n\t\3\t\3\t\3\t\5\t\u00b2\n\t\3\t\3")
        buf.write("\t\5\t\u00b6\n\t\3\n\3\n\3\n\7\n\u00bb\n\n\f\n\16\n\u00be")
        buf.write("\13\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\7\f\u00c8\n")
        buf.write("\f\f\f\16\f\u00cb\13\f\3\r\3\r\5\r\u00cf\n\r\3\16\3\16")
        buf.write("\3\16\5\16\u00d4\n\16\3\17\3\17\3\20\3\20\3\21\3\21\6")
        buf.write("\21\u00dc\n\21\r\21\16\21\u00dd\3\21\3\21\3\21\5\21\u00e3")
        buf.write("\n\21\3\22\5\22\u00e6\n\22\3\22\3\22\3\22\3\22\5\22\u00ec")
        buf.write("\n\22\3\22\5\22\u00ef\n\22\3\23\3\23\3\23\5\23\u00f4\n")
        buf.write("\23\3\24\3\24\3\24\6\24\u00f9\n\24\r\24\16\24\u00fa\3")
        buf.write("\25\3\25\3\25\3\26\3\26\3\26\3\26\7\26\u0104\n\26\f\26")
        buf.write("\16\26\u0107\13\26\3\26\3\26\3\27\3\27\5\27\u010d\n\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0115\n\30\3\31\3")
        buf.write("\31\3\31\3\31\5\31\u011b\n\31\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\7\33\u0124\n\33\f\33\16\33\u0127\13\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\5\34\u0130\n\34\3\34\5")
        buf.write("\34\u0133\n\34\3\35\3\35\3\35\3\35\3\35\7\35\u013a\n\35")
        buf.write("\f\35\16\35\u013d\13\35\5\35\u013f\n\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \7 \u014e")
        buf.write("\n \f \16 \u0151\13 \3 \3 \3!\3!\3!\5!\u0158\n!\3!\3!")
        buf.write("\5!\u015c\n!\3!\5!\u015f\n!\3\"\3\"\3\"\3\"\3\"\3\"\5")
        buf.write("\"\u0167\n\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\6\"\u0179\n\"\r\"\16\"\u017a\3")
        buf.write("\"\3\"\3\"\7\"\u0180\n\"\f\"\16\"\u0183\13\"\3#\3#\3#")
        buf.write("\3#\3#\3#\5#\u018b\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0196")
        buf.write("\n$\3%\3%\7%\u019a\n%\f%\16%\u019d\13%\3%\3%\3%\5%\u01a2")
        buf.write("\n%\3&\3&\3&\3&\3&\3&\7&\u01aa\n&\f&\16&\u01ad\13&\3&")
        buf.write("\3&\7&\u01b1\n&\f&\16&\u01b4\13&\3&\3&\3&\7&\u01b9\n&")
        buf.write("\f&\16&\u01bc\13&\3&\5&\u01bf\n&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\7\'\u01c8\n\'\f\'\16\'\u01cb\13\'\3\'\3\'\3(\3")
        buf.write("(\3(\3(\7(\u01d3\n(\f(\16(\u01d6\13(\3(\3(\3)\3)\3)\5")
        buf.write(")\u01dd\n)\3*\5*\u01e0\n*\3*\3*\3*\3*\5*\u01e6\n*\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\5.\u01f7\n.\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\63\2\3B\64\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bd\2\t\4")
        buf.write("\288=@\3\2\16\21\4\2\3\3AA\3\2%\'\3\2\32\36\3\2\37$\3")
        buf.write("\2)-\2\u0223\2g\3\2\2\2\4s\3\2\2\2\6x\3\2\2\2\bz\3\2\2")
        buf.write("\2\n}\3\2\2\2\f\u008c\3\2\2\2\16\u0092\3\2\2\2\20\u00ac")
        buf.write("\3\2\2\2\22\u00b7\3\2\2\2\24\u00bf\3\2\2\2\26\u00c4\3")
        buf.write("\2\2\2\30\u00cc\3\2\2\2\32\u00d3\3\2\2\2\34\u00d5\3\2")
        buf.write("\2\2\36\u00d7\3\2\2\2 \u00d9\3\2\2\2\"\u00e5\3\2\2\2$")
        buf.write("\u00f0\3\2\2\2&\u00f8\3\2\2\2(\u00fc\3\2\2\2*\u00ff\3")
        buf.write("\2\2\2,\u010c\3\2\2\2.\u010e\3\2\2\2\60\u0116\3\2\2\2")
        buf.write("\62\u011c\3\2\2\2\64\u0120\3\2\2\2\66\u012a\3\2\2\28\u0134")
        buf.write("\3\2\2\2:\u0142\3\2\2\2<\u0146\3\2\2\2>\u014a\3\2\2\2")
        buf.write("@\u0154\3\2\2\2B\u0166\3\2\2\2D\u018a\3\2\2\2F\u0195\3")
        buf.write("\2\2\2H\u0197\3\2\2\2J\u01a3\3\2\2\2L\u01c0\3\2\2\2N\u01ce")
        buf.write("\3\2\2\2P\u01dc\3\2\2\2R\u01df\3\2\2\2T\u01e7\3\2\2\2")
        buf.write("V\u01ee\3\2\2\2X\u01f1\3\2\2\2Z\u01f4\3\2\2\2\\\u01fa")
        buf.write("\3\2\2\2^\u01fc\3\2\2\2`\u01fe\3\2\2\2b\u0200\3\2\2\2")
        buf.write("d\u0202\3\2\2\2fh\5F$\2gf\3\2\2\2hi\3\2\2\2ig\3\2\2\2")
        buf.write("ij\3\2\2\2jk\3\2\2\2kl\7\2\2\3l\3\3\2\2\2mt\5\16\b\2n")
        buf.write("t\5\n\6\2ot\5\f\7\2pt\5\"\22\2qt\5\62\32\2rt\5<\37\2s")
        buf.write("m\3\2\2\2sn\3\2\2\2so\3\2\2\2sp\3\2\2\2sq\3\2\2\2sr\3")
        buf.write("\2\2\2t\5\3\2\2\2uy\5 \21\2vy\5\60\31\2wy\5.\30\2xu\3")
        buf.write("\2\2\2xv\3\2\2\2xw\3\2\2\2y\7\3\2\2\2z{\5\20\t\2{\t\3")
        buf.write("\2\2\2|~\7\23\2\2}|\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177")
        buf.write("\u0087\7A\2\2\u0080\u0083\5\36\20\2\u0081\u0082\7(\2\2")
        buf.write("\u0082\u0084\5B\"\2\u0083\u0081\3\2\2\2\u0083\u0084\3")
        buf.write("\2\2\2\u0084\u0088\3\2\2\2\u0085\u0086\7(\2\2\u0086\u0088")
        buf.write("\5B\"\2\u0087\u0080\3\2\2\2\u0087\u0085\3\2\2\2\u0088")
        buf.write("\u008a\3\2\2\2\u0089\u008b\7\67\2\2\u008a\u0089\3\2\2")
        buf.write("\2\u008a\u008b\3\2\2\2\u008b\13\3\2\2\2\u008c\u008d\7")
        buf.write("\22\2\2\u008d\u008e\7A\2\2\u008e\u008f\7(\2\2\u008f\u0090")
        buf.write("\5B\"\2\u0090\u0091\7\67\2\2\u0091\r\3\2\2\2\u0092\u0094")
        buf.write("\7\n\2\2\u0093\u0095\5\24\13\2\u0094\u0093\3\2\2\2\u0094")
        buf.write("\u0095\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\7A\2\2")
        buf.write("\u0097\u0099\7/\2\2\u0098\u009a\5\26\f\2\u0099\u0098\3")
        buf.write("\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009d")
        buf.write("\7\60\2\2\u009c\u009e\5\32\16\2\u009d\u009c\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a3\7\61\2")
        buf.write("\2\u00a0\u00a2\5F$\2\u00a1\u00a0\3\2\2\2\u00a2\u00a5\3")
        buf.write("\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a6")
        buf.write("\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a8\7\62\2\2\u00a7")
        buf.write("\u00a9\7\67\2\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9\3\2\2")
        buf.write("\2\u00a9\17\3\2\2\2\u00aa\u00ab\7A\2\2\u00ab\u00ad\7.")
        buf.write("\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae")
        buf.write("\3\2\2\2\u00ae\u00af\7A\2\2\u00af\u00b1\7/\2\2\u00b0\u00b2")
        buf.write("\5\22\n\2\u00b1\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b3\u00b5\7\60\2\2\u00b4\u00b6\7\67\2")
        buf.write("\2\u00b5\u00b4\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\21\3")
        buf.write("\2\2\2\u00b7\u00bc\5B\"\2\u00b8\u00b9\7\65\2\2\u00b9\u00bb")
        buf.write("\5B\"\2\u00ba\u00b8\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\23\3\2\2\2\u00be")
        buf.write("\u00bc\3\2\2\2\u00bf\u00c0\7/\2\2\u00c0\u00c1\7A\2\2\u00c1")
        buf.write("\u00c2\7A\2\2\u00c2\u00c3\7\60\2\2\u00c3\25\3\2\2\2\u00c4")
        buf.write("\u00c9\5\30\r\2\u00c5\u00c6\7\65\2\2\u00c6\u00c8\5\30")
        buf.write("\r\2\u00c7\u00c5\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7")
        buf.write("\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\27\3\2\2\2\u00cb\u00c9")
        buf.write("\3\2\2\2\u00cc\u00ce\7A\2\2\u00cd\u00cf\5\32\16\2\u00ce")
        buf.write("\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\31\3\2\2\2\u00d0")
        buf.write("\u00d4\5\36\20\2\u00d1\u00d4\5$\23\2\u00d2\u00d4\7A\2")
        buf.write("\2\u00d3\u00d0\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d2")
        buf.write("\3\2\2\2\u00d4\33\3\2\2\2\u00d5\u00d6\t\2\2\2\u00d6\35")
        buf.write("\3\2\2\2\u00d7\u00d8\t\3\2\2\u00d8\37\3\2\2\2\u00d9\u00db")
        buf.write("\7A\2\2\u00da\u00dc\5d\63\2\u00db\u00da\3\2\2\2\u00dc")
        buf.write("\u00dd\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2")
        buf.write("\u00de\u00df\3\2\2\2\u00df\u00e0\7(\2\2\u00e0\u00e2\5")
        buf.write("B\"\2\u00e1\u00e3\7\67\2\2\u00e2\u00e1\3\2\2\2\u00e2\u00e3")
        buf.write("\3\2\2\2\u00e3!\3\2\2\2\u00e4\u00e6\7\23\2\2\u00e5\u00e4")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7")
        buf.write("\u00eb\7A\2\2\u00e8\u00ec\5$\23\2\u00e9\u00ea\7(\2\2\u00ea")
        buf.write("\u00ec\5(\25\2\u00eb\u00e8\3\2\2\2\u00eb\u00e9\3\2\2\2")
        buf.write("\u00ec\u00ee\3\2\2\2\u00ed\u00ef\7\67\2\2\u00ee\u00ed")
        buf.write("\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef#\3\2\2\2\u00f0\u00f3")
        buf.write("\5&\24\2\u00f1\u00f4\5\36\20\2\u00f2\u00f4\7A\2\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4%\3\2\2\2\u00f5")
        buf.write("\u00f6\7\63\2\2\u00f6\u00f7\78\2\2\u00f7\u00f9\7\64\2")
        buf.write("\2\u00f8\u00f5\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\'\3\2\2\2\u00fc\u00fd")
        buf.write("\5$\23\2\u00fd\u00fe\5*\26\2\u00fe)\3\2\2\2\u00ff\u0100")
        buf.write("\7\61\2\2\u0100\u0105\5,\27\2\u0101\u0102\7\65\2\2\u0102")
        buf.write("\u0104\5,\27\2\u0103\u0101\3\2\2\2\u0104\u0107\3\2\2\2")
        buf.write("\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0108\3")
        buf.write("\2\2\2\u0107\u0105\3\2\2\2\u0108\u0109\7\62\2\2\u0109")
        buf.write("+\3\2\2\2\u010a\u010d\5*\26\2\u010b\u010d\5\34\17\2\u010c")
        buf.write("\u010a\3\2\2\2\u010c\u010b\3\2\2\2\u010d-\3\2\2\2\u010e")
        buf.write("\u010f\7A\2\2\u010f\u0110\7.\2\2\u0110\u0111\7A\2\2\u0111")
        buf.write("\u0112\7(\2\2\u0112\u0114\5B\"\2\u0113\u0115\7\67\2\2")
        buf.write("\u0114\u0113\3\2\2\2\u0114\u0115\3\2\2\2\u0115/\3\2\2")
        buf.write("\2\u0116\u0117\7A\2\2\u0117\u0118\7(\2\2\u0118\u011a\5")
        buf.write("8\35\2\u0119\u011b\7\67\2\2\u011a\u0119\3\2\2\2\u011a")
        buf.write("\u011b\3\2\2\2\u011b\61\3\2\2\2\u011c\u011d\7\13\2\2\u011d")
        buf.write("\u011e\7A\2\2\u011e\u011f\5\64\33\2\u011f\63\3\2\2\2\u0120")
        buf.write("\u0121\7\f\2\2\u0121\u0125\7\61\2\2\u0122\u0124\5\66\34")
        buf.write("\2\u0123\u0122\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123")
        buf.write("\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0128\3\2\2\2\u0127")
        buf.write("\u0125\3\2\2\2\u0128\u0129\7\62\2\2\u0129\65\3\2\2\2\u012a")
        buf.write("\u012f\7A\2\2\u012b\u0130\5\36\20\2\u012c\u0130\5$\23")
        buf.write("\2\u012d\u0130\5\64\33\2\u012e\u0130\7A\2\2\u012f\u012b")
        buf.write("\3\2\2\2\u012f\u012c\3\2\2\2\u012f\u012d\3\2\2\2\u012f")
        buf.write("\u012e\3\2\2\2\u0130\u0132\3\2\2\2\u0131\u0133\7\67\2")
        buf.write("\2\u0132\u0131\3\2\2\2\u0132\u0133\3\2\2\2\u0133\67\3")
        buf.write("\2\2\2\u0134\u0135\7A\2\2\u0135\u013e\7\61\2\2\u0136\u013b")
        buf.write("\5:\36\2\u0137\u0138\7\65\2\2\u0138\u013a\5:\36\2\u0139")
        buf.write("\u0137\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2")
        buf.write("\u013b\u013c\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3")
        buf.write("\2\2\2\u013e\u0136\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140")
        buf.write("\3\2\2\2\u0140\u0141\7\62\2\2\u01419\3\2\2\2\u0142\u0143")
        buf.write("\7A\2\2\u0143\u0144\7\66\2\2\u0144\u0145\5B\"\2\u0145")
        buf.write(";\3\2\2\2\u0146\u0147\7\13\2\2\u0147\u0148\7A\2\2\u0148")
        buf.write("\u0149\5> \2\u0149=\3\2\2\2\u014a\u014b\7\r\2\2\u014b")
        buf.write("\u014f\7\61\2\2\u014c\u014e\5@!\2\u014d\u014c\3\2\2\2")
        buf.write("\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3")
        buf.write("\2\2\2\u0150\u0152\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u0153")
        buf.write("\7\62\2\2\u0153?\3\2\2\2\u0154\u0155\7A\2\2\u0155\u0157")
        buf.write("\7/\2\2\u0156\u0158\5\26\f\2\u0157\u0156\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015b\7\60\2")
        buf.write("\2\u015a\u015c\5\32\16\2\u015b\u015a\3\2\2\2\u015b\u015c")
        buf.write("\3\2\2\2\u015c\u015e\3\2\2\2\u015d\u015f\7\67\2\2\u015e")
        buf.write("\u015d\3\2\2\2\u015e\u015f\3\2\2\2\u015fA\3\2\2\2\u0160")
        buf.write("\u0161\b\"\1\2\u0161\u0162\7\'\2\2\u0162\u0167\5B\"\7")
        buf.write("\u0163\u0164\7\33\2\2\u0164\u0167\5B\"\6\u0165\u0167\5")
        buf.write("D#\2\u0166\u0160\3\2\2\2\u0166\u0163\3\2\2\2\u0166\u0165")
        buf.write("\3\2\2\2\u0167\u0181\3\2\2\2\u0168\u0169\f\13\2\2\u0169")
        buf.write("\u016a\7&\2\2\u016a\u0180\5B\"\f\u016b\u016c\f\n\2\2\u016c")
        buf.write("\u016d\7%\2\2\u016d\u0180\5B\"\13\u016e\u016f\f\t\2\2")
        buf.write("\u016f\u0170\5`\61\2\u0170\u0171\5B\"\n\u0171\u0180\3")
        buf.write("\2\2\2\u0172\u0173\f\b\2\2\u0173\u0174\5^\60\2\u0174\u0175")
        buf.write("\5B\"\t\u0175\u0180\3\2\2\2\u0176\u0178\f\5\2\2\u0177")
        buf.write("\u0179\5d\63\2\u0178\u0177\3\2\2\2\u0179\u017a\3\2\2\2")
        buf.write("\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u0180\3")
        buf.write("\2\2\2\u017c\u017d\f\4\2\2\u017d\u017e\7.\2\2\u017e\u0180")
        buf.write("\7A\2\2\u017f\u0168\3\2\2\2\u017f\u016b\3\2\2\2\u017f")
        buf.write("\u016e\3\2\2\2\u017f\u0172\3\2\2\2\u017f\u0176\3\2\2\2")
        buf.write("\u017f\u017c\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3")
        buf.write("\2\2\2\u0181\u0182\3\2\2\2\u0182C\3\2\2\2\u0183\u0181")
        buf.write("\3\2\2\2\u0184\u018b\7A\2\2\u0185\u018b\5\34\17\2\u0186")
        buf.write("\u0187\7/\2\2\u0187\u0188\5B\"\2\u0188\u0189\7\60\2\2")
        buf.write("\u0189\u018b\3\2\2\2\u018a\u0184\3\2\2\2\u018a\u0185\3")
        buf.write("\2\2\2\u018a\u0186\3\2\2\2\u018bE\3\2\2\2\u018c\u0196")
        buf.write("\5\4\3\2\u018d\u0196\5\6\4\2\u018e\u0196\5\b\5\2\u018f")
        buf.write("\u0196\5H%\2\u0190\u0196\5J&\2\u0191\u0196\5N(\2\u0192")
        buf.write("\u0196\5V,\2\u0193\u0196\5X-\2\u0194\u0196\5Z.\2\u0195")
        buf.write("\u018c\3\2\2\2\u0195\u018d\3\2\2\2\u0195\u018e\3\2\2\2")
        buf.write("\u0195\u018f\3\2\2\2\u0195\u0190\3\2\2\2\u0195\u0191\3")
        buf.write("\2\2\2\u0195\u0192\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0194")
        buf.write("\3\2\2\2\u0196G\3\2\2\2\u0197\u019b\7A\2\2\u0198\u019a")
        buf.write("\5d\63\2\u0199\u0198\3\2\2\2\u019a\u019d\3\2\2\2\u019b")
        buf.write("\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019e\3\2\2\2")
        buf.write("\u019d\u019b\3\2\2\2\u019e\u019f\5b\62\2\u019f\u01a1\5")
        buf.write("B\"\2\u01a0\u01a2\7\67\2\2\u01a1\u01a0\3\2\2\2\u01a1\u01a2")
        buf.write("\3\2\2\2\u01a2I\3\2\2\2\u01a3\u01a4\7\6\2\2\u01a4\u01a5")
        buf.write("\7/\2\2\u01a5\u01a6\5B\"\2\u01a6\u01a7\7\60\2\2\u01a7")
        buf.write("\u01ab\7\61\2\2\u01a8\u01aa\5F$\2\u01a9\u01a8\3\2\2\2")
        buf.write("\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3")
        buf.write("\2\2\2\u01ac\u01ae\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae\u01b2")
        buf.write("\7\62\2\2\u01af\u01b1\5L\'\2\u01b0\u01af\3\2\2\2\u01b1")
        buf.write("\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2")
        buf.write("\u01b3\u01be\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01b6\7")
        buf.write("\7\2\2\u01b6\u01ba\7\61\2\2\u01b7\u01b9\5F$\2\u01b8\u01b7")
        buf.write("\3\2\2\2\u01b9\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba")
        buf.write("\u01bb\3\2\2\2\u01bb\u01bd\3\2\2\2\u01bc\u01ba\3\2\2\2")
        buf.write("\u01bd\u01bf\7\62\2\2\u01be\u01b5\3\2\2\2\u01be\u01bf")
        buf.write("\3\2\2\2\u01bfK\3\2\2\2\u01c0\u01c1\7\7\2\2\u01c1\u01c2")
        buf.write("\7\6\2\2\u01c2\u01c3\7/\2\2\u01c3\u01c4\5B\"\2\u01c4\u01c5")
        buf.write("\7\60\2\2\u01c5\u01c9\7\61\2\2\u01c6\u01c8\5F$\2\u01c7")
        buf.write("\u01c6\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9\u01c7\3\2\2\2")
        buf.write("\u01c9\u01ca\3\2\2\2\u01ca\u01cc\3\2\2\2\u01cb\u01c9\3")
        buf.write("\2\2\2\u01cc\u01cd\7\62\2\2\u01cdM\3\2\2\2\u01ce\u01cf")
        buf.write("\7\b\2\2\u01cf\u01d0\5P)\2\u01d0\u01d4\7\61\2\2\u01d1")
        buf.write("\u01d3\5F$\2\u01d2\u01d1\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4")
        buf.write("\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d7\3\2\2\2")
        buf.write("\u01d6\u01d4\3\2\2\2\u01d7\u01d8\7\62\2\2\u01d8O\3\2\2")
        buf.write("\2\u01d9\u01dd\5B\"\2\u01da\u01dd\5R*\2\u01db\u01dd\5")
        buf.write("T+\2\u01dc\u01d9\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01db")
        buf.write("\3\2\2\2\u01ddQ\3\2\2\2\u01de\u01e0\5\n\6\2\u01df\u01de")
        buf.write("\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1")
        buf.write("\u01e2\7\67\2\2\u01e2\u01e3\5B\"\2\u01e3\u01e5\7\67\2")
        buf.write("\2\u01e4\u01e6\5H%\2\u01e5\u01e4\3\2\2\2\u01e5\u01e6\3")
        buf.write("\2\2\2\u01e6S\3\2\2\2\u01e7\u01e8\t\4\2\2\u01e8\u01e9")
        buf.write("\7\65\2\2\u01e9\u01ea\7A\2\2\u01ea\u01eb\7(\2\2\u01eb")
        buf.write("\u01ec\7\26\2\2\u01ec\u01ed\7A\2\2\u01edU\3\2\2\2\u01ee")
        buf.write("\u01ef\7\25\2\2\u01ef\u01f0\7\67\2\2\u01f0W\3\2\2\2\u01f1")
        buf.write("\u01f2\7\24\2\2\u01f2\u01f3\7\67\2\2\u01f3Y\3\2\2\2\u01f4")
        buf.write("\u01f6\7\t\2\2\u01f5\u01f7\5B\"\2\u01f6\u01f5\3\2\2\2")
        buf.write("\u01f6\u01f7\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01f9\7")
        buf.write("\67\2\2\u01f9[\3\2\2\2\u01fa\u01fb\t\5\2\2\u01fb]\3\2")
        buf.write("\2\2\u01fc\u01fd\t\6\2\2\u01fd_\3\2\2\2\u01fe\u01ff\t")
        buf.write("\7\2\2\u01ffa\3\2\2\2\u0200\u0201\t\b\2\2\u0201c\3\2\2")
        buf.write("\2\u0202\u0203\7\63\2\2\u0203\u0204\5B\"\2\u0204\u0205")
        buf.write("\7\64\2\2\u0205e\3\2\2\2;isx}\u0083\u0087\u008a\u0094")
        buf.write("\u0099\u009d\u00a3\u00a8\u00ac\u00b1\u00b5\u00bc\u00c9")
        buf.write("\u00ce\u00d3\u00dd\u00e2\u00e5\u00eb\u00ee\u00f3\u00fa")
        buf.write("\u0105\u010c\u0114\u011a\u0125\u012f\u0132\u013b\u013e")
        buf.write("\u014f\u0157\u015b\u015e\u0166\u017a\u017f\u0181\u018a")
        buf.write("\u0195\u019b\u01a1\u01ab\u01b2\u01ba\u01be\u01c9\u01d4")
        buf.write("\u01dc\u01df\u01e5\u01f6")
        return buf.getvalue()


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
                     "<INVALID>", "<INVALID>", "'\n'" ]

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

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


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
            self.state = 101 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 100
                self.stmt()
                self.state = 103 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.VAR:
                self.state = 122
                self.match(MiniGoParser.VAR)


            self.state = 125
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 126
                self.primitive_type()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 127
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 128
                    self.expr(0)


                pass
            elif token in [MiniGoParser.ASSIGN]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.LB:
                self.state = 145
                self.method()


            self.state = 148
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 149
            self.match(MiniGoParser.LB)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 150
                self.param_list()


            self.state = 153
            self.match(MiniGoParser.RB)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 154
                self.types()


            self.state = 157
            self.match(MiniGoParser.LCB)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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
            if _la==MiniGoParser.SEMICOLON:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 174
                self.args()


            self.state = 177
            self.match(MiniGoParser.RB)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOLON:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = MiniGoParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_types)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.primitive_type()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.array_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = MiniGoParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_array" ):
                return visitor.visitAssign_array(self)
            else:
                return visitor.visitChildren(self)




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
                if not (_la==MiniGoParser.LSB):
                    break

            self.state = 221
            self.match(MiniGoParser.ASSIGN)
            self.state = 222
            self.expr(0)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOLON:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = MiniGoParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_array_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.VAR:
                self.state = 226
                self.match(MiniGoParser.VAR)


            self.state = 229
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LSB]:
                self.state = 230
                self.array_type()
                pass
            elif token in [MiniGoParser.ASSIGN]:
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
            if _la==MiniGoParser.SEMICOLON:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




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
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 239
                self.primitive_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




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
                if not (_la==MiniGoParser.LSB):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEle_list" ):
                return visitor.visitEle_list(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEle" ):
                return visitor.visitEle(self)
            else:
                return visitor.visitChildren(self)




    def ele(self):

        localctx = MiniGoParser.EleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_ele)
        try:
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LCB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.ele_list()
                pass
            elif token in [MiniGoParser.INT_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.NIL_LITERAL]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess_struct" ):
                return visitor.visitAccess_struct(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.SEMICOLON:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_struct" ):
                return visitor.visitAssign_struct(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.SEMICOLON:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type" ):
                return visitor.visitStruct_type(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.IDENTIFIER:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFields" ):
                return visitor.visitFields(self)
            else:
                return visitor.visitChildren(self)




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
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 297
                self.primitive_type()
                pass
            elif token in [MiniGoParser.LSB]:
                self.state = 298
                self.array_type()
                pass
            elif token in [MiniGoParser.STRUCT]:
                self.state = 299
                self.struct_type()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.state = 300
                self.match(MiniGoParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOLON:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 308
                self.field_lit()
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_lit" ):
                return visitor.visitField_lit(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_type" ):
                return visitor.visitInterface_type(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.IDENTIFIER:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.IDENTIFIER:
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
            if _la==MiniGoParser.SEMICOLON:
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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT]:
                self.state = 351
                self.match(MiniGoParser.NOT)
                self.state = 352
                self.expr(5)
                pass
            elif token in [MiniGoParser.SUB]:
                self.state = 353
                self.match(MiniGoParser.SUB)
                self.state = 354
                self.expr(4)
                pass
            elif token in [MiniGoParser.LB, MiniGoParser.INT_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.NIL_LITERAL, MiniGoParser.IDENTIFIER]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expr" ):
                return visitor.visitPrimary_expr(self)
            else:
                return visitor.visitChildren(self)




    def primary_expr(self):

        localctx = MiniGoParser.Primary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_primary_expr)
        try:
            self.state = 392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.INT_LITERAL, MiniGoParser.FLOAT_LITERAL, MiniGoParser.STRING_LITERAL, MiniGoParser.BOOLEAN_LITERAL, MiniGoParser.NIL_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.literals()
                pass
            elif token in [MiniGoParser.LB]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsm_stmt" ):
                return visitor.visitAsm_stmt(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.LSB:
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
            if _la==MiniGoParser.SEMICOLON:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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
            if _la==MiniGoParser.ELSE:
                self.state = 435
                self.match(MiniGoParser.ELSE)
                self.state = 436
                self.match(MiniGoParser.LCB)
                self.state = 440
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_stmt" ):
                return visitor.visitElse_if_stmt(self)
            else:
                return visitor.visitChildren(self)




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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_clause" ):
                return visitor.visitFor_clause(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFully_clause" ):
                return visitor.visitFully_clause(self)
            else:
                return visitor.visitChildren(self)




    def fully_clause(self):

        localctx = MiniGoParser.Fully_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_fully_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.VAR or _la==MiniGoParser.IDENTIFIER:
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
            if _la==MiniGoParser.IDENTIFIER:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_clause" ):
                return visitor.visitRange_clause(self)
            else:
                return visitor.visitChildren(self)




    def range_clause(self):

        localctx = MiniGoParser.Range_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_range_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__0 or _la==MiniGoParser.IDENTIFIER):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LB) | (1 << MiniGoParser.INT_LITERAL) | (1 << MiniGoParser.FLOAT_LITERAL) | (1 << MiniGoParser.STRING_LITERAL) | (1 << MiniGoParser.BOOLEAN_LITERAL) | (1 << MiniGoParser.NIL_LITERAL) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_ops" ):
                return visitor.visitBoolean_ops(self)
            else:
                return visitor.visitChildren(self)




    def boolean_ops(self):

        localctx = MiniGoParser.Boolean_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_boolean_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
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
        self.enterRule(localctx, 92, self.RULE_arithmetic_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
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
        self.enterRule(localctx, 94, self.RULE_relational_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
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
        self.enterRule(localctx, 96, self.RULE_assign_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.PLUS_ASSIGN) | (1 << MiniGoParser.MINUS_ASSIGN) | (1 << MiniGoParser.MULT_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
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
         




