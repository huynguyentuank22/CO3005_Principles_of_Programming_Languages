import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    """
    Parser test suite
    """
    def test_program(self):
        input = """
        var x int;
        const y = 10;

        func main() {
            println("Hello, MiniGo!");
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_program(self):
        input = """
        var x int;
        
        for i := 0; i < 10; i += 1 {
            println(i);
        }

        func main() {
            println("Hello, MiniGo!");
        }
        """
        expect = "Error on line 4 col 9: for"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_empty_program(self):
        input = """

        """
        expect = "Error on line 3 col 9: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_empty_block(self):
        input = """
        func main() {}
        """
        expect = "Error on line 2 col 22: }"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_array_type(self):
        input = """
        var arr [5]int // defines an array of 5 integers.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_multi_array_type(self):
        input = """
        var multi_arr [2][5]int // defines an array of 2 x 5 integers.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_array_type_with_const(self):
        input = """
        const row = 5
        const col = 3
        var arr [row][col]int // defines an array of 5 integers.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    
    def test_array_with_init(self):
        input = """
        var arr = [5]int{1,2,3,4,5} // defines an array of 5 integers.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_array_without_dim(self):
        input = """
        var arr []int;
        """
        expect = "Error on line 2 col 18: ]"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_struct_type(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_struct_with_all_type(self):
        input = """
        type FullStruct struct {
                    ID          int;              
                    Name        string;            
                    IsActive    boolean;              
                    Price       float;           
                    Ratings     [3]int;
                    David       Person;    
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_struct_without_type(self):
        input = """
        Person struct {
            name string;
            age int;
        }
        """
        expect = "Error on line 2 col 9: Person"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_struct_without_name(self):
        input = """
        type struct {
            name string;
            age int;
        }
        """
        expect = "Error on line 2 col 14: struct"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_struct_without_keyword(self):
        input = """
        type Person {
            name string;
            age int;
        }
        """
        expect = "Error on line 2 col 21: {"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_struct_without_field(self):
        input = """
        type Person struct {
        }
        """
        expect = "Error on line 3 col 9: }"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_struct_with_wrong_field(self):
        input = """
        type Person struct {
            name string
            age int
            address
        }
        """
        expect = "Error on line 5 col 20: ;"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_struct_with_wrong_field_2(self):
        input = """
        type Person struct {
            string
            age int
            address int
        }
        """
        expect = "Error on line 3 col 13: string"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_struct_with_wrong_field_3(self):
        input = """
        type Person struct {
            name, nickname string
            age int
            address int
        }
        """
        expect = "Error on line 3 col 17: ,"
        self.assertTrue(TestParser.checkParser(input,expect,218))

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
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_interface_without_type(self):
        input = """
        Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset()
            SayHello(name string)
        }
        """
        expect = "Error on line 2 col 9: Calculator"
        self.assertTrue(TestParser.checkParser(input,expect,220))

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
        self.assertTrue(TestParser.checkParser(input,expect,221))

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
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_interface_without_field(self):
        input = """
        type Calculator interface {
        }
        """
        expect = "Error on line 3 col 9: }"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_var_declare(self):
        input = """
        var x int = 10 + a[5];
        var y = "Hello";
        var z string;
        var t Person;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_var_declare_without_type(self):
        input = """
        var x ;
        """
        expect = "Error on line 2 col 15: ;"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_var_declare_without_name(self):
        input = """
        var int ;
        """
        expect = "Error on line 2 col 13: int"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    
    def test_var_declare_without_keyword(self):
        input = """
        x int;
        """
        expect = "Error on line 2 col 9: x"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_var_declare_with_wrong_assign(self):
        input = """
        var x int := "Hello" + "World";
        """
        expect = "Error on line 2 col 19: :="
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_const_declare(self):
        input = """
        const Pi = 3.14;
        const Greeting = "Hello, MiniGo!";
        const MaxSize = 100 + 50;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    
    def test_const_declare_with_type(self):
        input = """
        const Pi int = 3.14;
        """
        expect = "Error on line 2 col 18: int"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_const_declare_without_init(self):
        input = """
        const Pi;
        """
        expect = "Error on line 2 col 17: ;"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_const_declare_with_wrong_assign(self):
        input = """
        const Pi := 3.14 + "Hello";
        """
        expect = "Error on line 2 col 18: :="
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_func_declare(self):
        input = """
        func add(a, b int, c string) int {
            return a + b + len(c);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    
    def test_func_declare_without_name(self):
        input = """
        func (a, b int, c string) int {
            return a + b + len(c);
        }
        """
        expect = "Error on line 2 col 16: ,"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_func_declare_without_return(self):
        input = """
        func Add(x int, y int) {
            println(x + y);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_func_declare_without_param(self):
        input = """
        func Five() int {
            return 5;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_func_declare_nested(self):
        input = """
        func Hello() {
            func World() int {
                return 5;
            }
        };
        """
        expect = "Error on line 3 col 13: func"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_method_declare(self):
        input = """
        func (c Calculator) Add(x int) int {
            c.value += x;
            return c.value;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_method_declare_nested(self):
        input = """
        func (c Calculator) Add(x int) int {
            func (c Calculator) Sub(y int) int {
                return c.value;
            }
        }
        """
        expect = "Error on line 3 col 13: func"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_func_decl_nested_method(self):
        input = """
        func Hello() {
            func (c Calculator) World() int {
                return 5;
            }
        };
        """
        expect = "Error on line 3 col 13: func"
        self.assertTrue(TestParser.checkParser(input,expect,240))


    def test_arithmetic_expr(self):
        input = """
        func main() {
            var x int;
            x := 10 + 5 - 3 * 2 / 4 % 2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_relational_expr(self):
        input = """
        func main() {
            var x boolean;
            x := a == b && c != d || e < f || g >= h;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_boolean_expr(self):
        input = """
        func main() {
            var flag boolean
            flag := a && b || c && d || !e
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_full_operator_expr(self):
        input = """
        func main() {
            var x boolean;
            x := (a + b * c / d - e % f) == g && h.age > 18 || arr[i] < arr[j];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_complex_expr(self):
        input = """
        const Votien = 1[2] + foo()[2] + ID[2].b.b;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_access_array(self):
        input = """
        func main() {
            a[2][3] := b[2][4] + 1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    
    def test_access_struct(self):
        input = """
        func main() {
            p.name := "John";
            p.age := 20;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_mixed_access(self):
        input = """
        func main() {
            p.David.name := "David";
            admin := p.Metadata.CreatedBy()
            f.p[i].x()
            m["foo"] := 1 + i
            var a = a.foo().bar()[4 + y / 2];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_array_literal(self):
        input = """
        func main() {
            arr := [3]int{10, 20, 30}
            marr := [2][3]int{{1, 2, 3}, {4, 5, 6}}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_array_literal_with_negative_num(self):
        input = """
        func main() {
            arr := [3]int{10, -20, 30}
        }
        """
        expect = "Error on line 3 col 31: -"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_array_literal_without_int_dim(self):
        input = """
        func main() {
            arr := [2.3]int{10, 20, 30}
        }
        """
        expect = "Error on line 3 col 21: 2.3"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_array_literal_with_empty(self):
        input = """
        func main() {
            arr := [3]int{}
        }
        """
        expect = "Error on line 3 col 27: }"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_struct_literal(self):
        input = """
        func main() {
            p := Person{name: "John", age: 20}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_struct_literal_with_empty(self):
        input = """
        func main() {
            p := Person{}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_struct_literal_with_wrong_field(self):
        input = """
        func main() {
            p := Person{name: "John", age: 20, address:}
        }
        """
        expect = "Error on line 3 col 56: }"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_function_call(self):
        input = """
        func main() {
            Add(1, 2);
            reset()
            foo(2 + x, 4 / y)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_method_call(self):
        input = """
        func main() {
            calculator.add(3, 4)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_method_call_with_seq(self):
        input = """
        func main() {
            calculator.operator.add(3, 4)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_method_call_with_nested(self):
        input = """
        func main() {
            calculator.add(calculator.sub(5, 2), 4)
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_assignment_stmt(self):
        input = """
        func main() {
            x += 10; 
            x -= 5;
            y *= 23;
            z /= 2;
            t %= 23;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_lhs_assignment_stmt(self):
        input = """
        func main() {
            arr[2 + i] *= 3
            Person.age += 1
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_lhs_assignment_stmt_with_wrong(self):
        input = """
        func main() {
            2 + i *= 3
        }
        """
        expect = "Error on line 3 col 19: *="
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_rhs_assignment_stmt(self):
        input = """
        func main() {
            arr[3] := 10 + person.age
            y += a[2] * b[3][2]
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_if_statement(self):
        input = """
        func main() {
            if (a > b) {
                return a;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_if_else_statement(self):
        input = """
        func main() {
            if (a > b) {
                return a;
            } else {
                return b;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_if_elif_statement(self):
        input = """
        func main() {
            if (x > 10) {
                println("x is greater than 10");
            } else if (x == 10) {
                println("x is equal to 10");
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_if_elif_else_statement(self):
        input = """
        func main() {
            if (x > 10) {
                println("x is greater than 10");
            } else if (x == 10) {
                println("x is equal to 10");
            } else {
                println("x is less than 10");
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_nested_if_statement(self):
        input = """
        func main() {
            if (x > 5) {
                if (x < 10) {
                    println("x is between 5 and 10");
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_nested_if_else_statement(self):
        input = """
        func main() {
            if (x > 5) {
                if (x < 10) {
                    println("x is between 5 and 10");
                } else {
                    println("x is greater than 10");
                }
            } else {
                println("x is less than 5");
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_if_stmt_without_condition(self):
        input = """
        func main() {
            if {
                println("Hello");
            }
        }
        """
        expect = "Error on line 3 col 16: {"
        self.assertTrue(TestParser.checkParser(input,expect,270))    

    def test_if_stmt_without_bracket(self):
        input = """
        func main() {
            if x > 10 {
                println("Hello");
            }
        }
        """
        expect = "Error on line 3 col 16: x"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_if_stmt_without_curve_bracket(self):
        input = """
        func main() {
            if (x > 10)
                println("Hello");
        }
        """
        expect = "Error on line 3 col 24: ;"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    
    def test_if_stmt_with_wrong_else(self):
        input = """
        func main() {
            if (x > 10) {
                println("Hello");
            } 
            else
                println("World");
        }
        """
        expect = "Error on line 6 col 13: else"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_basic_for_statement(self):
        input = """
        func main() {
            for i < 10 {
                // loop body
                i += 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_for_stmt_endless(self):
        input = """
        func main() {
            for true {
                // loop body
                i += 1;
                if (i == 10) {
                    break;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_not_full_for_statement(self):
        input = """
        func main() {
            for i := 0; i < 10; {
                i += 1;
                sum += i; // loop body
            }
        }
        """
        expect = "Error on line 3 col 33: {"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_not_full_for_statement_2(self):
        input = """
        func main() {
            var i = 0;
            for ; i < 10; i += 1 {
                sum += i; // loop body
            }
        }
        """
        expect = "Error on line 4 col 17: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 277))       

    def test_full_for_statement(self):
        input = """
        func main() {
            for i := 0; i < 10; i += 1 {
                sum += i; // loop body
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))
    
    def test_range_for_statement(self):
        input = """
        func main() {
            arr := [3]int{10, 20, 30};
            for index, value := range arr {
                // index: 0, 1, 2
                // value: 10, 20, 30
                println(index, value);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_range_for_without_index(self):
        input = """
        func main() {
            arr := [3]int{10, 20, 30};
            for _, value := range arr {
                // value: 10, 20, 30
                println(value);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_nested_for_statement(self):
        input = """
        func main() {
            for i := 0; i < 10; i += 1 {
                for j := 0; j < 10; j += 1 {
                    sum += i + j;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_break_statement(self):
        input = """
        func main() {
            for i := 0; i < 10; i+=1 {
                if (i == 5) {
                    break;
                }
                // other statements
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_continue_statement(self):
        input = """
        func main() {
            for i := 0; i < 10; i += 1 {
                if (i == 5) {
                    continue;
                }
                // statements that will not execute when i == 5
            }
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_break_continue_stmt_not_in_loop(self):
        input = """
        func main() {
            break;
            continue;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_return_stmt(self):
        input = """
        func calc(x, y, z int) int {
            return 2 + x - y * z;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_return_stmt_with_var(self):
        input = """
        func calc(x, y, z int) int {
            var result int = 2 + x - y * z;
            return result;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_return_stmt_without_expr(self):
        input = """
        func calc(x, y, z int) {
            if (x > y) {
                return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    
    def test_return_stmt_with_wrong_expr(self):
        input = """
        func calc(x, y, z int) {
            if (x > y) {
                return (2 + x - y * z, 23);
            }
        }
        """
        expect = "Error on line 4 col 38: ,"
        self.assertTrue(TestParser.checkParser(input,expect,288))

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
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_full_interface(self):
        input = """
        type Shape interface {
            Area() float
            Perimeter() float
        }

        type Rectangle struct {
            Width float 
            Height float
        }

        func (r Rectangle) Area() float {
            return r.Width * r.Height
        }

        func (r Rectangle) Perimeter() float {
            return 2 * (r.Width + r.Height)
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_palindrome_number(self):
        input = """
        func isPalindrome(n int) bool {
            var reversed int = 0
            var original int = n
            for n > 0 {
                reversed := reversed * 10 + n % 10
                n := n / 10
            }
            return original == reversed
        }

        func main() {
            fmt.Println(isPalindrome(121)) // true
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_search_insert_position(self):
        input = """
        func searchInsert(nums [4]int, target int) int {
            var left int = 0
            var right int = len(nums) - 1
            for left <= right {
                var mid int = left + (right - left) / 2
                if (nums[mid] == target) {
                    return mid
                } else if (nums[mid] < target) {
                    left := mid + 1
                } else {
                    right := mid - 1
                }
            }
            return left
        }
        
        func main() {
            fmt.Println(searchInsert([4]int{1, 3, 5, 6}, 5)) // 2
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_pascal_triagle(self):
        input = """
        func generate(numRows int) [r][c]int {
            var res [r][c]int
            for i := 0; i < numRows; i+=1 {
                var row [r]int
                for j := 0; j <= i; j+=1 {
                    if (j == 0 || j == i) {
                        row := append(row, 1)
                    } else {
                        row := append(row, res[i-1][j-1] + res[i-1][j])
                    }
                }
                res := append(res, row)
            }
            return res
        }

        func main() {
            fmt.Println(generate(5)) // [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_fibonacci(self):
        input = """
        func fib(n int) int {
            if (n <= 1) {
                return n
            }
            return fib(n-1) + fib(n-2)
        }

        func main() {
            fmt.Println(fib(10)) // 55
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_gcd(self):
        input = """
        func gcd(a, b int) int {
            for b != 0 {
                tmp := a
                a := b
                b := tmp % b
            }
            return a
        }

        func main() {
            fmt.Println(gcd(24, 36)) // 12
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_lcm(self):
        input = """
        func lcm(a, b int) int {
            return a * b / gcd(a, b)
        }

        func main() {
            fmt.Println(lcm(24, 36)) // 72
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_is_prime(self):
        input = """
        func isPrime(n int) bool {
            if (n <= 1) {
                return false
            }
            for i := 2; i*i <= n; i+=1 {
                if (n % i == 0) {
                    return false
                }
            }
            return true
        }

        func main() {
            fmt.Println(isPrime(17)) // true
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_binary_search(self):
        input = """
        func binarySearch(nums [4]int, target int) int {
            var left int = 0
            var right int = len(nums) - 1
            for (left <= right) {
                var mid int = left + (right - left) / 2
                if (nums[mid] == target) {
                    return mid
                } else if (nums[mid] < target) {
                    left := mid + 1
                } else {
                    right := mid - 1
                }
            }
            return -1
        }

        func main() {
            var nums = [4]int{1, 3, 5, 6}
            fmt.Println(binarySearch(nums, 5)) // 2
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_bubble_sort(self):
        input = """
        func bubbleSort(nums [5]int) [5]int {
            for i := 0; i < len(nums); i+=1 {
                for j := 0; j < len(nums) - i - 1; j+=1 {
                    if (nums[j] > nums[j+1]) {
                        tmp := nums[j]
                        nums[j] := nums[j+1]
                        nums[j+1] := tmp
                    }
                }
            }
            return nums
        }

        func main() {
            var nums = [5]int{5, 2, 3, 1, 4}
            fmt.Println(bubbleSort(nums)) // [1, 2, 3, 4, 5]
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_quick_sort(self):
        input = """
        func quickSort(arr [100]int, low int, high int) {
            if (low < high) {
                pi := partition(arr, low, high);
                quickSort(arr, low, pi - 1);
                quickSort(arr, pi + 1, high);
            }
        }
        func partition(arr [100]int, low int, high int) int {
            pivot := arr[high];
            i := low - 1;
            for j := low; j < high; j += 1 {
                if (arr[j] < pivot) {
                    i += 1;
                    swap(arr, i, j);
                }
            }
            swap(arr, i + 1, high);
            return i + 1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))

    # def test_something(self):
    #     input = """
    #     func main() {
    #         var tmp int;
    #         tmp := 1[2] + foo()[2] + ID[2].b.b;
    #         const Votien = 1[2] + foo()[2] + ID[2].b.b;
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,998))