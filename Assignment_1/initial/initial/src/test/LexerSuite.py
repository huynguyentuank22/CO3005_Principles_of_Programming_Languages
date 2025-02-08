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
        self.assertTrue(TestLexer.checkLexeme("func abc ( ) {a};","""func,abc,(,),{,a,},;,<EOF>""",104))

    def test_comment(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("//abc\n","<EOF>",105))

    def test_comment_oneline(self):
        """test comment oneline"""
        self.assertTrue(TestLexer.checkLexeme("//abc","<EOF>",106))

    def test_multiline_comment(self):
        """test multiline comment"""
        self.assertTrue(TestLexer.checkLexeme("/*abc\nxyz*/","<EOF>",107))

    def test_nested_comment(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("/*abc/*xyz*/efg*/","<EOF>",108))

    def test_nested_comment_2(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("/*abc*/xyz/*efg*/","xyz,<EOF>",109))
    
    def test_nested_comment_3(self):
        """test nested comment"""
        self.assertTrue(TestLexer.checkLexeme("/*abc/*def*/*/","<EOF>",110))
    
    def test_integer(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("123","123,<EOF>",111))
    
    def test_integer_2(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("123a","123,a,<EOF>",112))
    
    def test_decimal_literal(self):
        """test decimal literal"""
        self.assertTrue(TestLexer.checkLexeme("123", "123,<EOF>", 113))

    def test_integer_literal(self):
        """test integer literal"""
        self.assertTrue(TestLexer.checkLexeme("123","123,<EOF>",114))
    
    def test_binary_literal(self):
        """test binary literal"""
        self.assertTrue(TestLexer.checkLexeme("0b101", "0b101,<EOF>", 115))

    def test_bin_literal(self):
        """test binary literal"""
        self.assertTrue(TestLexer.checkLexeme("0b110","0b110,<EOF>",116))
    
    def test_octal_literal(self):
        """test octal literal"""
        self.assertTrue(TestLexer.checkLexeme("0o123", "0o123,<EOF>", 117))

    def test_oct_literal(self):
        """test octal literal"""
        self.assertTrue(TestLexer.checkLexeme("0o123","0o123,<EOF>",118))
    
    def test_hex_literal(self):
        """test hex literal"""
        self.assertTrue(TestLexer.checkLexeme("0x1A3F", "0x1A3F,<EOF>", 119))
    
    def test_float_literal(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("1.2 0. 2.0e10 2.3e+7", "1.2,0.,2.0e10,2.3e+7,<EOF>", 120))
    
    def test_float_lit(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("123.123","123.123,<EOF>",121))
    
    def test_float_lit_with_exp(self):
        """test float literal with exponent"""
        self.assertTrue(TestLexer.checkLexeme("123.123e123","123.123e123,<EOF>",122))
    
    def test_string_literal(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme('"This is a string with a newline\\n"', '"This is a string with a newline\\n",<EOF>', 123))
    
    def test_str_lit(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme("\"abc\"","\"abc\",<EOF>",124))
    
    def test_str_lit_with_escape(self):
        """test string literal with escape"""
        self.assertTrue(TestLexer.checkLexeme("\"abc\\n\"","\"abc\\n\",<EOF>",125))
    
    def test_unclose_str(self):
        self.assertTrue(TestLexer.checkLexeme('"Hello world', "Unclosed string: Hello world", 126))
    
    def test_identifier(self):
        """test identifier"""
        self.assertTrue(TestLexer.checkLexeme("userName _tempVar count123", "userName,_tempVar,count123,<EOF>", 127))
    
    def test_parser(self):
        """test parser"""
        self.assertTrue(TestLexer.checkLexeme("var arr [5]int;", "var,arr,[,5,],int,;,<EOF>", 128))
    
    def test_assign(self):
        """test assign"""
        self.assertTrue(TestLexer.checkLexeme("a := 5;", "a,:=,5,;,<EOF>", 129))
    
    def test_arr_literal(self):
        """test arr literal"""
        self.assertTrue(TestLexer.checkLexeme("var arr = [5]int{1, 2, 3, 4, 5};", "var,arr,=,[,5,],int,{,1,,,2,,,3,,,4,,,5,},;,<EOF>", 130))
    
    def test_struct_literal(self):
        """test struct literal"""
        self.assertTrue(TestLexer.checkLexeme("p := Person{name: \"Alice\", age: 30}", "p,:=,Person,{,name,:,\"Alice\",,,age,:,30,},<EOF>", 131))

    def test_newline(self):
        """test newline"""
        input = """abc

        """
        expect = "abc,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,132))

    def test_newline_2(self):
        """test newline"""
        input = """abc /*abc
        
        */
        def;
        """
        expect = "abc,;,def,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,133))
