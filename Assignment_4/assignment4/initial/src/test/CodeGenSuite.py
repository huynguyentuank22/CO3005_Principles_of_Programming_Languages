import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_501(self):
        input = """func main() {putInt(5);};"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_502(self):
        input = """func main() {var a int = 20;  putInt(a);};"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_503(self):
        input = """var a int = 10; func main() { putInt(a);};"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_504(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_505(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
        expect = "500"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_506(self):  
        input = Program([VarDecl("a",IntType(),IntLiteral(5000)),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
        expect = "5000"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    def test_507(self):
        input = """
        
        func main() {
            putStringLn("Hello World");
        };
        """
        expect = "Hello World\n"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    def test_508(self):
        input = """
        func main() {
            var a int = 10;
            var b int = 20;
            putInt(a + b);
        };
        """
        expect = "30"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    def test_509(self):
        input = """
        func foo() int {
            return 5;
        };
        func main() {
            var a int = foo();
            putInt(a);
        };
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    def test_510(self):
        input = """
        const PI = 3.14;
        func main() {
            putFloat(PI);
        };
        """
        expect = "3.14"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    def test_511(self):
        input = """
        func foo(a int, b float) float{
            return a + b;
        };
        func main() {
            var a int = 5;
            var b float = 10.5;
            putFloat(foo(a, b));
        };
        """
        expect = "15.5"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    def test_512(self):
        input = """
        var a = "Hello";
        var b = "World";
        func main() {
            putStringLn(a + b);
        };
        """
        expect = "HelloWorld\n"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    def test_513(self):
        input = """
        func main(){
          
            putInt(5);
            putIntLn(5);
            putFloat(5.0);
            
            putFloatLn(5.0);
            
            putBool(true);
            putBoolLn(false);
            
            putString("Hello");
            putStringLn("World");
            putLn();
        };
        """
        expect = "55\n5.05.0\ntruefalse\nHelloWorld\n\n"
        self.assertTrue(TestCodeGen.test(input,expect,513))
    def test_514(self):
        input = """
        func main(){
            var a float = 5.0;
            var b = a + foo(5.6);
            putFloatLn(b);
        }
        func foo(a float) float {
            return a + 5.0;
        };
        """
        expect = "15.6\n"
        self.assertTrue(TestCodeGen.test(input,expect,514))
    def test_515(self):
        input = """
        var a int;
        var b float;
        func main(){
            c := a + b;
            putFloatLn(c);
        }
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,515))
    def test_516(self):
        input = """
        var a = 5 > 7;
        var b = 5.0 < 7.0;
        func main(){
            putBoolLn(a);
            putBoolLn(b);
        }
        """
        expect = "false\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,516))
    def test_517(self):
        input = """
        var a = true;
        var b = false;
        func main(){
            putBoolLn(a);
            putBoolLn(b);
            putBoolLn(a && b);
            putBoolLn(a || b);
        }
        """
        expect = "true\nfalse\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    def test_518(self):
        input = """
        func main(){
            a := true && false || true;
            putBoolLn(a);
            b := false || true && false;
            putBoolLn(b);
        }
        """
        expect = "true\nfalse\n"
        self.assertTrue(TestCodeGen.test(input,expect,518))
    def test_519(self):
        input = """
        func main(){
            a := !true;
            putBoolLn(a);
            b := !false;
            putBoolLn(b);
            c := !a;
            putBoolLn(c);
            d := !b;
            putBoolLn(d);
        }
        """
        expect = "false\ntrue\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input,expect,519))
    def test_520(self):
        input = """
        func main(){
            a := 5;
            b := 10;
            c := a + b;
            putIntLn(c);
            d := a - b;
            putIntLn(d);
            e := a * b;
            putIntLn(e);
            f := a / b;
            putIntLn(f);
        }
        """
        expect = "15\n-5\n50\n0\n"
        self.assertTrue(TestCodeGen.test(input,expect,520))
    def test_521(self):
        input = """
        func main(){
            a := -5 + 10;
            putIntLn(a);
            b := -5 - 10;
            putIntLn(b);
        }
        """
        expect = "5\n-15\n"
        self.assertTrue(TestCodeGen.test(input,expect,521))
    def test_522(self):
        input = """
        func foo(a int, b float, c boolean) {
            var a float;
            var b int;
            var c string;
            a := 5.0;
            b := 10;
            c := "Hello";
            putFloatLn(a);
            putIntLn(b);
            putStringLn(c);
        }
        func main(){
            foo(5, 10.0, true);
        }
        
        """
        expect = "5.0\n10\nHello\n"
        self.assertTrue(TestCodeGen.test(input,expect,522))
    def test_523(self):
        input = """
        var a string = "Hello";
        var b string = "World";
        func main(){
            var a int;
            var b int;
            a := 1 + 2;
            b := 3 - 4;
            putIntLn(a);
            putIntLn(b);
        }
        """
        expect = "3\n-1\n"
        self.assertTrue(TestCodeGen.test(input,expect,523))
    def test_524(self):
        input = """
        func main(){
            a := 5;
            foo();
        }
        var a string = "Hello";
        func foo(){
            putStringLn(a);
        }
        """
        expect = "Hello\n"
        self.assertTrue(TestCodeGen.test(input,expect,524))
    def test_525(self):
        input = """
        func main(){
            a := 5;
            b := 10;
            c := a + b;
            putIntLn(c);
            foo();
            bar();
        }
        var a int = 1;
        func foo(){
            putIntLn(a);
        }
        var b int = 2;
        func bar(){
            putIntLn(b);
        }
        """
        expect = "15\n1\n2\n"
        self.assertTrue(TestCodeGen.test(input,expect,525))
    def test_526(self):
        input = """
        type A struct {
            a int;
            b float;
        }
        func (a A) foo() int {
           return 1;
        }
        type B interface{
            foo() int;
        }
        type C interface{
            foo() int;
        }
        func main() {
            putInt(5);
            putFloat(10.0);
        }
        """
        expect = "510.0"
        self.assertTrue(TestCodeGen.test(input,expect,526))
    def test_527(self):
        input = """
        func main(){
            var a[2]int = [2]int{1,2};
            var b[2]float = [2]float{1.0,2.0};
            c := 1
            putInt(a[c]);
            putFloat(b[0]);
        }
        """
        expect = "21.0"
        self.assertTrue(TestCodeGen.test(input,expect,527))
    def test_528(self):
        input = """
        func main(){
            var a[3][4]int = [3][4]int{{1,2,3,4},{5,6,7,8},{9,10,11,12}};
            putInt(a[1][2]);
            putInt(a[2][3]);
        }
        """
        expect = "712"
        self.assertTrue(TestCodeGen.test(input,expect,528))
    def test_529(self):
        input = """
        const a = 5;
        func main() {
            var b = 3;
            var a [4]int = [4]int{5, 2, 3, 4}
            var arr [3][4]int = [3][4]int{{1, 2, 3, 4}, {1, 2, 3, 4}, {10, 20, 30, 40}};
            
            var x = 10;
            putIntLn(a[0] + arr[2][1] * 2)
            putIntLn(arr[0][3])
            arr[0][3] := 10
            putIntLn(arr[0][3])
        }
        """
        expect = "45\n4\n10\n"
        self.assertTrue(TestCodeGen.test(input,expect,529))
    def test_530(self):
        input = """
        func main(){
            var a[3]int;
            a := [3]int{1,2,3};
            a[0] := 5;
            putIntLn(a[0]);
        }
        """
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input,expect,530))
    def test_531(self):
        input = """
        type A struct {
            x int;
            y float;
        }
        func (a A) foo() int {
            return a.x + 1;
        }
        func (a A) bar() float {
            return a.y + 1.0;
        }
        func main() {
            var a A;
            a := A{x: 5, y: 10.0};
            putIntLn(a.foo());
            putFloatLn(a.bar());
            var b = A{x: 10, y: 20.0};
            putIntLn(b.foo());
            var c A = A{y: 8.5, x: 10}
            putIntLn(c.foo())
        }
        """
        expect = "6\n11.0\n11\n11\n"
        self.assertTrue(TestCodeGen.test(input, expect, 531))
    def test_532(self):
        input = """
        type A struct {
            x int;
            y float;
        }
        type B interface {
            foo() int;
        }
        func (a A) foo() int {
            return a.x + 1;
        }
        func main() {
            var a A;
            a := A{x: 5, y: 10.0};
            putIntLn(a.foo());
            var b B = a;
            putIntLn(b.foo());
            var c B = A{x: 10, y: 20.0};
            putIntLn(c.foo());
            var d B;
            d := A{y: 8.5, x: 10}
            putIntLn(d.foo());
        }
        """
        expect = "6\n6\n11\n11\n"
        self.assertTrue(TestCodeGen.test(input, expect, 532))
    def test_533(self):
            input = """
            type Car struct {
                name string;
                year int;
            }

            type Person struct {
                name string;
                age int;
                height float;
                car Car
            }

            func init(name string, age int, height float, car Car) Person {
                return Person{name: name, age: age, height: height, car: car}
            }

            func (c Car) init(name string, year int) Car {
                return Car{name: name, year: year}
            }

            func (c Car) print() {
                putStringLn(c.name)
                putIntLn(c.year)
            }
            func (c Car) changed(){
                c.name := "Honda"
                c.year := 2021
            }
            func (p Person) bar() {
                putStringLn(p.name)
                putIntLn(p.age)
                putFloatLn(p.height)
                p.car.print()
            }

            func main() {
                var car Car = Car{name: "Toyota", year: 2020}
                car.print()
                car.changed()
                car.print()
                var x Person = init("John", 30, 177.3, car)
                x.bar()
                
            }
            """
            expect = "Toyota\n2020\nHonda\n2021\nJohn\n30\n177.3\nHonda\n2021\n"
            self.assertTrue(TestCodeGen.test(input,expect,533))
    def test_534(self):
        input = """
            var arr [4]A;
            var arr1 = [4]A{A{x: 1, y: 2.0}, A{x: 3, y: 4.0}, A{x: 5, y: 6.0}, A{x: 7, y: 8.0}}
            type A struct {
                x int;
                y float;
            }
            func (a A) foo() int {
                return a.x + 1;
            }
            func main(){
                arr := [4]A{A{x: 1, y: 2.0}, A{x: 3, y: 4.0}, A{x: 5, y: 6.0}, A{x: 7, y: 8.0}}
                putIntLn(arr[0].foo())
                putIntLn(arr[1].foo())
                putIntLn(arr[2].foo())
                putIntLn(arr[3].foo())
                
                putIntLn(arr1[0].foo())
                putIntLn(arr1[1].foo())
                putIntLn(arr1[2].foo())
                putIntLn(arr1[3].foo())
            }
            """
        expect = "2\n4\n6\n8\n2\n4\n6\n8\n"
        self.assertTrue(TestCodeGen.test(input,expect,534))
    def test_535(self):
        input = """
        var a[5]int = [5]int{1,2,3,4,5}
        var b[3]A = [3]A{A{x: 1, y: 2.0}, A{x: 3, y: 4.0}, A{x: 5, y: 6.0}}
        func main(){
            putInt(a[0])
            putInt(a[1])
            putInt(a[2])
            putInt(a[3])
            putInt(a[4])
            
            putIntLn(b[0].foo())
            putIntLn(b[1].foo())
            putIntLn(b[2].foo())
        }
        type A struct {
            x int;
            y float;
        }
        func (x A) foo() int {
            return x.x + 1;
        }
        """
        expect = "123452\n4\n6\n"
        self.assertTrue(TestCodeGen.test(input,expect,535))
    def test_536(self):
        input = """
        func main(){
            var a [2][2]A = [2][2]A{{A{x: 1, y: 2.0}, A{x: 3, y: 4.0}}, {A{x: 5, y: 6.0}, A{x: 7, y: 8.0}}}
            putIntLn(a[0][0].foo())
            putIntLn(a[0][1].foo())
            var b [2]A = [2]A{A{x: 1, y: 2.0}, A{x: 3, y: 4.0}}
            putIntLn(b[0].foo())
        }
        type A struct {
            x int;
            y float;
        }
        func (x A) foo() int {
            return x.x + 1;
        }
        """
        expect = "2\n4\n2\n"
        self.assertTrue(TestCodeGen.test(input,expect,536))
    def test_537(self):
        input = """
        type Person struct{
            name string;
            age int;
            cars [2]Car;
        }
        func (q  Person) print(){
            putStringLn(q.name)
            putIntLn(q.age)
            q.cars[0].print()
        }
        func (p Person) changed(){
            p.name := "Peter"
            p.age := 81
            p.cars[0].changed()
        }
        type Car struct{
            name string;
            year int;
        }
        func (a Car) print(){
            putStringLn(a.name)
            putIntLn(a.year)
        }
        func (c Car) changed(){
            c.name := "Honda"
            c.year := 2019
        }
        type AI interface{
            getCar() Car;
        }
        func (p Person) getCar() Car {
            return p.cars[0];
        }
        func main(){
            var p Person;
            p := Person{name: "John", age: 30, cars: [2]Car{Car{name: "Toyota", year: 2020}, Car{name: "Honda", year: 2021}}}
            p.print()
            p.changed()
            p.print()
            var bot AI = p
            var car Car = bot.getCar()
            car.print()
            car.changed()
            car.print()
            bot.getCar().print()
        }
        """
        expect = "John\n30\nToyota\n2020\nPeter\n81\nHonda\n2019\nHonda\n2019\nHonda\n2019\nHonda\n2019\n"
        self.assertTrue(TestCodeGen.test(input,expect,537))
    def test_538(self):
        input = """
        func main(){
            a := "Hello"
            foo();
            putStringLn(a);
        }
        var a = "World"
        func foo() {
            putStringLn(a)
        }
        """
        expect = "World\nHello\n"
        self.assertTrue(TestCodeGen.test(input,expect,538))
    def test_539(self):
        input = """
        var a = 5
        func main(){
            var a = 10
            putIntLn(a)
            foo()
        }
        func foo() {
            putIntLn(a)
        }
        """
        expect = "10\n5\n"
        self.assertTrue(TestCodeGen.test(input,expect,539))
    def test_540(self):
        input = """
        var b = "Hello"
        func main(){
            b += " World"
            putStringLn(b)
        }
        """
        expect = "Hello World\n"
        self.assertTrue(TestCodeGen.test(input,expect,540))
    def test_541(self):
        input = """
        func genArr() [5]int {
            return [5]int{1, 2, 3, 4, 5}
        }
        func main(){
            var a = genArr()
            putIntLn(a[0])
            a[0] := 10
            putInt(a[0])
        }
        """
        expect = "1\n10"
        self.assertTrue(TestCodeGen.test(input,expect,541))
    def test_542(self):
        input = """
        func getArr() [5]int {
            return [5]int{1, 2, 3, 4, 5}
        }
        func main(){
            var a[2][5]int;
            a[0] := getArr()
            a[1] := getArr()
            putIntLn(a[0][0])
            putInt(a[1][0])
        }
        """
        expect = "1\n1"
        self.assertTrue(TestCodeGen.test(input,expect,542))
    def test_543(self):
        input = """
        func getArr() [2]Person {
            return [2]Person{Person{name: "John", age: 30}, Person{name: "Jane", age: 25}}
        }
        func main (){
            var a[2]Person;
            a := getArr()
            a[0].print()
            
        }
        type Person struct{
            name string;
            age int;
        }
        func (p Person) print(){
            putStringLn(p.name)
            putIntLn(p.age)
        }
        """
        expect = "John\n30\n"
        self.assertTrue(TestCodeGen.test(input,expect,543))
    def test_544(self):
        input = """
        func main(){
            putIntLn([2]int{1,2}[0])
            putIntLn([2]int{1,2}[1])
            putFloatLn([2]float{1.0,2.0}[0])
            putFloatLn([2]float{1.0,2.0}[1])
            putStringLn([2]string{"Hello","World"}[0])
            putStringLn([2]string{"Hello","World"}[1])
        }
        """
        expect = "1\n2\n1.0\n2.0\nHello\nWorld\n"
        self.assertTrue(TestCodeGen.test(input,expect,544))
    def test_545(self):
        input = """
        var k = 5
        func main(){
            putInt(A{x: 1, y: 2.0}.foo())
            putFloat(A{x: 3, y: 4.0}.bar())
        }
        type A struct{
            x int;
            y float;
        }
        func (a A) foo() int {
            return a.x + k;
        }
        func (b A) bar() float {
            return b.y + k;
        }
        """
        expect = "69.0"
        self.assertTrue(TestCodeGen.test(input,expect,545))
    def test_546(self):
        input = """
        var a = 5
        var b = 10
        var c = 10.0
        var d = 20.0
        func main(){
            if (a < b) {
                putIntLn(a + foo())
            } else{
                if (c > d) {
                    putFloatLn(c + d)
                } else {
                    putFloatLn(c - d)
                }
            }
        }
        func foo() int {
            return 1 + 2;
        }
        """
        expect = "8\n"
        self.assertTrue(TestCodeGen.test(input,expect,546))
    def test_547(self):
        input = """
        var a = 1 + foo() + 2
        var b = 3
        var c = 4.0
        var d = 6.0
        func main(){
            if (c > d){
                if (a > b){
                    putIntLn(a + b)
                }
            } else if (a * b > 18){
                putFloatLn(c + d)
            } else {
                putFloatLn(c - d)
            }
        }
        func foo() int{
            return 1 + 2;
        }
        """
        expect = "-2.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,547))
    def test_548(self):
        input = """
        const a = 20 * 10
        var y = 15.5

        func main() {
            if (y >= 16) {
                putInt(a + foo())
            } else {
                if (a + 10 >= 211) {
                    putIntLn(234)
                } else {
                    var x = 5;
                    for x < 10 {
                        putIntLn(567)
                        x += 1;
                    }
                }
                putInt(a + foo() + 1)
            }
            for i := 0; i < 10; i += 1 {
              putInt(i)
            }
        };
        
        func foo() int {
            return 1 + 2;
        }
        """
        expect = "567\n567\n567\n567\n567\n2040123456789"
        self.assertTrue(TestCodeGen.test(input,expect,548))
    def test_549(self):
        input = """
        func main(){
            foo(10)
        }
        func foo(n int){
            for var i = 1; i < n; i += 1 {
                putInt(i)
            }
            for i := 1; i < n; i += 1 {
                putInt(i)
            }
        }
        """
        expect = "123456789123456789"
        self.assertTrue(TestCodeGen.test(input,expect,549))
    def test_550(self):
        input = """
        func main(){
            for i := 1; i < 10; i += 1 {
                if (i % 2 != 0) {
                    continue
                }
                putInt(i)
            }
            for var i = 1; i < 10; i += 1 {
                putInt(i)
                if (i == 7) {
                    break
                }
            }
        }
        """
        expect = "24681234567"
        self.assertTrue(TestCodeGen.test(input,expect,550))
    def test_551(self):
        input = """
        var a = "Hello"
        var c = "xin chao"
        var d = "Bonjour"
        var e = "Hallo"
        var f = "Ciao"
        var g = "Konnichiwa"
        var h = "Annyeonghaseyo"
        func main(){
            if (a >= c) {
                if (a < d){
                    putStringLn(a)
                } else {
                    putStringLn(c)
                }
            } else if (a < d) {
                putStringLn(d)
            } else {
                putStringLn(e)
            }
            if (a == "Hello") {
                putStringLn(f)
            } else {
                putStringLn(g)
            }
        }
        """
        expect = "Hallo\nCiao\n"
        self.assertTrue(TestCodeGen.test(input,expect,551))
    def test_552(self):
        input = """
        var arr[5]int = [5]int{1,2,3,4,5}
        func main(){
            for i := 0; i < 5; i += 1 {
                if (arr[i] % 2 == 0) {
                    putInt(arr[i])
                }
            }
            for var i = 0; i < 5; i += 1 {
                if (arr[i] % 2 != 0) {
                    putInt(arr[i])
                }
            }
        }
        """
        expect = "24135"
        self.assertTrue(TestCodeGen.test(input,expect,552))
    def test_553(self):
        input = """
        func main(){
            var a[2][2][2]int = [2][2][2]int{{{1,2},{3,4}},{{5,6},{7,8}}}
            putInt(a[0][0][0])
            putInt(a[0][1][1])
        }
        """
        expect = "14"
        self.assertTrue(TestCodeGen.test(input,expect,553))
    def test_554(self):
        input = """
        var a = "Hello"
        var b B = B{a: 5, b: 10.0}
        var c C = b
        func main(){
            testPassByRef(a, b, c)
            putStringLn(a)
            putIntLn(b.getA())
            putIntLn(c.getA())
        }
        func testPassByRef(s string, m B, n C) {
            s := "hello"
            m.foo()
        }
        
        func (a B) foo() {
            a.a := 10
            a.b := 20.0
        }
        type B struct {
            a int;
            b float;
        }
        func (a B) getA() int {
            return a.a
        }
        type C interface {
            foo();
            getA() int;
        }
        """
        expect = "hello\n10\n10\n"
        self.assertTrue(TestCodeGen.test(input,expect,554))
    def test_555(self):
        input = """
        const MAX = 5;
        func init(q [MAX]int, v [MAX]boolean){
            q := [MAX]int{0, 0, 0, 0, 0};
            v := [MAX]boolean{false, false, false, false, false};
        }
        func bfs(graph [MAX][MAX]int, start int){
            var visited [MAX] boolean;
            var queue [MAX] int;
            init(queue, visited);
            var front = 0;
            var rear = 0;
            visited[start] := true;
            queue[rear] := start;
            rear += 1;
            
            for front < rear {
                var u = queue[front]
                front += 1;
                putInt(u)
                putString(" ")
                for v := 0; v < MAX; v += 1{
                    if (graph[u][v] == 1 && !visited[v]){
                        visited[v] := true;
                        queue[rear] := v;
                        rear += 1;
                    }
                }   
            }
        }
        
        func main(){
            var graph = [MAX][MAX] int {{0, 1, 0, 0, 0}, {1, 0, 1, 0, 0}, {0, 1, 0, 1, 0}, {0, 0, 1, 0, 1}, {0, 0, 0, 1, 0}};
            bfs(graph, 0);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "0 1 2 3 4 ", 555))
    def test_556(self):
        input = """
        const MAX = 5
        func main(){
            var a[MAX]int;
            a := [MAX]int{1,2,3,4,5}
            putIntLn(a[0])
            a[0] += 2
            putIntLn(a[0])
            for i := 0; i<MAX; i+=1{
                putInt(a[i])
            }
        }
        """
        expect = "1\n3\n32345"
        self.assertTrue(TestCodeGen.test(input, expect, 556))
    def test_557(self):
        input = """
        const MAX = 3
        func main(){
            var a[MAX][MAX]int;
            a := [MAX][MAX]int{{1,2,3},{4,5,6},{7,8,9}}
            putIntLn(a[0][0])
            a[0][0] += 2
            putIntLn(a[0][0])
            a[1][1] += 3
            a[2][2] += 4
            for i := 0; i<MAX; i+=1{
                for j := 0; j<MAX; j+=1{
                    putInt(a[i][j])
                }
            }
        }
        """
        expect = "1\n3\n3234867813"
        self.assertTrue(TestCodeGen.test(input, expect, 557))
    def test_558(self):
        input = """
        const MAX = 2
        func main(){
            var a[MAX][MAX][MAX]int;
            a := [MAX][MAX][MAX]int{{{1,2},{3,4}},{{5,6},{7,8}}}
            putIntLn(a[0][0][0])
            a[0][1][1] += 2
            putIntLn(a[0][1][1])
            for i := 0; i<MAX; i+=1{
                for j := 0; j<MAX; j+=1{
                    for k := 0; k<MAX; k+=1{
                        putInt(a[i][j][k])
                    }
                }
            }
        }
        """
        expect = "1\n6\n12365678"
        self.assertTrue(TestCodeGen.test(input, expect, 558))
    def test_559(self):
        input = """
        type A struct{
            x int;
            b B
        }
        type B struct {
            y int
        }
        const MAX = 2
        func main(){
            var arr[MAX] A;
            arr := [MAX] A{A{x: 1, b: B{y: 2}}, A{x: 3, b: B{y: 4}}}
            for i:=0; i<MAX; i+=1{
                arr[i].foo()
            }
        }
        func (a A) foo(){
            putIntLn(a.x)
            a.b.foo()
        }
        func (b B) foo(){
            putIntLn(b.y)
        }
        """
        expect = "1\n2\n3\n4\n"
        self.assertTrue(TestCodeGen.test(input, expect, 559))
    def test_560(self):
        input = """
        type A struct{
            x int;
        }
        func (b A) foo() int{
            return b.x
        }
        type B interface{
            foo() int
        }
        const MAX = 2
        func main(){
            var a[MAX]B
            a := [MAX]B{A{x: 1}, A{x: 2}}
            for i:=0; i<MAX; i+=1{
                putIntLn(a[i].foo())
            }
        }
        """
        expect = "1\n2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 560))
    def test_561(self):
        input = """
        type A struct{
            x int;
            y float;
            z boolean;
            s string;
            arr [5]int
            b A
        }
        func (z A) foo(){
            putInt(z.x)
            putFloat(z.y)
            putString(z.s)
            putBool(z.z)
        }
        func (y A) initarr(val int){
            y.arr := [5]int{val, val, val, val, val}
        }
        func (a A) printArr(){
            for i:=0; i<5; i+=1{
                putInt(a.arr[i])
            }
        }
        func (a A) testB(){
            a.b.foo()
            a.b.initarr(6)
            a.b.printArr()
        }
        func (k A) initB(){
            k.b := initA(1, true, "kakaka")
        }
        func initA(x int, z boolean, s string) A {
            return A{x: x, z: z, s: s}
        }
        func main(){
            var a A
            a := initA(1, true, "Hello")
            a.foo()
            a.initarr(5)
            a.printArr()
            a.initB()
            a.testB()
        }
        """
        expect = "10.0Hellotrue5555510.0kakakatrue66666"
        self.assertTrue(TestCodeGen.test(input, expect, 561))
    def test_562(self):
        input = """
        type A struct {
            x int
            y float
            z boolean
            s string
        }
        func (a A) print(){
            putIntLn(a.x)
            putFloatLn(a.y)
            putStringLn(a.s)
            putBoolLn(a.z)
        }
        func main(){
            temp := A{x:1}
            temp.print()
            temp1 := A{y:2.0}
            temp1.print()
            temp2 := A{z:true}
            temp2.print()
            temp3 := A{s:"abc"}
            temp3.print()
        }
        """
        expect = "1\n0.0\n\nfalse\n0\n2.0\n\nfalse\n0\n0.0\n\ntrue\n0\n0.0\nabc\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 562))
    def test_563(self):
        input = """
        const MAX = 5
        func foo(arr [MAX]float){
            for i:=0; i<MAX; i+=1{
                arr[i] *=2
            }
        }
        func main(){
            var a [MAX]float
            a := [MAX]float{1.0,2.0,3.0,4.0,5.0}
            foo(a)
            for i:=0; i<MAX; i+=1{
                putFloat(a[i])
            }
        }        
        """
        expect = "2.04.06.08.010.0"
        self.assertTrue(TestCodeGen.test(input, expect, 563))
    def test_564(self):
        input = """
        const M = 0b10
        const N = 0o02
        const P = 0x02
        func main(){
            a := [M][N][P]int{{{1,2},{3,4}},{{5,6},{7,8}}}
            putInt(a[0o00][0b00][0x00])
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 564))
    def test_565(self):
        input = """
        func main(){
            putFloatLn(3.14)
            putFloatLn(0.)
            putFloatLn(2.0e2)
            putFloatLn(1.0e-2)
            putFloatLn(1.0E-3)
            putFloatLn(1.2E+2)
        }
        """
        expect = "3.14\n0.0\n200.0\n0.01\n0.001\n120.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 565))
    def test_566(self):
        input = """
        const MAX = 3
        func main(){
            var a[MAX][MAX]float;
            a := [MAX][MAX]float{{4,4.0,4},{4,4.0,4},{4,4.0,4}}
            putFloatLn(a[0][0])
        }
        func arrint(val int) [MAX]int{
            return [MAX]int{val, val, val}
        }
        """
        expect = "4.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 566))
    def test_567(self):
        input = """
        var a = "Hello"
        var b = "World"
        func main(){
            putStringLn(a)
            putStringLn(b)
            a += " " 
            a += b 
            putStringLn(a)
            b := a
            putStringLn(b)
        }
        """
        expect = "Hello\nWorld\nHello World\nHello World\n"
        self.assertTrue(TestCodeGen.test(input, expect, 567))
    def test_568(self):
        input = """
        func fibo(n int) int{
            if (n < 2){
                return n
            }
            return fibo(n-1) + fibo(n-2)
        }
        func main(){
            putIntLn(fibo(3))
            putIntLn(fibo(4))
        }
        """
        expect = "2\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 568))
    def test_569(self):
        input = """
        const MAX = 10
        func arrsort (arr [MAX]int){
            for i := 0; i<MAX; i+=1{
                for j:=0; j < i; j+=1{
                    if (arr[i] < arr[j]){
                        var temp = arr[i]
                        arr[i] := arr[j]
                        arr[j] := temp
                    }
                }
            }
        }
        func main(){
            var arr[MAX]int = [MAX]int{4,2,3,7,8,9,12,14,15,11}
            arrsort(arr)
            for i := 0; i<MAX; i+=1{
                putInt(arr[i])
            }
        }
        """
        expect = "23478911121415"
        self.assertTrue(TestCodeGen.test(input, expect, 569))
    def test_570(self):
        input = """
        func foo(){
            a := "World"
            putStringLn(a)
        }
        func main(){
            a := "Hello"
            putStringLn(a)
            foo()
            putStringLn(a)
        }
        """
        expect = "Hello\nWorld\nHello\n"
        self.assertTrue(TestCodeGen.test(input, expect, 570))
    def test_571(self):
        input = """
        var a = "Hello"
        func main(){
            putString(a)
        }
        """
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 571))
    def test_572(self):
        input = """
        func test() string{
            var a = "Hello"
            var b = "World"
            c := a + b
            return c
        }
        func test1() string{
            return "vibe coding"
        }
        func foo(s string) {
            s += "lala"
            s += "meowmeow"
        }
        func main(){
            var str1 = test()
            foo(str1)
            putString(str1)
            str2 := test1()
            putString(str2)
            foo(str2)
            putString(str2)
        }
        """
        expect = "HelloWorldlalameowmeowvibe codingvibe codinglalameowmeow"
        self.assertTrue(TestCodeGen.test(input, expect, 572))
    def test_573(self):
        input = """
        var a = "ahhaaha"
        var b string = "hjhjhj"
        func main(){
            putStringLn(a)
            putStringLn(b)
        }
        """
        expect = "ahhaaha\nhjhjhj\n"
        self.assertTrue(TestCodeGen.test(input, expect, 573))
    def test_574(self):
        input = """
        const MAX = 2
        var a = [MAX]string{"aa","bb"}
        func main(){
            a1 := [MAX]string{"cc","zz"}
            foo(a[1])
            foo(a1[0])
            foo(a1[1])
            for i := 0; i<MAX; i+=1{
                putStringLn(a[i])
                putStringLn(a1[i])
            }
            str := "xx"
            foo(str)
            putStringLn(str)
        }
        func foo(s string){
            if (s < "uu"){
                s += "passbyref"
            } else {
                s := "pass"
            }
        }
        """
        expect = "aa\nccpassbyref\nbbpassbyref\npass\npass\n"
        self.assertTrue(TestCodeGen.test(input, expect, 574))
    def test_575(self):
        input = """
        const MAX = 2
        var a = [MAX][MAX]string{{"aa","bb"},{"cc","zz"}}
        func main(){
            a1 := [MAX]string{"cc","zz"}
            foo(a[1][1])
            foo(a1[0])
            foo(a1[1])
            for i := 0; i<MAX; i+=1{
                putStringLn(a1[i])
            }
            for i := 0; i<MAX; i+=1{
                putStringLn(a[i][i])
            }
            str := "xx"
            foo(str)
            putStringLn(str)
        }
        func foo(s string){
            if (s < "uu"){
                s += "passbyref"
            } else {
                s := "pass"
            }
        }
        """
        expect = "ccpassbyref\npass\naa\npass\npass\n"
        self.assertTrue(TestCodeGen.test(input, expect, 575))
    def test_576(self):
        input = """
        func main() {
            putBoolLn(false && true)
            putBoolLn(false && false)
            
            putBoolLn(true || false)
            putBoolLn(true || true)
        }
        """
        expect = "false\nfalse\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 576))
    def test_576(self):
        input = """
        func main() {
            var a = 5
            var b = 0
            // Without short circuit, this would cause runtime error
            if (b != 0 && a/b > 2) {
                putStringLn("Division result > 2")
            } else {
                putStringLn("Safe from division by zero")
            }
        
            b := 2
            if (b != 0 && a/b > 2) {
                putStringLn("Division result > 2")
            } else {
                putStringLn("Division result <= 2")
            }
        }
        """
        expect = "Safe from division by zero\nDivision result <= 2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 576))
    def test_577(self):
        input = """
        var counter = 0

        func main() {
            // This should call incrementAndGet only once
            if (false && incrementAndGet() > 0 && incrementAndGet() > 0) {
                putStringLn("This won't print")
            }
            putIntLn(counter) // expect 0
            
            counter := 0
            // This should call incrementAndGet only once
            if (true || incrementAndGet() > 0 || incrementAndGet() > 0) {
                putIntLn(counter) // 0
            }
        }

        func incrementAndGet() int {
            counter += 1
            return counter
        }
        """
        expect = "0\n0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 577))
    def test_578(self):
        input = """
        var callCount = 0
        
        func factorial(n int) int {
            callCount += 1
            
            // Base case
            if (n <= 1) {
                return 1
            }
            
            return n * factorial(n-1)
        }
        
        func main() {
            // Short circuit prevents evaluating factorial(5)
            if (false && factorial(5) > 10) {
                putStringLn("Won't print")
            }
            
            putIntLn(callCount) // Should be 0
            
            if (true || factorial(5) > 10) {
                putStringLn("Short-circuited")
            }
            
            putIntLn(callCount) // Still 0

            result := factorial(5)
            putIntLn(result)  // 120
            putIntLn(callCount) // 5
        }
        """
        expect = "0\nShort-circuited\n0\n120\n5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 578))
    def test_579(self):
        input = """
        type Library struct {
            name string
            books [3]string
        }
        func (lib Library) printBooks() {
            for i := 0; i < 3; i += 1 {
                if (lib.books[i] != "") {
                    putStringLn("- " + lib.books[i])
                }
            }
        }
        func main() {
            myLib := Library{name: "Central Library", books: [3]string{"Go Programming", "Python Basics", ""}}
            myLib.printBooks()

        }
        """
        expect = "- Go Programming\n- Python Basics\n"
        self.assertTrue(TestCodeGen.test(input, expect, 579))
    def test_580(self):
        input = """
        const MAX = 2
        func arrStr(v string) [MAX]string{
            return [MAX]string{"abc", "xyz"}
        }
        func main(){
            var a = arrStr("Hello")
            putStringLn(a[0])
            putStringLn(a[1])
            var b = a[0]
            a[0] := "def"
            putStringLn(b)
            putStringLn(a[0])
            putStringLn(a[1])
        }
        """
        expect = "abc\nxyz\nabc\ndef\nxyz\n"
        self.assertTrue(TestCodeGen.test(input, expect, 580))
    def test_581(self):
        input = """
        const MAX = 2
        func genStr(v string) string{
            return v + "aa" + "bc"
        }
        func main(){
            var a = [MAX]string{"pp", "cc"};
            var b = genStr("jj")
            var c string = genStr("ii")
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 581))
    def test_582(self):
        input = """
        type A struct{
            s string
        }
        func (a A) foo() string {
            return a.s + "foo"
        }
        func (a A) setS(s string) {
            a.s := s
        }
        func (a A) getS()string {
            return a.s
        }
        func main(){
            var a A = A{}
            putStringLn(a.foo())
            a.setS("Hello")
            putStringLn(a.getS())
        }
        """
        expect = "foo\nHello\n"
        self.assertTrue(TestCodeGen.test(input, expect, 582))
    def test_582(self):
        input = """
        type A struct{
            s string
        }
        func (a A) foo() string {
            return a.s + "foo"
        }
        func (a A) setS(s string) {
            a.s := s
        }
        func (a A) getS()string {
            return a.s
        }
        func main(){
            var a A = A{}
            putStringLn(a.foo())
            a.setS("Hello")
            putStringLn(a.getS())
            var b B = a
            b.setS("aaa")
            putStringLn(b.getS())
        }
        type B interface{
            setS(s string)
            getS() string
        }
        """
        expect = "foo\nHello\naaa\n"
        self.assertTrue(TestCodeGen.test(input, expect, 583))
    def test_584(self):
        input = """
        const MAX = 2
        type A struct{
            s string
        }
        func (a A) getS() string{
            return a.s
        }
        type B interface{
            getS() string
        }
        func complex(a A, arr [MAX]string, b B){
            putString(a.getS())
            putString(arr[0])
            putString(arr[1])
            putString(b.getS())
        }
        func main(){
            complex(A{}, [MAX]string{"aa", "bb"}, A{s:"uu"})
        }
        """
        expect = "aabbuu"
        self.assertTrue(TestCodeGen.test(input, expect, 584))
    def test_585(self):
        input = """
        func test(x string, a A, b B) {
            x := "Hello"
            a.setS("World")
            b.setS("!")
        }
        type A struct {
            s string
        }
        type B interface {
            setS(s string)
            getS() string
        }
        func (a A) setS(s string) {
            a.s := s
        }
        func (a A) getS() string {
            return a.s
        }
        func main() {
            var a A = A{}
            var b B = a
            var c string;
            putStringLn(c)
            putStringLn(a.getS())
            putStringLn(b.getS())
            test(c, a, b)
            putStringLn(c)
            putStringLn(a.getS())
            putStringLn(b.getS())
        }
        """
        expect = "\n\n\nHello\n!\n!\n"
        self.assertTrue(TestCodeGen.test(input, expect, 585))
    def test_586(self):
        input = """
        var e int = getInt()
        var d = getString()
        func main(){
            var a = getString()
            var b int = getInt()
            var c = getBool()
            var d float = getFloat()
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 586))
    def test_587(self):
        input = """
        const a = 1
        const b = 2 + a * 7
        const c = 3 * b
        const d = 4 * c // 27 * 4
        const e = 5.0 * c // 27 * 5
        func main(){
            putIntLn(a)
            putIntLn(b)
            putIntLn(c)
            putIntLn(d)
            putFloatLn(e)
        }
        """
        expect = "1\n9\n27\n108\n135.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 587))
    def test_588(self):
        input = """
        type A struct{
            _s [5]string
        }
        func (a A) setS(s [5]string ) {
            a._s := s
        }
        func (a A) getS() [5]string {
            return a._s
        }
        func (a A) printS() {
            for i := 0; i < 5; i += 1 {
                putStringLn(a._s[i])
            }
        }
        type B interface {
            setS(s [5]string )
            getS() [5]string
        }
        func main(){
            var a A 
            var b B = a
            var c [5]string = [5]string{"Hello", "World", "!", "This", "is"}
            b.setS(c)
            putStringLn(b.getS()[0])
            putStringLn(b.getS()[1])
            putStringLn(b.getS()[2])
        }
        """
        expect = "Hello\nWorld\n!\n"
        self.assertTrue(TestCodeGen.test(input, expect, 588))
    def test_589(self):
        input = """
        type A struct {
            x int
            y float
        
        }
        func (a A) main(s string) {
            putStringLn(s)
            putIntLn(a.x)
            putFloatLn(a.y)
        }
        func main() {
            var a A = A{}
            a.main("Hello")
        }
        """
        expect = "Hello\n0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 589))
    def test_590(self):
        input = """
        type A struct {
            x int
            y float
        
        }
        func (a A) main(s string) {
            putStringLn(s)
            putIntLn(a.x)
            putFloatLn(a.y)
        }
        const a = [3]int{1,2,3}
        const b = [2]float{1.5, 4.5}
        const c = [2]string{"hh", "ll"}
        const d = [2]A{A{}, A{}}
        const e = [2][2]int{{1,2}, {3,4}}
        func main() {
            putInt(a[0])
            putFloat(b[1])
            putStringLn(c[0])
            d[1].main("honors")
            putInt(e[0][0])
        }
        """
        expect = "14.5hh\nhonors\n0\n0.0\n1"
        self.assertTrue(TestCodeGen.test(input, expect, 590))
    def test_591(self):
        input = """
        type A struct {
            x int
            y float
        
        }
        func (a A) main(s string) {
            putStringLn(s)
            putIntLn(a.x)
            putFloatLn(a.y)
        }
        func main() {
            const a = [3]int{1,2,3}
            const b = [2]float{1.5, 4.5}
            const c = [2]string{"hh", "ll"}
            const d = [2]A{A{}, A{}}
            const e = [2][2]int{{1,2}, {3,4}}
            const f = "aaa"
            const g = f + "hhh"
            const a1 = 1
            const b1 = 2 + a1 * 7
            const c1 = 3 * b1
            const d1 = 4 * c1 // 27 * 4
            const e1 = 5.0 * c1 // 27 * 5
            putInt(a[0])
            putFloat(b[1])
            putStringLn(c[0])
            d[1].main("honors")
            putInt(e[0][0])
            putStringLn(f)
            putStringLn(g)
            putIntLn(a1)
            putIntLn(b1)
            putIntLn(c1)
            putIntLn(d1)
            putFloatLn(e1)
        }
        """
        expect = "14.5hh\nhonors\n0\n0.0\n1aaa\naaahhh\n1\n9\n27\n108\n135.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 591))