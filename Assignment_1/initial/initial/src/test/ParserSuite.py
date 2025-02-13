import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    """
    Parser test suite
    """
    def test_array_type(self):
        input = """
        var arr [5]int // defines an array of 5 integers.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_multi_array_type(self):
        input = """
        var multi_arr [2][5]int // defines an array of 2 x 5 integers.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_array_type_with_const(self):
        input = """
        const row = 5
        const col = 3
        var arr [row][col]int // defines an array of 5 integers.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    
    def test_array_with_init(self):
        input = """
        var arr = [5]int{1,2,3,4,5} // defines an array of 5 integers.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_array_without_dim(self):
        input = """
        var arr []int;
        """
        expect = "Error on line 2 col 18: ]"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_struct_type(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_struct_with_all_type(self):
        input = """
        type FullStruct struct {
                    ID          int;              
                    Name        string;            
                    IsActive    boolean;              
                    Price       float;           
                    Ratings     [3]int;
                    David       Person;    
                    Metadata    struct {          
                        CreatedBy string
                        UpdatedBy string
                    }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_struct_without_type(self):
        input = """
        Person struct {
            name string;
            age int;
        }
        """
        expect = "Error on line 2 col 16: struct"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_struct_without_name(self):
        input = """
        type struct {
            name string;
            age int;
        }
        """
        expect = "Error on line 2 col 14: struct"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_struct_without_keyword(self):
        input = """
        type Person {
            name string;
            age int;
        }
        """
        expect = "Error on line 2 col 21: {"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_struct_without_field(self):
        input = """
        type Person struct {
        }
        """
        expect = "Error on line 3 col 9: }"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_struct_with_wrong_field(self):
        input = """
        type Person struct {
            name string
            age int
            address
        }
        """
        expect = "Error on line 5 col 20: ;"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_struct_with_wrong_field_2(self):
        input = """
        type Person struct {
            string
            age int
            address int
        }
        """
        expect = "Error on line 3 col 13: string"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_interface_type(self):
        input = """
        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset()
            SayHello(name string)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_interface_without_type(self):
        input = """
        Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset()
            SayHello(name string)
        }
        """
        expect = "Error on line 2 col 20: interface"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_interface_without_name(self):
        input = """
        type interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset()
            SayHello(name string)
        }
        """
        expect = "Error on line 2 col 14: interface"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_interface_without_keyword(self):
        input = """
        type Calculator {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset()
            SayHello(name string)
        }
        """
        expect = "Error on line 2 col 25: {"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_interface_without_field(self):
        input = """
        type Calculator interface {
        }
        """
        expect = "Error on line 3 col 9: }"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_var_declare(self):
        input = """
        var x int = 10 + a[5];
        var y = "Hello";
        var z string;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_var_declare_without_type(self):
        input = """
        var x ;
        """
        expect = "Error on line 2 col 15: ;"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_var_declare_without_name(self):
        input = """
        var int ;
        """
        expect = "Error on line 2 col 13: int"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    
    def test_var_declare_without_keyword(self):
        input = """
        x int;
        """
        expect = "Error on line 2 col 11: int"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_var_declare_with_wrong_assign(self):
        input = """
        var x int := "Hello" + "World";
        """
        expect = "Error on line 2 col 19: :="
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_const_declare(self):
        input = """
        const Pi = 3.14;
        const Greeting = "Hello, MiniGo!";
        const MaxSize = 100 + 50;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    
    def test_const_declare_with_type(self):
        input = """
        const Pi int = 3.14;
        """
        expect = "Error on line 2 col 18: int"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_const_declare_without_init(self):
        input = """
        const Pi;
        """
        expect = "Error on line 2 col 17: ;"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_const_declare_with_wrong_assign(self):
        input = """
        const Pi := 3.14 + "Hello";
        """
        expect = "Error on line 2 col 18: :="
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_func_declare(self):
        input = """
        func add(a, b int, c string) int {
            return a + b + len(c);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    
    def test_func_declare_without_name(self):
        input = """
        func (a, b int, c string) int {
            return a + b + len(c);
        }
        """
        expect = "Error on line 2 col 16: ,"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_func_declare_without_return(self):
        input = """
        func Add(x int, y int) {
            println(x + y);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_func_declare_without_param(self):
        input = """
        func Five() int {
            return 5;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_func_declare_without_block(self):
        input = """
        func Hello() {};
        """
        expect = "Error on line 2 col 23: }"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_method_declare(self):
        input = """
        func (c Calculator) Add(x int) int {
            c.value += x;
            return c.value;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_arithmetic_expr(self):
        input = """
        var x int;
        x := 10 + 5 - 3 * 2 / 4 % 2;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_relational_expr(self):
        input = """
        var x boolean;
        x := a == b && c != d || e < f || g >= h;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_boolean_expr(self):
        input = """
        var flag boolean
        flag := a && b || c && d || !e
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_full_operator(self):
        input = """
        var x boolean;
        x := (a + b * c / d - e % f) == g && h.age > 18 || arr[i] < arr[j];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_access_array(self):
        input = """
        a[2][3] := b[2] + 1;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    
    def test_access_struct(self):
        input = """
        p.name := "John";
        p.age := 20;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_mixed_access(self):
        input = """
        p.David.name := "David";
        admin := p.Metadata.CreatedBy()
        f.p[i].x()
        m["foo"]
        var a = a.foo().bar()[4];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_array_literal(self):
        input = """
        arr := [3]int{10, 20, 30}
        marr := [2][3]int{{1, 2, 3}, {4, 5, 6}}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_array_literal_without_int_dim(self):
        input = """
        arr := [2.3]int{10, 20, 30}
        """
        expect = "Error on line 2 col 17: 2.3"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_array_literal_with_empty(self):
        input = """
        arr := [3]int{}
        """
        expect = "Error on line 2 col 23: }"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_struct_literal(self):
        input = """
        p := Person{name: "John", age: 20}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_struct_literal_with_empty(self):
        input = """
        p := Person{}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_function_call(self):
        input = """
        Add(1, 2);
        reset()
        foo(2 + x, 4 / y)
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_method_call(self):
        input = """
        calculator.add(3, 4)

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_method_call_with_seq(self):
        input = """
        calculator.operator.add(3, 4)
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_method_call_with_nested(self):
        input = """
        calculator.add(calculator.sub(5, 2), 4)
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_assignment_stmt(self):
        input = """
        x += 10; 
        x -= 5;
        y *= 23;
        z /= 2;
        t %= 23;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_lhs_assignment_stmt(self):
        input = """
        arr[2] *= 3
        Person.age += 1
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_rhs_assignment_stmt(self):
        input = """
        arr[3] := 10 + person.age
        y += a[2] * b[3][2]
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_if_statement(self):
        input = """
        if (a > b) {
            return a;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_if_else_statement(self):
        input = """
        if (a > b) {
            return a;
        } else {
            return b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_if_elif_statement(self):
        input = """
        if (x > 10) {
            println("x is greater than 10");
        } else if (x == 10) {
            println("x is equal to 10");
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_nested_if_statement(self):
        input = """
        if (x > 5) {
            if (x < 10) {
                println("x is between 5 and 10");
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_nested_if_else_statement(self):
        input = """
        if (x > 5) {
            if (x < 10) {
                println("x is between 5 and 10");
            } else {
                println("x is greater than 10");
            }
        } else {
            println("x is less than 5");
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_if_stmt_without_condition(self):
        input = """
        if {
            println("Hello");
        }
        """
        expect = "Error on line 2 col 12: {"
        self.assertTrue(TestParser.checkParser(input,expect,259))    

    def test_if_stmt_without_bracket(self):
        input = """
        if x > 10 {
            println("Hello");
        }
        """
        expect = "Error on line 2 col 12: x"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_if_stmt_without_curve_bracket(self):
        input = """
        if (x > 10)
            println("Hello");
        """
        expect = "Error on line 2 col 20: ;"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    
    def test_if_stmt_with_wrong_else(self):
        input = """
        if (x > 10) {
            println("Hello");
        } 
        else
            println("World");
        """
        expect = "Error on line 5 col 9: else"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_something(self):
        input = """
        func Add() {
            ID.age.c += 2;
        };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))