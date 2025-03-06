import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_prim_type(self):
        input = """
        var x int;
        var y float;
        var z boolean;
        var t string;
        """
        expect = str(Program([VarDecl("x",IntType(),None),VarDecl("y",FloatType(),None),VarDecl("z",BoolType(),None),VarDecl("t",StringType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_array_type(self):
        input = """
        var arr [5]float;
        """
        expect = str(Program([VarDecl("arr",ArrayType([IntLiteral(5)],FloatType()),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_array_type_with_mul_dim(self):
        input = """
        var multi_arr [2][5][3]int;
        """
        expect = str(Program([VarDecl("multi_arr",ArrayType([IntLiteral(2),IntLiteral(5),IntLiteral(3)],IntType()),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
    def test_var_decl_struct_type(self):
        input = """
        var huy Person;
        """
        expect = str(Program([VarDecl("huy",Id("Person"),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_struct_type(self):
        input = """
        type Point struct {
            x int
            y int
        }
        """
        expect = str(Program([StructType("Point",[("x",IntType()),("y",IntType())],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_struct_type_with_prim_type(self):
        input = """
        type FullStruct struct {
            ID          int;              
            Name        string;            
            IsActive    boolean;              
            Price       float;             
        }
        """
        expect = str(Program([StructType("FullStruct",[("ID",IntType()),("Name",StringType()),("IsActive",BoolType()),("Price",FloatType())],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_struct_type_with_array_type(self):
        input = """
        type FullStruct struct {
            Ratings     [3]int;       
        }
        """
        expect = str(Program([StructType("FullStruct",[("Ratings",ArrayType([IntLiteral(3)],IntType()))],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_struct_type_with_struct_type(self):
        input = """
        type FullStruct struct {
            David       Person
        }
        """
        expect = str(Program([StructType("FullStruct",[("David",Id("Person"))],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_interface_type(self):
        input = """
        type Calculator interface {
            Reset()
        }
        """
        expect = str(Program([InterfaceType("Calculator",[Prototype("Reset",[],VoidType())])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_interface_type_2(self):
        input = """
        type Calculator interface {
            SayHello(name string)
        }
        """
        expect = str(Program([InterfaceType("Calculator",[Prototype("SayHello",[StringType()],VoidType())])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_interface_type_3(self):
        input = """
        type Calculator interface {
            Add(x, y int) int;
        }
        """
        expect = str(Program([InterfaceType("Calculator",[Prototype("Add",[IntType(),IntType()],IntType())])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_interface_type_4(self):
        input = """
        type Calculator interface {
            Subtract(a, b float, c int) [2]float;
        }
        """
        expect = str(Program([InterfaceType("Calculator",[Prototype("Subtract",[FloatType(),FloatType(),IntType()],ArrayType([IntLiteral(2)],FloatType()))])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_prim_literal(self):
        input = """
        var x = 5;
        var y = 5.5;
        var z = true;
        var t = "Hello";
        """
        expect = str(Program([VarDecl("x",None,IntLiteral(5)),VarDecl("y",None,FloatLiteral(5.5)),VarDecl("z",None,BooleanLiteral(True)),VarDecl("t",None,StringLiteral("\"Hello\""))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    
    def test_complex_int_literal(self):
        input = """
        func main() {
            var x = 0x1;
            var y = 0o1;
            var z = 0b1;
            var t = 0X1;
            var u = 0O1;
            var v = 0B1;
        }
        """
        expect = str(Program([FuncDecl('main',[],VoidType(),Block([VarDecl('x',None,IntLiteral('0x1')),VarDecl('y',None,IntLiteral('0o1')),VarDecl('z',None,IntLiteral('0b1')),VarDecl('t',None,IntLiteral('0X1')),VarDecl('u',None,IntLiteral('0O1')),VarDecl('v',None,IntLiteral('0B1'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_complex_float_literal(self):
        input = """
        func main() {
            var x = 1.e12;
            var y = 1.0e-2;
            var z = 1.0e+2
            var t = 1.0e2
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("x",None,FloatLiteral('1.e12')),VarDecl("y",None,FloatLiteral('1.0e-2')),VarDecl("z",None,FloatLiteral('1.0e+2')),VarDecl("t",None,FloatLiteral('1.0e2'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_array_literal(self):
        input = """
        var arr = [5]int{1,2,3,4,5};
        """
        expect = str(Program([VarDecl("arr",None,ArrayLiteral([IntLiteral(5)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_array_literal_with_mul_dim(self):
        input = """
        var multi_arr = [2][5][3]int{{1,2,3,4,5},{6,7,8,9,10}};
        """
        expect = str(Program([VarDecl("multi_arr",None,ArrayLiteral([IntLiteral(2),IntLiteral(5),IntLiteral(3)],IntType(),[[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)],[IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10)]]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_mixed_array_literal(self):
        input = """
        var arr = [5]int{"1",2,3.4,true,nil};
        """
        expect = str(Program([VarDecl("arr",None,ArrayLiteral([IntLiteral(5)],IntType(),[StringLiteral("\"1\""),IntLiteral(2),FloatLiteral(3.4),BooleanLiteral(True),NilLiteral()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_struct_literal(self):
        input = """
        var p = Person{name: "John", age: 20}
        """
        expect = str(Program([VarDecl("p",None,StructLiteral("Person",[("name",StringLiteral("\"John\"")),("age",IntLiteral(20))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_struct_literal_with_empty(self):
        input = """
        var p = Person{}
        """
        expect = str(Program([VarDecl("p",None,StructLiteral("Person",[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_var_decl(self):
        input = """
        var x int = 5
        var y float = 5.5
        var z boolean = true
        var t string = "Hello"
        """
        expect = str(Program([VarDecl("x",IntType(),IntLiteral(5)),VarDecl("y",FloatType(),FloatLiteral(5.5)),VarDecl("z",BoolType(),BooleanLiteral(True)),VarDecl("t",StringType(),StringLiteral("\"Hello\""))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321)) 

    def test_var_decl_with_expr(self):
        input = """
        var x int = y
        """
        expect = str(Program([VarDecl("x",IntType(),Id("y"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_var_decl_with_complex_expr(self):
        input = """
        var x int = 5 + 3 * 4.5 
        var y float = -34
        var z boolean = true && false
        var t string = "Hello" + "World"
        """
        expect = str(Program([VarDecl("x",IntType(),BinaryOp("+",IntLiteral(5),BinaryOp("*",IntLiteral(3),FloatLiteral(4.5)))),VarDecl("y",FloatType(),UnaryOp("-",IntLiteral(34))),VarDecl("z",BoolType(),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False))),VarDecl("t",StringType(),BinaryOp("+",StringLiteral("\"Hello\""),StringLiteral("\"World\"")))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_const_decl(self):
        input = """
        const Pi = 3.14
        const Greeting = "Hello, MiniGo!"
        const MaxSize = 100 + 50
        """
        expect = str(Program([ConstDecl("Pi",None,FloatLiteral(3.14)),ConstDecl("Greeting",None,StringLiteral("\"Hello, MiniGo!\"")),ConstDecl("MaxSize",None,BinaryOp("+",IntLiteral(100),IntLiteral(50)))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_const_with_arithmetic_expr(self):
        input = """
        const x = 10 + 5 - 3 * 2 / 4 % 2;
        """
        expect = str(Program([ConstDecl("x",None,BinaryOp("-",BinaryOp("+",IntLiteral(10),IntLiteral(5)),BinaryOp("%",BinaryOp("/",BinaryOp("*",IntLiteral(3),IntLiteral(2)),IntLiteral(4)),IntLiteral(2))))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_const_with_relational_expr(self):
        input = """
        const x = a == b && c != d || e < f || g >= h;
        """
        expect = str(Program([ConstDecl("x",None,BinaryOp("||",BinaryOp("||",BinaryOp("&&",BinaryOp("==",Id("a"),Id("b")),BinaryOp("!=",Id("c"),Id("d"))),BinaryOp("<",Id("e"),Id("f"))),BinaryOp(">=",Id("g"),Id("h"))))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_const_with_boolean_expr(self):
        input = """
        const flag = a && b || c && d || !e
        """
        expect = str(Program([ConstDecl("flag",None,BinaryOp("||",BinaryOp("||",BinaryOp("&&",Id("a"),Id("b")),BinaryOp("&&",Id("c"),Id("d"))),UnaryOp("!",Id("e"))))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_const_with_full_operator_expr(self):
        input = """
        const x = (a + b * c / d - e % f) == g && h.age > 18 || arr[i] < arr[j];
        """
        expect = str(Program([ConstDecl("x",None,BinaryOp("||",BinaryOp("&&",BinaryOp("==",BinaryOp("-",BinaryOp("+",Id("a"),BinaryOp("/",BinaryOp("*",Id("b"),Id("c")),Id("d"))),BinaryOp("%",Id("e"),Id("f"))),Id("g")),BinaryOp(">",FieldAccess(Id("h"),"age"),IntLiteral(18))),BinaryOp("<",ArrayCell(Id("arr"),[Id("i")]),ArrayCell(Id("arr"),[Id("j")]))))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_const_with_array_cell_seq(self):
        input = """
        const a = a[1][2][3][4];
        """
        expect = str(Program([ConstDecl("a",None,ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 329))

    def test_const_with_index_expr(self):
        input = """
        const a = a[1 + 2];
        """
        expect = str(Program([ConstDecl("a",None,ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(1),IntLiteral(2))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 330))

    def test_const_with_field_access_seq(self):
        input = """
        const a = a.b.c.d.e;
        """
        expect = str(Program([ConstDecl("a",None,FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e"))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 331))

    def test_func_decl(self):
        input = """func main() {
            var x int
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("x",IntType(),None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_func_decl_with_param(self):
        input = """func main(x int, y float) {
            var z string
        }
        """
        expect = str(Program([FuncDecl("main",[ParamDecl("x",IntType()),ParamDecl("y",FloatType())],VoidType(),Block([VarDecl("z",StringType(),None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_func_decl_with_array_param(self):
        input = """
        func foo(a int, b [1]int) {
            return;
        }
        """
        expect = str(Program([FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",ArrayType([IntLiteral(1)],IntType()))],VoidType(),Block([Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 334))

    def test_func_decl_with_seq_param(self):
        input = """
        func foo(a int, b float, c string, d Person, f[1][2]int) Person{
            return d;
        }
        """
        expect = str(Program([FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",FloatType()),ParamDecl("c",StringType()),ParamDecl("d",Id("Person")),ParamDecl("f",ArrayType([IntLiteral(1),IntLiteral(2)],IntType()))],Id("Person"),Block([Return(Id("d"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_func_decl_with_return(self):
        input = """
        func main() int {
            return 1
        }
        """
        expect = str(Program([FuncDecl("main",[],IntType(),Block([Return(IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_func_decl_with_array_return(self):
        input = """
        func foo() [2]int {
            return;
        }
        """
        expect = str(Program([FuncDecl("foo",[],ArrayType([IntLiteral(2)],IntType()),Block([Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 337))

    def test_func_decl_with_param_and_return(self):
        input = """
        func main(x int, y float) string {
            return "Hello"
        }
        """
        expect = str(Program([FuncDecl("main",[ParamDecl("x",IntType()),ParamDecl("y",FloatType())],StringType(),Block([Return(StringLiteral("\"Hello\""))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_method_decl(self):
        input = """
        func (p Person) foo() {
            var x int
        }
        """
        expect = str(Program([MethodDecl("p",Id("Person"),FuncDecl("foo",[],VoidType(),Block([VarDecl("x",IntType(),None)])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_method_decl_with_param(self):
        input = """
        func  (Cat c) foo(a int) {
            return;
        }
        """
        expect = str(Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[ParamDecl("a",IntType())],VoidType(),Block([Return(None)])))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 340))

    def test_method_decl_with_array_param(self):
        input = """
        func  (Cat c) foo(a [2]ID) {
            return;
        }
        """
        expect = str(Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[ParamDecl("a",ArrayType([IntLiteral(2)],Id("ID")))],VoidType(),Block([Return(None)])))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 341))

    def test_method_decl_with_seq_param(self):
        input = """
        func (e Cal) foo(a int, b float, c string, d Person, f[1][2]int) Person{
            return d;
        }
        """
        expect = str(Program([MethodDecl("e",Id("Cal"),FuncDecl("foo",[ParamDecl("a",IntType()),ParamDecl("b",FloatType()),ParamDecl("c",StringType()),ParamDecl("d",Id("Person")),ParamDecl("f",ArrayType([IntLiteral(1),IntLiteral(2)],IntType()))],Id("Person"),Block([Return(Id("d"))])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_method_decl_with_return(self):
        input = """
        func  (Cat c) foo() int {
            return;
        }
        """
        expect = str(Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[],IntType(),Block([Return(None)])))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 343))

    def test_method_decl_with_array_return(self):
        input = """
        func  (Cat c) foo() [2]string {
            return;
        }
        """
        expect = str(Program([MethodDecl("Cat",Id("c"),FuncDecl("foo",[],ArrayType([IntLiteral(2)],StringType()),Block([Return(None)])))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 344))

    def test_mixed_decl(self):
        input = """
        var x int = 5
        const Two = 2
        func Three() int {
            return 3
        }
        """
        expect = str(Program([VarDecl("x",IntType(),IntLiteral(5)),ConstDecl("Two",None,IntLiteral(2)),FuncDecl("Three",[],IntType(),Block([Return(IntLiteral(3))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_mixed_decl_2(self):
        input = """
        type Point struct {
            x int
            y int
        }
        func main() {
            var p = Point{x: 1, y: 2}
        }
        """
        expect = str(Program([StructType("Point",[("x",IntType()),("y",IntType())],[]),FuncDecl("main",[],VoidType(),Block([VarDecl("p",None,StructLiteral("Point",[("x",IntLiteral(1)),("y",IntLiteral(2))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_mixed_decl_3(self):
        input = """
        type Point struct {
            x int
            y int
        }

        func (p Point) printPoint() {
            print("(", p.x, ", ", p.y, ")")
        }

        func main() {
            var p = Point{}
        }
        """
        expect = str(Program([StructType("Point",[("x",IntType()),("y",IntType())],[]),MethodDecl("p",Id("Point"),FuncDecl("printPoint",[],VoidType(),Block([FuncCall("print",[StringLiteral("\"(\""),FieldAccess(Id("p"),"x"),StringLiteral("\", \""),FieldAccess(Id("p"),"y"),StringLiteral("\")\"")])]))),FuncDecl("main",[],VoidType(),Block([VarDecl("p",None,StructLiteral("Point",[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    
    def test_mixed_decl_4(self):
        input = """
        type Shape interface {
            Area() float
        }        

        func (c Circle) Area() float {
            return 1
        }
        """
        expect = str(Program([InterfaceType("Shape",[Prototype("Area",[],FloatType())]),MethodDecl("c",Id("Circle"),FuncDecl("Area",[],FloatType(),Block([Return(IntLiteral(1))])))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_mixed_decl_5(self):
        input = """
        func swap(x, y int) int {
            var temp = x
            x := y
            y := temp
            return true
        }
        func main() {
            var flag = swap(1, 2)
        }
        """
        expect = str(Program([FuncDecl("swap",[ParamDecl("x",IntType()),ParamDecl("y",IntType())],IntType(),Block([VarDecl("temp",None,Id("x")),Assign(Id("x"),Id("y")),Assign(Id("y"),Id("temp")),Return(BooleanLiteral(True))])),FuncDecl("main",[],VoidType(),Block([VarDecl("flag",None,FuncCall("swap",[IntLiteral(1),IntLiteral(2)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
        
    def test_arithmetic_expr(self):
        input = """
        func main() {
            var x int;
            x := 10 + 5 - 3 * 2 / 4 % 2;
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("x",IntType(),None),Assign(Id("x"),BinaryOp("-",BinaryOp("+",IntLiteral(10),IntLiteral(5)),BinaryOp("%",BinaryOp("/",BinaryOp("*",IntLiteral(3),IntLiteral(2)),IntLiteral(4)),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_relational_expr(self):
        input = """
        func main() {
            var x boolean;
            x := a == b && c != d || e < f || g >= h;
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("x",BoolType(),None),Assign(Id("x"),BinaryOp("||",BinaryOp("||",BinaryOp("&&",BinaryOp("==",Id("a"),Id("b")),BinaryOp("!=",Id("c"),Id("d"))),BinaryOp("<",Id("e"),Id("f"))),BinaryOp(">=",Id("g"),Id("h"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_boolean_expr(self):
        input = """
        func main() {
            var flag boolean
            flag := a && b || c && d || !e
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("flag",BoolType(),None),Assign(Id("flag"),BinaryOp("||",BinaryOp("||",BinaryOp("&&",Id("a"),Id("b")),BinaryOp("&&",Id("c"),Id("d"))),UnaryOp("!",Id("e"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_full_operator_expr(self):
        input = """
        func main() {
            var x boolean;
            x := (a + b * c / d - e % f) == g && h.age > 18 || arr[i] < arr[j];
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("x",BoolType(),None),Assign(Id("x"),BinaryOp("||",BinaryOp("&&",BinaryOp("==",BinaryOp("-",BinaryOp("+",Id("a"),BinaryOp("/",BinaryOp("*",Id("b"),Id("c")),Id("d"))),BinaryOp("%",Id("e"),Id("f"))),Id("g")),BinaryOp(">",FieldAccess(Id("h"),"age"),IntLiteral(18))),BinaryOp("<",ArrayCell(Id("arr"),[Id("i")]),ArrayCell(Id("arr"),[Id("j")]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_array_cell_seq_expr(self):
        input = """
        func main() {
            var a float
            a := a[1][2][3][4];
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",FloatType(),None),Assign(Id("a"),ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 354))

    def test_array_cell_with_index_expr(self):
        input = """
        func main() {
            var a Person
            a := a[1 + 2];
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",Id("Person"),None),Assign(Id("a"),ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(1),IntLiteral(2))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 355))

    def test_field_access_seq_expr(self):
        input = """
        func main() {
            var a string
            a := a.b.c.d.e;
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",StringType(),None),Assign(Id("a"),FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),"b"),"c"),"d"),"e"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 356))

    def test_complex_expr(self):
        input = """
        func main() {
            var tmp int;
            tmp := 1[2] + foo()[2] + ID[2].b.b;
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([VarDecl("tmp",IntType(),None),Assign(Id("tmp"),BinaryOp("+",BinaryOp("+",ArrayCell(IntLiteral(1),[IntLiteral(2)]),ArrayCell(FuncCall("foo",[]),[IntLiteral(2)])),FieldAccess(FieldAccess(ArrayCell(Id("ID"),[IntLiteral(2)]),"b"),"b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_access_array(self):
        input = """
        func main() {
            a[2][3] := b[2][4] + 1;
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([Assign(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)]),BinaryOp("+",ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(4)]),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    
    def test_access_struct(self):
        input = """
        func main() {
            p.name := "John";
            p.age := 20;
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([Assign(FieldAccess(Id("p"),"name"),StringLiteral("\"John\"")),Assign(FieldAccess(Id("p"),"age"),IntLiteral(20))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

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
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([Assign(FieldAccess(FieldAccess(Id("p"),"David"),"name"),StringLiteral("\"David\"")),Assign(Id("admin"),MethCall(FieldAccess(Id("p"),"Metadata"),"CreatedBy",[])),MethCall(ArrayCell(FieldAccess(Id("f"),"p"),[Id("i")]),"x",[]),Assign(ArrayCell(Id("m"),[StringLiteral("\"foo\"")]),BinaryOp("+",IntLiteral(1),Id("i"))),VarDecl("a",None,ArrayCell(MethCall(MethCall(Id("a"),"foo",[]),"bar",[]),[BinaryOp("+",IntLiteral(4),BinaryOp("/",Id("y"),IntLiteral(2)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_function_call(self):
        input = """
        func main() {
            Add(1, 2);
            reset()
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([FuncCall("Add",[IntLiteral(1),IntLiteral(2)]),FuncCall("reset",[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_func_call_with_expr_param(self):
        input = """
        func main() {
            Add(1 + 2, 3 * 4);
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([FuncCall("Add",[BinaryOp("+",IntLiteral(1),IntLiteral(2)),BinaryOp("*",IntLiteral(3),IntLiteral(4))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_func_call_with_seq_param(self):
        input = """
        func main(){
            foo("abc", 5, 5.5, true, nil, false, Person{name: "John", age: 25});
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([FuncCall("foo",[StringLiteral("\"abc\""),IntLiteral(5),FloatLiteral(5.5),BooleanLiteral(True),NilLiteral(),BooleanLiteral(False),StructLiteral("Person",[("name",StringLiteral("\"John\"")),("age",IntLiteral(25))])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_func_call_nested(self):
        input = """
        func main() {
            foo(foo(1,2), foo(4,5));
            goo(goo(goo(goo(goo(goo(1))))));
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([FuncCall("foo",[FuncCall("foo",[IntLiteral(1),IntLiteral(2)]),FuncCall("foo",[IntLiteral(4),IntLiteral(5)])]),FuncCall("goo",[FuncCall("goo",[FuncCall("goo",[FuncCall("goo",[FuncCall("goo",[FuncCall("goo",[IntLiteral(1)])])])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_method_call(self):
        input = """
        func main() {
            calculator.add(3, 4)
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([MethCall(Id("calculator"),"add",[IntLiteral(3),IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_method_call_with_seq(self):
        input = """
        func main() {
            calculator.operator.add(3, 4)
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([MethCall(FieldAccess(Id("calculator"),"operator"),"add",[IntLiteral(3),IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_method_call_with_nested(self):
        input = """
        func main() {
            calculator.add(calculator.sub(5, 2), 4)
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([MethCall(Id("calculator"),"add",[MethCall(Id("calculator"),"sub",[IntLiteral(5),IntLiteral(2)]),IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

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
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(10))),Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(5))),Assign(Id("y"),BinaryOp("*",Id("y"),IntLiteral(23))),Assign(Id("z"),BinaryOp("/",Id("z"),IntLiteral(2))),Assign(Id("t"),BinaryOp("%",Id("t"),IntLiteral(23)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_lhs_assignment_stmt(self):
        input = """
        func main() {
            arr[2 + i] *= 3
            Person.age += 1
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([Assign(ArrayCell(Id("arr"),[BinaryOp("+",IntLiteral(2),Id("i"))]),BinaryOp("*",ArrayCell(Id("arr"),[BinaryOp("+",IntLiteral(2),Id("i"))]),IntLiteral(3))),Assign(FieldAccess(Id("Person"),"age"),BinaryOp("+",FieldAccess(Id("Person"),"age"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_rhs_assignment_stmt(self):
        input = """
        func main() {
            arr[3] := 10 + person.age
            y += a[2] * b[3][2]
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([Assign(ArrayCell(Id("arr"),[IntLiteral(3)]),BinaryOp("+",IntLiteral(10),FieldAccess(Id("person"),"age"))),Assign(Id("y"),BinaryOp("+",Id("y"),BinaryOp("*",ArrayCell(Id("a"),[IntLiteral(2)]),ArrayCell(Id("b"),[IntLiteral(3),IntLiteral(2)]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_if_statement(self):
        input = """
        func main() {
            if (a > b) {
                return a;
            }
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([If(BinaryOp(">",Id("a"),Id("b")),Block([Return(Id("a"))]),None)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

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
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([If(BinaryOp(">",Id("a"),Id("b")),Block([Return(Id("a"))]),Block([Return(Id("b"))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

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
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([If(BinaryOp(">",Id("x"),IntLiteral(10)),Block([FuncCall("println",[StringLiteral("\"x is greater than 10\"")])]),If(BinaryOp("==",Id("x"),IntLiteral(10)),Block([FuncCall("println",[StringLiteral("\"x is equal to 10\"")])]),None))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

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
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([If(BinaryOp(">",Id("x"),IntLiteral(10)),Block([FuncCall("println",[StringLiteral("\"x is greater than 10\"")])]),If(BinaryOp("==",Id("x"),IntLiteral(10)),Block([FuncCall("println",[StringLiteral("\"x is equal to 10\"")])]),Block([FuncCall("println",[StringLiteral("\"x is less than 10\"")])])))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

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
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([If(BinaryOp(">",Id("x"),IntLiteral(5)),Block([If(BinaryOp("<",Id("x"),IntLiteral(10)),Block([FuncCall("println",[StringLiteral("\"x is between 5 and 10\"")])]),None)]),None)]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

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
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([If(BinaryOp(">",Id("x"),IntLiteral(5)),Block([If(BinaryOp("<",Id("x"),IntLiteral(10)),Block([FuncCall("println",[StringLiteral("\"x is between 5 and 10\"")])]),Block([FuncCall("println",[StringLiteral("\"x is greater than 10\"")])]))]),Block([FuncCall("println",[StringLiteral("\"x is less than 5\"")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_basic_for_statement(self):
        input = """
        func main() {
            for i < 10 {
                // loop body
                i += 1;
            }
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([ForBasic(BinaryOp("<",Id("i"),IntLiteral(10)),Block([Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_basic_for_stmt_with_complex_expr(self):
        input = """
        func main() {
            for a.i[8] {
                return;
                return 1;
            }
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([ForBasic(ArrayCell(FieldAccess(Id("a"),"i"),[IntLiteral(8)]),Block([Return(None),Return(IntLiteral(1))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

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
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([ForBasic(BooleanLiteral(True),Block([Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(BinaryOp("==",Id("i"),IntLiteral(10)),Block([Break()]),None)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_full_for_statement(self):
        input = """
        func main() {
            for i := 0; i < 10; i += 1 {
                sum += i; // loop body
            }
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Assign(Id("sum"),BinaryOp("+",Id("sum"),Id("i")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_full_for_stmt_with_complex_expr(self):
        input = """
        func main() {
            for i := 0; i[1] < 10; i *= 2+3  {
                return;
                return 1;
            }
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",ArrayCell(Id("i"),[IntLiteral(1)]),IntLiteral(10)),Assign(Id("i"),BinaryOp("*",Id("i"),BinaryOp("+",IntLiteral(2),IntLiteral(3)))),Block([Return(None),Return(IntLiteral(1))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))
    
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
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([Assign(Id("arr"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(10),IntLiteral(20),IntLiteral(30)])),ForEach(Id("index"),Id("value"),Id("arr"),Block([FuncCall("println",[Id("index"),Id("value")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

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
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([Assign(Id("arr"),ArrayLiteral([IntLiteral(3)],IntType(),[IntLiteral(10),IntLiteral(20),IntLiteral(30)])),ForEach(Id("_"),Id("value"),Id("arr"),Block([FuncCall("println",[Id("value")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_range_for_with_range_expr(self):
        input = """
        func main() {
            for index, value := range [2]int{1,2} {
                    return;
                return 1;
            }
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([ForEach(Id("index"),Id("value"),ArrayLiteral([IntLiteral(2)],IntType(),[IntLiteral(1),IntLiteral(2)]),Block([Return(None),Return(IntLiteral(1))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 384))

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
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([ForStep(Assign(Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),IntLiteral(10)),Assign(Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([Assign(Id("sum"),BinaryOp("+",Id("sum"),BinaryOp("+",Id("i"),Id("j"))))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_nested_for_statement_2(self):
        input = """
        func main(){
            for true {
                for false{
                    for i < 10{
                        putInt(i);
                    }
                }
            }
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([ForBasic(BooleanLiteral(True),Block([ForBasic(BooleanLiteral(False),Block([ForBasic(BinaryOp("<",Id("i"),IntLiteral(10)),Block([FuncCall("putInt",[Id("i")])]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_nested_for_statement_3(self):
        input = """
        func main() {
            for idx, value := range arr {
                for _, v := range arr[idx] {
                    for _, x := range arr[idx + x] {
                        println(value, v, x);
                    }
                }
            }
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([ForEach(Id("idx"),Id("value"),Id("arr"),Block([ForEach(Id("_"),Id("v"),ArrayCell(Id("arr"),[Id("idx")]),Block([ForEach(Id("_"),Id("x"),ArrayCell(Id("arr"),[BinaryOp("+",Id("idx"),Id("x"))]),Block([FuncCall("println",[Id("value"),Id("v"),Id("x")])]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

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
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",Id("i"),IntLiteral(5)),Block([Break()]),None)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

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
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([ForStep(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",Id("i"),IntLiteral(5)),Block([Continue()]),None)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_break_continue_stmt_not_in_loop(self):
        input = """
        func main() {
            break;
            continue;
        }
        """
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([Break(),Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_return_stmt(self):
        input = """
        func calc(x, y, z int) int {
            return 2 + x - y * z;
        }
        """
        expect = str(Program([FuncDecl("calc",[ParamDecl("x",IntType()),ParamDecl("y",IntType()),ParamDecl("z",IntType())],IntType(),Block([Return(BinaryOp("-",BinaryOp("+",IntLiteral(2),Id("x")),BinaryOp("*",Id("y"),Id("z"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_return_stmt_with_func_call(self):
        input = """
        func calc(x, y, z int) int {
            return add(x, y) * z;
        }
        """
        expect = str(Program([FuncDecl("calc",[ParamDecl("x",IntType()),ParamDecl("y",IntType()),ParamDecl("z",IntType())],IntType(),Block([Return(BinaryOp("*",FuncCall("add",[Id("x"),Id("y")]),Id("z")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_return_stmt_with_complex_expr(self):
        input = """
        func calc(x, y, z int) int {
            return (x - y) / z <= a && b || !c + d[23 + 5] % huy.abc(12, 4);
        }
        """
        expect = str(Program([FuncDecl("calc",[ParamDecl("x",IntType()),ParamDecl("y",IntType()),ParamDecl("z",IntType())],IntType(),Block([Return(BinaryOp("||",BinaryOp("&&",BinaryOp("<=",BinaryOp("/",BinaryOp("-",Id("x"),Id("y")),Id("z")),Id("a")),Id("b")),BinaryOp("+",UnaryOp("!",Id("c")),BinaryOp("%",ArrayCell(Id("d"),[BinaryOp("+",IntLiteral(23),IntLiteral(5))]),MethCall(Id("huy"),"abc",[IntLiteral(12),IntLiteral(4)])))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))  

    def test_return_stmt_with_var(self):
        input = """
        func calc(x, y, z int) int {
            var result int = 2 + x - y * z;
            return result;
        }
        """
        expect = str(Program([FuncDecl("calc",[ParamDecl("x",IntType()),ParamDecl("y",IntType()),ParamDecl("z",IntType())],IntType(),Block([VarDecl("result",IntType(),BinaryOp("-",BinaryOp("+",IntLiteral(2),Id("x")),BinaryOp("*",Id("y"),Id("z")))),Return(Id("result"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_return_stmt_without_expr(self):
        input = """
        func calc(x, y, z int) {
            if (x > y) {
                return;
            }
        }
        """
        expect = str(Program([FuncDecl("calc",[ParamDecl("x",IntType()),ParamDecl("y",IntType()),ParamDecl("z",IntType())],VoidType(),Block([If(BinaryOp(">",Id("x"),Id("y")),Block([Return(None)]),None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

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
        expect = str(Program([FuncDecl("isPalindrome",[ParamDecl("n",IntType())],Id("bool"),Block([VarDecl("reversed",IntType(),IntLiteral(0)),VarDecl("original",IntType(),Id("n")),ForBasic(BinaryOp(">",Id("n"),IntLiteral(0)),Block([Assign(Id("reversed"),BinaryOp("+",BinaryOp("*",Id("reversed"),IntLiteral(10)),BinaryOp("%",Id("n"),IntLiteral(10)))),Assign(Id("n"),BinaryOp("/",Id("n"),IntLiteral(10)))])),Return(BinaryOp("==",Id("original"),Id("reversed")))])),FuncDecl("main",[],VoidType(),Block([MethCall(Id("fmt"),"Println",[FuncCall("isPalindrome",[IntLiteral(121)])])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

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
        expect = str(Program([FuncDecl("fib",[ParamDecl("n",IntType())],IntType(),Block([If(BinaryOp("<=",Id("n"),IntLiteral(1)),Block([Return(Id("n"))]),None),Return(BinaryOp("+",FuncCall("fib",[BinaryOp("-",Id("n"),IntLiteral(1))]),FuncCall("fib",[BinaryOp("-",Id("n"),IntLiteral(2))])))])),FuncDecl("main",[],VoidType(),Block([MethCall(Id("fmt"),"Println",[FuncCall("fib",[IntLiteral(10)])])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

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
        expect = str(Program([FuncDecl("gcd",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],IntType(),Block([ForBasic(BinaryOp("!=",Id("b"),IntLiteral(0)),Block([Assign(Id("tmp"),Id("a")),Assign(Id("a"),Id("b")),Assign(Id("b"),BinaryOp("%",Id("tmp"),Id("b")))])),Return(Id("a"))])),FuncDecl("main",[],VoidType(),Block([MethCall(Id("fmt"),"Println",[FuncCall("gcd",[IntLiteral(24),IntLiteral(36)])])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_lcm(self):
        input = """
        func lcm(a, b int) int {
            return a * b / gcd(a, b)
        }

        func main() {
            fmt.Println(lcm(24, 36)) // 72
        }
        """
        expect = str(Program([FuncDecl("lcm",[ParamDecl("a",IntType()),ParamDecl("b",IntType())],IntType(),Block([Return(BinaryOp("/",BinaryOp("*",Id("a"),Id("b")),FuncCall("gcd",[Id("a"),Id("b")])))])),FuncDecl("main",[],VoidType(),Block([MethCall(Id("fmt"),"Println",[FuncCall("lcm",[IntLiteral(24),IntLiteral(36)])])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

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
        expect = str(Program([FuncDecl("isPrime",[ParamDecl("n",IntType())],Id("bool"),Block([If(BinaryOp("<=",Id("n"),IntLiteral(1)),Block([Return(BooleanLiteral(False))]),None),ForStep(Assign(Id("i"),IntLiteral(2)),BinaryOp("<=",BinaryOp("*",Id("i"),Id("i")),Id("n")),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),Block([Return(BooleanLiteral(False))]),None)])),Return(BooleanLiteral(True))])),FuncDecl("main",[],VoidType(),Block([MethCall(Id("fmt"),"Println",[FuncCall("isPrime",[IntLiteral(17)])])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))


