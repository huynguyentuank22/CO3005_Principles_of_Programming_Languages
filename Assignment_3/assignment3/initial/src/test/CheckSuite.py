import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_var_redeclared(self):
        input = """var a int; var b int; var a Huy; """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_var_redeclared_2(self):
        input = """
        func foo(a int, b int, c int) {
            var a int;
            return
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_const_redeclared(self):
        input = """const a = 1; const b = 2; const a = 3;"""
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_const_redeclared_local(self):
        input = """
        func foo() {
            const a = 1;
        }
        
        const a = 2
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_const_redeclared_global(self):
        input = """
        const a = 2
        func foofaa() {
            var c int;
            var d int;
            var b = a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_func_redeclared(self):
        input = """
        func foofoo() {
            return
        } 
        func foofoo() {
            return
        }
        """
        expect = "Redeclared Function: foofoo\n"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_param_redeclared(self):
        input = """
        func foo(a, b int, a int) {
            return
        }
        """
        expect = "Redeclared Parameter: a\n"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_method_redeclared(self):
        input = """
        var foo int;
        func (a Person) foo() {
            return
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_method_redeclared_2(self):
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
        self.assertTrue(TestChecker.test(input,expect,408))  

    def test_method_redeclared_3(self):
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
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_method_redeclared_4(self):
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
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_global(self):
        input = """
        func (a Person) name() {
            return
        }
        type Person struct {
            name string
        }
        """
        expect = "Redeclared Method: name\n"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_method_redeclared_5(self):
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
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_struct_redeclared(self):
        input = """
        type Person struct {
            name string
        }
        type Person struct {
            age int
        }
        """
        expect = "Redeclared Type: Person\n"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_field_redeclared(self):
        input = """
        type Person struct {
            name string
            age int
            name string
        }
        """
        expect = "Redeclared Field: name\n"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_interface_redeclared(self):
        input = """
        type Person interface {
            foo()
        }
        type Person interface {
            foo1()
        }
        """
        expect = "Redeclared Type: Person\n"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_interface_redeclared_2(self):
        input = """
        type Person interface {
            foo()
        }
        type Huy interface {
            foo()
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_prototype_redeclared(self):
        input = """
        type Person interface {
            foo(a int)
            foo()
        }
        """
        expect = "Redeclared Prototype: foo\n"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_mixed_redeclared(self):
        input = """var a int; const a = 1;"""
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_mixed_redeclared_2(self):
        input = """
        var foo int;
        func foo() {
            return
        }
        """
        expect = "Redeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_mixed_redeclared_3(self):
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
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_mix_redeclared_4(self):
        input = """
        const b = 1;
        func foo() {
            var b int
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_mix_redeclared_5(self):
        input = """
        func foo() {
            return
        }
        func (a Person) foo() {
            return
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_mix_redeclared_6(self):
        input = """
        type Person struct {
            name string
        }
        type Person interface {
            age()
        }
        """
        expect = "Redeclared Type: Person\n"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_undeclared_identifier(self):
        input = "var a = b;"
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_undeclared_identifier_2(self):
        input = """
        type Person struct {
            name string
        }
        var a Person;
        var b = c.name;
        """
        expect = "Undeclared Identifier: c\n"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_undeclared_identifier_3(self):
        input = """
        type Person struct {
            name string
        }
        var a Person;
        var b = c.d.name;
        """
        expect = "Undeclared Identifier: c\n"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_undeclared_func(self):
        input = "var a = foo();"
        expect = "Undeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_undeclared_func_2(self):
        input = """
        var foo int 
        func main() {
            foo();
        }
        """
        expect = "Undeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_undeclared_func_3(self):
        input = """
        func main() {
            foo();
        }
        func foo(a, b int) {
            return
        }
        """
        expect = "Type Mismatch: FuncCall(foo,[])\n"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_undeclared_func_4(self):
        input = """
        func main() {
            foo(12,23,45);
        }
        func foo(a, b int) {
            return
        }
        """
        expect = "Type Mismatch: FuncCall(foo,[IntLiteral(12),IntLiteral(23),IntLiteral(45)])\n"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_undeclared_func_5(self):
        input = """
        func main() {
            foo(12, 2.3);
        }
        func foo(a, b int) {
            return
        }
        """
        expect = "Type Mismatch: FuncCall(foo,[IntLiteral(12),FloatLiteral(2.3)])\n"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_undeclared_method(self):
        input = """
        type Person struct {
            name string
        }
        var a Person;
        var b = a.foo();
        """
        expect = "Undeclared Method: foo\n"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_undeclared_method_2(self):
        input = """
        var a Persondepchai;
        var b = a.foo();

        type Persondepchai struct {
            name string
        }

        func (a Persondepchai) foo() {
            return
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,433))    

    def test_undeclared_method_3(self):
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
        self.assertTrue(TestChecker.test(input,expect,434))
    
    def test_undeclared_method_4(self):
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
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_undeclared_method_5(self):
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
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_undeclared_method_6(self):
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
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_undeclared_method_7(self):
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
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_undeclared_field(self):
        input = """
        type Person struct {
            name string
        }
        var a Person;
        var b = a.age;
        """
        expect = "Undeclared Field: age\n"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_undeclared_field_2(self):
        input = """
        type Person struct {
            name string
        }
        var a Person;
        var b = a.name
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_undeclared_field_3(self):
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
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_undeclared_field_4(self):
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
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_undeclared_field_5(self):
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
        self.assertTrue(TestChecker.test(input,expect,508))

    def test_undeclared_mix_access(self):
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
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_undeclared_mix_access_2(self):
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
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_type_mismatch_int_with_float(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test_type_missmatch_int_with_string(self):
        input = """var a int = "huy";"""
        expect = """Type Mismatch: VarDecl(a,IntType,StringLiteral("huy"))\n"""
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_type_missmatch_int_with_bool(self):
        input = """var a int = true;"""
        expect = "Type Mismatch: VarDecl(a,IntType,BooleanLiteral(true))\n"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_type_missmatch_float_with_int(self):
        input = """var a float = 1;"""
        expect = "Type Mismatch: VarDecl(a,FloatType,IntLiteral(1))\n"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_type_missmatch_float_with_string(self):
        input = """var a float = "huy";"""
        expect = "Type Mismatch: VarDecl(a,FloatType,StringLiteral(\"huy\"))\n"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_type_missmatch_float_with_bool(self):
        input = """var a float = false;"""
        expect = "Type Mismatch: VarDecl(a,FloatType,BooleanLiteral(false))\n"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_type_missmatch_return(self):
        input = """
        func foo() int {
            return "huy";
        }
        """
        expect = "Type Mismatch: Return(StringLiteral(\"huy\"))\n"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_type_missmatch_return_2(self):
        input = """
        func foo() int {
            return true;
        }
        """
        expect = "Type Mismatch: Return(BooleanLiteral(true))\n"
        self.assertTrue(TestChecker.test(input,expect,452))
    
    def test_type_missmatch_return_3(self):
        input = """
        func foo() int {
            return 12;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,453))
    
    def test_type_missmatch_plus(self):
        input = """
        func foo() {
            var c = 12 + "huy";
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(12),+,StringLiteral(\"huy\"))\n"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_type_missmatch_plus_2(self):
        input = """
        func foo() {
            var c = true + "huy";
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),+,StringLiteral(\"huy\"))\n"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_type_missmatch_plus_3(self):
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
        self.assertTrue(TestChecker.test(input,expect,456))
    
    def test_type_missmatch_minus(self):
        input = """
        func foo() {
            var c = true - 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),-,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_type_missmatch_minus_2(self):
        input = """
        func foo() {
            var c = "huy" - 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(StringLiteral(\"huy\"),-,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_type_missmatch_mul(self):
        input = """
        func foo() {
            var c = true * 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),*,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_type_missmatch_mul_2(self):
        input = """
        func foo() {
            var c = "huy" * 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(StringLiteral(\"huy\"),*,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_type_missmatch_div(self):
        input = """
        func foo() {
            var c = true / 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),/,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_type_missmatch_div_2(self):
        input = """
        func foo() {
            var c = "huy" / 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(StringLiteral(\"huy\"),/,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,462))        

    def test_type_missmatch_minus_mul_div(self):
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
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_type_missmatch_modulo(self):
        input = """
        func foo() {
            var c = true % 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),%,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_type_missmatch_modulo_2(self):
        input = """
        func foo() {
            var c = "huy" % 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(StringLiteral(\"huy\"),%,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_type_missmatch_modulo_3(self):
        input = """
        func foo() {
            var a = 123 % 45.6
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(123),%,FloatLiteral(45.6))\n"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_type_missmatch_modulo_4(self):
        input = """
        func foo() {
            var a = 123 % 45
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_type_missmatch_equal(self):
        input = """
        func foo() {
            var c = true == 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),==,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_type_missmatch_equal_2(self):
        input = """
        func foo() {
            var c = "huy" == 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(StringLiteral(\"huy\"),==,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_type_missmatch_not_equal(self):
        input = """
        func foo() {
            var c = true != 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),!=,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_type_missmatch_not_equal_2(self):
        input = """
        func foo() {
            var c = 123 != 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(123),!=,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_type_missmatch_less_than(self):
        input = """
        func foo() {
            var c = true < 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),<,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_type_missmatch_less_than_2(self):
        input = """
        func foo() {
            var c = 123 < 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(123),<,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_type_missmatch_less_than_equal(self):
        input = """
        func foo() {
            var c = true <= 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),<=,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_type_missmatch_less_than_equal_2(self):
        input = """
        func foo() {
            var c = 123 <= 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(123),<=,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_type_missmatch_greater_than(self):
        input = """
        func foo() {
            var c = true > 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),>,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,476))
    
    def test_type_missmatch_greater_than_2(self):
        input = """
        func foo() {
            var c = 123 > 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(123),>,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,477))
    
    def test_type_missmatch_greater_than_equal(self):
        input = """
        func foo() {
            var c = true >= 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),>=,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_type_missmatch_greater_than_equal_2(self):
        input = """
        func foo() {
            var c = 123 >= 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(123),>=,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_type_missmatch_relational(self):
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
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_type_missmatch_and(self):
        input = """
        func foo() {
            var c = true && 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),&&,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_type_missmatch_and_2(self):
        input = """
        func foo() {
            var c = 123 && 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(123),&&,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_type_missmatch_or(self):
        input = """
        func foo() {
            var c = true || 123;
        }
        """
        expect = "Type Mismatch: BinaryOp(BooleanLiteral(true),||,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,483))
    
    def test_type_missmatch_or_2(self):
        input = """
        func foo() {
            var c = 123 || 12.3;
        }
        """
        expect = "Type Mismatch: BinaryOp(IntLiteral(123),||,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_type_missmatch_and_or(self):
        input = """
        func foo() {
            var a = true && false
            var b = true || false
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_type_missmatch_neg(self):
        input = """
        func foo() {
            var c = -true;
        }
        """
        expect = "Type Mismatch: UnaryOp(-,BooleanLiteral(true))\n"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_type_missmatch_neg_2(self):
        input = """
        func foo() {
            var c = -"huy";
        }
        """
        expect = "Type Mismatch: UnaryOp(-,StringLiteral(\"huy\"))\n"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_type_missmatch_neg_3(self):
        input = """
        func foo() {
            var a = -123 
            var c = -12.3;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_type_missmatch_not(self):
        input = """
        func foo() {
            var c = !123;
        }
        """
        expect = "Type Mismatch: UnaryOp(!,IntLiteral(123))\n"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_type_missmatch_not_2(self):
        input = """
        func foo() {
            var c = !"huy";
        }
        """
        expect = "Type Mismatch: UnaryOp(!,StringLiteral(\"huy\"))\n"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_type_missmatch_not_3(self):
        input = """
        func foo() {
            var a = !12.3
        }
        """
        expect = "Type Mismatch: UnaryOp(!,FloatLiteral(12.3))\n"
        self.assertTrue(TestChecker.test(input,expect,491))
    
    def test_type_missmatch_not_4(self):
        input = """
        func foo() {
            var a = !true
            var b = !false
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_type_missmatch_field(self):
        input = """
        type Person struct {
            name string
        }
        var a int;
        var b = a.name;
        """
        expect = "Type Mismatch: FieldAccess(Id(a),name)\n"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_type_missmatch_field_2(self):
        input = """
        type Person struct {
            name string
        }

        var a Person;
        var b = a.name.first_name;
        """
        expect = "Type Mismatch: FieldAccess(FieldAccess(Id(a),name),first_name)\n"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_type_missmatch_field_3(self):
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
        self.assertTrue(TestChecker.test(input,expect,510))

    def test_type_missmatch_method(self):
        input = """
        var a Persondepchai;
        var b = a.foo();

        type Persondepchai struct {
            name string
        }

        func (a Persondepchai) foo(a, b int) {
            return
        }
        """
        expect = "Type Mismatch: MethodCall(Id(a),foo,[])\n"
        self.assertTrue(TestChecker.test(input,expect,495))  

    def test_type_missmatch_method_2(self):
        input = """
        var a Persondepchai;
        var b = a.foo(12, 34, 45);

        type Persondepchai struct {
            name string
        }

        func (a Persondepchai) foo(a, b int) {
            return
        }
        """
        expect = "Type Mismatch: MethodCall(Id(a),foo,[IntLiteral(12),IntLiteral(34),IntLiteral(45)])\n"
        self.assertTrue(TestChecker.test(input,expect,496))  

    def test_type_missmatch_method_3(self):
        input = """
        var a Persondepchai;
        var b = a.foo(12, 3.4);

        type Persondepchai struct {
            name string
        }

        func (a Persondepchai) foo(a, b int) {
            return
        }
        """
        expect = "Type Mismatch: MethodCall(Id(a),foo,[IntLiteral(12),FloatLiteral(3.4)])\n"
        self.assertTrue(TestChecker.test(input,expect,497))  

    def test_type_missmatch_method_4(self):
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
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_type_missmatch_method_5(self):
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
        self.assertTrue(TestChecker.test(input,expect,499))
    

    def test_type_missmatch_array_cell(self):
        input = """
        func foo() {
            var a [5]int;
            var b = 2;
            var c = a[b][23];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,500))

    def test_type_missmatch_array_cell_2(self):
        input = """
        func foo() {
            var a [5]int;
            var b = 2.3;
            var c = a[b];
        }
        """
        expect = "Type Mismatch: ArrayCell(Id(a),[Id(b)])\n"
        self.assertTrue(TestChecker.test(input,expect,501))

    def test_type_missmatch_array_cell_3(self):
        input = """
        func foo() {
            var a int;
            var b = 2;
            var c = a[b][23];
        }
        """
        expect = "Type Mismatch: ArrayCell(Id(a),[Id(b),IntLiteral(23)])\n"
        self.assertTrue(TestChecker.test(input,expect,502))

    def test_type_missmatch_array_cell_4(self):
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
        self.assertTrue(TestChecker.test(input,expect,503))

    def test_type_missmatch_array_cell_5(self):
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
        self.assertTrue(TestChecker.test(input,expect,504))

    def test_type_missmatch_array_cell_6(self):
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
        self.assertTrue(TestChecker.test(input,expect,505))

    def test_type_missmatch_if_stmt(self):
        input = """
        func foo() {
            if (1.2) {
                return
            }
        }
        """
        expect = "Type Mismatch: If(FloatLiteral(1.2),Block([Return()]))\n"
        self.assertTrue(TestChecker.test(input,expect,506))

    def test_type_missmatch_if_stmt_2(self):
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
        self.assertTrue(TestChecker.test(input,expect,507))

    def test_type_missmatch_if_stmt_3(self):
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
        self.assertTrue(TestChecker.test(input,expect,509))

    def test_type_missmatch_if_stmt_4(self):
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
        self.assertTrue(TestChecker.test(input,expect,511))

    def test_type_missmatch_if_stmt_5(self):
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
        self.assertTrue(TestChecker.test(input,expect,512))

    def test_type_missmatch_for_basic_stmt(self):
        input = """
        func foo() {
            for (1.2) {
                return
            }
        }
        """
        expect = "Type Mismatch: For(FloatLiteral(1.2),Block([Return()]))\n"
        self.assertTrue(TestChecker.test(input,expect,513))

    def test_type_missmatch_for_step_stmt(self):
        input = """
        func foo() {
            for var i = 0; 23 + 45; i += 1 {
                return
            }
        }
        """
        expect = "Type Mismatch: For(VarDecl(i,IntType,IntLiteral(0)),BinaryOp(IntLiteral(23),+,IntLiteral(45)),Assign(Id(i),BinaryOp(Id(i),+,IntLiteral(1))),Block([Return()]))\n"
        self.assertTrue(TestChecker.test(input,expect,514))

    def test_type_missmatch_for_each(self):
        input = """
        func foo() {
            var arr [5]int
            for i, i := range arr {
                return
            }
        }
        """
        expect = "Redeclared Variable: i\n"
        self.assertTrue(TestChecker.test(input,expect,515))

    def test_type_missmatch_for_each_2(self):
        input = """
        func foo() {
            var arr int
            for idx, val := range arr {
                return
            }
        }
        """
        expect = "Type Mismatch: ForEach(Id(idx),Id(val),Id(arr),Block([Return()]))\n"
        self.assertTrue(TestChecker.test(input,expect,516))

    