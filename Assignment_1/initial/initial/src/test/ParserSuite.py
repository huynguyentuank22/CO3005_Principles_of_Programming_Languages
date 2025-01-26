import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_array_type(self):
        input = """var arr [4]int;
                    var multi_arr [2][7]int;
                    var multi_arr2 [2][8][3]int;
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_struct_type(self):
        input = """type Person struct {
                        name string
                        age int
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    
    def test_mixed_struct_type(self):
        input = """type FullStruct struct {
                    ID          int;              
                    Name        string;            
                    IsActive    bool;              
                    Price       float;           
                    Ratings     [3]int;            
                    Metadata    struct {          
                        CreatedBy string
                        UpdatedBy string
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_var_declare(self):
        input = """var x int = 10 + a[5];
                    var y = "Hello";
                    var z string;
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_const_declare(self):
        input = """const Pi = 3.14;
                    const Greeting = "Hello, MiniGo!";
                    const MaxSize = 100 + 50;
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_func_declare(self):
        input = """func add(a int, b string) int {};
                    func sub(a, b int) {}
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_index_ops(self):
        input = """var arr [5]int;
                    arr[3] = 10;
                    arr[4] = arr[3] + 5;
                    a[2][3] := b[2] + 1;
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_arr_literal(self):
        input = """var arr = [5]int{1, 2, 3, 4, 5};
                    var arr2 = [3]string{"a", "b", "c"};
                    marr := [2][3]int{{1, 2, 3}, {4, 5, 6}}
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_struct_literal(self):
        input = """p := Person{name: "Alice", age: 30}
                    q := Person{}
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_access_field(self):
        input = """p := Person{name: "Alice", age: 30}
                    p.name = "Bob";
                    p.age = 25;
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_func_call(self):
        input = """add(1, 2);
                    sub(3, 4)
                    reset()
                    calculator.add(3, 4)
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_func_call_2(self):
        input = """foo(2 + x, 4 / y); m.goo();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_interface_decl(self):
        input = """type Calculator interface {
                        Add(x, y int) int;
                        Subtract(a, b float, c int) float;
                        Reset()
                        SayHello(name string)
                        }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_asm_ops(self):
        input = """x := 5;
                    x += 10;
                    arr[2] *= 3;
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_if_stmt(self):
        input = """if (x > 5) {
                        str = "x is greater than 5";
                    } else if (x == 5) {
                        str = "x is equal to 5";
                    } else {
                        str = "x is less than 5";
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_nested_if_stmt(self):
        input = """if (x > 5) {
                        if (x < 10) {
                            str = "x is between 5 and 10";
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_for_stmt(self):
        input = """for i := 0; i < 10; i += 1 {
                        sum += i;
                    }
                    for i < 10 {
                        // loop body
                        i += 1;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_range_for_stmt(self):
        input = """ arr := [3]int{10, 20, 30}
                    for index, value := range arr {
                    // index: 0, 1, 2
                    // value: 10, 20, 30
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_range_for_without_index(self):
        input = """ arr := [3]int{10, 20, 30}
                    for _, value := range arr {
                    // value: 10, 20, 30
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_nested_for_stmt(self):
        input = """for i := 0; i < 10; i += 1 {
                        for j := 0; j < 10; j += 1 {
                            sum += i + j;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_break_stmt(self):
        input = """for i := 0; i < 10; i += 1 {
                        if (i == 5) {
                            break;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_continue_stmt(self):
        input = """for i := 0; i < 10; i += 1 {
                        if (i % 2 == 0) {
                            continue;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_return_stmt(self):
        input = """func add(a, b int) int {
                        return a + b;
                    }
                    func sub(a, b int) {
                        return;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_complex_func(self):
        input = """func add(a, b int) int {
                        if (a == 0) {
                            return b;
                        }
                        return a + b;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))