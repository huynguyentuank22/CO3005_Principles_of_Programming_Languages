import unittest
from TestUtils import TestChecker
from AST import *
import inspect
class CheckSuite(unittest.TestCase):
    def test_redeclared_builtin_(self):
        input = """
        func getInt() int {
            return 42;
        }
        """
        expect = "Redeclared Function: getInt\n"
        self.assertTrue(TestChecker.test(input,expect,400))
        
    def test_redeclared_builtin_2(self):
        input = """
        func putInt(x float) {
            return;
        }
        """
        expect = "Redeclared Function: putInt\n"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_redeclared_builtin_3(self):
        input = """
        func putIntLn(x int, y int) {
            return;
        }
        """
        expect = "Redeclared Function: putIntLn\n"
        self.assertTrue(TestChecker.test(input,expect,402))
        
    def test_redeclared_builtin_4(self):
        input = """
        func getFloat() int {
            return 1;
        }
        """
        expect = "Redeclared Function: getFloat\n"
        self.assertTrue(TestChecker.test(input,expect,403))
        
    def test_redeclared_builtin_5(self):
        input = """
        func putFloat(a float, b float) {
            putLn();
        }
        """
        expect = "Redeclared Function: putFloat\n"
        self.assertTrue(TestChecker.test(input,expect,404))
        
    def test_redeclared_builtin_6(self):
        input = """
        const putFloatLn = 1;
        func putFloatLn() string {
            return "hello";
        }
        """
        expect = "Redeclared Constant: putFloatLn\n"
        self.assertTrue(TestChecker.test(input,expect,405))
        
    def test_redeclared_builtin_7(self):
        input = """
        var getBool = 1;
        func getBool() string {
            return "true";
        }
        """
        expect = "Redeclared Variable: getBool\n"
        self.assertTrue(TestChecker.test(input,expect,406))
        
    def test_redeclared_builtin_8(self):
        input = """
        type putBool struct {
            a int;
        }
        func putBool(b boolean, extra string) {
            return;
        }
        """
        expect = "Redeclared Type: putBool\n"
        self.assertTrue(TestChecker.test(input,expect,407))
        
    def test_redeclared_builtin_9(self):
        input = """
        type putBoolLn interface {
            Add(a int) int;
        }
        func putBoolLn() int {
            return 0;
        }
        """
        expect = "Redeclared Type: putBoolLn\n"
        self.assertTrue(TestChecker.test(input,expect,408))
        
    def test_redeclared_builtin_10(self):
        input = """
        func getString() {
            return;
        }
        """
        expect = "Redeclared Function: getString\n"
        self.assertTrue(TestChecker.test(input,expect,409))
        
    def test_redeclared_builtin_11(self):
        input = """
        func putLn(message string) {
            return;
        }
        """
        expect = "Redeclared Function: putLn\n"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_var_redeclared(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """var a int; var b int; var a Huy; """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_var_redeclared_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo(a int, b int, c int) {
            var a int;
            return
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_const_redeclared(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """const a = 1; const b = 2; const a = 3;"""
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_const_redeclared_local(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            const a = 1;
        }
        
        const a = 2
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_const_redeclared_global(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        const a = 2
        func foofaa() {
            var c int;
            var d int;
            var b = a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_func_redeclared(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foofoo() {
            return
        } 
        func foofoo() {
            return
        }
        """
        expect = "Redeclared Function: foofoo\n"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_param_redeclared(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo(a, b int, a int) {
            return
        }
        """
        expect = "Redeclared Parameter: a\n"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_param_redeclared_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
        }
        func (a Person) foo(a, b int, c int) {
            return
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_method_redeclared(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        var foo int;
        type Person struct {
            name string
        }
        func (a Person) foo() {
            return
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_method_redeclared_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func (b Lina) foo() {
            return
        }
        type Lina struct {
            name string
        }
        func (a Lina) foo() {
            return
        }
        """
        expect = "Redeclared Method: foo\n"
        self.assertTrue(TestChecker.test(input,expect,420))  

    def test_method_redeclared_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person123 struct {
            name string
        }
        func (a Person123) foo() {
            return
        }
        func (a Huy) foo() {
            return
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_method_redeclared_4(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
        }
        func (a Person) name() {
            return
        }
        func (a Huy) foo() {
            return
        }
        """
        expect = "Redeclared Method: name\n"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_global(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func (a Person) name() {
            return
        }
        type Person struct {
            name string
        }
        """
        expect = "Redeclared Method: name\n"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_method_redeclared_5(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person321 struct {
            name string
        }
        func (a Person321) foo() {
            return
        }
        func (a Huy) name() {
            return
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_struct_redeclared(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
        }
        type Person struct {
            age int
        }
        """
        expect = "Redeclared Type: Person\n"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_field_redeclared(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
            age int
            name string
        }
        """
        expect = "Redeclared Field: name\n"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_interface_redeclared(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person interface {
            foo()
        }
        type Person interface {
            foo1()
        }
        """
        expect = "Redeclared Type: Person\n"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_interface_redeclared_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person interface {
            foo()
        }
        type Huy interface {
            foo()
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_prototype_redeclared(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person interface {
            foo(a int)
            foo()
        }
        """
        expect = "Redeclared Prototype: foo\n"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_mixed_redeclared(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """var a int; const a = 1;"""
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_mixed_redeclared_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        var foo int;
        func foo() {
            return
        }
        """
        expect = "Redeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_mixed_redeclared_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        const b = 1;
        func foo() {
            var a int;
            var b int;
            var a int;
            return
        }
        """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_mix_redeclared_4(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        const b = 1;
        func foo() {
            var b int
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_mix_redeclared_5(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            return
        }
        func (a Person) foo() {
            return
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_mix_redeclared_6(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
        }
        type Person interface {
            age()
        }
        """
        expect = "Redeclared Type: Person\n"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_undeclared_identifier(self):
        # print(inspect.currentframe().f_code.co_name)
        input = "var a = b;"
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_undeclared_identifier_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
        }
        var a Person;
        var b = c.name;
        """
        expect = "Undeclared Identifier: c\n"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_undeclared_identifier_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
        }
        var a Person;
        var b = c.d.name;
        """
        expect = "Undeclared Identifier: c\n"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_undeclared_func(self):
        # print(inspect.currentframe().f_code.co_name)
        input = "var a = foo();"
        expect = "Undeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_undeclared_func_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        var foo int 
        func main() {
            foo();
        }
        """
        expect = "Undeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_undeclared_func_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func main() {
            foo();
        }
        func foo(a, b int) {
            return
        }
        """
        expect = "Type Mismatch: FuncCall(foo,[])\n"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_undeclared_func_4(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func main() {
            foo(12,23,45);
        }
        func foo(a, b int) {
            return
        }
        """
        expect = "Type Mismatch: FuncCall(foo,[IntLiteral(12),IntLiteral(23),IntLiteral(45)])\n"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_undeclared_func_5(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func main() {
            foo(12, 2.3);
        }
        func foo(a, b int) {
            return
        }
        """
        expect = "Type Mismatch: FuncCall(foo,[IntLiteral(12),FloatLiteral(2.3)])\n"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_undeclared_method(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
        }
        var a Person;
        var b = a.foo();
        """
        expect = "Undeclared Method: foo\n"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_undeclared_method_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        var a Persondepchai;
        var b = a.foo();

        type Persondepchai struct {
            name string
        }

        func (a Persondepchai) foo() int {
            return 2
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,445))    

    def test_undeclared_method_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type MyStruct struct {
            value int
        }

        func (m MyStruct) GetNext() MyStruct {
            var a int
        }

        func (m MyStruct) Double() MyStruct {
            var b int
        }

        func main() {
            var obj MyStruct
            var result = obj.GetNext().Double()  
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,446))
    
    def test_undeclared_method_4(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type MyStruct struct {
            value int
        }

        func (m MyStruct) Double() MyStruct {
            var b int
        }

        func main() {
            var obj MyStruct
            var result = obj.GetNext().Double()  
        }
        """
        expect = "Undeclared Method: GetNext\n"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_undeclared_method_5(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type MyStruct struct {
            value int
        }

        func (m MyStruct) GetNext() MyStruct {
            var a int
        }

        func main() {
            var obj MyStruct
            var result = obj.GetNext().Double()  
        }
        """
        expect = "Undeclared Method: Double\n"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_undeclared_method_6(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Calculator interface {
            Add(a, b int) int
            Subtract(a, b int) int
        }

        func main() {
            var obj Calculator
            var result = obj.Multiply(1, 2)
        }
        """
        expect = "Undeclared Method: Multiply\n"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_undeclared_method_7(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Calculator interface {
            Add(a, b int) int
            Subtract(a, b int) int
        }

        func main() {
            var obj Calculator
            var result = obj.Add(1, 2)
            var result2 = obj.Subtract(1, 2)
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_undeclared_field(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
        }
        var a Person;
        var b = a.age;
        """
        expect = "Undeclared Field: age\n"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_undeclared_field_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
        }
        var a Person;
        var b = a.name
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_undeclared_field_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Address struct {
            street string
            city string
        }
        type Person struct {
            name string
            address Address
        }
        var huy Person;
        var country = huy.address.country;
        """
        expect = "Undeclared Field: country\n"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_undeclared_field_4(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Address struct {
            street string
            city string
            country string
        }
        type Person struct {
            name string
            address Address
        }
        var huy Person;
        var country = huy.address.country;
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_undeclared_field_5(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Community struct {
            commu [3]Person
        }
        type Person struct {
            name string
        }
        
        func main() {
            var obj Community
            var result = obj.commu[3].age
        }
        """
        expect = "Undeclared Field: age\n"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_undeclared_mix_access(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Address struct {
            street string
            city string
            country string
        }
        type Person struct {
            name string
            address Address
        }
        var huy Person;
        var loc = huy.address.location();
        """
        expect = "Undeclared Method: location\n"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_undeclared_mix_access_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Address struct {
            street string
            city string
            country string
        }
        func (p Person) location() Address {
            var a int
        }
        type Person struct {
            name string
        }
        var huy Person;
        var add = huy.location().location;
        """
        expect = "Undeclared Field: location\n"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_type_mismatch_int_with_float(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input,expect,458))
    
    def test_type_missmatch_int_with_string(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """var a int = "huy";"""
        expect = """Type Mismatch: VarDecl(a,IntType,StringLiteral("huy"))\n"""
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_type_missmatch_int_with_bool(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """var a int = true;"""
        expect = "Type Mismatch: VarDecl(a,IntType,BooleanLiteral(true))\n"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_type_missmatch_float_with_int(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """var a float = 1;"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_type_missmatch_float_with_string(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """var a float = "huy";"""
        expect = "Type Mismatch: VarDecl(a,FloatType,StringLiteral(\"huy\"))\n"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_type_missmatch_float_with_bool(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """var a float = false;"""
        expect = "Type Mismatch: VarDecl(a,FloatType,BooleanLiteral(false))\n"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_type_missmatch_return(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() int {
            return "huy";
        }
        """
        expect = "Type Mismatch: Return(StringLiteral(\"huy\"))\n"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_type_missmatch_return_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() int {
            return true;
        }
        """
        expect = "Type Mismatch: Return(BooleanLiteral(true))\n"
        self.assertTrue(TestChecker.test(input,expect,465))
    
    def test_type_missmatch_return_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() int {
            return 12;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,466))
    
    def test_type_missmatch_plus(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = 12 + "huy";
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(12),+,StringLiteral(\"huy\"))\n"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_type_missmatch_plus_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = true + "huy";
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),+,StringLiteral(\"huy\"))\n"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_type_missmatch_plus_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var a = "Hello" + "huy";
            var b = 123 + 456
            var c = 12.3 + 45.6
            var d = 123 + 45.6
            var e = 123.4 + 45
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,469))
    
    def test_type_missmatch_minus(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = true - 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),-,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_type_missmatch_minus_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = "huy" - 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(StringLiteral(\"huy\"),-,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_type_missmatch_mul(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = true * 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),*,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_type_missmatch_mul_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = "huy" * 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(StringLiteral(\"huy\"),*,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_type_missmatch_div(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = true / 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),/,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_type_missmatch_div_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = "huy" / 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(StringLiteral(\"huy\"),/,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,475))        

    def test_type_missmatch_minus_mul_div(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var a = 123 - 456
            var b = 12.3 - 45.6
            var c = 123 - 45.6
            var d = 123.4 - 45
            var e = 123 * 456
            var f = 12.3 * 45.6
            var g = 123 * 45.6
            var h = 123.4 * 45
            var i = 123 / 456
            var j = 12.3 / 45.6
            var k = 123 / 45.6
            var l = 123.4 / 45
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_type_missmatch_modulo(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = true % 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),%,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_type_missmatch_modulo_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = "huy" % 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(StringLiteral(\"huy\"),%,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_type_missmatch_modulo_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var a = 123 % 45.6
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(123),%,FloatLiteral(45.6))\n"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_type_missmatch_modulo_4(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var a = 123 % 45
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_type_missmatch_equal(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = true == 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),==,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_type_missmatch_equal_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = "huy" == 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(StringLiteral(\"huy\"),==,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_type_missmatch_not_equal(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = true != 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),!=,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_type_missmatch_not_equal_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = 123 != 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(123),!=,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_type_missmatch_less_than(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = true < 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),<,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_type_missmatch_less_than_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = 123 < 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(123),<,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_type_missmatch_less_than_equal(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = true <= 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),<=,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_type_missmatch_less_than_equal_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = 123 <= 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(123),<=,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_type_missmatch_greater_than(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = true > 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),>,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,489))
    
    def test_type_missmatch_greater_than_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = 123 > 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(123),>,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,490))
    
    def test_type_missmatch_greater_than_equal(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = true >= 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),>=,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_type_missmatch_greater_than_equal_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = 123 >= 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(123),>=,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_type_missmatch_relational(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var a = 123 == 456
            var b = 12.3 == 45.6
            var c = "hello" == "world"

            var d = 123 != 456
            var e = 12.3 != 45.6
            var f = "hello" != "world"

            var g = 123 < 456
            var h = 12.3 < 45.6
            var i = "hello" < "world"

            var j = 123 <= 456
            var k = 12.3 <= 45.6
            var l = "hello" <= "world"

            var m = 123 > 456
            var n = 12.3 > 45.6
            var o = "hello" > "world"

            var p = 123 >= 456
            var q = 12.3 >= 45.6
            var r = "hello" >= "world"
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_type_missmatch_and(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = true && 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),&&,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_type_missmatch_and_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = 123 && 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(123),&&,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_type_missmatch_or(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = true || 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),||,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,496))
    
    def test_type_missmatch_or_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = 123 || 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(123),||,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_type_missmatch_and_or(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var a = true && false
            var b = true || false
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_type_missmatch_neg(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = -true;
        }
        """
        expect = "Type Mismatch: UnaryOp(-,BooleanLiteral(true))\n"
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_type_missmatch_neg_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = -"huy";
        }
        """
        expect = "Type Mismatch: UnaryOp(-,StringLiteral(\"huy\"))\n"
        self.assertTrue(TestChecker.test(input,expect,500))

    def test_type_missmatch_neg_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var a = -123 
            var c = -12.3;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,501))

    def test_type_missmatch_not(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = !123;
        }
        """
        expect = "Type Mismatch: UnaryOp(!,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,502))

    def test_type_missmatch_not_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var c = !"huy";
        }
        """
        expect = "Type Mismatch: UnaryOp(!,StringLiteral(\"huy\"))\n"
        self.assertTrue(TestChecker.test(input,expect,503))

    def test_type_missmatch_not_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var a = !12.3
        }
        """
        expect = "Type Mismatch: UnaryOp(!,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,504))
    
    def test_type_missmatch_not_4(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var a = !true
            var b = !false
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,505))

    def test_type_missmatch_field(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
        }
        var a int;
        var b = a.name;
        """
        expect = "Type Mismatch: FieldAccess(Id(a),name)\n"
        self.assertTrue(TestChecker.test(input,expect,506))

    def test_type_missmatch_field_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
        }

        var a Person;
        var b = a.name.first_name;
        """
        expect = "Type Mismatch: FieldAccess(FieldAccess(Id(a),name),first_name)\n"
        self.assertTrue(TestChecker.test(input,expect,507))

    def test_type_missmatch_field_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Community struct {
            commu [3]Person
        }
        type Person struct {
            name string
        }
        
        func main() {
            var obj Community
            var result = obj.commu.age
        }
        """
        expect = "Type Mismatch: FieldAccess(FieldAccess(Id(obj),commu),age)\n"
        self.assertTrue(TestChecker.test(input,expect,508))

    def test_type_missmatch_method(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        var a Persondepchai;
        var b = a.foo();

        type Persondepchai struct {
            name string
        }

        func (c Persondepchai) foo(a, b int) {
            return
        }
        """
        expect = "Type Mismatch: MethodCall(Id(a),foo,[])\n"
        self.assertTrue(TestChecker.test(input,expect,509))  

    def test_type_missmatch_method_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        var a Persondepchai;
        var b = a.foo(12, 34, 45);

        type Persondepchai struct {
            name string
        }

        func (c Persondepchai) foo(a, b int) {
            return
        }
        """
        expect = "Type Mismatch: MethodCall(Id(a),foo,[IntLiteral(12),IntLiteral(34),IntLiteral(45)])\n"
        self.assertTrue(TestChecker.test(input,expect,510))  

    def test_type_missmatch_method_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        var a Persondepchai;
        var b = a.foo(12, 3.4);

        type Persondepchai struct {
            name string
        }

        func (c Persondepchai) foo(a, b int) {
            return
        }
        """
        expect = "Type Mismatch: MethodCall(Id(a),foo,[IntLiteral(12),FloatLiteral(3.4)])\n"
        self.assertTrue(TestChecker.test(input,expect,511))  

    def test_type_missmatch_method_4(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Calculator interface {
            Add(a, b int) int
            Subtract(a, b int) int
        }

        func main() {
            var obj Calculator
            var result = obj.Add(1.2, 2.3)
        }
        """
        expect = "Type Mismatch: MethodCall(Id(obj),Add,[FloatLiteral(1.2),FloatLiteral(2.3)])\n"
        self.assertTrue(TestChecker.test(input,expect,512))

    def test_type_missmatch_method_5(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Calculator interface {
            Add(a, b int) int
            Subtract(a, b int) int
        }

        func main() {
            var obj Calculator
            var result = obj.Add(1, 2, 3)
        }
        """
        expect = "Type Mismatch: MethodCall(Id(obj),Add,[IntLiteral(1),IntLiteral(2),IntLiteral(3)])\n"
        self.assertTrue(TestChecker.test(input,expect,513))
    

    def test_type_missmatch_array_cell(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var a [5]int;
            var b = 2;
            var c = a[b][23];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,514))

    def test_type_missmatch_array_cell_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var a [5]int;
            var b = 2.3;
            var c = a[b];
        }
        """
        expect = "Type Mismatch: ArrayCell(Id(a),[Id(b)])\n"
        self.assertTrue(TestChecker.test(input,expect,515))

    def test_type_missmatch_array_cell_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var a int;
            var b = 2;
            var c = a[b][23];
        }
        """
        expect = "Type Mismatch: ArrayCell(Id(a),[Id(b),IntLiteral(23)])\n"
        self.assertTrue(TestChecker.test(input,expect,516))

    def test_type_missmatch_array_cell_4(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
            nickname [2]string
        }
        func foo() {
            var huy Person
            var c = huy.nickname[2];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,517))

    def test_type_missmatch_array_cell_5(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
        }
        func (p Person) foo() [3]int {
            var a int
        }
        func foo() {
            var huy Person
            var c = huy.foo()[23];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,518))

    def test_type_missmatch_array_cell_6(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
        }
        func (p Person) foo() int {
            var a int
        }
        func foo() {
            var huy Person
            var c = huy.foo()[23];
        }
        """
        expect = "Type Mismatch: ArrayCell(MethodCall(Id(huy),foo,[]),[IntLiteral(23)])\n"
        self.assertTrue(TestChecker.test(input,expect,519))
    
    def test_type_missmatch_func_call(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var a = 1
        }
        func main() {
            var b = foo();
        }
        """
        expect = "Type Mismatch: VarDecl(b,FuncCall(foo,[]))\n"
        self.assertTrue(TestChecker.test(input,expect,520))

    def test_type_missmatch_func_call_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() int {
            return 2
        }
        func main() {
            foo();
        }
        """
        expect = "Type Mismatch: FuncCall(foo,[])\n"
        self.assertTrue(TestChecker.test(input,expect,521))

    def test_type_missmatch_method_call(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
        }
        func (p Person) foo() int {
            return 2
        }
        func main() {
            var huy Person
            huy.foo();
        }
        """
        expect = "Type Mismatch: MethodCall(Id(huy),foo,[])\n"
        self.assertTrue(TestChecker.test(input,expect,522))

    def test_type_missmatch_method_call_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type Person struct {
            name string
        }
        func (p Person) foo() {
            return 
        }
        func main() {
            var huy Person
            var a = huy.foo();
        }
        """
        expect = "Type Mismatch: VarDecl(a,MethodCall(Id(huy),foo,[]))\n"
        self.assertTrue(TestChecker.test(input,expect,523))

    def test_type_missmatch_if_stmt(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            if (1.2) {
                return
            }
        }
        """
        expect = "Type Mismatch: If(FloatLiteral(1.2),Block([Return()]))\n"
        self.assertTrue(TestChecker.test(input,expect,524))

    def test_type_missmatch_if_stmt_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            if (true) {
                return
            } else {
                return
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,525))

    def test_type_missmatch_if_stmt_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            if (true) {
                if (1 + 2) {
                    return
                }
            }
        }
        """
        expect = "Type Mismatch: If(BinaryOp(IntLiteral(1),+,IntLiteral(2)),Block([Return()]))\n"
        self.assertTrue(TestChecker.test(input,expect,526))

    def test_type_missmatch_if_stmt_4(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            if (true) {
                break
            } else if (1.2 + 3) {
                continue
            } else {
                return
            }
        }
        """        
        expect = "Type Mismatch: If(BinaryOp(FloatLiteral(1.2),+,IntLiteral(3)),Block([Continue()]),Block([Return()]))\n"
        self.assertTrue(TestChecker.test(input,expect,527))

    def test_type_missmatch_if_stmt_5(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            if (true) {
                break
            } else if (1.2 + 3) {
                continue
            } else if (false) {
                return
            } else {
                return
            }
        }
        """        
        expect = "Type Mismatch: If(BinaryOp(FloatLiteral(1.2),+,IntLiteral(3)),Block([Continue()]),If(BooleanLiteral(false),Block([Return()]),Block([Return()])))\n"
        self.assertTrue(TestChecker.test(input,expect,528))

    def test_type_missmatch_for_basic_stmt(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            for (1.2) {
                return
            }
        }
        """
        expect = "Type Mismatch: For(FloatLiteral(1.2),Block([Return()]))\n"
        self.assertTrue(TestChecker.test(input,expect,529))

    def test_type_missmatch_for_step_stmt(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            for var i = 0; 23 + 45; i += 1 {
                return
            }
        }
        """
        expect = "Type Mismatch: For(VarDecl(i,IntType,IntLiteral(0)),BinaryOp(IntLiteral(23),+,IntLiteral(45)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([Return()]))\n"
        self.assertTrue(TestChecker.test(input,expect,530))

    def test_type_missmatch_for_step_stmt_2(self):
        input = """
        func foo() {
            for var i = 0; true; i += 1 {
                var i = 1;
                return
            }
        }
        """
        expect = "Redeclared Variable: i\n"
        self.assertTrue(TestChecker.test(input,expect,531))

    def test_type_missmatch_for_each(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var arr [5]int
            for i, i := range arr {
                return
            }
        }
        """
        expect = "Undeclared Identifier: i\n"
        self.assertTrue(TestChecker.test(input,expect,532))

    def test_type_missmatch_for_each_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var arr int
            for idx, val := range arr {
                return
            }
        }
        """
        expect = "Type Mismatch: ForEach(Id(idx),Id(val),Id(arr),Block([Return()]))\n"
        self.assertTrue(TestChecker.test(input,expect,533))

    def test_type_missmatch_assign(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var a = 5
            var c float
            c := a
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,534))

    def test_type_missmatch_assign_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var a = "huy"
            var c float
            c := a + "hello"
        }
        """
        expect = "Type Mismatch: Assign(Id(c),BinaryOp(Id(a),+,StringLiteral(\"hello\")))\n"
        self.assertTrue(TestChecker.test(input,expect,535))

    def test_type_missmatch_assign_array(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            const one = 1
            var row = 2 + one
            var col = 3 + 2 * one
            var a [3][5]int
            var b [row][col]int
            var c [3][5]float
            b := a
            c := a
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,536))

    def test_type_missmatch_assign_array_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var row = 2 + 1
            var col = 3 + 1 + 1
            var a [3][5]int
            var b [row][col][col]int
            b := a
        }
        """
        expect = "Type Mismatch: Assign(Id(b),Id(a))\n"
        self.assertTrue(TestChecker.test(input,expect,537))

    def test_type_missmatch_assign_array_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var row = 2 + 1
            var col = 3 + 1
            var a [3][5]int
            var b [row][col]float
            b := a
        }
        """
        expect = "Type Mismatch: Assign(Id(b),Id(a))\n"
        self.assertTrue(TestChecker.test(input,expect,538))

    def test_type_missmatch_assign_array_4(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo() {
            var row float = 2.0 + 1.0
            var col = 3 + 1 + 1
            var a [3][5]int
            var b [row][col]float
            b := a
        }
        """
        expect = "Type Mismatch: ArrayType(FloatType,[Id(row),Id(col)])\n"
        self.assertTrue(TestChecker.test(input,expect,539))

    def test_type_missmatch_assign_aka_declared(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func test(x, y int, z float) {
            var x int;
            var z float;
            t := 1;
            const t = 2;
        }
        """
        expect = "Redeclared Constant: t\n"
        self.assertTrue(TestChecker.test(input,expect,540))

    def test_type_missmatch_arr_lit(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        var col = 3.5
        var arr = [2][col]int{1,2,3,4}
        """
        expect = "Type Mismatch: ArrayLiteral([IntLiteral(2),Id(col)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)])\n"
        self.assertTrue(TestChecker.test(input,expect,541))

    def test_type_missmatch_interface_implement(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type hihi interface {
            foo(a int)
            faa(b int)
        }
        type Person struct {
            a int
        }
        func main() {
            var a Person
            var b hihi
            b := a
        }
        """
        expect = "Type Mismatch: Assign(Id(b),Id(a))\n"
        self.assertTrue(TestChecker.test(input, expect, 542))

    def test_type_missmatch_interface_implement_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type hihi interface {
            foo(a int)
        }
        func (p Person) foo() {
            var a int
        }
        type Person struct {
            a int
        }
        func main() {
            var a Person
            var b hihi
            b := a
        }
        """
        expect = "Type Mismatch: Assign(Id(b),Id(a))\n"
        self.assertTrue(TestChecker.test(input, expect, 543))

    def test_type_missmatch_interface_implement_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type hihi interface {
            foo(a int) int
        }
        func (p Person) foo(a int) {
            var a int
        }
        type Person struct {
            a int
        }
        func main() {
            var a Person
            var b hihi
            b := a
        }
        """
        expect = "Type Mismatch: Assign(Id(b),Id(a))\n"
        self.assertTrue(TestChecker.test(input, expect, 544))

    def test_type_missmatch_interface_implement_4(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type hihi interface {
            foo(a int) int
        }
        func (p Person) foo(a float) int {
            var a int
        }
        type Person struct {
            a int
        }
        func main() {
            var a Person
            var b hihi
            b := a
        }
        """
        expect = "Type Mismatch: Assign(Id(b),Id(a))\n"
        self.assertTrue(TestChecker.test(input, expect, 545))

    def test_type_missmatch_interface_implement_5(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type hihi interface {
            foo(a int) int
        }
        func (p Person) foo(a int) int {
            var a int
        }
        type Person struct {
            a int
        }
        func main() {
            var a Person
            var b hihi
            b := a
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 546))

    def test_type_missmatch_interface_implement_6(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        type A interface{
            getInt() int
        }
        type B struct {
            x int;
        }
        func (b B) getInt() int {
            return b.x
        }
        func (b B) dosth(){
            return;
        }

        func main (){
            var a A
            A := B{x:1}
            a.dosth()
        }
        """
        expect = "Type Mismatch: MethodCall(Id(a),dosth,[])\n"
        self.assertTrue(TestChecker.test(input, expect, 547))

    def test_scope_var_decl(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        var b boolean;
        var c int;
        var a = c+d;
        var d = b + c;
        var e = b + 1;
        """
        expect = "Undeclared Identifier: d\n"
        self.assertTrue(TestChecker.test(input,expect,548))

    def test_scope_var_decl_2(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        var a = 2 + 5 * 3;
        var b = a + 1;
        var c = a * b;
        var d = c - 1;
        var e = d / 2;
        func foo(){
            k := a + b;
            putInt(k);
            var c = d + e;
            putInt(c);
            var e = h + 1;
        }
        """
        expect = "Undeclared Identifier: h\n"
        self.assertTrue(TestChecker.test(input,expect,549))

    def test_scope_var_decl_3(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        var a[1]int = [1]int{1};
        var b [5]float;
        func foo(){
            b := [5]int{1,2,3,4,5};
            var c = a[0];
            putInt(c);
            var d = e+1;
        }
        var e int = 2;
        """
        expect = "Undeclared Identifier: e\n"
        self.assertTrue(TestChecker.test(input,expect,550))

    def test_scope_var_decl_4(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        const a = 1;
        const b = 2;
        const c = d + 3;
        const d = 4;
        """
        expect = "Undeclared Identifier: d\n"
        self.assertTrue(TestChecker.test(input,expect,551))

    def test_scope_var_decl_5(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        var a[1]int = [1]int{1};
        var b [5]float;
        func foo(){
            a[0] := 2;
            putInt(a[0]);
            b[0] := c;
        }
        var c int = 2;
        """
        expect = "Undeclared Identifier: c\n"
        self.assertTrue(TestChecker.test(input,expect,552))

    def test_struct_lit(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func foo(a,b,c int) A{
            return A{a:a, b:b, c:c, d:d}
        }
        func main(){
            var b A;
            b := foo(1,2,3)
        }
        type A struct{
            a int;
            b int;
            c int;
        }
        """
        expect = "Undeclared Field: d\n"
        self.assertTrue(TestChecker.test(input, expect, 553))

    def test_something(self):
        # print(inspect.currentframe().f_code.co_name)
        input = """
        func main() {
            for i := 0; i < 10; i+=1 {
                if (i == 5) {
                    break
                    var a int
                } else if (i == 6) {
                    continue
                    var b int
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 554))

    def test_something_2(self):
        input = """
        func foo(a int){
            foo(1);
            var foo int;
            foo(2);
        }
        """
        expect = "Undeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 555))

    def test_something_3(self):
        input = """
        func main(){
            var index string = "hello";
            var value int;
            for index, value := range [5]int{1,2,3,4,5} {
                putInt(value);
            }
        }
        """
        expect = "Type Mismatch: ForEach(Id(index),Id(value),ArrayLiteral([IntLiteral(5)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]),Block([FuncCall(putInt,[Id(value)])]))\n"
        self.assertTrue(TestChecker.test(input, expect, 556))

    def test_something_4(self):
        input = """
        func main(){
            var value_ int;
            for index, value_ := range [5]int{1,2,3,4,5} {
                putInt(value_);
            }
        }
        """
        expect = "Undeclared Identifier: index\n"
        self.assertTrue(TestChecker.test(input, expect, 557))

    def test_something_5(self):
        input = """
        func main(){
            var index int;
            for _, value := range [5]int{1,2,3,4,5} {
                putInt(value);
            }
        }
        """
        expect = "Undeclared Identifier: value\n"
        self.assertTrue(TestChecker.test(input, expect, 558))
        
    def test_something_6(self):
        input = """
        func main(){
            var index int
            var value int
            for index, value := range arr {
                putInt(value);
            }
            
        }
        """
        expect = "Undeclared Identifier: arr\n"
        self.assertTrue(TestChecker.test(input, expect, 559))

    def test_something_7(self):
        input = """
        var a [2][2]int;
        func main(){
            a[0] := 1;
        }
        """
        expect = "Type Mismatch: Assign(ArrayCell(Id(a),[IntLiteral(0)]),IntLiteral(1))\n"
        self.assertTrue(TestChecker.test(input, expect, 560))

    def test_something_8(self):
        input = """
        var a [3][4] int;
        var b [4] int = a;
        """
        expect = """Type Mismatch: VarDecl(b,ArrayType(IntType,[IntLiteral(4)]),Id(a))\n"""
        self.assertTrue(TestChecker.test(input, expect, 561))

    def test_something_9(self):
        input = """ 
        const a = 2
        const b = 2
        func foo () [a]int {
            var arr[2][2]int;
            arr[0] := [2]int{1,2};
            return arr[0];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 562))

    def test_something_10(self):
        input = """
        const a = 2
        const b = 3
        var arr[2][2]int;
        func main(){
            arr[0] := [3]int{1,2,3}
        }

        """
        expect = "Type Mismatch: Assign(ArrayCell(Id(arr),[IntLiteral(0)]),ArrayLiteral([IntLiteral(3)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))\n"
        self.assertTrue(TestChecker.test(input, expect, 563))
        
    def test_something_11(self):
        input = """
        func foo(a int, b float, c string){
            var a int;
            var b float;
            var c string;
            putInt(a);
        }
        func main(){
            foo(foo(1, 2.0, "hello"), 2.0, "hello");
        }
        """
        expect = "Type Mismatch: FuncCall(foo,[FuncCall(foo,[IntLiteral(1),FloatLiteral(2.0),StringLiteral(\"hello\")]),FloatLiteral(2.0),StringLiteral(\"hello\")])\n"
        self.assertTrue(TestChecker.test(input, expect, 564))

    def test_something_12(self):
        input = """
        func foo() {
            foo := 1
            foo()
        }
        """
        expect = 'Undeclared Function: foo\n'
        self.assertTrue(TestChecker.test(input, expect, 565))

    def test_something_13(self):
        input = """
        func foo() {
            var a = 2
            a += 1
            var arr [3]int
            var array [a]int
            arr := array
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 566))

    def test_something_14(self):
        input = """
        func foo(){
            var a int; 
            a := 1;
            putInt(a);
        }
        func main(){
            var b int;
            b := foo() + 2
        }
        """
        expect = "Type Mismatch: BinaryOp(FuncCall(foo,[]),+,IntLiteral(2))\n"
        self.assertTrue(TestChecker.test(input, expect, 567))