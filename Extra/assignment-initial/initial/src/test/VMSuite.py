import unittest
from TestUtils import TestVM
import inspect

"""436, 438, 440, 441, 442"""
class VMSuite(unittest.TestCase):
    def test_401_simple_program(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[],[])],[call(writeInt,[3])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 401))

    def test_402_simple_expression(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeInt,[add(3,1)])]]."""
        expect = "4"
        self.assertTrue(TestVM.test(input, expect, 402))

    def test_403_minus_expression(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeInt,[sub(3,1)])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 403))

    def test_404_nested_expression(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeInt,[add(4,sub(3,1))])]]."""
        expect = "6"
        self.assertTrue(TestVM.test(input, expect, 404))

    def test_405_redeclared_built_in(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeInt,integer)],[],[]]."""
        expect = "Redeclared identifier: var(writeInt,integer)"
        self.assertTrue(TestVM.test(input, expect, 405))

    def test_406_redeclared_built_in_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeIntLn, integer)], [], []]."""
        expect = "Redeclared identifier: var(writeIntLn,integer)"
        self.assertTrue(TestVM.test(input, expect, 406))

    def test_407_redeclared_built_in_3(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeReal, integer)], [], []]."""
        expect = "Redeclared identifier: var(writeReal,integer)"
        self.assertTrue(TestVM.test(input, expect, 407))
    
    def test_408_redeclared_built_in_4(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeRealLn, integer)], [], []]."""
        expect = "Redeclared identifier: var(writeRealLn,integer)"
        self.assertTrue(TestVM.test(input, expect, 408))

    def test_409_redeclared_built_in_5(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeBool, integer)], [], []]."""
        expect = "Redeclared identifier: var(writeBool,integer)"
        self.assertTrue(TestVM.test(input, expect, 409))

    def test_410_redeclared_built_in_6(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeBoolLn, integer)], [], []]."""
        expect = "Redeclared identifier: var(writeBoolLn,integer)"
        self.assertTrue(TestVM.test(input, expect, 410))

    def test_411_redeclared_built_in_7(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeStr, integer)], [], []]."""
        expect = "Redeclared identifier: var(writeStr,integer)"
        self.assertTrue(TestVM.test(input, expect, 411))

    def test_412_redeclared_built_in_8(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeStrLn, integer)], [], []]."""
        expect = "Redeclared identifier: var(writeStrLn,integer)"
        self.assertTrue(TestVM.test(input, expect, 412))

    def test_413_redeclared_built_in_9(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeLn, integer)], [], []]."""
        expect = "Redeclared identifier: var(writeLn,integer)"
        self.assertTrue(TestVM.test(input, expect, 413))

    def test_414_redeclared_built_in_10(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(readInt, integer)], [], []]."""
        expect = "Redeclared identifier: var(readInt,integer)"
        self.assertTrue(TestVM.test(input, expect, 414))

    def test_415_redeclared_built_in_11(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(readReal, integer)], [], []]."""
        expect = "Redeclared identifier: var(readReal,integer)"
        self.assertTrue(TestVM.test(input, expect, 415))

    def test_416_redeclared_built_in_12(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(readBool, integer)], [], []]."""
        expect = "Redeclared identifier: var(readBool,integer)"
        self.assertTrue(TestVM.test(input, expect, 416))

    def test_417_redeclared_var(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,integer),var(a,float)],[],[call(writeInt,[1])]]."""
        expect = "Redeclared identifier: var(a,float)"
        self.assertTrue(TestVM.test(input, expect, 417))

    def test_418_redeclared_var_2(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[const(a,2),var(b,integer),var(a,float)],[],[call(writeInt,[1])]]."""
        expect = "Redeclared identifier: var(a,float)"
        self.assertTrue(TestVM.test(input, expect, 418))    

    def test_419_redeclared_const(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[const(writeInt, 7)],[],[]]."""
        expect = "Redeclared identifier: const(writeInt,7)"
        self.assertTrue(TestVM.test(input, expect, 419))

    def test_420_redeclared_const_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[const(a,2),var(b,integer),const(a,8)],[],[call(writeInt,[1])]]."""
        expect = "Redeclared identifier: const(a,8)"
        self.assertTrue(TestVM.test(input, expect, 420))

    def test_421_redeclared_const_3(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,integer),const(a,9)],[],[call(writeInt,[1])]]."""
        expect = "Redeclared identifier: const(a,9)"
        self.assertTrue(TestVM.test(input, expect, 421))

    def test_422_redeclared_func(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(readInt,[],real,[])],[]]."""
        expect = """Redeclared function: readInt"""
        self.assertTrue(TestVM.test(input, expect, 422))

    def test_423_redclared_func_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(foo, integer),const(faa,2)],[func(foo,[],real,[])],[]]."""
        expect = """Redeclared function: foo"""
        self.assertTrue(TestVM.test(input, expect, 423))

    def test_424_redclared_func_3(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[const(foo, 3)],[func(foo,[],real,[])],[]]."""
        expect = """Redeclared function: foo"""
        self.assertTrue(TestVM.test(input, expect, 424))

    def test_425_redeclared_func_4(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],
        [func(foo,[],real,[]),
        func(foo,[],integer,[])],
        []]."""
        expect = """Redeclared function: foo"""
        self.assertTrue(TestVM.test(input, expect, 425))

    def test_426_redeclared_proc(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(readInt,[],[])],[]]."""
        expect = """Redeclared procedure: readInt"""
        self.assertTrue(TestVM.test(input, expect, 426))

    def test_427_redclared_proc_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(foo, integer),const(faa,2)],[proc(foo,[],[])],[]]."""
        expect = """Redeclared procedure: foo"""
        self.assertTrue(TestVM.test(input, expect, 427))

    def test_428_redclared_proc_3(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[const(foo, 3)],[proc(foo,[],[])],[]]."""
        expect = """Redeclared procedure: foo"""
        self.assertTrue(TestVM.test(input, expect, 428))

    def test_429_redeclared_proc_4(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[],integer,[]),proc(foo,[],[])],[]]."""
        expect = """Redeclared procedure: foo"""
        self.assertTrue(TestVM.test(input, expect, 429))

    def test_430_redeclared_proc_5(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[],[]),proc(foo,[],[])],[]]."""
        expect = """Redeclared procedure: foo"""
        self.assertTrue(TestVM.test(input, expect, 430))

    def test_431_redeclared_param(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[par(a,integer),par(b,integer),par(a,real)],[])],[]]."""
        expect = """Redeclared identifier: par(a,real)"""
        self.assertTrue(TestVM.test(input, expect, 431))

    def test_432_redeclared_param_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[par(a,integer),par(b,integer),par(a,real)],integer,[])],[]]."""
        expect = """Redeclared identifier: par(a,real)"""
        self.assertTrue(TestVM.test(input, expect, 432))

    def test_433_redeclared_local(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[],[const(a,7),var(a,real)])],[]]."""
        expect = """Redeclared identifier: var(a,real)"""
        self.assertTrue(TestVM.test(input, expect, 433))

    def test_434_redeclared_local_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[],[var(a,real),[var(a,integer)]])],[call(writeIntLn,[3])]]."""
        expect = """3\n"""
        self.assertTrue(TestVM.test(input, expect, 434))

    def test_435_type_mismatch(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeInt,[add(10,true)])]]."""
        expect = """Type mismatch: add(10,true)"""
        self.assertTrue(TestVM.test(input, expect, 435))

    def test_436_type_mismatch_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeBool,[add(10,3)])]]."""
        expect = """Type mismatch: call(writeBool,[add(10,3)])"""
        self.assertTrue(TestVM.test(input, expect, 436))

    def test_437_type_mismatch_3(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,3),if(a,call(writeInt,[3]))]]."""
        expect = """Type mismatch: if(a,call(writeInt,[3]))"""
        self.assertTrue(TestVM.test(input, expect, 437))

    def test_438_type_mismatch_4(self):
        print(inspect.currentframe().f_code.co_name)
        input = """
        [[],
        [func(foo,[],float,[assign(foo,3.0)])], 
        [call(writeInt,[call(foo,[])])]]."""
        expect = """Type mismatch: call(writeInt,[call(foo,[])])"""
        self.assertTrue(TestVM.test(input, expect, 438))

    def test_439_undeclared_id(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,add(b,1)),call(writeIntLn,[a])]]."""
        expect = """Undeclared identifier: b"""
        self.assertTrue(TestVM.test(input, expect, 439))

    def test_440_undeclared_id_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],
        [proc(foo,[],[var(b,integer),assign(b,1),assign(a,b)])], 
        [call(writeIntLn,[b])]]."""
        expect = """Undeclared identifier: b"""
        self.assertTrue(TestVM.test(input, expect, 440))

    def test_441_wrong_num_of_args(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[],[])],[call(foo,[1])]]."""
        expect = """Wrong number of arguments: call(foo,[1])"""
        self.assertTrue(TestVM.test(input, expect, 441))

    def test_442_wrong_num_of_args_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[par(a,integer)],[])],[call(foo,[])]]."""
        expect = """Wrong number of arguments: call(foo,[])"""
        self.assertTrue(TestVM.test(input, expect, 442))

    def test_443_wrong_num_of_args_3(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[par(a,integer)],integer,[])],[call(foo,[])]]."""
        expect = """Wrong number of arguments: call(foo,[])"""
        self.assertTrue(TestVM.test(input, expect, 443))
    
    def test_444_wrong_num_of_args_4(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[par(a,integer)],integer,[])],[call(foo,[1,2])]]."""
        expect = """Wrong number of arguments: call(foo,[1,2])"""
        self.assertTrue(TestVM.test(input, expect, 444))

    def test_445_invalid_expr(self):
        print(inspect.currentframe().f_code.co_name)
        input = """
        [[var(a,integer)],
        [func(foo,[],integer,[])],
        [assign(a,call(foo,[]))]].
        """
        expect = """Invalid expression: call(foo,[])"""
        self.assertTrue(TestVM.test(input, expect, 445))

    def test_446_invalid_expr_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[call(writeInt,[a])]]."""
        expect = """Invalid expression: a"""
        self.assertTrue(TestVM.test(input, expect, 446))

    def test_447_undeclared_func(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,call(foo,[]))]]."""
        expect = """Undeclared function: call(foo,[])"""
        self.assertTrue(TestVM.test(input, expect, 447))

    def test_448_undeclared_proc(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(foo,[])]]."""
        expect = """Undeclared procedure: call(foo,[])"""
        self.assertTrue(TestVM.test(input, expect, 448))

    def test_449_break_not_in_loop(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[break(null)]]."""
        expect = """Break not in a loop: break(null)"""
        self.assertTrue(TestVM.test(input, expect, 449))

    def test_450_break_not_in_loop_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[],[],[break(null)])],[do(call(foo,[]),true)]]."""
        expect = """Break not in a loop: break(null)"""
        self.assertTrue(TestVM.test(input, expect, 450))

    def test_451_continue_not_in_loop(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[continue(null)]]."""
        expect = """Continue not in a loop: continue(null)"""
        self.assertTrue(TestVM.test(input, expect, 451))

    def test_452_continue_not_in_loop_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[],[],[continue(null)])],[do(call(foo,[]),true)]]."""
        expect = """Continue not in a loop: continue(null)"""
        self.assertTrue(TestVM.test(input, expect, 452))
    
    def test_453_assign_to_const(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[const(a,7)],[],[assign(a,8)]]."""
        expect = """Cannot assign to a constant: assign(a,8)"""
        self.assertTrue(TestVM.test(input, expect, 453))

    def test_454_func_call_expr(self):
        print(inspect.currentframe().f_code.co_name)
        input = """
        [[var(a,integer)],
        [func(foo,[par(a,integer),par(b,integer)], integer,
            [assign(a,add(a,b)),assign(foo,a)])], 
        [assign(a,3),call(writeIntLn,[call(foo,[a,3])]),call(writeIntLn,[a])]]."""
        expect = """6\n3\n"""    
        self.assertTrue(TestVM.test(input, expect, 454))

    def test_455_proc_call_stmt(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,3),call(writeIntLn,[a])]]."""
        expect = """3\n"""    
        self.assertTrue(TestVM.test(input, expect, 455))

    def test_456_return_stmt(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[],integer,[assign(foo,3)])],[call(writeIntLn,[call(foo,[])])]]."""
        expect = """3\n"""    
        self.assertTrue(TestVM.test(input, expect, 456))

    def test_457_1something(self):
        print(inspect.currentframe().f_code.co_name)
        input = """
        [[var(a,integer)],
        [func(foo,[par(a,integer)],integer,
            [assign(foo,add(a,1))])], 
        [assign(a,call(foo,[1])),call(writeIntLn,[a])]]."""
        expect = """2\n"""    
        self.assertTrue(TestVM.test(input, expect, 457))

    def test_458_redeclaration(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,integer),var(a,float)],[],[call(writeInt,[1])]]."""
        expect = "Redeclared identifier: var(a,float)"
        self.assertTrue(TestVM.test(input, expect, 458))

    def test_459_constant_declaration(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[const(a,1),const(b,2),const(a,3.14)],[],[call(writeInt,[1])]]."""
        expect = "Redeclared identifier: const(a,3.14)"
        self.assertTrue(TestVM.test(input, expect, 459))

    def test_460_times_expression(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeInt,[times(4,sub(3,1))])]]."""
        expect = "8"
        self.assertTrue(TestVM.test(input, expect, 460))

    def test_461_div_expression(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeInt,[rdiv(4,sub(3,1))])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 461))

    def test_462_add_expression_2(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeInt,[add(3.5,1)])]]."""
        expect = "Type mismatch: call(writeInt,[add(3.5,1)])"
        self.assertTrue(TestVM.test(input, expect, 462))

    def test_463_unary_sub_expression(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeInt,[sub(1)])]]."""
        expect = "-1"
        self.assertTrue(TestVM.test(input, expect, 463))

    def test_464_unary_sub_expression_0(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,sub(1))]]."""
        expect = ""
        self.assertTrue(TestVM.test(input, expect, 464))

    def test_465_unary_sub_expression_2(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,float),var(c,integer),var(d,boolean),var(e,string)],[],[assign(c,1)]]."""
        expect = ""
        self.assertTrue(TestVM.test(input, expect, 465))

    def test_466_unary_sub_expression_3(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,float),var(c,integer),var(d,boolean),var(e,string)],[],[assign(b,1)]]."""
        expect = "Type mismatch: assign(b,1)"
        self.assertTrue(TestVM.test(input, expect, 466))

    def test_467_unary_sub_expression_4(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,float),var(c,integer),var(d,boolean),var(e,integer)],[],[assign(a,1),assign(c,2),assign(e,3)]]."""
        expect = ""
        self.assertTrue(TestVM.test(input, expect, 467))

    def test_468_415(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,1),call(writeInt,[1])]]."""
        expect = "1"
        self.assertTrue(TestVM.test(input, expect, 468))

    def test_469_416(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,1),call(writeInt,[a])]]."""
        expect = "1"
        self.assertTrue(TestVM.test(input, expect, 469))

    def test_470_417(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,integer)],[],[assign(a,1),assign(b,add(a,1)),call(writeInt,[b])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 470))

    def test_471_418(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,integer)],[],[assign(a,8),assign(b,idiv(a,2)),call(writeInt,[b])]]."""
        expect = "4"
        self.assertTrue(TestVM.test(input, expect, 471))

    def test_472_419(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,float)],[],[assign(a,8),assign(b,rdiv(a,0.5)),call(writeInt,[b])]]."""
        expect = "Type mismatch: call(writeInt,[b])"
        self.assertTrue(TestVM.test(input, expect, 472))

    def test_473_420(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,integer)],[],[assign(a,8),assign(b,idiv(a,2)),call(writeIntLn,[b])]]."""
        expect = "4\n"
        self.assertTrue(TestVM.test(input, expect, 473))

    def test_474_421(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,string),var(b,integer)],[],[assign(a,"Hello"),call(writeStr,[a])]]."""
        expect = "Hello"
        self.assertTrue(TestVM.test(input, expect, 474))

    def test_475_422(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,boolean),var(b,integer)],[],[assign(a,true),call(writeBool,[a])]]."""
        expect = "true"
        self.assertTrue(TestVM.test(input, expect, 475))

    def test_476_423(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,boolean),var(b,integer)],[],[assign(a,true),call(writeBoolLn,[a])]]."""
        expect = "true\n"
        self.assertTrue(TestVM.test(input, expect, 476))

    def test_477_424(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,boolean),var(b,boolean)],[],[assign(a,true),assign(b,false),call(writeBool,[bnot(a)])]]."""
        expect = "false"
        self.assertTrue(TestVM.test(input, expect, 477))

    def test_478_425(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,boolean),var(b,boolean)],[],[assign(a,true),assign(b,false),call(writeBool,[bnot(b)])]]."""
        expect = "true"
        self.assertTrue(TestVM.test(input, expect, 478))

    def test_479_426(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,boolean),var(b,boolean)],[],[assign(a,true),assign(b,false),call(writeBool,[band(a,b)])]]."""
        expect = "false"
        self.assertTrue(TestVM.test(input, expect, 479))

    def test_480_427(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,boolean),var(b,boolean)],[],[assign(a,true),assign(b,true),call(writeBool,[band(a,b)])]]."""
        expect = "true"
        self.assertTrue(TestVM.test(input, expect, 480))

    def test_481_428(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,boolean),var(b,boolean)],[],[assign(a,true),assign(b,false),call(writeBool,[bor(a,b)])]]."""
        expect = "true"
        self.assertTrue(TestVM.test(input, expect, 481))

    def test_482_429(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,boolean),var(b,boolean)],[],[assign(a,false),assign(b,false),call(writeBool,[bor(a,b)])]]."""
        expect = "false"
        self.assertTrue(TestVM.test(input, expect, 482))

    def test_483_430(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,boolean),var(b,integer)],[],[assign(a,false),assign(b,1),call(writeBool,[band(a,b)])]]."""
        expect = "false"
        self.assertTrue(TestVM.test(input, expect, 483))

    def test_484_431(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,boolean),var(b,integer)],[],[assign(a,true),assign(b,1),call(writeBool,[band(a,b)])]]."""
        expect = "Type mismatch: band(a,b)"
        self.assertTrue(TestVM.test(input, expect, 484))

    def test_485_432(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,boolean),var(b,integer)],[],[assign(a,true),assign(b,1),call(writeBool,[bor(a,b)])]]."""
        expect = "true"
        self.assertTrue(TestVM.test(input, expect, 485))

    def test_486_432(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,boolean),var(b,integer)],[],[assign(a,false),assign(b,1),call(writeBool,[bor(a,b)])]]."""
        expect = "Type mismatch: bor(a,b)"
        self.assertTrue(TestVM.test(input, expect, 486))

    def test_487_433(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,float),var(b,integer)],[],[assign(a,3.4),assign(b,1),call(writeBool,[greater(a,b)])]]."""
        expect = "true"
        self.assertTrue(TestVM.test(input, expect, 487))

    def test_488_434(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,float),var(b,integer)],[],[assign(a,0.1),assign(b,1),call(writeBool,[greater(a,b)])]]."""
        expect = "false"
        self.assertTrue(TestVM.test(input, expect, 488))

    def test_489_435(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,integer)],[],[assign(a,1),assign(b,1),call(writeBool,[ne(a,b)])]]."""
        expect = "false"
        self.assertTrue(TestVM.test(input, expect, 489))

    def test_490_436(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,boolean),var(b,integer)],[],[assign(a,true),assign(b,1),call(writeBool,[ne(a,b)])]]."""
        expect = "Type mismatch: ne(a,b)"
        self.assertTrue(TestVM.test(input, expect, 490))

    def test_491_437(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,boolean),var(b,boolean)],[],[assign(a,true),assign(b,false),call(writeBool,[ne(a,b)])]]."""
        expect = "true"
        self.assertTrue(TestVM.test(input, expect, 491))

    def test_492_438(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[assign(a,true)]]."""
        expect = "Undeclared identifier: a"
        self.assertTrue(TestVM.test(input, expect, 492))

    def test_493_439(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[assign(a,true)]]."""
        expect = "Undeclared identifier: a"
        self.assertTrue(TestVM.test(input, expect, 493))

    def test_494_function_decl(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,integer),var(c,integer)],[func(foo,[par(a,integer),par(b,integer)],integer,[])],[call(writeInt,[3])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 494))

    def test_495_proc_decl(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,integer),var(c,integer)],[func(foo,[par(a,integer),par(b,integer)],integer,[]),proc(bar,[par(a,integer),par(b,integer)],[call(foo,[a,b])])],[call(writeInt,[3])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 495))


    def test_496_442(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[if(false,assign(a,1),assign(a,2)),call(writeInt,[a])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 496))

    def test_497_443(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[if(add(1,2),assign(a,1),assign(a,2)),call(writeInt,[a])]]."""
        expect = "Type mismatch: if(add(1,2),assign(a,1),assign(a,2))"
        self.assertTrue(TestVM.test(input, expect, 497))

    
    def test_498_444(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[if(true,assign(a,1)),call(writeInt,[a])]]."""
        expect = "1"
        self.assertTrue(TestVM.test(input, expect, 498))


    def test_499_445(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,integer),var(c,integer)],[],[block([var(d,integer),var(e,integer)],[assign(a,1)]),assign(a,2),call(writeInt,[a])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 499))

    def test_500_446(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[if(true,assign(a,1),assign(a,2)),call(writeInt,[a])]]."""
        expect = "1"
        self.assertTrue(TestVM.test(input, expect, 500))

    def test_501_447(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,0),while(less(a,10),block([],[assign(a,add(a,1))])),call(writeInt,[a])]]."""
        expect = "10"
        self.assertTrue(TestVM.test(input, expect, 501))


    def test_502_448(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,0),block([],[assign(a,add(a,2))]),call(writeInt,[a])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 502))

    def test_503_449(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,0),block([var(b,integer)],[assign(a,add(a,2))]),call(writeInt,[a])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 503))

    def test_504_450(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,0),while(less(a,10),block([],[assign(a,add(a,1)),call(writeIntLn,[a])]))]]."""
        expect = """1
2
3
4
5
6
7
8
9
10
"""
        self.assertTrue(TestVM.test(input, expect, 504))

    def test_505_451(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,0),do([assign(a,add(a,1))],le(a,10)),call(writeInt,[a])]]."""
        expect = "11"
        self.assertTrue(TestVM.test(input, expect, 505))

    def test_506_452(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,0),loop(3,assign(a,add(a,1))),call(writeInt,[a])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 506))

    def test_507_454(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,0),while(less(a,10),block([],[assign(a,add(a,1)),if(eql(a,5),continue(null)),call(writeIntLn,[a])]))]]."""
        expect = """1
2
3
4
6
7
8
9
10
"""
        self.assertTrue(TestVM.test(input, expect, 507))

    def test_508_453(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,0),while(less(a,10),block([],[assign(a,add(a,1)),if(eql(a,5),break(null)),call(writeIntLn,[a])]))]]."""
        expect = """1
2
3
4
"""
        self.assertTrue(TestVM.test(input, expect, 508))

    def test_509_455(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,0),do([assign(a,add(a,1)),if(eql(a,5),break(null))],le(a,10)),call(writeInt,[a])]]."""
        expect = "5"
        self.assertTrue(TestVM.test(input, expect, 509))

    def test_510_456(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,0),loop(10,block([],[assign(a,add(a,1)),if(eql(a,5),continue(null)),call(writeInt,[a])]))]]."""
        expect = "1234678910"
        self.assertTrue(TestVM.test(input, expect, 510))

    def test_511_457(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,0),loop(10,block([],[assign(a,add(a,1)),if(eql(a,5),continue(null)),call(writeInt,[a])])),break(null)]]."""
        expect = "1234678910Break not in a loop: break(null)"
        self.assertTrue(TestVM.test(input, expect, 511))

    def test_512_458(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,0),continue(null)]]."""
        expect = "Continue not in a loop: continue(null)"
        self.assertTrue(TestVM.test(input, expect, 512))

    def test_513_459(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[],integer,[assign(foo,1)])],[call(writeInt,[call(foo,[])])]]."""
        expect = "1"
        self.assertTrue(TestVM.test(input, expect, 513))

    def test_514_460(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[par(a,integer),par(b,boolean)],integer,[if(b,assign(foo,a),assign(foo,0))])],[call(writeInt,[call(foo,[2,true])])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 514))

    def test_515_461(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[par(a,integer),par(b,boolean)],integer,[if(b,assign(foo,a),assign(foo,0))])],[call(writeInt,[call(foo,[2,false])])]]."""
        expect = "0"
        self.assertTrue(TestVM.test(input, expect, 515))

    def test_516_462(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[par(a,integer),par(b,boolean)],integer,[if(b,assign(foo,a),assign(foo,0))])],[call(writeInt,[call(foo,[])])]]."""
        expect = "Wrong number of arguments: call(foo,[])"
        self.assertTrue(TestVM.test(input, expect, 516))

    def test_517_463(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[par(a,integer),par(b,boolean)],integer,[if(b,assign(foo,a),assign(foo,0))])],[call(writeInt,[call(goo,[])])]]."""
        expect = "Undeclared function: call(goo,[])"
        self.assertTrue(TestVM.test(input, expect, 517))

    def test_518_464(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[func(foo,[],integer,[assign(a,3),assign(foo,1)])],[call(writeInt,[call(foo,[])]),call(writeInt,[a])]]."""
        expect = "13"
        self.assertTrue(TestVM.test(input, expect, 518))

    def test_519_465(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[proc(foo,[],[call(writeInt,[1])])],[call(foo,[])]]."""
        expect = "1"
        self.assertTrue(TestVM.test(input, expect, 519))

    def test_520_466(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[proc(foo,[],[assign(a,0),call(writeInt,[a])])],[call(foo,[])]]."""
        expect = "0"
        self.assertTrue(TestVM.test(input, expect, 520))

    def test_521_467(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[proc(foo,[],[assign(a,0),call(writeInt,[a])])],[assign(a,1),call(writeIntLn,[a]),call(foo,[])]]."""
        expect = "1\n0"
        self.assertTrue(TestVM.test(input, expect, 521))

    def test_522_468(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[proc(foo,[par(b,integer),par(c,integer)],[assign(b,2),assign(c,1),assign(a,add(b,c)),call(writeInt,[a])])],[assign(a,1),call(writeIntLn,[a]),call(foo,[2]),call(writeIntLn,[a])]]."""
        expect = """1
Wrong number of arguments: call(foo,[2])"""
        self.assertTrue(TestVM.test(input, expect, 522))

    def test_523_469(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[proc(foo,[par(b,integer),par(c,integer)],[assign(a,add(b,c)),call(writeInt,[a])])],[assign(a,1),call(writeIntLn,[a]),call(foo,[1,2]),call(writeIntLn,[a])]]."""
        expect = """1
33
"""
        self.assertTrue(TestVM.test(input, expect, 523))

    def test_524_470(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[proc(foo,[par(b,integer),par(c,integer)],[assign(a,add(b,c)),call(writeInt,[a])])],[assign(a,1),call(writeIntLn,[a]),call(goo,[1,2]),call(writeIntLn,[a])]]."""
        expect = """1
Undeclared procedure: call(goo,[1,2])"""
        self.assertTrue(TestVM.test(input, expect, 524))

    def test_525_471(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[proc(foo,[],[call(writeRealLn,[1.25])])],[loop(3,call(foo,[]))]]."""
        expect = """1.25
1.25
1.25
"""
        self.assertTrue(TestVM.test(input, expect, 525))

    def test_526_472(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[proc(foo,[],[call(writeRealLn,[1.25])])],[loop(3,call(goo,[]))]]."""
        expect = """Undeclared procedure: call(goo,[])"""
        self.assertTrue(TestVM.test(input, expect, 526))

    def test_527_473(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[proc(foo,[par(a,integer)],[])],[assign(a,0),call(foo,[1]),call(writeIntLn,[a]),assign(a,1),call(writeIntLn,[a])]]."""
        expect = """0
1
"""
        self.assertTrue(TestVM.test(input, expect, 527))

    def test_528_474(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[proc(foo,[par(a,integer),par(b,integer)],[assign(a,sub(a,b)),call(writeIntLn,[a])])],[assign(a,0),call(goo,[2,1]),call(writeIntLn,[a])]]."""
        expect = """Undeclared procedure: call(goo,[2,1])"""
        self.assertTrue(TestVM.test(input, expect, 528))

    def test_529_475(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[func(foo,[par(a,integer)],integer,[assign(a,3),call(writeIntLn,[a]),assign(foo,1)])],[assign(a,0),call(writeIntLn,[call(foo,[1])]),call(writeInt,[a])]]."""
        expect = """3
1
0"""
        self.assertTrue(TestVM.test(input, expect, 529))

    def test_530_476(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[proc(foo,[par(a,integer),par(b,integer)],[assign(a,sub(a,b)),call(writeIntLn,[a])])],[assign(a,0),call(goo,[2,1]),call(writeIntLn,[a])]]."""
        expect = """Undeclared procedure: call(goo,[2,1])"""
        self.assertTrue(TestVM.test(input, expect, 530))


    def test_531_477(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[proc(foo,[par(a,integer),par(b,integer)],[assign(a,sub(a,b)),call(writeIntLn,[a])])],[assign(a,0),loop(3,call(foo,[2,1])),call(writeIntLn,[a])]]."""
        expect = """1
1
1
0
"""
        self.assertTrue(TestVM.test(input, expect, 531))

    def test_532_478(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[call(writeStr,["Hello"]),call(writeLn,[]),call(writeStr,["World"])]]."""
        expect = """Hello
World"""
        self.assertTrue(TestVM.test(input, expect, 532))
#WITH READ TESTCASE, ONLY UNCOMMENT ONE AT A TIME TO AVOID CONFUSION


#     def test_533_479(self):        
#   print(inspect.currentframe().f_code.co_name)    
#     input = """[[var(a,integer)],[],[assign(a,call(readInt,[])),call(writeInt,[a])]]."""
#         expect = """"""
#         self.assertTrue(TestVM.test(input, expect, 533))

    # def test_534_480(self):        
    #   print(inspect.currentframe().f_code.co_name)
    #     input = """[[var(a,integer)],[],[assign(a,call(readInt,[1])),call(writeInt,[a])]]."""
    #     expect = """Wrong number of arguments: call(readInt,[1])"""
    #     self.assertTrue(TestVM.test(input, expect, 534))

    # def test_535_481(self):        
    #   print(inspect.currentframe().f_code.co_name)
    #     input = """[[var(a,boolean)],[],[assign(a,call(readBool,[])),call(writeBool,[a])]]."""
    #     expect = """"""
    #     self.assertTrue(TestVM.test(input, expect, 535))

    # def test_536_482(self):        
    #   print(inspect.currentframe().f_code.co_name)
    #     input = """[[var(a,float)],[],[assign(a,call(readReal,[])),call(writeReal,[a])]]."""
    #     expect = """"""
    #     self.assertTrue(TestVM.test(input, expect, 536))

    def test_537_483(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,float)],[],[call(writeRealLn,[a])]]."""
        expect = """Undefined variable: a"""
        self.assertTrue(TestVM.test(input, expect, 537))

    #SAMPLE TESTCASES FROM SPEC

    def test_538_484(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[func(foo,[par(a,integer),par(b,integer)],integer,[assign(a,add(a,b)),assign(foo,a)])],[assign(a,3),call(writeIntLn,[call(foo,[a,3])]),call(writeIntLn,[a])]]."""
        expect = """6
3
"""
        self.assertTrue(TestVM.test(input, expect, 538))

    def test_539_redeclaration(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,integer),var(a,float)],[],[call(writeInt,[1])]]."""
        expect = "Redeclared identifier: var(a,float)"
        self.assertTrue(TestVM.test(input, expect, 539))

    # def test_540_406(self):        # Read test
    #   print(inspect.currentframe().f_code.co_name)
    #     input = """[[],[],[call(readInt)]]."""
    #     expect = """"""
    #     self.assertTrue(TestVM.test(input, expect, 540))

    def test_541_407(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeInt,[sub(3,1)])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 541))

    def test_542_408(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeReal,[add(sub(1),times(sub(1,2),rdiv(3,4)))])]]."""
        expect = "Type mismatch: call(writeReal,[add(sub(1),times(sub(1,2),3 rdiv 4))])"
        self.assertTrue(TestVM.test(input, expect, 542))

    def test_543_409(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeInt,[add(sub(1),times(sub(1,2),idiv(3,4)))])]]."""
        expect = "-1"
        self.assertTrue(TestVM.test(input, expect, 543))

    def test_544_410(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeInt,[add(sub(1),times(sub(1,2),imod(3,4)))])]]."""
        expect = "-4"
        self.assertTrue(TestVM.test(input, expect, 544))

    def test_545_411(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeBool,[bnot(true)])]]."""
        expect = "false"
        self.assertTrue(TestVM.test(input, expect, 545))

    def test_546_412(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeBool,[bnot(true)]),call(writeBool,[bnot(false)]),call(writeBool,[band(false,true)]),call(writeBool,[bor(true,false)])]]."""
        expect = "falsetruefalsetrue"
        self.assertTrue(TestVM.test(input, expect, 546))

    def test_547_413(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,3),call(writeIntLn,[a])]]."""
        expect = "3\n"
        self.assertTrue(TestVM.test(input, expect, 547))

    def test_548_414(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,boolean)],[],[assign(a,3),call(writeIntLn,[a])]]."""
        expect = "Type mismatch: assign(a,3)"
        self.assertTrue(TestVM.test(input, expect, 548))

    def test_549_415(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[const(a,7)],[],[assign(a,8)]]."""
        expect = "Cannot assign to a constant: assign(a,8)"
        self.assertTrue(TestVM.test(input, expect, 549))

    def test_550_416(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[call(writeIntLn,[a])]]."""
        expect = "Invalid expression: a"
        self.assertTrue(TestVM.test(input, expect, 550))

    def test_551_417(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeReal,[add(1,2.3)])]]."""
        expect = "3.3"
        self.assertTrue(TestVM.test(input, expect, 551))

    def test_552_418(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeReal,[add(1,false)])]]."""
        expect = "Type mismatch: add(1,false)"
        self.assertTrue(TestVM.test(input, expect, 552))

    def test_553_419(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeReal,[sub(false)])]]."""
        expect = """Type mismatch: sub(false)"""
        self.assertTrue(TestVM.test(input, expect, 553))

    def test_554_420(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeBool,[band(false, 123)])]]."""
        expect = """false"""
        self.assertTrue(TestVM.test(input, expect, 554))

    def test_555_421(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeBool,[bor(true, 123)])]]."""
        expect = """true"""
        self.assertTrue(TestVM.test(input, expect, 555))

    # def test_556_422(self):        # Read test
    #   print(inspect.currentframe().f_code.co_name)
    #     input = """[[],[],[
    #         call(writeInt, [call(readInt)] )
    #     ]]."""
    #     expect = """5"""
    #     self.assertTrue(TestVM.test(input, expect, 556))

    def test_557_423(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],
            [
                func(f, [par(a, integer)], integer, [assign(f, add(a, 1))])
            ],
            [
                call(writeIntLn, [call(f, [122])])
            ]
        ]."""
        expect = """123\n"""
        self.assertTrue(TestVM.test(input, expect, 557))

    def test_558_424(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(b, integer)
            ],
            [
                func(f, [par(a, integer)], integer, [assign(b, add(a, 100)), call(writeIntLn, [b]), assign(f, add(a, 1))])
            ],
            [
                call(writeIntLn, [call(f, [122])]),
                call(writeIntLn, [b])
            ]
        ]."""
        expect = """222\n123\n222\n"""
        self.assertTrue(TestVM.test(input, expect, 558))

    def test_559_425(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(a, integer),
                var(b, integer)
            ],
            [
                func(
                    f, [par(a, integer)], integer, [
                        assign(b, add(a, 100)), 
                        call(writeIntLn, [b]),
                        assign(a, 0),
                        assign(f, add(a, 1))
                    ]
                )
            ],
            [
                assign(a, 1000),
                call(writeIntLn, [call(f, [122])]),
                call(writeIntLn, [a]),
                call(writeIntLn, [b])
            ]
        ]."""
        expect = """222\n1\n1000\n222\n"""
        self.assertTrue(TestVM.test(input, expect, 559))

    def test_560_426(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [],
            [
                proc(f, [par(s, string)], [call(writeStr, [s])])
            ],
            [
                call(f, ["Hello world!"])
            ]
        ]."""
        expect = """Hello world!"""
        self.assertTrue(TestVM.test(input, expect, 560))

    def test_561_427(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [],
            [
                proc(f, [], [call(writeStr, ["Hello "]), call(g, [])]),
                proc(g, [], [call(writeStr, ["world!"])])
            ],
            [
                call(f, [])
            ]
        ]."""
        expect = """Hello world!"""
        self.assertTrue(TestVM.test(input, expect, 561))

    def test_562_428(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(a, integer),
                var(b, integer),
                var(c, integer),
                var(d, integer)
            ],
            [],
            [
                assign(a, 0),
                assign(b, 0),
                assign(c, 0),
                assign(d, 0),
                if(true, assign(a, 1)),
                if(eql(3, add(1, 2)), assign(b, 2)),
                  if(false, assign(c, 3)),
                if(ne(3, add(1, 2)), assign(d, 4)),
                call(writeInt, [a]),
                call(writeInt, [b]),
                call(writeInt, [c]),
                call(writeInt, [d])
            ]
        ]."""
        expect = """1200"""
        self.assertTrue(TestVM.test(input, expect, 562))

    def test_563_429(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(a, integer),
                var(b, integer),
                var(c, integer),
                var(d, integer)
            ],
            [],
            [
                assign(a, 0),
                assign(b, 0),
                assign(c, 0),
                assign(d, 0),
                if(eql(3, add(1, 2)), assign(a, 1), assign(b, 2)),
                  if(ne(3, add(1, 2)), assign(c, 3), assign(d, 4)),
                call(writeInt, [a]),
                call(writeInt, [b]),
                call(writeInt, [c]),
                call(writeInt, [d])
            ]
        ]."""
        expect = """1004"""
        self.assertTrue(TestVM.test(input, expect, 563))

    def test_564_430(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(a, integer),
                var(b, integer)
            ],
            [],
            [
                assign(a, 0),
                assign(b, 0),
                if(add(1, 2), assign(a, 1), assign(b, 2))
            ]
        ]."""
        expect = """Type mismatch: if(add(1,2),assign(a,1),assign(b,2))"""
        self.assertTrue(TestVM.test(input, expect, 564))

    def test_565_431(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(a, integer)
            ],
            [],
            [
                assign(a, 0),
                if(add(1, 2), assign(a, 1))
            ]
        ]."""
        expect = """Type mismatch: if(add(1,2),assign(a,1))"""
        self.assertTrue(TestVM.test(input, expect, 565))
    
    def test_566_432(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(i, integer)
            ],
            [
                proc(whileBody, [], [call(writeInt, [i]), assign(i, add(i, 1))])
            ],
            [
                assign(i, 0),
                while(ne(i, 10), call(whileBody, [])),
                while(ne(i, 10), call(whileBody, []))
            ]
        ]."""
        expect = """0123456789"""
        self.assertTrue(TestVM.test(input, expect, 566))

    def test_567_433(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(i, integer)
            ],
            [
                proc(doWhileBody, [], [call(writeInt, [i]), assign(i, add(i, 1))])
            ],
            [
                assign(i, 0),
                do([call(doWhileBody, [])], less(i, 10)),
                do([call(doWhileBody, [])], less(i, 10))
            ]
        ]."""
        expect = """012345678910"""
        self.assertTrue(TestVM.test(input, expect, 567))

    def test_568_434(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(i, integer)
            ],
            [
                proc(loopBody, [], [call(writeInt, [i]), assign(i, add(i, 1))])
            ],
            [
                assign(i, 0),
                loop(add(i, 10), call(loopBody, [])),
                loop(-1, call(loopBody, [])),
                loop(0, call(loopBody, []))
            ]
        ]."""
        expect = """0123456789"""
        self.assertTrue(TestVM.test(input, expect, 568))

    def test_569_435(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(i, integer)
            ],
            [
            ],
            [
                assign(i, 0),
                while(ne(i, 10), block([], [call(writeInt, [i]), assign(i, add(i, 1)), break(null)])),
                call(writeInt, [i])
            ]
        ]."""
        expect = """01"""
        self.assertTrue(TestVM.test(input, expect, 569))

    def test_570_436(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(i, integer)
            ],
            [
            ],
            [
                assign(i, 0),
                while(ne(i, 10), block([],[call(writeInt, [i]), assign(i, add(i, 1)), continue(null), assign(i, add(i, 100))])),
                call(writeInt, [i])
            ]
        ]."""
        expect = """012345678910"""
        self.assertTrue(TestVM.test(input, expect, 570))

    def test_571_437(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(i, integer)
            ],
            [
            ],
            [
                assign(i, 0),
                do([call(writeInt, [i]), assign(i, add(i, 1)), continue(null), assign(i, add(i, 100))], less(i, 10)),
                call(writeInt, [i])
            ]
        ]."""
        expect = """012345678910"""
        self.assertTrue(TestVM.test(input, expect, 571))

    def test_572_438(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(i, integer)
            ],
            [
            ],
            [
                assign(i, 0),
                do([call(writeInt, [i]), assign(i, add(i, 1)), break(null), assign(i, add(i, 100))], less(i, 10)),
                call(writeInt, [i])
            ]
        ]."""
        expect = """01"""
        self.assertTrue(TestVM.test(input, expect, 572))

    def test_573_439(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(i, integer)
            ],
            [
            ],
            [
                assign(i, 0),
                loop(add(i, 10), block([],[call(writeInt, [i]), assign(i, add(i, 1)), continue(null), assign(i, add(i, 100))])),
                call(writeInt, [i])
            ]
        ]."""
        expect = """012345678910"""
        self.assertTrue(TestVM.test(input, expect, 573))

    def test_574_440(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(i, integer)
            ],
            [
            ],
            [
                assign(i, 0),
                loop(add(i, 10), block([],[call(writeInt, [i]), assign(i, add(i, 1)), break(null), assign(i, add(i, 100))])),
                call(writeInt, [i])
            ]
        ]."""
        expect = """01"""
        self.assertTrue(TestVM.test(input, expect, 574))

    def test_575_441(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(i, integer)
            ],
            [],
            [
                assign(i, 0),
                do([call(writeInt, [i]), assign(i, add(1, i))], less(i, 10)),
                call(writeInt, [i])
            ]
        ]."""
        expect = """012345678910"""
        self.assertTrue(TestVM.test(input, expect, 575))

    def test_576_442(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(i, integer)
            ],
            [],
            [
                assign(i, 0),
                do([call(writeInt, [i]), assign(i, add(1, i)), continue(null), assign(i, add(100, i))], less(i, 10)),
                call(writeInt, [i])
            ]
        ]."""
        expect = """012345678910"""
        self.assertTrue(TestVM.test(input, expect, 576))

    def test_577_443(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
                var(i, integer)
            ],
            [],
            [
                assign(i, 0),
                do([call(writeInt, [i]), assign(i, add(1, i)), break(null), assign(i, add(100, i))], less(i, 10)),
                call(writeInt, [i])
            ]
        ]."""
        expect = """01"""
        self.assertTrue(TestVM.test(input, expect, 577))
    
    def test_578_444(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [],
            [],
            [
                block([var(i, integer)], [call(writeInt, [i])])
            ]
        ]."""
        expect = """Invalid expression: i"""
        self.assertTrue(TestVM.test(input, expect, 578))

    def test_579_445(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [],
            [],
            [
                block([var(i, integer)], [
                    assign(i, 0),
                    do([call(writeInt, [i]), assign(i, add(1, i))], less(i, 10))
                ])
            ]
        ]."""
        expect = """0123456789"""
        self.assertTrue(TestVM.test(input, expect, 579))

    def test_580_446(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
            [
            ],
            [
                proc(f, [par(a, integer)], [call(writeInt, [a])]),
                func(g, [par(a, integer)], integer, [assign(g, a)])
            ],
            [
                call(writeInt, [call(g, [1])])
            ]
        ]."""
        expect = """1"""
        self.assertTrue(TestVM.test(input, expect, 580))

    def test_581_447(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
        [
            var(n,integer),
            const(m, 50)
            ],
            [
                func(
                    isPrime,
                    [par(n,integer)],
                    boolean,
                    [
                        assign(isPrime,true),
                        block(
                            [var(div,integer)],
                            [assign(div,2),
                                while(
                                    less(div,n),
                                    block([],[
                                        if(eql(imod(n,div),0),
                                            block([],[
                                                assign(isPrime,false),
                                                break(null)
                                            ])
                                        ),
                                        assign(div,add(div,1))
                                    ]
                                    )
                                )
                            ]
                        )
                    ]
                )
            ],
            [
                assign(n,2),
                while(less(n,m),
                    block([],[
                            if(call(isPrime,[n]),
                                block([],[call(writeInt,[n]), call(writeStr,[" "])])),
                            assign(n,add(n,1))
                        ]
                    )
                )
            ]
        ]."""
        expect = """2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 """
        self.assertTrue(TestVM.test(input, expect, 581))

    def test_582_448(self):
        print(inspect.currentframe().f_code.co_name)
        input = """
        [
            [],
            [],
            [
                call(writeInt, [1]),
                call(writeLn, []),
                call(writeIntLn, [2]),
                call(writeLn, []),
                call(writeReal, [3.14]),
                call(writeLn, []),
                call(writeRealLn, [4.2025]),
                call(writeLn, []),
                call(writeBool, [true]),
                call(writeLn, []),
                % call(writeBoolLn, [false]),
                call(writeLn, []),
                call(writeStrLn, ["Ganyu iz tha bezt"]),
                call(writeStr, ["HCMUT"])
            ]
        ]."""
        expect = \
"""1
2

3.14
4.2025

true

Ganyu iz tha bezt
HCMUT"""
        self.assertTrue(TestVM.test(input, expect, 582))

    def test_583_449(self):
        print(inspect.currentframe().f_code.co_name)
        input = """
        [
            [],
            [
                func(fibonacci, [par(n, integer)], integer, [
                    if(eql(n, 0), assign(fibonacci, 0)),
                    if(eql(n, 1), assign(fibonacci, 1)),
                    if(greater(n, 1), assign(fibonacci, add(call(fibonacci, [sub(n, 1)]), call(fibonacci, [sub(n, 2)]))))
                ])
            ],
            [
                call(writeInt, [call(fibonacci, [10])])
            ]
        ]."""
        expect = """55"""
        self.assertTrue(TestVM.test(input, expect, 583))

    ######################################### Begin of sample testcases from spec #########################################

    def test_584_450(self):
        print(inspect.currentframe().f_code.co_name)
        input = """
        [[var(a,integer)],[func(foo,[par(a,integer)],integer,[assign(foo,add(a,1))])],[assign(a,call(foo,[1]))]]."""
        expect = """"""
        self.assertTrue(TestVM.test(input, expect, 584))

    def test_585_451(self):
        print(inspect.currentframe().f_code.co_name)
        input = """
        [[var(a1,integer), var(a2,float), var(a3,string), var(a4,boolean)],[],[
            assign(a1,1),
            assign(a2,2.3),
            assign(a3,"Hello world!"),
            assign(a4,true),
            call(writeInt, [a1]),
            call(writeLn, []),
            call(writeReal, [a2]),
            call(writeLn, []),
            call(writeStr, [a3]),
            call(writeLn, []),
            call(writeBool, [a4]),
            call(writeLn, [])
        ]]."""
        expect = """1
2.3
Hello world!
true
"""
        self.assertTrue(TestVM.test(input, expect, 585))

    def test_586_452(self):
        print(inspect.currentframe().f_code.co_name)
        input = """
        [[const(a, 1), const(b, 2.3), const(c, "Hello world!"), const(d, true)],[],[
            call(writeInt, [a]),
            call(writeLn, []),
            call(writeReal, [b]),
            call(writeLn, []),
            call(writeStr, [c]),
            call(writeLn, []),
            call(writeBool, [d]),
            call(writeLn, [])
        ]]."""
        expect = """1
2.3
Hello world!
true
"""
        self.assertTrue(TestVM.test(input, expect, 586))

    def test_587_453(self):
        print(inspect.currentframe().f_code.co_name)
        input = """
        [
        [],[
            func(f,[par(a,integer)],integer,[
                assign(f,add(a,1))
            ]),
            func(g,[par(a,float)],float,[
                assign(g,add(a,1))
            ]),
            func(h,[par(a,string)],string,[
                assign(h,a)
            ]),
            func(i,[par(a,boolean)],boolean,[
                assign(i,a)
            ])
        
        ],[
            call(writeInt,[call(f,[1])]),
            call(writeLn,[]),
            call(writeReal,[call(g,[2.3])]),
            call(writeLn,[]),
            call(writeStr,[call(h,["Hello world!"])]),
            call(writeLn,[]),
            call(writeBool,[call(i,[true])]),
            call(writeLn,[])
        ]
        ]."""
        expect = """2
3.3
Hello world!
true
"""
        self.assertTrue(TestVM.test(input, expect, 587))

    def test_588_454(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[
        [],[
            proc(f,[par(a,integer)],[call(writeInt,[a])]),
            proc(g,[par(a,float)],[call(writeReal,[a])]),
            proc(h,[par(a,string)],[call(writeStr,[a])]),
            proc(i,[par(a,boolean)],[call(writeBool,[a])]),
            proc(j,[par(a,integer),par(b,float),par(c,integer)],[call(writeReal,[add(a,add(b,c))])])
        ],[
            call(f,[1]),
            call(g,[2.3]),
            call(h,["Hello world!"]),
            call(i,[true]),
            call(j,[1,2.3,4])
        ]
        ]."""
        expect = """12.3Hello world!true7.3"""
        self.assertTrue(TestVM.test(input, expect, 588))

    def test_589_455(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer), var(b,float), var(c,integer), var(d,float)],[],[
            assign(a,1),
            assign(b,2.3),
            assign(c,4),
            assign(d,5.6),
            call(writeInt,[sub(a)]),
            call(writeReal,[sub(b)]),
            call(writeInt,[add(a,c)]),
            call(writeReal,[add(b,c)]),
            call(writeReal,[add(c,d)]),
            call(writeReal,[add(b,d)]),
            call(writeInt,[sub(a,c)]),
            call(writeReal,[sub(b,c)]),
            call(writeReal,[sub(c,d)]),
            call(writeReal,[sub(b,d)]),
            call(writeInt,[times(a,c)]),
            call(writeReal,[times(b,c)]),
            call(writeReal,[times(c,d)]),
            call(writeReal,[times(b,d)]),
            call(writeInt,[rdiv(a,c)]),
            call(writeReal,[rdiv(b,c)]),
            call(writeReal,[rdiv(c,d)]),
            call(writeReal,[rdiv(b,d)]),
            call(writeInt,[idiv(a,c)]),
            call(writeInt,[idiv(123,10)]),
            call(writeInt,[imod(a,c)]),
            call(writeInt,[imod(123,10)])
        ]]."""
        expect = """-1-2.356.39.67.8999999999999995-3-1.7000000000000002-1.5999999999999996-3.349.222.412.87999999999999900.5750.71428571428571430.410714285714285701213"""
        self.assertTrue(TestVM.test(input, expect, 589))

    def test_590_456(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,boolean), var(b,boolean)],[],[
            assign(a,true),
            assign(b,false),
            call(writeBool,[bnot(a)]),
            call(writeBool,[bnot(b)]),
            call(writeBool,[band(b,b)]),
            call(writeBool,[band(b,a)]),
            call(writeBool,[band(a,b)]),
            call(writeBool,[band(a,a)]),
            call(writeBool,[bor(b,b)]),
            call(writeBool,[bor(b,a)]),
            call(writeBool,[bor(a,b)]),
            call(writeBool,[bor(a,a)]),
            call(writeBool,[band(b,"test shortcut")]),
            call(writeBool,[bor(a,"test shortcut")])
        ]]."""
        expect = """falsetruefalsefalsefalsetruefalsetruetruetruefalsetrue"""
        self.assertTrue(TestVM.test(input, expect, 590))

    def test_591_457(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[
            call(writeBool,[greater(1,2)]),
            call(writeBool,[greater(2,1)]),
            call(writeBool,[greater(1,1)]),
            call(writeBool,[greater(2.0,2)]),
            call(writeBool,[greater(2,2.0)]),
            call(writeBool,[greater(2.0,2.0)]),
            call(writeBool,[less(1,2)]),
            call(writeBool,[less(2,1)]),
            call(writeBool,[less(1,1)]),
            call(writeBool,[less(2.0,2)]),
            call(writeBool,[less(2,2.0)]),
            call(writeBool,[less(2.0,2.0)]),
            call(writeBool,[ge(1,2)]),
            call(writeBool,[ge(2,1)]),
            call(writeBool,[ge(1,1)]),
            call(writeBool,[ge(2.0,2)]),
            call(writeBool,[ge(2,2.0)]),
            call(writeBool,[ge(2.0,2.0)]),
            call(writeLn,[]),
            call(writeBool,[le(1,2)]),
            call(writeBool,[le(2,1)]),
            call(writeBool,[le(1,1)]),
            call(writeBool,[le(2.0,2)]),
            call(writeBool,[le(2,2.0)]),
            call(writeBool,[le(2.0,2.0)]),
            call(writeBool,[eql(1,2)]),
            call(writeBool,[eql(2,1)]),
            call(writeBool,[eql(1,1)]),
            call(writeBool,[eql(true,false)]),
            call(writeBool,[eql(false,true)]),
            call(writeBool,[eql(true,true)]),
            call(writeBool,[ne(1,2)]),
            call(writeBool,[ne(2,1)]),
            call(writeBool,[ne(1,1)]),
            call(writeBool,[ne(true,false)]),
            call(writeBool,[ne(false,true)]),
            call(writeBool,[ne(true,true)])
        ]]."""
        expect = """falsetruefalsefalsefalsefalsetruefalsefalsefalsefalsefalsefalsetruetruetruetruetrue
truefalsetruetruetruetruefalsefalsetruefalsefalsetruetruetruefalsetruetruefalse"""
        self.assertTrue(TestVM.test(input, expect, 591))

    def test_592_458(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[func(foo,[par(a,integer),par(b,integer)],integer,
                    [assign(a,add(a,b)),assign(foo,a)])],
                    [assign(a,3),call(writeIntLn,[call(foo,[a,3])]),call(writeIntLn,[a])]]."""
        expect = """6\n3\n"""
        self.assertTrue(TestVM.test(input, expect, 592))

    def test_593_459(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[const(a,1),const(b,2.3),const(c,"Hello world!"),const(d,true)],[],[
            call(writeInt,[a]),
            call(writeLn,[]),
            call(writeReal,[b]),
            call(writeLn,[]),
            call(writeStr,[c]),
            call(writeLn,[]),
            call(writeBool,[d]),
            call(writeLn,[])
        ]]."""
        expect = """1
2.3
Hello world!
true
"""
        self.assertTrue(TestVM.test(input, expect, 593))

    def test_594_460(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[
            block([var(i, integer)], [
                if(true, call(writeInt, [111])),
                if(false, call(writeInt, [222])),
                if(true, call(writeInt, [333]), call(writeInt, [444])),
                if(false, call(writeInt, [555]), call(writeInt, [666])),
                assign(i, 0),
                do([call(writeInt, [i]), assign(i, add(i, 1))], less(i, 10)),
                assign(i, 0),
                loop(add(i, 10), call(writeInt, [i])),
                assign(i, 0),
                while(ne(i, 10), block([], [call(writeInt, [i]), assign(i, add(i, 1))])),
                assign(i, 0),
                do([call(writeInt, [i]), assign(i, add(i, 1)), break(null), call(writeInt, [1000])], less(i, 10)),
                assign(i, 0),
                loop(add(i, 10), block([], [call(writeInt, [i]), break(null), call(writeInt, [1000])])),
                assign(i, 0),
                while(ne(i, 10), block([], [call(writeInt, [i]), assign(i, add(i, 1)), break(null), call(writeInt, [1000])])),
                assign(i, 0),
                do([call(writeInt, [i]), assign(i, add(i, 1)), continue(null), call(writeInt, [1000])], less(i, 10)),
                assign(i, 0),
                loop(add(i, 10), block([], [call(writeInt, [i]), continue(null), call(writeInt, [1000])])),
                assign(i, 0),
                while(ne(i, 10), block([], [call(writeInt, [i]), assign(i, add(i, 1)), continue(null), call(writeInt, [1000])]))
            ])
        ]]."""
        expect = """111333666012345678900000000000123456789000012345678900000000000123456789"""
        self.assertTrue(TestVM.test(input, expect, 594))

    def test_595_461(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[],integer,[assign(foo,3)])],[call(writeIntLn,[call(foo,[])])]]."""
        expect = """3\n"""
        self.assertTrue(TestVM.test(input, expect, 595))

    def test_596_462(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,3),call(writeIntLn,[a])]]."""
        expect = """3\n"""
        self.assertTrue(TestVM.test(input, expect, 596))

    def test_597_463(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,real),var(a,boolean)],[],[]]."""
        expect = """Redeclared identifier: var(a,boolean)"""
        self.assertTrue(TestVM.test(input, expect, 597))

    def test_598_464(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[par(a,integer),par(b,integer),par(a,real)],[])],[]]."""
        expect = """Redeclared identifier: par(a,real)"""
        self.assertTrue(TestVM.test(input, expect, 598))

    # def test_599_465(self): #TODO:        # hể sao var với const là stmt?
    #   print(inspect.currentframe().f_code.co_name)
    #     input = """[[],[proc(foo,[],[const(a,7),var(a,real)])],[]]."""
    #     expect = """Redeclared identifier: var(a,real)"""
    #     self.assertTrue(TestVM.test(input, expect, 599))

    # def test_600_466(self):
    #   print(inspect.currentframe().f_code.co_name)
    #     input = """[[],[proc(foo,[],[var(a,real),[var(a,integer)]])],[call(writeIntLn,[3])]]."""
    #     expect = """3\n"""
    #     self.assertTrue(TestVM.test(input, expect, 600))

    def test_601_467(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(readInt,[],real,[])],[]]."""
        expect = """Redeclared function: readInt"""
        self.assertTrue(TestVM.test(input, expect, 601))

    def test_602_468(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[],integer,[]),proc(foo,[par(a, integer)],[])],[]]."""
        expect = """Redeclared procedure: foo"""
        self.assertTrue(TestVM.test(input, expect, 602))

    def test_603_469(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(foo,integer)],[proc(foo,[par(a, integer)],[])],[]]."""
        expect = """Redeclared procedure: foo"""
        self.assertTrue(TestVM.test(input, expect, 603))

    def test_604_470(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeInt,[add(10,true)])]]."""
        expect = """Type mismatch: add(10,true)"""
        self.assertTrue(TestVM.test(input, expect, 604))

    def test_605_471(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeBool,[add(10,3)])]]."""
        expect = """Type mismatch: call(writeBool,[add(10,3)])"""
        self.assertTrue(TestVM.test(input, expect, 605))

    def test_606_472(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,3),if(a,call(writeInt,[3]))]]."""
        expect = """Type mismatch: if(a,call(writeInt,[3]))"""
        self.assertTrue(TestVM.test(input, expect, 606))

    def test_607_473(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[],float,[assign(foo,3.0)])],
[call(writeInt,[call(foo,[])])]]."""
        expect = """Type mismatch: call(writeInt,[call(foo,[])])"""
        self.assertTrue(TestVM.test(input, expect, 607))

    def test_608_474(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,add(b,1)),call(writeIntLn,[a])]]."""
        expect = """Undeclared identifier: b"""
        self.assertTrue(TestVM.test(input, expect, 608))

    def test_609_475(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[proc(foo,[],[var(b,integer),assign(b,1),assign(a,b)])],
[call(writeIntLn,[b])]]."""
        expect = """Undeclared identifier: b"""
        self.assertTrue(TestVM.test(input, expect, 609))

    def test_610_476(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[],[])],[call(foo,[1])]]."""
        expect = """Wrong number of arguments: call(foo,[1])"""
        self.assertTrue(TestVM.test(input, expect, 610))
    
    def test_611_477(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[par(a,integer)],[])],[call(foo,[])]]."""
        expect = """Wrong number of arguments: call(foo,[])"""
        self.assertTrue(TestVM.test(input, expect, 611))

    def test_612_478(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[func(foo,[],integer,[])],[assign(a,call(foo,[]))]]."""
        expect = """Invalid expression: call(foo,[])"""
        self.assertTrue(TestVM.test(input, expect, 612))

    def test_613_479(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[call(writeInt,[a])]]."""
        expect = """Invalid expression: a"""
        self.assertTrue(TestVM.test(input, expect, 613))

    def test_614_480(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,call(foo,[]))]]."""
        expect = """Undeclared function: call(foo,[])"""
        self.assertTrue(TestVM.test(input, expect, 614))

    def test_615_481(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(foo,[])]]."""
        expect = """Undeclared procedure: call(foo,[])"""
        self.assertTrue(TestVM.test(input, expect, 615))

    def test_616_482(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[break(null)]]."""
        expect = """Break not in a loop: break(null)"""
        self.assertTrue(TestVM.test(input, expect, 616))

    def test_617_483(self):  
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[],[break(null)])],[do([call(foo,[])],true)]]."""
        expect = """Break not in a loop: break(null)"""
        self.assertTrue(TestVM.test(input, expect, 617))

    def test_618_484(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[continue(null)]]."""
        expect = """Continue not in a loop: continue(null)"""
        self.assertTrue(TestVM.test(input, expect, 618))

    def test_619_485(self): 
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[],[continue(null)])],[do([call(foo,[])],true)]]."""
        expect = """Continue not in a loop: continue(null)"""
        self.assertTrue(TestVM.test(input, expect, 619))

    def test_620_486(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[const(a,7)],[],[assign(a,8)]]."""
        expect = """Cannot assign to a constant: assign(a,8)"""
        self.assertTrue(TestVM.test(input, expect, 620))

    ######################################### End of sample testcases from spec #########################################

    def test_621_487(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[
            var(a,float)
        ],[
            func(f,[par(a,integer)],integer,[
                assign(f,add(a,1))
            ])
        ],[
            assign(a,call(f,[1]))
        ]]."""
        expect = """Type mismatch: assign(a,call(f,[1]))""" # Hoặc cái này: Type mismatch: assign(a,2)
        self.assertTrue(TestVM.test(input, expect, 621))

    def test_622_488(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[
            var(a,integer)
        ],[
            func(f,[par(a,integer)],integer,[
                assign(f,add(a,1))
            ])
        ],[
            assign(a,call(f,[1.0]))
        ]]."""
        expect = """Type mismatch: call(f,[1.0])""" 
        self.assertTrue(TestVM.test(input, expect, 622))