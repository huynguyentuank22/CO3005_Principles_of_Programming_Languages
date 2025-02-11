import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    """
    Lexer test suite   
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
        input = "if else for struct interface string const var return func int type float boolean continue break range nil true false"
        expect = "if,else,for,struct,interface,string,const,var,return,func,int,type,float,boolean,continue,break,range,nil,true,false,<EOF>"
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
        input = "( ) [ ] { } , ;"
        expect = "(,),[,],{,},,,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 122))

    def test_separator_2(self):
        """test separator"""
        input = """
        (name, age)
        [123, 456, 789]
        {true, nil}
        """
        expect = "(,name,,,age,),;,[,123,,,456,,,789,],;,{,true,,,nil,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 123))
    
    def test_decimal_literal(self):
        """test decimal literal"""
        input = "0 42 12345"
        expect = "0,42,12345,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 124))

    def test_binary_literal(self):
        """test binary literal"""
        input = "0b101 0B1101"
        expect = "0b101,0B1101,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 125))

    def test_octal_literal(self):
        """test octal literal"""
        input = "0o12 0O77"
        expect = "0o12,0O77,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 126))

    def test_hex_literal(self):
        """test hex literal"""
        input = "0x1A 0XFF"
        expect = "0x1A,0XFF,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 127))

    def test_float_literal(self):
        """test float literal"""
        input = "3.14 0. 2.0e10 0.e+19 0.111e-19 .e-20"
        expect = "3.14,0.,2.0e10,0.e+19,0.111e-19,.,e,-,20,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 128))

    def test_string_literal(self):
        """test string literal"""
        input = "\"hello\" \"123\""
        expect = "hello,123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 129))

    def test_string_literal_with_valid_esc(self):
        input = '\"Hello World \\t \\r \\n \\" \\\\\"'
        expect = 'Hello World \\t \\r \\n \\" \\\\,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 130))

    def test_string_literal_with_unvalid_esc(self):
        input = r"\"Hello \ World\""
        expect = "ErrorToken \\"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 131))

    def test_mulitple_string(self):
        input = '"Hello" "World"'
        expect = "Hello,World,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 132))

    def test_unclosed_string(self):
        input = '"Hello world'
        expect = 'Unclosed string: "Hello world'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 133))
    
    def test_multiple_unclosed_string(self):
        input = '"Hello world" "Goodbye world'
        expect = 'Hello world,Unclosed string: "Goodbye world'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 134))

    def test_illegal_escape(self):
        input = '"Hello \\a world"'
        expect = 'Illegal escape in string: Hello \\a'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 135))

    def test_complex_string(self):
        input = '"This is a complex string with \\"quote\\" and has comment /*abcd*/"'
        expect = 'This is a complex string with \\"quote\\" and has comment /*abcd*/,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 136))

    def test_array_type(self):
        input = "var arr [5]int; /* defines an array of 5 integers. */"
        expect = "var,arr,[,5,],int,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 137))

    def test_array_type_2(self):
        input = "var multi_arr [2][5]int; // defines an array of 2 x 5 integers."
        expect = "var,multi_arr,[,2,],[,5,],int,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 138))

    def test_array_type_3(self):
        input = "var arr [3]int {1, 2, 3};"
        expect = "var,arr,[,3,],int,{,1,,,2,,,3,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 139))

    def test_array_type_4(self):
        input = "marr := [2][3]int{{1, 2, 3}, {4, 5, 6}};"
        expect = "marr,:=,[,2,],[,3,],int,{,{,1,,,2,,,3,},,,{,4,,,5,,,6,},},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 140))

    def test_access_array(self):
        input = "a[2][3] := b[2] + 1;"
        expect = "a,[,2,],[,3,],:=,b,[,2,],+,1,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 141))

    def test_struct_type(self):
        input = """
        type Person struct {
            name string ;
            age int ;
        }
        """
        expect = "type,Person,struct,{,name,string,;,age,int,;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 142))

    def test_struct_type_2(self):
        input = 'p := Person{name: "Alice", age: 30}'
        expect = 'p,:=,Person,{,name,:,Alice,,,age,:,30,},<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 143))

    def test_struct_type_3(self):
        input = 'p := Person{}'
        expect = 'p,:=,Person,{,},<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 144))

    def test_access_struct(self):
        input = """
        PutStringLn(p.name); // Output: Alice
        PutIntLn(p.age); // Output: 30
        """
        expect = 'PutStringLn,(,p,.,name,),;,PutIntLn,(,p,.,age,),;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 145))

    def test_modify_struct(self):
        input = """
        p.age := 31;
        p.name := "Alice";
        """
        expect = 'p,.,age,:=,31,;,p,.,name,:=,Alice,;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 146))

    def test_access_method(self):
        input = 'PutStringLn(p.Greet()); // Output: Hello, Alice'
        expect = 'PutStringLn,(,p,.,Greet,(,),),;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 147))

    def test_mixed_access(self):
        input = 'a.foo().bar()[4]'
        expect = 'a,.,foo,(,),.,bar,(,),[,4,],<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 148))

    def test_mixed_access_2(self):
        input = 'Student[4].age().name'
        expect = 'Student,[,4,],.,age,(,),.,name,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 149))

    def test_interface_type(self):
        input = """
        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset()
            SayHello(name string)
        }
        """
        expect = 'type,Calculator,interface,{,Add,(,x,,,y,int,),int,;,Subtract,(,a,,,b,float,,,c,int,),float,;,Reset,(,),;,SayHello,(,name,string,),;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 150))

    def test_var_decl(self):
        input = "var x int = 10;"
        expect = "var,x,int,=,10,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 151))
    
    def test_var_decl_2(self):
        input = 'var y = "Hello";'
        expect = 'var,y,=,Hello,;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 152))

    def test_var_decl_3(self):
        input = 'var z float;'
        expect = 'var,z,float,;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 153))

    def test_const_decl(self):
        input = "const Pi = 3.14;"
        expect = "const,Pi,=,3.14,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 154))

    def test_const_decl_2(self):
        input = 'const Greeting = "Hello, MiniGo!";'
        expect = 'const,Greeting,=,Hello, MiniGo!,;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 155))

    def test_const_decl_3(self):
        input = 'const MaxSize = 100 + 50;'
        expect = 'const,MaxSize,=,100,+,50,;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 156))

    def test_func_decl(self):
        input = """
        func Add(x int, y int) int {
            return x + y;
        }
        """
        expect = 'func,Add,(,x,int,,,y,int,),int,{,return,x,+,y,;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 157))

    def test_method_decl(self):
        input = """
        func (c Calculator) Add(x int) int {
            c.value += x;
            return c.value;
        }
        """
        expect = 'func,(,c,Calculator,),Add,(,x,int,),int,{,c,.,value,+=,x,;,return,c,.,value,;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 158))

    def test_method_decl_2(self):
        input = """
        func (p Person) Greet() string {
            return "Hello, " + p.name;
        }
        """
        expect = 'func,(,p,Person,),Greet,(,),string,{,return,Hello, ,+,p,.,name,;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 159))

    def test_func_call(self):
        input = """
        add(1, 2);
        reset();
        """
        expect = 'add,(,1,,,2,),;,reset,(,),;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 160))

    def test_func_call_2(self):
        input = "add(2 + x, 4 / y, 5);"
        expect = "add,(,2,+,x,,,4,/,y,,,5,),;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 161))

    def test_nested_func_call(self):
        input = """
        add(sub(3, 4), 5);
        """
        expect = 'add,(,sub,(,3,,,4,),,,5,),;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 162))

    def test_method_call(self):
        input = """
        calculator.add(3, 4);
        calculator.reset();
        """
        expect = 'calculator,.,add,(,3,,,4,),;,calculator,.,reset,(,),;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 163))
    
    def test_nested_method_call(self):
        input = """
        calculator.add(calculator.sub(3, 4), 5);
        calculator.reset();
        """
        expect = 'calculator,.,add,(,calculator,.,sub,(,3,,,4,),,,5,),;,calculator,.,reset,(,),;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 164))
    
    def test_expression(self):
        input = "a + b * c / d - e % f"
        expect = "a,+,b,*,c,/,d,-,e,%,f,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 165))

    def test_expression_2(self):
        input = "a && b || c && d || !e"
        expect = "a,&&,b,||,c,&&,d,||,!,e,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 166))
    
    def test_expression_3(self):
        input = "a == b && c != d || e < f || g >= h"
        expect = "a,==,b,&&,c,!=,d,||,e,<,f,||,g,>=,h,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 167))

    def test_full_op_expr(self):
        input = "(a + b * c / d - e % f) == g && h.age > 18 || arr[i] < arr[j]"
        expect = "(,a,+,b,*,c,/,d,-,e,%,f,),==,g,&&,h,.,age,>,18,||,arr,[,i,],<,arr,[,j,],<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 168))

    def test_if_statement(self):
        input = """
        if a > b {
            return a;
        }
        """
        expect = 'if,a,>,b,{,return,a,;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 169))

    def test_if_else_statement(self):
        input = """
        if a > b {
            return a;
        } else {
            return b;
        }
        """
        expect = 'if,a,>,b,{,return,a,;,},else,{,return,b,;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 170))

    def test_if_elif_statement(self):
        input = """
        if (x > 10) {
            println("x is greater than 10");
        } else if (x == 10) {
            println("x is equal to 10");
        }
        """
        expect = 'if,(,x,>,10,),{,println,(,x is greater than 10,),;,},else,if,(,x,==,10,),{,println,(,x is equal to 10,),;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 171))

    def test_if_elif_else_statement(self):
        input = """
        if (x > 10) {
            println("x is greater than 10");
        } else if (x == 10) {
            println("x is equal to 10");
        } else {
            println("x is less than 10");
        }
        """
        expect = 'if,(,x,>,10,),{,println,(,x is greater than 10,),;,},else,if,(,x,==,10,),{,println,(,x is equal to 10,),;,},else,{,println,(,x is less than 10,),;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 172))

    def test_nested_if_statement(self):
        input = """
        if (x > 5) {
            if (x < 10) {
                println("x is between 5 and 10");
            }
        }
        """
        expect = 'if,(,x,>,5,),{,if,(,x,<,10,),{,println,(,x is between 5 and 10,),;,},;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 173))

    def test_nested_if_else_statement(self):
        input = """
        if (x > 5) {
            if (x < 10) {
                println("x is between 5 and 10");
            } else {
                println("x is greater than 10");
            }
        }
        else {
            println("x is less than 5");
        }
        """
        expect = 'if,(,x,>,5,),{,if,(,x,<,10,),{,println,(,x is between 5 and 10,),;,},else,{,println,(,x is greater than 10,),;,},;,},;,else,{,println,(,x is less than 5,),;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 174))

    def test_basic_for_statement(self):
        input = """
        for i < 10 {
            // loop body
            i += 1;
        }
        """
        expect = 'for,i,<,10,{,i,+=,1,;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 175))

    def test_not_full_for_statement(self):
        input = """
        for i := 0; i < 10; {
            i += 1;
            sum += i; // loop body
        }
        """
        expect = 'for,i,:=,0,;,i,<,10,;,{,i,+=,1,;,sum,+=,i,;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 176))

    def test_not_full_for_statement_2(self):
        input = """
        var i = 0;
        for ; i < 10; i += 1 {
            sum += i; // loop body
        }
        """
        expect = 'var,i,=,0,;,for,;,i,<,10,;,i,+=,1,{,sum,+=,i,;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 177))

    def test_full_for_statement(self):
        input = """
        for i := 0; i < 10; i += 1 {
            sum += i; // loop body
        }
        """
        expect = 'for,i,:=,0,;,i,<,10,;,i,+=,1,{,sum,+=,i,;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 178))

    def test_range_for_statement(self):
        input = """
        arr := [3]int{10, 20, 30};
        for index, value := range arr {
            // index: 0, 1, 2
            // value: 10, 20, 30
        }
        """
        expect = 'arr,:=,[,3,],int,{,10,,,20,,,30,},;,for,index,,,value,:=,range,arr,{,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 179))

    def test_range_for_without_index(self):
        input = """
        arr := [3]int{10, 20, 30};
        for _, value := range arr {
            // value: 10, 20, 30
        }
        """
        expect = 'arr,:=,[,3,],int,{,10,,,20,,,30,},;,for,_,,,value,:=,range,arr,{,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 180))

    def test_nested_for_statement(self):
        input = """
        for i := 0; i < 10; i += 1 {
            for j := 0; j < 10; j += 1 {
                sum += i + j;
            }
        }
        """
        expect = 'for,i,:=,0,;,i,<,10,;,i,+=,1,{,for,j,:=,0,;,j,<,10,;,j,+=,1,{,sum,+=,i,+,j,;,},;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 181))

    def test_break_statement(self):
        input = """
        for i := 0; i < 10; i+=1 {
            if (i == 5) {
            break;
            }
            // other statements
        }
        """
        expect = 'for,i,:=,0,;,i,<,10,;,i,+=,1,{,if,(,i,==,5,),{,break,;,},;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 182))

    def test_continue_statement(self):
        input = """
        for i := 0; i < 10; i += 1 {
            if (i == 5) {
            continue;
            }
            // statements that will not execute when i == 5
        }
        """
        expect = 'for,i,:=,0,;,i,<,10,;,i,+=,1,{,if,(,i,==,5,),{,continue,;,},;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 183))

    def test_eos(self):
        input = """
        a := 1
        b := true
        c := "hello"
        d := 3.14
        """
        expect = 'a,:=,1,;,b,:=,true,;,c,:=,hello,;,d,:=,3.14,;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 184))

    def test_full_eos(self):
        input = """
        abc
        5
        3.14
        "Hello"
        true
        nill
        int
        float
        string
        boolean
        return
        break
        continue
        )
        ]
        }
        """
        expect = "abc,;,5,;,3.14,;,Hello,;,true,;,nill,;,int,;,float,;,string,;,boolean,;,return,;,break,;,continue,;,),;,],;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 185))

    def test_not_eos(self):
        input = """
        a {
        """
        expect = "a,{,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 186))

    def test_double_eos(self):
        input = """
        a := 1


        b := true
        """
        expect = "a,:=,1,;,b,:=,true,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 187))

    def test_empty_program(self):
        input = """



        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 188))

    def test_full_struct(self):
        input = """
        type Knight struct {
            HP  int
            ATK int
            DEF int
        }

        func (k Knight) Attack() int {
            return k.ATK
        }

        func (k Knight) Defend() int {
            return k.DEF
        }

        func (k Knight) TakeDamage(dmg int) {
            k.HP -= dmg
        }
        """
        expect = 'type,Knight,struct,{,HP,int,;,ATK,int,;,DEF,int,;,},;,func,(,k,Knight,),Attack,(,),int,{,return,k,.,ATK,;,},;,func,(,k,Knight,),Defend,(,),int,{,return,k,.,DEF,;,},;,func,(,k,Knight,),TakeDamage,(,dmg,int,),{,k,.,HP,-=,dmg,;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 189))

    def test_full_interface(self):
        input = """
        type Calculator interface {
            Add(a, b int) int
            Subtract(a, b int) int
            Multiply(a, b int) int
            Divide(a, b int) (int, error)
        }

        type SimpleCalculator struct{}

        func (sc SimpleCalculator) Divide(a, b int) (int, error) {
            if b == 0 {
                return 0, errors.New("error: division by zero")
            }
            return a / b, nil
        """
        expect = 'type,Calculator,interface,{,Add,(,a,,,b,int,),int,;,Subtract,(,a,,,b,int,),int,;,Multiply,(,a,,,b,int,),int,;,Divide,(,a,,,b,int,),(,int,,,error,),;,},;,type,SimpleCalculator,struct,{,},;,func,(,sc,SimpleCalculator,),Divide,(,a,,,b,int,),(,int,,,error,),{,if,b,==,0,{,return,0,,,errors,.,New,(,error: division by zero,),;,},;,return,a,/,b,,,nil,;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 190))

    def test_palindrome_number(self):
        input = """
        func isPalindrome(n int) bool {
            var reversed int = 0
            var original int = n
            for n > 0 {
                reversed = reversed * 10 + n % 10
                n = n / 10
            }
            return original == reversed
        }

        func main() {
            fmt.Println(isPalindrome(121)) // true
        }
        """
        expect = 'func,isPalindrome,(,n,int,),bool,{,var,reversed,int,=,0,;,var,original,int,=,n,;,for,n,>,0,{,reversed,=,reversed,*,10,+,n,%,10,;,n,=,n,/,10,;,},;,return,original,==,reversed,;,},;,func,main,(,),{,fmt,.,Println,(,isPalindrome,(,121,),),;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 191))

    def test_search_insert_position(self):
        input = """
        func searchInsert(nums []int, target int) int {
            var left int = 0
            var right int = len(nums) - 1
            for left <= right {
                var mid int = left + (right - left) / 2
                if nums[mid] == target {
                    return mid
                } else if nums[mid] < target {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
            }
            return left
        }
        
        func main() {
            fmt.Println(searchInsert([]int{1, 3, 5, 6}, 5)) // 2
        }
        """
        expect = 'func,searchInsert,(,nums,[,],int,,,target,int,),int,{,var,left,int,=,0,;,var,right,int,=,len,(,nums,),-,1,;,for,left,<=,right,{,var,mid,int,=,left,+,(,right,-,left,),/,2,;,if,nums,[,mid,],==,target,{,return,mid,;,},else,if,nums,[,mid,],<,target,{,left,=,mid,+,1,;,},else,{,right,=,mid,-,1,;,},;,},;,return,left,;,},;,func,main,(,),{,fmt,.,Println,(,searchInsert,(,[,],int,{,1,,,3,,,5,,,6,},,,5,),),;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 192))

    def test_pascal_triagle(self):
        input = """
        func generate(numRows int) [][]int {
            var res [][]int
            for i := 0; i < numRows; i++ {
                var row []int
                for j := 0; j <= i; j++ {
                    if j == 0 || j == i {
                        row = append(row, 1)
                    } else {
                        row = append(row, res[i-1][j-1] + res[i-1][j])
                    }
                }
                res = append(res, row)
            }
            return res
        }
        """
        expect = 'func,generate,(,numRows,int,),[,],[,],int,{,var,res,[,],[,],int,;,for,i,:=,0,;,i,<,numRows,;,i,+,+,{,var,row,[,],int,;,for,j,:=,0,;,j,<=,i,;,j,+,+,{,if,j,==,0,||,j,==,i,{,row,=,append,(,row,,,1,),;,},else,{,row,=,append,(,row,,,res,[,i,-,1,],[,j,-,1,],+,res,[,i,-,1,],[,j,],),;,},;,},;,res,=,append,(,res,,,row,),;,},;,return,res,;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 193))

    def test_fibonacci(self):
        input = """
        func fib(n int) int {
            if n <= 1 {
                return n
            }
            return fib(n-1) + fib(n-2)
        }

        func main() {
            fmt.Println(fib(10)) // 55
        }
        """
        expect = 'func,fib,(,n,int,),int,{,if,n,<=,1,{,return,n,;,},;,return,fib,(,n,-,1,),+,fib,(,n,-,2,),;,},;,func,main,(,),{,fmt,.,Println,(,fib,(,10,),),;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 194))

    def test_gcd(self):
        input = """
        func gcd(a, b int) int {
            for b != 0 {
                a, b = b, a % b
            }
            return a
        }

        func main() {
            fmt.Println(gcd(24, 36)) // 12
        }
        """
        expect = 'func,gcd,(,a,,,b,int,),int,{,for,b,!=,0,{,a,,,b,=,b,,,a,%,b,;,},;,return,a,;,},;,func,main,(,),{,fmt,.,Println,(,gcd,(,24,,,36,),),;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 195))

    def test_lcm(self):
        input = """
        func lcm(a, b int) int {
            return a * b / gcd(a, b)
        }

        func main() {
            fmt.Println(lcm(24, 36)) // 72
        }
        """
        expect = 'func,lcm,(,a,,,b,int,),int,{,return,a,*,b,/,gcd,(,a,,,b,),;,},;,func,main,(,),{,fmt,.,Println,(,lcm,(,24,,,36,),),;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 196))

    def test_is_prime(self):
        input = """
        func isPrime(n int) bool {
            if n <= 1 {
                return false
            }
            for i := 2; i*i <= n; i++ {
                if n % i == 0 {
                    return false
                }
            }
            return true
        }

        func main() {
            fmt.Println(isPrime(17)) // true
        }
        """
        expect = 'func,isPrime,(,n,int,),bool,{,if,n,<=,1,{,return,false,;,},;,for,i,:=,2,;,i,*,i,<=,n,;,i,+,+,{,if,n,%,i,==,0,{,return,false,;,},;,},;,return,true,;,},;,func,main,(,),{,fmt,.,Println,(,isPrime,(,17,),),;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 197))

    def test_binary_search(self):
        input = """
        func binarySearch(nums []int, target int) int {
            var left int = 0
            var right int = len(nums) - 1
            for left <= right {
                var mid int = left + (right - left) / 2
                if nums[mid] == target {
                    return mid
                } else if nums[mid] < target {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
            }
            return -1
        }

        func main() {
            var nums []int = []int{1, 3, 5, 6}
            fmt.Println(binarySearch(nums, 5)) // 2
        }
        """
        expect = 'func,binarySearch,(,nums,[,],int,,,target,int,),int,{,var,left,int,=,0,;,var,right,int,=,len,(,nums,),-,1,;,for,left,<=,right,{,var,mid,int,=,left,+,(,right,-,left,),/,2,;,if,nums,[,mid,],==,target,{,return,mid,;,},else,if,nums,[,mid,],<,target,{,left,=,mid,+,1,;,},else,{,right,=,mid,-,1,;,},;,},;,return,-,1,;,},;,func,main,(,),{,var,nums,[,],int,=,[,],int,{,1,,,3,,,5,,,6,},;,fmt,.,Println,(,binarySearch,(,nums,,,5,),),;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 198))

    def test_merge_sort(self):
        input = """
        func mergeSort(nums []int) []int {
            if len(nums) <= 1 {
                return nums
            }
            var mid int = len(nums) / 2
            var left []int = mergeSort(nums[:mid])
            var right []int = mergeSort(nums[mid:])
            return merge(left, right)
        }

        func main() {
            var nums []int = []int{3, 2, 1, 4, 5}
            fmt.Println(mergeSort(nums)) // [1, 2, 3, 4, 5]
        }
        """

    def test_find_depth_tree(self):
        input = """
        func findDepthTree(arr []int) int {
            var maxDepth int = 0
            var depth int = 0
            for _, val := range arr {
                if val == -1 {
                    maxDepth = max(maxDepth, depth)
                    depth = 0
                } else {
                    depth += 1
                }
            }
            return maxDepth
        }
        
        func main() {
            var arr []int = []int{1, 2, 3, -1, 4, -1, -1, 5, 6}
            fmt.Println(findDepthTree(arr)) // 3
        }
        """
        expect = 'func,findDepthTree,(,arr,[,],int,),int,{,var,maxDepth,int,=,0,;,var,depth,int,=,0,;,for,_,,,val,:=,range,arr,{,if,val,==,-,1,{,maxDepth,=,max,(,maxDepth,,,depth,),;,depth,=,0,;,},else,{,depth,+=,1,;,},;,},;,return,maxDepth,;,},;,func,main,(,),{,var,arr,[,],int,=,[,],int,{,1,,,2,,,3,,,-,1,,,4,,,-,1,,,-,1,,,5,,,6,},;,fmt,.,Println,(,findDepthTree,(,arr,),),;,},;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(input, expect, 199))
