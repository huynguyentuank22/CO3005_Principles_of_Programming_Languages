import unittest
from TestUtils import TestVM
import inspect

"""436, 438, 440, 441, 442"""
class VMSuite(unittest.TestCase):
    def test_simple_program(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[],[])],[call(writeInt,[3])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 401))

    def test_simple_expression(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeInt,[add(3,1)])]]."""
        expect = "4"
        self.assertTrue(TestVM.test(input, expect, 402))

    def test_minus_expression(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeInt,[sub(3,1)])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 403))

    def test_nested_expression(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeInt,[add(4,sub(3,1))])]]."""
        expect = "6"
        self.assertTrue(TestVM.test(input, expect, 404))

    def test_redeclared_built_in(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeInt,integer)],[],[]]."""
        expect = "Redeclared identifier: var(writeInt,integer)"
        self.assertTrue(TestVM.test(input, expect, 405))

    def test_redeclared_built_in_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeIntLn, integer)], [], []]."""
        expect = "Redeclared identifier: var(writeIntLn,integer)"
        self.assertTrue(TestVM.test(input, expect, 406))

    def test_redeclared_built_in_3(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeReal, integer)], [], []]."""
        expect = "Redeclared identifier: var(writeReal,integer)"
        self.assertTrue(TestVM.test(input, expect, 407))
    
    def test_redeclared_built_in_4(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeRealLn, integer)], [], []]."""
        expect = "Redeclared identifier: var(writeRealLn,integer)"
        self.assertTrue(TestVM.test(input, expect, 408))

    def test_redeclared_built_in_5(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeBool, integer)], [], []]."""
        expect = "Redeclared identifier: var(writeBool,integer)"
        self.assertTrue(TestVM.test(input, expect, 409))

    def test_redeclared_built_in_6(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeBoolLn, integer)], [], []]."""
        expect = "Redeclared identifier: var(writeBoolLn,integer)"
        self.assertTrue(TestVM.test(input, expect, 410))

    def test_redeclared_built_in_7(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeStr, integer)], [], []]."""
        expect = "Redeclared identifier: var(writeStr,integer)"
        self.assertTrue(TestVM.test(input, expect, 411))

    def test_redeclared_built_in_8(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeStrLn, integer)], [], []]."""
        expect = "Redeclared identifier: var(writeStrLn,integer)"
        self.assertTrue(TestVM.test(input, expect, 412))

    def test_redeclared_built_in_9(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(writeLn, integer)], [], []]."""
        expect = "Redeclared identifier: var(writeLn,integer)"
        self.assertTrue(TestVM.test(input, expect, 413))

    def test_redeclared_built_in_10(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(readInt, integer)], [], []]."""
        expect = "Redeclared identifier: var(readInt,integer)"
        self.assertTrue(TestVM.test(input, expect, 414))

    def test_redeclared_built_in_11(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(readReal, integer)], [], []]."""
        expect = "Redeclared identifier: var(readReal,integer)"
        self.assertTrue(TestVM.test(input, expect, 415))

    def test_redeclared_built_in_12(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(readBool, integer)], [], []]."""
        expect = "Redeclared identifier: var(readBool,integer)"
        self.assertTrue(TestVM.test(input, expect, 416))

    def test_redeclared_var(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,integer),var(a,float)],[],[call(writeInt,[1])]]."""
        expect = "Redeclared identifier: var(a,float)"
        self.assertTrue(TestVM.test(input, expect, 417))

    def test_redeclared_var_2(self):        
        print(inspect.currentframe().f_code.co_name)
        input = """[[const(a,2),var(b,integer),var(a,float)],[],[call(writeInt,[1])]]."""
        expect = "Redeclared identifier: var(a,float)"
        self.assertTrue(TestVM.test(input, expect, 418))    

    def test_redeclared_const(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[const(writeInt, 7)],[],[]]."""
        expect = "Redeclared identifier: const(writeInt,7)"
        self.assertTrue(TestVM.test(input, expect, 419))

    def test_redeclared_const_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[const(a,2),var(b,integer),const(a,8)],[],[call(writeInt,[1])]]."""
        expect = "Redeclared identifier: const(a,8)"
        self.assertTrue(TestVM.test(input, expect, 420))

    def test_redeclared_const_3(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer),var(b,integer),const(a,9)],[],[call(writeInt,[1])]]."""
        expect = "Redeclared identifier: const(a,9)"
        self.assertTrue(TestVM.test(input, expect, 421))

    def test_redeclared_func(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(readInt,[],real,[])],[]]."""
        expect = """Redeclared function: readInt"""
        self.assertTrue(TestVM.test(input, expect, 422))

    def test_redclared_func_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(foo, integer),const(faa,2)],[func(foo,[],real,[])],[]]."""
        expect = """Redeclared function: foo"""
        self.assertTrue(TestVM.test(input, expect, 423))

    def test_redclared_func_3(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[const(foo, 3)],[func(foo,[],real,[])],[]]."""
        expect = """Redeclared function: foo"""
        self.assertTrue(TestVM.test(input, expect, 424))

    def test_redeclared_func_4(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],
        [func(foo,[],real,[]),
        func(foo,[],integer,[])],
        []]."""
        expect = """Redeclared function: foo"""
        self.assertTrue(TestVM.test(input, expect, 425))

    def test_redeclared_proc(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(readInt,[],[])],[]]."""
        expect = """Redeclared procedure: readInt"""
        self.assertTrue(TestVM.test(input, expect, 426))

    def test_redclared_proc_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(foo, integer),const(faa,2)],[proc(foo,[],[])],[]]."""
        expect = """Redeclared procedure: foo"""
        self.assertTrue(TestVM.test(input, expect, 427))

    def test_redclared_proc_3(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[const(foo, 3)],[proc(foo,[],[])],[]]."""
        expect = """Redeclared procedure: foo"""
        self.assertTrue(TestVM.test(input, expect, 428))

    def test_redeclared_proc_4(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[],integer,[]),proc(foo,[],[])],[]]."""
        expect = """Redeclared procedure: foo"""
        self.assertTrue(TestVM.test(input, expect, 429))

    def test_redeclared_proc_5(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[],[]),proc(foo,[],[])],[]]."""
        expect = """Redeclared procedure: foo"""
        self.assertTrue(TestVM.test(input, expect, 430))

    def test_redeclared_param(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[par(a,integer),par(b,integer),par(a,real)],[])],[]]."""
        expect = """Redeclared identifier: par(a,real)"""
        self.assertTrue(TestVM.test(input, expect, 431))

    def test_redeclared_param_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[par(a,integer),par(b,integer),par(a,real)],integer,[])],[]]."""
        expect = """Redeclared identifier: par(a,real)"""
        self.assertTrue(TestVM.test(input, expect, 432))

    def test_redeclared_local(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[],[const(a,7),var(a,real)])],[]]."""
        expect = """Redeclared identifier: var(a,real)"""
        self.assertTrue(TestVM.test(input, expect, 433))

    def test_redeclared_local_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[],[var(a,real),[var(a,integer)]])],[call(writeIntLn,[3])]]."""
        expect = """3\n"""
        self.assertTrue(TestVM.test(input, expect, 434))

    def test_type_mismatch(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeInt,[add(10,true)])]]."""
        expect = """Type mismatch: add(10,true)"""
        self.assertTrue(TestVM.test(input, expect, 435))

    def test_type_mismatch_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(writeBool,[add(10,3)])]]."""
        expect = """Type mismatch: call(writeBool,[add(10,3)])"""
        self.assertTrue(TestVM.test(input, expect, 436))

    def test_type_mismatch_3(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,3),if(a,call(writeInt,[3]))]]."""
        expect = """Type mismatch: if(a,call(writeInt,[3]))"""
        self.assertTrue(TestVM.test(input, expect, 437))

    def test_type_mismatch_4(self):
        print(inspect.currentframe().f_code.co_name)
        input = """
        [[],
        [func(foo,[],float,[assign(foo,3.0)])], 
        [call(writeInt,[call(foo,[])])]]."""
        expect = """Type mismatch: call(writeInt,[call(foo,[])])"""
        self.assertTrue(TestVM.test(input, expect, 438))

    def test_undeclared_id(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,add(b,1)),call(writeIntLn,[a])]]."""
        expect = """Undeclared identifier: b"""
        self.assertTrue(TestVM.test(input, expect, 439))

    def test_undeclared_id_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],
        [proc(foo,[],[var(b,integer),assign(b,1),assign(a,b)])], 
        [call(writeIntLn,[b])]]."""
        expect = """Undeclared identifier: b"""
        self.assertTrue(TestVM.test(input, expect, 440))

    def test_wrong_num_of_args(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[],[])],[call(foo,[1])]]."""
        expect = """Wrong number of arguments: call(foo,[1])"""
        self.assertTrue(TestVM.test(input, expect, 441))

    def test_wrong_num_of_args_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[proc(foo,[par(a,integer)],[])],[call(foo,[])]]."""
        expect = """Wrong number of arguments: call(foo,[])"""
        self.assertTrue(TestVM.test(input, expect, 442))

    def test_wrong_num_of_args_3(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[par(a,integer)],integer,[])],[call(foo,[])]]."""
        expect = """Wrong number of arguments: call(foo,[])"""
        self.assertTrue(TestVM.test(input, expect, 443))
    
    def test_wrong_num_of_args_4(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[par(a,integer)],integer,[])],[call(foo,[1,2])]]."""
        expect = """Wrong number of arguments: call(foo,[1,2])"""
        self.assertTrue(TestVM.test(input, expect, 444))

    def test_invalid_expr(self):
        print(inspect.currentframe().f_code.co_name)
        input = """
        [[var(a,integer)],
        [func(foo,[],integer,[])],
        [assign(a,call(foo,[]))]].
        """
        expect = """Invalid expression: call(foo,[])"""
        self.assertTrue(TestVM.test(input, expect, 445))

    def test_invalid_expr_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[call(writeInt,[a])]]."""
        expect = """Invalid expression: a"""
        self.assertTrue(TestVM.test(input, expect, 446))

    def test_undeclared_func(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,call(foo,[]))]]."""
        expect = """Undeclared function: call(foo,[])"""
        self.assertTrue(TestVM.test(input, expect, 447))

    def test_undeclared_proc(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[call(foo,[])]]."""
        expect = """Undeclared procedure: call(foo,[])"""
        self.assertTrue(TestVM.test(input, expect, 448))

    def test_break_not_in_loop(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[break(null)]]."""
        expect = """Break not in a loop: break(null)"""
        self.assertTrue(TestVM.test(input, expect, 449))

    def test_break_not_in_loop_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[],[],[break(null)])],[do(call(foo,[]),true)]]."""
        expect = """Break not in a loop: break(null)"""
        self.assertTrue(TestVM.test(input, expect, 450))

    def test_continue_not_in_loop(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[],[continue(null)]]."""
        expect = """Continue not in a loop: continue(null)"""
        self.assertTrue(TestVM.test(input, expect, 451))

    def test_continue_not_in_loop_2(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[],[],[continue(null)])],[do(call(foo,[]),true)]]."""
        expect = """Continue not in a loop: continue(null)"""
        self.assertTrue(TestVM.test(input, expect, 452))
    
    def test_assign_to_const(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[const(a,7)],[],[assign(a,8)]]."""
        expect = """Cannot assign to a constant: assign(a,8)"""
        self.assertTrue(TestVM.test(input, expect, 453))

    def test_func_call_expr(self):
        print(inspect.currentframe().f_code.co_name)
        input = """
        [[var(a,integer)],
        [func(foo,[par(a,integer),par(b,integer)], integer,
            [assign(a,add(a,b)),assign(foo,a)])], 
        [assign(a,3),call(writeIntLn,[call(foo,[a,3])]),call(writeIntLn,[a])]]."""
        expect = """6\n3\n"""    
        self.assertTrue(TestVM.test(input, expect, 454))

    def test_proc_call_stmt(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[var(a,integer)],[],[assign(a,3),call(writeIntLn,[a])]]."""
        expect = """3\n"""    
        self.assertTrue(TestVM.test(input, expect, 455))

    def test_return_stmt(self):
        print(inspect.currentframe().f_code.co_name)
        input = """[[],[func(foo,[],integer,[assign(foo,3)])],[call(writeIntLn,[call(foo,[])])]]."""
        expect = """3\n"""    
        self.assertTrue(TestVM.test(input, expect, 456))

    def test_1something(self):
        print(inspect.currentframe().f_code.co_name)
        input = """
        [[var(a,integer)],
        [func(foo,[par(a,integer)],integer,
            [assign(foo,add(a,1))])], 
        [assign(a,call(foo,[1])),call(writeIntLn,[a])]]."""
        expect = """2\n"""    
        self.assertTrue(TestVM.test(input, expect, 457))