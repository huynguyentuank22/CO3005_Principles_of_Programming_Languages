import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))

    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))

    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))

    def test_comment(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("//abc\n","<EOF>",105))

    def test_multiline_comment(self):
        """test multiline comment"""
        self.assertTrue(TestLexer.checkLexeme("/*abc\nxyz*/","<EOF>",106))

    def test_nested_comment(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("/*abc/*xyz*/efg*/","<EOF>",107))

    def test_nested_comment_2(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("/*abc*/xyz/*efg*/","xyz,<EOF>",108))

    def test_integer(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("123","123,<EOF>",109))

    def test_integer_2(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("123a","123,a,<EOF>",110))

    def test_decimal_literal(self):
        """test decimal literal"""
        self.assertTrue(TestLexer.checkLexeme("123", "123,<EOF>", 111))

    def test_binary_literal(self):
        """test binary literal"""
        self.assertTrue(TestLexer.checkLexeme("0b101", "0b101,<EOF>", 112))

    def test_octal_literal(self):
        """test octal literal"""
        self.assertTrue(TestLexer.checkLexeme("0o123", "0o123,<EOF>", 113))

    def test_hex_literal(self):
        """test hex literal"""
        self.assertTrue(TestLexer.checkLexeme("0x1A3F", "0x1A3F,<EOF>", 114))

    def test_float_literal(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("1.2 0. 2.0e10 2.3e+7", "1.2,0.,2.0e10,2.3e+7,<EOF>", 115))

    def test_string_literal(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme('"This is a string with a newline\\n"', '"This is a string with a newline\\n",<EOF>', 116))

    def test_unclose_str(self):
        self.assertTrue(TestLexer.checkLexeme('"Hello world', "Unclosed string: Hello world", 117))

    def test_identifier(self):
        """test identifier"""
        self.assertTrue(TestLexer.checkLexeme("userName _tempVar count123", "userName,_tempVar,count123,<EOF>", 118))

    def test_parser(self):
        """test parser"""
        self.assertTrue(TestLexer.checkLexeme("var arr [5]int;", "var,arr,[,5,],int,;,<EOF>", 119))

    def test_assign(self):
        """test assign"""
        self.assertTrue(TestLexer.checkLexeme("a := 5;", "a,:=,5,;,<EOF>", 120))

    def test_arr_literal(self):
        """test arr literal"""
        self.assertTrue(TestLexer.checkLexeme("var arr = [5]int{1, 2, 3, 4, 5};", "var,arr,=,[,5,],int,{,1,,,2,,,3,,,4,,,5,},;,<EOF>", 121))

    def test_struct_literal(self):
        """test struct literal"""
        self.assertTrue(TestLexer.checkLexeme("p := Person{name: \"Alice\", age: 30}", "p,:=,Person,{,name,:,\"Alice\",,,age,:,30,},<EOF>", 122))
        
    