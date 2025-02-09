import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    """
    test comment one line x
    test comment multi line x
    test comment nested x
    test valid identifier x
    test invalid identifier x
    test keyword x
    test operator x
    test separator x
    test decimal literal
    test binary literal
    test octal literal
    test hex literal
    test float literal
    test string literal
    test boolean literal
    test nil literal
    test array type
    test struct type
    test interface type
    test var declaration
    test const declaration
    test function declaration
    test method 
    test expression
    test array access
    test struct access
    test array literal
    test struct literal
    test function call
    test method call
    test assign statement
    test if statement
    test for statement
    test break statement
    test continue statement
    test call statement
    test return statement    
    """
    def test_comment_one_line(self):
        """test comment one line"""
        self.assertTrue(TestLexer.checkLexeme("// This is a comment \n", "<EOF>", 101))

    def test_comment_with_escape(self):
        """test comment with escape"""
        input = "// This is a comment has \\n \\t \\f \\r \\b \\\\"
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 102))

    def test_sequence_comment(self):
        """test sequence comment"""
        input = "// This is a comment // This is a comment // This is a comment"
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 103))
    
    def test_comment_multi_line(self):
        """test comment multi line"""
        input = """
        /* 
        This is a multiline comment 
        This is a multiline comment 
        */
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 104))

    def test_nongreedy_comment(self):
        """test nongreedy comment"""
        input = """
        /* 
        This is a nested comment */ 
        */
        """
        expect = "*,/,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 105))

    def test_nested_comment(self):
        """test nested comment"""
        input = """
        /* 
        This is a /* nested 
            multi-line
            comment */
        abc
        */
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 106))

    def test_nested_comment_2(self):
        """test nested comment"""
        input = """
        /* 
        This is a 
        */ 
        nested
        /* 
        multi-line comment
        */
        """
        expect = "nested,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 107))

    def test_mixed_comment(self):
        """test mixed comment"""
        input = """
        // This is a comment /* abc */
        abc
        /* 
        This is a comment // hello
        */
        """
        expect = "abc,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 108))

    def test_lower_identifier(self):
        """test lower identifier"""
        input = "abc temp flag"
        expect = "abc,temp,flag,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 109))

    def test_upper_identifier(self):
        """test upper identifier"""
        input = "ABC TEMP FLAG"
        expect = "ABC,TEMP,FLAG,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 110))

    def test_alphabet_identifier(self):
        """test alphabet identifier"""
        input = "AbcDef TempFlag HelloWorld"
        expect = "AbcDef,TempFlag,HelloWorld,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 111))

    def test_alphanumeric_identifier(self):
        """test alphanumeric identifier"""
        input = "Abc123 Temp456 Flag789"
        expect = "Abc123,Temp456,Flag789,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 112))

    def test_underscore_identifier(self):
        """test underscore identifier"""
        input = "_name check_Flag _hello_world"
        expect = "_name,check_Flag,_hello_world,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 113))

    def test_invalid_identifier(self):
        """test invalid identifier"""
        input = "123variable my-variable"
        expect = "123,variable,my,-,variable,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 114))

    def test_wrong_identifier(self):
        """test wrong identifier"""
        input = "abc@def"
        expect = "abc,ErrorToken @"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 115))

    def test_escape_identifier(self):
        """test escape identifier"""
        input = "abc\\n"
        expect = "abc,ErrorToken \\"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 116))

    def test_keyword(self):
        """test keyword"""
        input = "if else for struct interface string const var return func int type float boolean continue break range true false"
        expect = "if,else,for,struct,interface,string,const,var,return,func,int,type,float,boolean,continue,break,range,true,false,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 117))

    def test_arithmetic_operator(self):
        """test arithmetic operator"""
        input = "+ - * / %"
        expect = "+,-,*,/,%,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 118))

    def test_relational_operator(self):
        """test relational operator"""
        input = "== != < <= > >="
        expect = "==,!=,<,<=,>,>=,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 119))

    def test_boolean_operator(self):
        """test boolean operator"""
        input = "&& || !"
        expect = "&&,||,!,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 120))

    def test_assignment_operator(self):
        """test assignment operator"""
        input = ":= += -= *= /= %= = ."
        expect = ":=,+=,-=,*=,/=,%=,=,.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 121))

    def test_separator(self):
        """test separator"""
        input = "( ) [ ] { } , ; :"
        expect = "(,),[,],{,},,,;,:,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 122))
    
    def test_decimal_literal(self):
        """test decimal literal"""
        input = "0 42 12345"
        expect = "0,42,12345,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 123))

    def test_binary_literal(self):
        """test binary literal"""
        input = "0b101 0B1101"
        expect = "0b101,0B1101,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 124))

    def test_octal_literal(self):
        """test octal literal"""
        input = "0o12 0O77"
        expect = "0o12,0O77,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 125))

    def test_hex_literal(self):
        """test hex literal"""
        input = "0x1A 0XFF"
        expect = "0x1A,0XFF,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 126))

    def test_float_literal(self):
        """test float literal"""
        input = "3.14 0. 2.0e10 0.e+19 0.111e-19 .e-20"
        expect = "3.14,0.,2.0e10,0.e+19,0.111e-19,.,e,-,20,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 127))

    def test_string_literal(self):
        """test string literal"""
        input = "\"hello\" \"123\""
        expect = "hello,123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 128))

    def test_string_literal_with_esc(self):
        """test string literal"""
        input = "\"This is a string with a newline\\n\""
        expect = "This is a string with a newline\\n,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 129))