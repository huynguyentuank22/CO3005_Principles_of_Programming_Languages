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
        expect = str(Program([
            VarDecl("x",IntType(),None),
            VarDecl("y",FloatType(),None),
            VarDecl("z",BoolType(),None),
            VarDecl("t",StringType(),None)
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_array_type(self):
        input = """
        var arr [5]Person;
        var multi_arr [2][5]int;
        """
        expect = str(Program([
            VarDecl("arr",ArrayType([IntLiteral(5)], Id("Person")),None),
            VarDecl("multi_arr",ArrayType([IntLiteral(2),IntLiteral(5)], IntType()),None)
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_struct_type(self):
        input = """
        type Point struct {
            x int
            y int
        }
        """
        expect = str(Program([
            StructType("Point",
            [('x',IntType()), ('y',IntType())], 
            [])
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_struct_type_all_type(self):
        input = """
        type FullStruct struct {
            ID          int;              
            Name        string;            
            IsActive    boolean;              
            Price       float;           
            Ratings     [3]int;
            David       Person;

            func (s FullStruct) foo() int {
                return 1;
            }    
        }
        """
        expect = str(Program([
            StructType("FullStruct",
            [
                ('ID',IntType()),
                ('Name',StringType()),
                ('IsActive',BoolType()),
                ('Price',FloatType()),
                ('Ratings',ArrayType([IntLiteral(3)], IntType())),
                ('David',Id("Person"))
            ],
            [
                MethodDecl("s",Id("FullStruct"),FuncDecl("foo",[],IntType(),Block([Return(IntLiteral(1))])))
            ])
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_interface_type(self):
        input = """
        type Calculator interface {
            Add(x, y int) int;
            Subtract(a, b float, c int) float;
            Reset()
            SayHello(name string)
        }
        """
        expect = str(Program([
            InterfaceType("Calculator",
            [
                Prototype("Add",[IntType(),IntType()],IntType()),
                Prototype("Subtract",[FloatType(),FloatType(),IntType()],FloatType()),
                Prototype("Reset",[],VoidType()),
                Prototype("SayHello",[StringType()],VoidType())
            ])
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_prim_literal(self):
        input = """
        var x = 5;
        var y = 5.5;
        var z = true;
        var t = "Hello";
        """
        expect = str(Program([
            VarDecl("x",None,IntLiteral(5)),
            VarDecl("y",None,FloatLiteral(5.5)),
            VarDecl("z",None,BooleanLiteral(True)),
            VarDecl("t",None,StringLiteral("\"Hello\""))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_array_literal(self):
        input = """
        var arr = [5]int{1,2,3,4,5};
        var multi_arr = [2][5]int{{1,2,3,4,5},{6,7,8,9,10}};
        """
        expect = str(Program([
            VarDecl("arr",None,ArrayLiteral([IntLiteral(5)], IntType(), [IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),
            VarDecl("multi_arr",None,ArrayLiteral([IntLiteral(2),IntLiteral(5)], IntType(), [[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)], [IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10)]]))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_mixed_array_literal(self):
        input = """
        var arr = [5]int{"1",2,3.4,true,nil};
        """
        expect = str(Program([
            VarDecl("arr",None,ArrayLiteral([IntLiteral(5)], IntType(), [StringLiteral("\"1\""),IntLiteral(2),FloatLiteral(3.4),BooleanLiteral(True),NilLiteral()]))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_struct_literal(self):
        input = """
        var p = Person{name: "John", age: 20}
        """
        expect = str(Program([
            VarDecl("p",None,StructLiteral("Person",[("name",StringLiteral("\"John\"")),("age",IntLiteral(20))]))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_struct_literal_with_empty(self):
        input = """
        var p = Person{}
        """
        expect = str(Program([
            VarDecl("p",None,StructLiteral("Person",[]))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_var_decl(self):
        input = """
        var x int = 5
        var y float = 5.5
        var z boolean = true
        var t string = "Hello"
        """
        expect = str(Program([
            VarDecl("x",IntType(),IntLiteral(5)),
            VarDecl("y",FloatType(),FloatLiteral(5.5)),
            VarDecl("z",BoolType(),BooleanLiteral(True)),
            VarDecl("t",StringType(),StringLiteral("\"Hello\""))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311)) 

    def test_var_decl_with_expr(self):
        input = """
        var x int = y
        """
        expect = str(Program([
            VarDecl("x",IntType(),Id("y"))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_var_decl_with_complex_expr(self):
        input = """
        var x int = 5 + 3 * 4.5 
        var y float = -34
        var z boolean = true && false
        var t string = "Hello" + "World"
        """
        expect = str(Program([
            VarDecl("x",IntType(),BinaryOp("+",IntLiteral(5),BinaryOp("*",IntLiteral(3),FloatLiteral(4.5)))),
            VarDecl("y",FloatType(),UnaryOp("-",IntLiteral(34))),
            VarDecl("z",BoolType(),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False))),
            VarDecl("t",StringType(),BinaryOp("+",StringLiteral("\"Hello\""),StringLiteral("\"World\"")))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_const_decl(self):
        input = """
        const Pi = 3.14
        const Greeting = "Hello, MiniGo!"
        const MaxSize = 100 + 50
        """
        expect = str(Program([
            ConstDecl("Pi",None,FloatLiteral(3.14)),
            ConstDecl("Greeting",None,StringLiteral("\"Hello, MiniGo!\"")),
            ConstDecl("MaxSize",None,BinaryOp("+",IntLiteral(100),IntLiteral(50)))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_const_decl_full(self):
        input = """
        const Pi float = 3.14
        const Greeting string = "Hello, MiniGo!"
        const MaxSize int = 100 + 50
        """
        expect = str(Program([
            ConstDecl("Pi",FloatType(),FloatLiteral(3.14)),
            ConstDecl("Greeting",StringType(),StringLiteral("\"Hello, MiniGo!\"")),
            ConstDecl("MaxSize",IntType(),BinaryOp("+",IntLiteral(100),IntLiteral(50)))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_func_decl(self):
        input = """func main() {
            var x int
        }
        """
        expect = str(Program(
            [FuncDecl("main",[],VoidType(),
            Block(
                [VarDecl("x",IntType(),None)]
                )
            )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_func_decl_with_param(self):
        input = """func main(x int, y float) {
            var z string
        }
        """
        expect = str(Program(
            [FuncDecl("main",
            [ParamDecl("x",IntType()), ParamDecl("y",FloatType())],
            VoidType(),
            Block(
                [VarDecl("z",StringType(),None)]
                )
            )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_func_decl_with_return(self):
        input = """func main() int {
            return 1
        }
        """
        expect = str(Program(
            [FuncDecl("main",[],IntType(),
            Block(
                [Return(IntLiteral(1))]
                )
            )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_func_decl_with_param_and_return(self):
        input = """func main(x int, y float) string {
            return "Hello"
        }
        """
        expect = str(Program(
            [FuncDecl("main",
            [ParamDecl("x",IntType()), ParamDecl("y",FloatType())],
            StringType(),
            Block(
                [Return(StringLiteral("\"Hello\""))]
                )
            )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_method_decl(self):
        input = """func (p Person) foo() {
            var x int
        }
        """
        expect = str(Program(
            [MethodDecl("p",Id("Person"),FuncDecl("foo",[],VoidType(),
            Block(
                [VarDecl("x",IntType(),None)]
                )
            ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_something(self):
        input = """
        func main(){
            b.a[1][2][3][5] := 1;
        }
        """
        expect = str(Program([
            VarDecl("x",IntType(),IntLiteral(5))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
