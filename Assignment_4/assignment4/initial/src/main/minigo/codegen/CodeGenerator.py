'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from AST import *
from copy import deepcopy

def print_env(env):
    for i, scope in enumerate(env):
        print(f"Scope {i}:")
        for sym in scope:
            print(sym)
                   
class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int
        self.value = value

class CName(Val):
    def __init__(self, value):
        self.value = value

class ClassType(Type): 
    def __init__(self, name):
        #value: Id
        self.name = name
    def __str__(self):
        return "Class{0}".format(self.name)
    def accept(self, v, param): return None
       
class Access():
    def __init__(self, frame, sym, isLeft, isArrayFloat = False):
        #frame: Frame
        #sym: Symbol
        #isLeft: Boolean
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isArrayFloat = isArrayFloat

class CodeGenerator():
    def __init__(self):
        self.libName = "io"
        
    def init(self):
        return [Symbol("getInt", MType([], IntType()), CName(self.libName)),
                Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("getFloat", MType([], FloatType()), CName(self.libName)),
                Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("getBool", MType([], BoolType()), CName(self.libName)),
                Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("getString", MType([], StringType()), CName(self.libName)),
                Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("putLn", MType([], VoidType()), CName(self.libName))]
        
    def gen(self, ast, path):
        gloabl_env = self.init() 
        setup = SetupCodeGen(gloabl_env)
        setup.visit(ast, None) 
        code_gen = CodeGenVisitor(setup.env, path, setup.structTypes, setup.structMethods, setup.interfaceTypes)
        code_gen.visit(ast, None)
          
class SetupCodeGen(BaseVisitor):
    def __init__(self, env):
        self.env = env
        self.className = "MiniGoClass"    
        self.structTypes = {} 
        self.structMethods = {}
        self.interfaceTypes = {}
    
    def visitProgram(self, ast, c): 
        global_env = self.env

        global_ast = [decl for decl in ast.decl if isinstance(decl, (FuncDecl, StructType, InterfaceType, VarDecl, ConstDecl))]
        global_env = reduce(lambda acc,ele: self.visit(ele, acc), global_ast, global_env)

        global_ast = [decl for decl in ast.decl if isinstance(decl, MethodDecl)]
        global_env = reduce(lambda acc,ele: self.visit(ele, acc), global_ast, global_env)
    
        self.env = global_env
        return c

    def visitVarDecl(self, ast, c):
        return c + [Symbol(ast.varName, ast, CName(self.className))]
    
    def visitConstDecl(self, ast, c):
        return c + [Symbol(ast.conName, ast, CName(self.className))]
    
    def visitFuncDecl(self, ast, c): 
        returnType = ast.retType
        paramTypes = [param.parType for param in ast.params]
        if isinstance(returnType, StringType):
            returnType = ClassType("String_MiniGo")
        return c + [Symbol(ast.name, MType(paramTypes, returnType), CName(self.className))]
    
    def visitStructType(self, ast, c): 
        self.structTypes[ast.name] = ast
        return c + [Symbol(ast.name, ClassType(ast.name), CName(self.className))]
    
    def visitInterfaceType(self, ast, c): 
        self.interfaceTypes[ast.name] = ast
        return c + [Symbol(ast.name, ClassType(ast.name), CName(self.className))]
        
    def visitMethodDecl(self, ast, c): 
        structName = ast.recType.name
        if structName not in self.structMethods:
            self.structMethods[structName] = {}
            
        self.structMethods[structName][ast.fun.name] = ast
        return c

class CodeGenVisitor(BaseVisitor):
    def __init__(self, env, path, structTypes, structMethods, interfaceTypes):
        self.className = "MiniGoClass"
        self.env = env 
        self.path = path
        self.emit = Emitter(path + "/" + self.className + ".j")
        self.structTypes = structTypes
        self.structMethods = structMethods
        self.interfaceTypes = interfaceTypes

    def check_array_type(self, arr, type):
        return isinstance(arr, ArrayType) and isinstance(arr.eleType, type)  
     
    def gen_default_constructor(self, strEmitter):
        frame = Frame("<init>", VoidType())
        strEmitter.printout(strEmitter.emitMETHOD("<init>", MType([], VoidType()), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("String_MiniGo"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("String_MiniGo"), 0, frame))
        strEmitter.printout(strEmitter.emitINVOKESPECIAL(frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("String_MiniGo"), 0, frame))
        strEmitter.printout(strEmitter.emitPUSHCONST("\"\"", StringType(), frame))
        strEmitter.printout(strEmitter.emitPUTFIELD("String_MiniGo/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitRETURN(VoidType(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()

    def gen_constructor_with_str_param(self, strEmitter):
        frame = Frame("<init>", VoidType())
        strEmitter.printout(strEmitter.emitMETHOD("<init>", MType([StringType()], VoidType()), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("String_MiniGo"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "str", StringType(), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("String_MiniGo"), 0, frame))
        strEmitter.printout(strEmitter.emitINVOKESPECIAL(frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("String_MiniGo"), 0, frame))
        strEmitter.printout(strEmitter.emitREADVAR("str", StringType(), 1, frame))
        strEmitter.printout(strEmitter.emitPUTFIELD("String_MiniGo/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitRETURN(VoidType(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()

    def gen_compare_method(self, strEmitter):
        frame = Frame("compare", IntType())
        strEmitter.printout(strEmitter.emitMETHOD("compare", MType([ClassType("String_MiniGo")], IntType()), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("String_MiniGo"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "other", ClassType("String_MiniGo"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("String_MiniGo"), 0, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("String_MiniGo/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("other", ClassType("String_MiniGo"), 1, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("String_MiniGo/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitINVOKEVIRTUAL("java/lang/String/compareTo", 
                                                    MType([StringType()], IntType()), frame))
        
        strEmitter.printout(strEmitter.emitRETURN(IntType(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()

    def gen_concat_method(self, strEmitter):
        frame = Frame("concat", ClassType("String_MiniGo"))
        strEmitter.printout(strEmitter.emitMETHOD("concat", MType([ClassType("String_MiniGo")], ClassType("String_MiniGo")), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("String_MiniGo"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "other", ClassType("String_MiniGo"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        
        strEmitter.printout(strEmitter.emitNEW("String_MiniGo", frame))
        strEmitter.printout(strEmitter.emitDUP(frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("String_MiniGo"), 0, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("String_MiniGo/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("other", ClassType("String_MiniGo"), 1, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("String_MiniGo/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitINVOKEVIRTUAL("java/lang/String/concat", 
                                                    MType([StringType()], StringType()), frame))
        
        strEmitter.printout(strEmitter.emitINVOKESPECIAL(frame, "String_MiniGo/<init>", 
                                                    MType([StringType()], VoidType())))
        
        strEmitter.printout(strEmitter.emitRETURN(ClassType("String_MiniGo"), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()

    def gen_toString_method(self, strEmitter):
        frame = Frame("toString", StringType())
        strEmitter.printout(strEmitter.emitMETHOD("toString", MType([], StringType()), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("String_MiniGo"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("String_MiniGo"), 0, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("String_MiniGo/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitRETURN(StringType(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()

    def gen_getValue_method(self, strEmitter):
        frame = Frame("getValue", StringType())
        strEmitter.printout(strEmitter.emitMETHOD("getValue", MType([], StringType()), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("String_MiniGo"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("String_MiniGo"), 0, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("String_MiniGo/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitRETURN(StringType(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()

    def gen_setValue_method(self, strEmitter):
        frame = Frame("setValue", VoidType())
        strEmitter.printout(strEmitter.emitMETHOD("setValue", MType([StringType()], VoidType()), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("String_MiniGo"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "str", StringType(), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("String_MiniGo"), 0, frame))
        strEmitter.printout(strEmitter.emitREADVAR("str", StringType(), 1, frame))
        strEmitter.printout(strEmitter.emitPUTFIELD("String_MiniGo/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitRETURN(VoidType(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()

    def gen_String_MiniGo_type(self):
        goStringFile = self.path + "/String_MiniGo.j"
        strEmitter = Emitter(goStringFile)
        
        strEmitter.printout(strEmitter.emitPROLOG("String_MiniGo", "java/lang/Object"))
        strEmitter.printout(".field private value Ljava/lang/String;\n\n")
        
        self.gen_default_constructor(strEmitter)
        self.gen_constructor_with_str_param(strEmitter)
        self.gen_compare_method(strEmitter)
        self.gen_concat_method(strEmitter)
        self.gen_toString_method(strEmitter)
        self.gen_getValue_method(strEmitter)
        self.gen_setValue_method(strEmitter)
        
        strEmitter.emitEPILOG()
            
    def get_default_val(self, type):
        if isinstance(type, IntType):
            return IntLiteral(0)
        elif isinstance(type, FloatType):
            return FloatLiteral(0.0)
        elif isinstance(type, StringType):
            return StringLiteral("\"\"")
        elif isinstance(type, BoolType):
            return BooleanLiteral(False)
        else:
            return NilLiteral()
    
    def check_same_prototype(self, method, prototype):
        if method.name != prototype.name:
            return False
        if len(method.params) != len(prototype.params):
            return False
        if any(type(p.parType) is not type(q) for p, q in zip(method.params, prototype.params)):
            return False
        if type(method.retType) is not type(prototype.retType):
            return False
        return True

    def get_interface_for_struct(self, struct_name):
        struct_methods = self.structMethods.get(struct_name, {}) 
        interfaces_lst = []

        for interface_name, interface_ast in self.interfaceTypes.items():
            if all(any(method_name == proto.name and self.check_same_prototype(method_def.fun, proto)
                    for method_name, method_def in struct_methods.items())
                for proto in interface_ast.methods):
                interfaces_lst += [interface_name]

        return interfaces_lst
                
    def gen_interface(self, interfaceName):
        interfaceFile = self.path + "/" + interfaceName + ".j"
        interfaceEmit = Emitter(interfaceFile)
        
        interfaceEmit.printout(interfaceEmit.emitPROLOG(interfaceName, "java/lang/Object", isInterface=True))
        
        interfaceEmit.printout(".class public abstract interface " + interfaceName + "\n")
        interfaceEmit.printout(".super java/lang/Object\n\n")
        
        interface_ast = self.interfaceTypes[interfaceName]
        
        for method in interface_ast.methods:
            returnType = method.retType
            if isinstance(returnType, StringType):
                returnType = ClassType("String_MiniGo")
            elif self.check_array_type(returnType, StringType):
                returnType.eleType = ClassType("String_MiniGo")
            paramTypes = []
            for param in method.params:
                type = param
                if isinstance(type, StringType):
                    type = ClassType("String_MiniGo")
                elif self.check_array_type(type, StringType):
                    type.eleType = ClassType("String_MiniGo")
                paramTypes += [type]

            methodType = MType(paramTypes, returnType)
                        
            method_signature = ".method public abstract " + method.name + interfaceEmit.getJVMType(methodType) + "\n"
            interfaceEmit.printout(method_signature)
            
            interfaceEmit.printout(".end method\n\n")
        
        interfaceEmit.emitEPILOG()
          
    def gen_struct(self, structName, fields, methods):
        classFile = self.path + "/" + structName + ".j"
        structEmit = Emitter(classFile)
        
        interfaces_lst = self.get_interface_for_struct(structName)
        structEmit.printout(structEmit.emitPROLOG(structName, "java/lang/Object", interfaces_lst))
        
        for fieldName, fieldType in fields:
            if isinstance(fieldType, StringType):
                fieldType = ClassType("String_MiniGo")
            if self.check_array_type(fieldType, StringType):
                fieldType.eleType = ClassType("String_MiniGo")
            structEmit.printout(structEmit.emitATTRIBUTE(fieldName, fieldType, True, False, None, isStruct=True))
        
        self.gen_struct_constructor(structName, structEmit)
        for method in methods.values():
            self.gen_struct_method(method, structName, structEmit)
        
        structEmit.emitEPILOG()
    
    def gen_struct_constructor(self, structName, structEmit):
        frame = Frame("<init>", VoidType())
        structEmit.printout(structEmit.emitMETHOD("<init>", MType([], VoidType()), False, frame))
        frame.enterScope(True)
        structEmit.printout(structEmit.emitVAR(frame.getNewIndex(), "this", ClassType(structName), frame.getStartLabel(), frame.getEndLabel(), frame))
        structEmit.printout(structEmit.emitLABEL(frame.getStartLabel(), frame))
        structEmit.printout(structEmit.emitREADVAR("this", ClassType(structName), 0, frame))
        structEmit.printout(structEmit.emitINVOKESPECIAL(frame))
        structEmit.printout(structEmit.emitLABEL(frame.getEndLabel(), frame))
        structEmit.printout(structEmit.emitRETURN(VoidType(), frame))
        structEmit.printout(structEmit.emitENDMETHOD(frame))
        frame.exitScope()

    def gen_struct_method(self, method, structName, structEmit): 
        original_emitter = self.emit
        self.emit = structEmit
        original_className = self.className
        self.className = structName
        
        frame = Frame(method.fun.name, method.fun.retType)
        env = {}
        env['env'] = [[]] + [self.env] 
        env['frame'] = frame
        
        ret = method.fun.retType if not isinstance(method.fun.retType, Id) else ClassType(method.fun.retType.name)
        if isinstance(ret, StringType):
            ret = ClassType("String_MiniGo")
        elif self.check_array_type(ret, StringType):
            ret.eleType = ClassType("String_MiniGo")
        intyp = []
        for param in method.fun.params:
            if isinstance(param.parType, Id):
                param.parType = ClassType(param.parType.name)
            if isinstance(param.parType, StringType):
                param.parType = ClassType("String_MiniGo")
            if self.check_array_type(param.parType, StringType):
                param.parType.eleType = ClassType("String_MiniGo")
            intyp += [param.parType]
            
        self.emit.printout(self.emit.emitMETHOD(method.fun.name, MType(intyp, ret), False, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this" , ClassType(structName), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        for param in method.fun.params:
            idx = frame.getNewIndex()
            if isinstance(param.parType, StringType):
                param.parType = ClassType("String_MiniGo")
            self.emit.printout(self.emit.emitVAR(idx, param.parName, param.parType, frame.getStartLabel(), frame.getEndLabel(), frame))
            env['env'][0] = [Symbol(param.parName, param.parType, Index(idx))] + env['env'][0]
        
        env['env'][0] = [Symbol(method.receiver, ClassType(structName), Index(0))] + env['env'][0]
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.visit(method.fun.body, env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        
        if isinstance(method.fun.retType, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
            
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        
        self.emit = original_emitter
        self.className = original_className
    
    def gen_method(self, ast, env, frame): 
        is_init = ast.name == '<init>'
        is_clinit = ast.name == '<clinit>'
        is_main = ast.name == 'main' and len(ast.params) == 0 and ast.retType == VoidType()

        ret_type = self.get_return_type(ast, is_init, is_clinit)
        input_types = self.get_input_types(ast, is_main)

        method_type = MType(input_types, ret_type)
        method_name = '<init>' if is_init else ast.name
        is_struct_type = self.className != 'MiniGoClass'

        self.emit.printout(self.emit.emitMETHOD(method_name, method_type, not is_init if not is_struct_type else False, frame))
        frame.enterScope(True)

        if is_init:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif is_clinit:
            self.generate_clinit_body(env, frame)
        elif is_main:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            self.declare_parameters(ast, env, frame)

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        if is_init:
            self.handle_init_logic(frame)
        if not is_clinit:
            self.visit(ast.body, env)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if isinstance(ret_type, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def get_return_type(self, ast, is_init, is_clinit):
        if is_init or is_clinit:
            return VoidType()
        ret_type = ast.retType if not isinstance(ast.retType, Id) else ClassType(ast.retType.name)
        if isinstance(ret_type, StringType):
            return ClassType("String_MiniGo")
        if self.check_array_type(ret_type, StringType):
            ret_type.eleType = ClassType("String_MiniGo")
        return ret_type

    def get_input_types(self, ast, is_main):
        if is_main:
            return [ArrayType([None], StringType())]
        input_types = [param.parType for param in ast.params]
        for i, param_type in enumerate(input_types):
            if isinstance(param_type, StringType):
                input_types[i] = ClassType("String_MiniGo")
            elif self.check_array_type(param_type, StringType):
                param_type.eleType = ClassType("String_MiniGo")
        return input_types

    def declare_parameters(self, ast, env, frame):
        for param in ast.params:
            idx = frame.getNewIndex()
            if isinstance(param.parType, Id):
                param.parType = ClassType(param.parType.name)
            if isinstance(param.parType, StringType):
                param.parType = ClassType("String_MiniGo")
            if self.check_array_type(param.parType, StringType):
                param.parType.eleType = ClassType("String_MiniGo")
            self.emit.printout(self.emit.emitVAR(idx, param.parName, param.parType, frame.getStartLabel(), frame.getEndLabel(), frame))
            env['env'][0].append(Symbol(param.parName, param.parType, Index(idx)))

    def generate_clinit_body(self, env, frame):
        initialized = {}
        for sym in env['env'][-1]:
            if sym.name in initialized:
                continue
            if isinstance(sym.mtype, VarDecl):
                expr = sym.mtype.varInit if sym.mtype.varInit else self.get_default_val(sym.mtype.varType)
                if isinstance(expr, NilLiteral):
                    initialized[sym.name] = True
                    continue
                code, typ = self.visit(expr, Access(frame, env['env'], False))
                if not sym.mtype.varType:
                    sym.mtype.varType = typ
                if isinstance(sym.mtype.varType, Id):
                    sym.mtype.varType = ClassType(sym.mtype.varType.name)
                code += self.emit.emitPUTSTATIC(f"{self.className}/{sym.name}", sym.mtype.varType, frame)
                self.emit.printout(code)
                initialized[sym.name] = True
            elif isinstance(sym.mtype, ConstDecl):
                code, typ = self.visit(sym.mtype.iniExpr, Access(frame, env['env'], False))
                sym.mtype.conType = typ
                code += self.emit.emitPUTSTATIC(f"{self.className}/{sym.name}", sym.mtype.conType, frame)
                self.emit.printout(code)
                initialized[sym.name] = True

    def handle_init_logic(self, frame):
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
            
    def visitProgram(self, ast, c):
        curr_env = {}
        curr_env['env'] = [self.env]

        self.gen_String_MiniGo_type()
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        for decl in ast.decl:
            if isinstance(decl, (VarDecl, ConstDecl)):
                curr_env = self.visit(decl, curr_env)

        for iface_name, iface_ast in self.interfaceTypes.items():
            self.gen_interface(iface_name)

        for struct_name, struct_def in self.structTypes.items():
            self.gen_struct(struct_name, struct_def.elements, self.structMethods.get(struct_name, {}))

        curr_env['env'] = [[]] + curr_env['env']

        for decl in ast.decl:
            if isinstance(decl, (VarDecl, ConstDecl)):
                decl_name = decl.varName if isinstance(decl, VarDecl) else decl.conName
                matched_sym = next((sym for sym in curr_env['env'][-1]
                    if sym.name == decl_name and not isinstance(sym.mtype, (VarDecl, ConstDecl))),
                    None
                )
                curr_env['env'][0] += [matched_sym]
            elif not isinstance(decl, (StructType, MethodDecl, InterfaceType)):
                curr_env = self.visit(decl, curr_env)

        self.gen_method(FuncDecl("<init>", [], VoidType(), Block([])), curr_env, Frame("<init>", VoidType()))
        self.gen_method(FuncDecl("<clinit>", [], VoidType(), Block([])), curr_env, Frame("<clinit>", VoidType()))

        self.emit.printout(self.emit.emitEPILOG())
        return curr_env

    def visitVarDecl(self, ast, c):
        if 'frame' not in c: 
            if ast.varInit:
                frame_tmp = Frame("<init>", VoidType())
                code_gen, type = self.visit(ast.varInit, Access(frame_tmp, c['env'], False))
                if not ast.varType:
                    ast.varType = type
                if isinstance(ast.varType, StringType):
                    ast.varType = ClassType("String_MiniGo")
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, ""))
            c['env'][0] += [Symbol(ast.varName, ast.varType, CName(self.className))]
        else: 
            frame = c['frame']
            idx = frame.getNewIndex()
            code_gen, type = "", None
            
            if ast.varType and isinstance(ast.varType, ArrayType) and not ast.varInit:
                if isinstance(ast.varType.eleType, StringType):
                    ast.varType.eleType = ClassType("String_MiniGo")
                self.emit.printout(self.emit.emitVAR(idx, ast.varName, ast.varType, 
                                                    frame.getStartLabel(), frame.getEndLabel(), frame))
                
                dims = ast.varType.dimens
                element_type = ast.varType.eleType
                if len(dims) == 1:
                    size = dims[0].value if hasattr(dims[0], 'value') else dims[0]
                    if isinstance(size, Id):
                        size = self.visit(size, Access(frame, c['env'], False))[0]
                        self.emit.printout(size)
                    else:
                        self.emit.printout(self.emit.emitPUSHICONST(size, frame))
                    if isinstance(element_type, (IntType, BoolType, FloatType)):
                        self.emit.printout(self.emit.jvm.emitNEWARRAY(self.emit.getFullType(element_type)))
                    else:
                        self.emit.printout(self.emit.jvm.emitANEWARRAY(self.emit.getFullType(element_type)))
                else:
                    for dim in dims:
                        dim_value = dim.value if hasattr(dim, 'value') else dim
                        if isinstance(dim_value, Id):
                            dim_value = self.visit(dim_value, Access(frame, c['env'], False))[0]
                            self.emit.printout(dim_value)
                        else:
                            self.emit.printout(self.emit.emitPUSHICONST(dim_value, frame))
                    
                    self.emit.printout(self.emit.emitNEWARRAY(ast.varType, frame))
                
                self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, idx, frame))
                c['env'][0] += [Symbol(ast.varName, ast.varType, Index(idx))]
                return c
            
            if ast.varType and isinstance(ast.varType, Id):
                struct_name = ast.varType.name
                ast.varType = ClassType(struct_name)
                isStruct = struct_name in self.structTypes
                self.emit.printout(self.emit.emitVAR(idx, ast.varName, ast.varType, 
                                                    frame.getStartLabel(), frame.getEndLabel(), frame))
                if not isStruct and not ast.varInit:
                    c['env'][0] += [Symbol(ast.varName, ast.varType, Index(idx))]
                    return c
                if ast.varInit:
                    init_code, _ = self.visit(ast.varInit, Access(frame, c['env'], False))
                    self.emit.printout(init_code)
                elif isStruct:
                    self.emit.printout(self.emit.emitNEW(struct_name, frame))
                    self.emit.printout(self.emit.emitDUP(frame))
                    self.emit.printout(self.emit.emitINVOKESPECIAL(frame, f"{struct_name}/<init>", MType([], VoidType())))
                
                self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, idx, frame))
                c['env'][0] += [Symbol(ast.varName, ast.varType, Index(idx))]
                return c
            
            init_val = ast.varInit if ast.varInit else self.get_default_val(ast.varType)
            code_gen, type = "", None
            
            if self.check_array_type(ast.varType, StringType):
                ast.varType.eleType = ClassType("String_MiniGo")
            if not isinstance(init_val, NilLiteral):
                if isinstance(ast.varType, ArrayType) and isinstance(init_val, ArrayLiteral):
                    i2f = (isinstance(ast.varType.eleType, FloatType) and isinstance(init_val.eleType, IntType))
                    code_gen, type = self.visit(init_val, Access(frame, c['env'], False, i2f))
                else:
                    code_gen, type = self.visit(init_val, Access(frame, c['env'], False))
            
            if not ast.varType and not isinstance(type, VoidType):
                if self.check_array_type(type, StringType):
                    type.eleType = ClassType("String_MiniGo")
                ast.varType = type  
            elif isinstance(ast.varType, Id):
                ast.varType = ClassType(ast.varType.name)
            elif isinstance(ast.varType, StringType):
                ast.varType = ClassType("String_MiniGo")
            
            self.emit.printout(self.emit.emitVAR(idx, ast.varName, ast.varType, 
                                                frame.getStartLabel(), frame.getEndLabel(), frame))
            self.emit.printout(code_gen)
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, idx, frame))
            c['env'][0] += [Symbol(ast.varName, ast.varType, Index(idx))]
        return c
    
    def visitConstDecl(self, ast, c):
        if 'frame' not in c: 
            frame_tmp = Frame("<init>", VoidType())
            code_gen, type = self.visit(ast.iniExpr, Access(frame_tmp, c['env'], False))
            ast.conType = type
            self.emit.printout(self.emit.emitATTRIBUTE(ast.conName, ast.conType, True, True, ""))
            c['env'][0] += [Symbol(ast.conName, ast.conType, CName(self.className))]
        else: 
            frame = c['frame']
            idx = frame.getNewIndex()
            code_gen, const_type = self.visit(ast.iniExpr, Access(frame, c['env'], False))
            if self.check_array_type(const_type, StringType):
                const_type.eleType = ClassType("String_MiniGo")
            ast.conType = const_type
            self.emit.printout(self.emit.emitVAR(idx, ast.conName, ast.conType, 
                                                frame.getStartLabel(), frame.getEndLabel(), frame))
            self.emit.printout(code_gen)
            self.emit.printout(self.emit.emitWRITEVAR(ast.conName, ast.conType, idx, frame))
                    
            c['env'][0] = [Symbol(ast.conName, ast.conType, Index(idx))] + c['env'][0]
        return c

    def visitFuncDecl(self, ast, c):
        frame = Frame(ast.name, ast.retType)
        is_main = ast.name == "main"
        c_local = c.copy()
        mtype = None
        
        if is_main:
            mtype = MType([ArrayType([None], StringType())], VoidType())
        else:
            ret = ast.retType if not isinstance(ast.retType, Id) else ClassType(ast.retType.name)
            if isinstance(ret, StringType):
                ret = ClassType("String_MiniGo")
            elif self.check_array_type(ret, StringType):
                ret.eleType = ClassType("String_MiniGo")
            params = []
            for param in ast.params:
                if isinstance(param.parType, Id):
                    param.parType = ClassType(param.parType.name)
                if isinstance(param.parType, StringType):
                    param.parType = ClassType("String_MiniGo")
                params += [param.parType]
            mtype = MType(params, ret)
        c_local['env'][0] += [Symbol(ast.name, mtype, CName(self.className))]
        c_local['frame'] = frame
        c_local['env'] = [[]] + c_local['env']
        self.gen_method(ast, c_local, frame)
        c['frame'] = frame        
        return c
    
    def visitParamDecl(self, ast, c):
        idx = c['frame'].getNewIndex()
        c['env'][0] = [Symbol(ast.parName, ast.parType, Index(idx))] + o['env'][0]
        return idx

    def visitBlock(self, ast, c):
        env = c.copy()
        frame = env['frame']
        env['env'] = [[]] + env['env'] 
        frame.enterScope(False) 
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        for stmt in ast.member:
            if isinstance(stmt, (VarDecl, ConstDecl)):
                self.visit(stmt, env)
            elif isinstance(stmt, Assign):
                assign_code, assign_type = self.visit(stmt, env)
                self.emit.printout(assign_code)
            elif isinstance(stmt, MethCall):
                code, _ = self.visit(stmt, env)
                self.emit.printout(code)
            else:
                env = self.visit(stmt, env)                
                if isinstance(env, tuple): 
                    frame_tmp = env[0]['frame']
                    env_tmp = env[0]['env']
                    env = {'env': env_tmp, 'frame': frame_tmp}
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
    
    def visitAssign(self, ast, c):
        frame = c['frame']
        env = c['env']
        if isinstance(ast.lhs, ArrayCell):
            rc, rt = self.visit(ast.rhs, Access(frame, env, False))
            lc, lt = self.visit(ast.lhs, Access(frame, env, True))
            if isinstance(lt, FloatType) and isinstance(rt, IntType):
                rc += self.emit.emitI2F(frame)
            
            if isinstance(rt, ArrayType):
                store_code = self.emit.emitASTORE(rt, frame)
                return lc + rc + store_code, VoidType()
            store_code = self.emit.emitASTORE(lt, frame) 
            
            return lc + rc + store_code, VoidType()

        if isinstance(ast.lhs, FieldAccess): 
            rc, rt = self.visit(ast.rhs, Access(frame, env, False))
            lc, lt = self.visit(ast.lhs, Access(frame, env, True))
            lst_codes = lc.split('\n')
            if isinstance(rt, ClassType) and rt.name == "String_MiniGo":
                rc, rt = self.visit(ast.rhs, Access(frame, env, False))
                lc, lt = self.visit(ast.lhs, Access(frame, env, False))
                lst_codes = lc.split('\n')
                struct_name = lst_codes[1].split(' ')[1].split('/')[0]
                get_field = self.emit.emitGETFIELD(f"{struct_name}/{ast.lhs.field}", rt, frame)
                get_val = self.emit.emitINVOKEVIRTUAL(f"{rt.name}/getValue", MType([], StringType()), frame)
                set_val = self.emit.emitINVOKEVIRTUAL(f"{rt.name}/setValue", MType([StringType()], VoidType()), frame)
                return lst_codes[0] + "\n " + get_field + "\n" + rc + "\n" + get_val + "\n" + set_val + "\n", VoidType()
            load = lst_codes[0]
            store = lst_codes[1]
            return load + "\n" + rc + "\n" + store + "\n", VoidType()
            
        rc, rt = self.visit(ast.rhs, Access(frame, env, False))
        
        flag = False
        if isinstance(ast.lhs, Id):
            ret = self.visit(ast.lhs, Access(frame, env, False))
            flag_1 = ret is not None            
            flag_2 = any(sym.name == ast.lhs.name for scope in env[:-1] for sym in scope)
            flag = flag_1 and flag_2
        if not flag and isinstance(ast.lhs, Id): 
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, ast.lhs.name, rt, 
                                                frame.getStartLabel(), frame.getEndLabel(), frame))
            env[0] += [Symbol(ast.lhs.name, rt, Index(idx))]
            code = self.emit.emitWRITEVAR(ast.lhs.name, rt, idx, frame)
            return rc + code, rt
        else: 
            lc, lt = self.visit(ast.lhs, Access(frame, env, True))
            if isinstance(lt, ArrayType) and isinstance(rt, ArrayType):
                i2f = (isinstance(lt.eleType, FloatType) and isinstance(rt.eleType, IntType))
                rc, rt = self.visit(ast.rhs, Access(frame, env, False, i2f))
                return rc + lc, VoidType()
            if isinstance(lt, ClassType) and lt.name == "String_MiniGo":
                lc, _ = self.visit(ast.lhs, Access(frame, env, False))
                rc, rt = self.visit(ast.rhs, Access(frame, env, False))
                get_val = self.emit.emitINVOKEVIRTUAL(f"{lt.name}/getValue", MType([], StringType()), frame)
                set_val = self.emit.emitINVOKEVIRTUAL(f"{lt.name}/setValue", MType([StringType()], VoidType()), frame)
                return lc + rc  + get_val + set_val, VoidType()
            if isinstance(lt, FloatType) and isinstance(rt, IntType):
                rc += self.emit.emitI2F(frame)
                
            return rc + lc, VoidType()
           
    def visitIf(self, ast, c):
        frame = c['frame']
        env = c['env']
        
        cond_code, _ = self.visit(ast.expr, Access(frame, env, False))
        self.emit.printout(cond_code)
        
        falseLabel = frame.getNewLabel()
        endLabel = frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(falseLabel, frame))
        
        if isinstance(ast.thenStmt, Block):
            blockLabel = frame.getNewLabel()
            self.emit.printout(self.emit.emitLABEL(blockLabel, frame))
            self.visit(ast.thenStmt, c)
        else:
            self.visit(ast.thenStmt, c)
        
        if ast.elseStmt:
            self.emit.printout(self.emit.emitGOTO(endLabel, frame))
            self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
            
            if isinstance(ast.elseStmt, If):
                self.visit(ast.elseStmt, c)
            elif isinstance(ast.elseStmt, Block):
                blockLabel = frame.getNewLabel()
                self.emit.printout(self.emit.emitLABEL(blockLabel, frame))
                self.visit(ast.elseStmt, c)
            else:
                self.visit(ast.elseStmt, c)
            
            self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        else:
            self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
            self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        
        return c

    def visitForBasic(self, ast, c):
        frame = c['frame']
        env = c['env']
        
        frame.enterLoop()
        
        continueLabel = frame.getContinueLabel()
        breakLabel = frame.getBreakLabel()
        
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
        
        cond_code, _ = self.visit(ast.cond, Access(frame, env, False))
        self.emit.printout(cond_code)
        self.emit.printout(self.emit.emitIFFALSE(breakLabel, frame))
        
        self.visit(ast.loop, c)
        
        self.emit.printout(self.emit.emitGOTO(continueLabel, frame))
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))
        
        frame.exitLoop()
        return c
     
    def visitForStep(self, ast, c):
        frame = c['frame']
        
        frame.enterLoop()
        
        loop_start_label = frame.getNewLabel()
        loop_end_label = frame.getNewLabel()
        cond_label = frame.getNewLabel()
        body_label = frame.getNewLabel()
        update_label = frame.getContinueLabel()
        end_label = frame.getBreakLabel()
        
        loop_env = {}
        loop_env['frame'] = frame
        loop_env['env'] = [[]] + c['env']
        
        self.emit.printout(self.emit.emitLABEL(loop_start_label, frame))
        name_i = ast.init.varName if isinstance(ast.init, VarDecl) else ast.init.lhs.name
        if isinstance(ast.init, VarDecl):
            rc, rt = self.visit(ast.init.varInit, Access(frame, loop_env, False))
            ast.init.varType = rt
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, name_i, rt, loop_start_label, loop_end_label, frame))
            loop_env['env'][0] += [Symbol(name_i, rt, Index(idx))]
            code = self.emit.emitWRITEVAR(name_i, rt, idx, frame)
            self.emit.printout(rc + code)
        else:
            rc, rt = self.visit(ast.init.rhs, Access(frame, loop_env, False))
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, name_i, rt, loop_start_label, loop_end_label, frame))
            loop_env['env'][0] += [Symbol(name_i, rt, Index(idx))]
            code = self.emit.emitWRITEVAR(name_i, rt, idx, frame)
            self.emit.printout(rc + code)
            
        self.emit.printout(self.emit.emitLABEL(cond_label, frame))
        cond_code, _ = self.visit(ast.cond, Access(frame, loop_env['env'], False))
        self.emit.printout(cond_code)
        self.emit.printout(self.emit.emitIFFALSE(end_label, frame))
        self.emit.printout(self.emit.emitGOTO(body_label, frame))
        
        self.emit.printout(self.emit.emitLABEL(update_label, frame))
        update_code, _ = self.visit(ast.upda, loop_env)  
        self.emit.printout(update_code)
        self.emit.printout(self.emit.emitGOTO(cond_label, frame))
        
        self.emit.printout(self.emit.emitLABEL(body_label, frame))
        
        if isinstance(ast.loop, Block):
            self.visit(ast.loop, loop_env)
        
        self.emit.printout(self.emit.emitGOTO(update_label, frame))
        
        self.emit.printout(self.emit.emitLABEL(end_label, frame))
        self.emit.printout(self.emit.emitLABEL(loop_end_label, frame))
        
        frame.exitLoop()
        return c

    def visitForEach(self, ast, c):
        return c

    def visitBreak(self, ast, c):
        frame = c['frame']
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))
        return c

    def visitContinue(self, ast, c):
        frame = c['frame']
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))
        return c
        
    def visitReturn(self, ast, c):
        frame = c['frame']
        env = c['env']
        result = []
        
        if ast.expr:
            expr_code, expr_type = self.visit(ast.expr, Access(frame, env, False))
            result += [expr_code]
            if isinstance(frame.returnType, FloatType) and isinstance(expr_type, IntType):
                result += [self.emit.emitI2F(frame)]
            if isinstance(frame.returnType, Id):
                frame.returnType = ClassType(frame.returnType.name)
            result += [self.emit.emitRETURN(frame.returnType, frame)]
            self.emit.printout(''.join(result))

    def visitFieldAccess(self, ast, c):
        frame = c.frame
        env = c.sym
        isLeft = c.isLeft
        
        rec_code, rec_type = self.visit(ast.receiver, Access(frame, env, False))
        
        struct_name = rec_type.name if isinstance(rec_type, ClassType) else rec_type.name
        field_type = None
        
        if struct_name in self.structTypes:
            struct_def = self.structTypes[struct_name]
            field_pair = next(((field_name, field_type) for field_name, field_type in struct_def.elements if field_name == ast.field), None)
            if field_pair:
                field_type = field_pair[1]
                if isinstance(field_type, StringType):
                    field_type = ClassType("String_MiniGo")
                if self.check_array_type(field_type, StringType):
                    field_type.eleType = ClassType("String_MiniGo")
        
        if isLeft:
            return rec_code + self.emit.emitPUTFIELD(f"{struct_name}/{ast.field}", field_type, frame), field_type
        else:  
            return rec_code + self.emit.emitGETFIELD(f"{struct_name}/{ast.field}", field_type, frame), field_type

    def visitArrayCell(self, ast, c):
        frame = c.frame
        env = c.sym
        is_left = c.isLeft
        
        array_code, array_type = self.visit(ast.arr, Access(frame, env, False))
        current_type = array_type
        if isinstance(current_type.eleType, StringType):
            current_type.eleType = ClassType("String_MiniGo")
        
        code_parts = [array_code]
        for i, idx in enumerate(ast.idx):
            idx_code, _ = self.visit(idx, Access(frame, env, False))
            code_parts += [idx_code]
            if i < len(ast.idx) - 1:
                code_parts += [self.emit.emitALOAD(current_type, frame)]
        
        result_type = current_type.eleType if isinstance(current_type, ArrayType) else current_type
        if not is_left:
            code_parts += [self.emit.emitALOAD(result_type, frame)]
        
        return ''.join(code_parts), result_type

    def visitBinaryOp(self, ast, c):
        frame = c.frame
        env = c.sym

        left_code, left_type = self.visit(ast.left, Access(frame, env, False))
        right_code, right_type = self.visit(ast.right, Access(frame, env, False))
        
        result_type = left_type
        if isinstance(left_type, FloatType) or isinstance(right_type, FloatType):
            result_type = FloatType()
            if isinstance(left_type, IntType):
                left_code += self.emit.emitI2F(frame)
            if isinstance(right_type, IntType):
                right_code += self.emit.emitI2F(frame)
                
        op_code_dict = {
            '+': lambda: self.emit.emitINVOKEVIRTUAL("String_MiniGo/concat", MType([ClassType("String_MiniGo")], ClassType("String_MiniGo")), frame)
                if result_type == ClassType("String_MiniGo") else self.emit.emitADDOP('+', result_type, frame),
            '-': lambda: self.emit.emitADDOP('-', result_type, frame),
            '*': lambda: self.emit.emitMULOP('*', result_type, frame),
            '/': lambda: self.emit.emitMULOP('/', result_type, frame),
            '%': lambda: self.emit.emitMOD(frame),
            '==': lambda: self.emit.emitREOP('==', left_type, frame),
            '!=': lambda: self.emit.emitREOP('!=', left_type, frame),
            '<': lambda: self.emit.emitREOP('<', left_type, frame),
            '<=': lambda: self.emit.emitREOP('<=', left_type, frame),
            '>': lambda: self.emit.emitREOP('>', left_type, frame),
            '>=': lambda: self.emit.emitREOP('>=', left_type, frame),
            '&&': lambda: self.emit.emitANDOP(frame),
            '||': lambda: self.emit.emitOROP(frame),
        }
        op_code = op_code_dict.get(ast.op, lambda: "")()
        if ast.op in ['==', '!=', '<', '<=', '>', '>=', '&&', '||']:
            result_type = BoolType()
        
        return left_code + right_code + op_code, result_type

    def visitUnaryOp(self, ast, c):
        frame = c.frame
        env = c.sym
        
        body_code, body_type = self.visit(ast.body, Access(frame, env, False))
        if ast.op == '-':
            return body_code + self.emit.emitNEGOP(body_type, frame), body_type
        elif ast.op == '!':
            return body_code + self.emit.emitNOT(body_type, frame), BoolType()
            
        return body_code, body_type

    def visitFuncCall(self, ast, c):
        frame = c['frame'] if isinstance(c, dict) else c.frame
        env = c['env'] if isinstance(c, dict) else c.sym
        if ast.funName in ["getInt", "getFloat", "getBool", "getString"]:
            func_sym = next((s for s in env[-1] if s.name == ast.funName), None)
            ret_type = func_sym.mtype.rettype
            default_val = self.get_default_val(ret_type)
            code, ret_type = self.visit(default_val, Access(frame, env, False))
            return code, ret_type
        func_sym = next((sym for scope in env for sym in scope if sym.name == ast.funName), None)
        args_code = ""
        for arg in ast.args:
            arg_code, arg_type = self.visit(arg, Access(frame, env, False, False))
            if isinstance(arg_type, ClassType) and arg_type.name == "String_MiniGo" and (ast.funName == "putString" or ast.funName =="putStringLn"): arg_code += self.emit.emitINVOKEVIRTUAL("String_MiniGo/getValue", MType([], StringType()), frame)
            args_code += arg_code
            if len(func_sym.mtype.partype) > 0 and isinstance(func_sym.mtype.partype[0], FloatType) and isinstance(arg_type, IntType):
                args_code += self.emit.emitI2F(frame)
        
        if ast.funName in ["putString", "putStringLn"]:
            call_code = self.emit.emitINVOKESTATIC(
                f"{func_sym.value.value}/{ast.funName}", func_sym.mtype, frame)
        else:
            for i, t in enumerate(func_sym.mtype.partype):
                if isinstance(t, StringType):
                    func_sym.mtype.partype[i] = ClassType("String_MiniGo")
            call_code = self.emit.emitINVOKESTATIC(
                f"{func_sym.value.value}/{ast.funName}", func_sym.mtype, frame)
        if isinstance(func_sym.mtype.rettype, VoidType):
            self.emit.printout(args_code + call_code)
        elif ast.funName in ["getInt", "getFloat", "getBool", "getString"]:
            return c
        if isinstance(c, dict) and isinstance(func_sym.mtype.rettype, VoidType):
            frame = c['frame']
            env = c['env']
            return {'env': env, 'frame': frame}
        else:
            return (args_code + call_code, func_sym.mtype.rettype)

    def visitMethCall(self, ast, c):
        frame = c['frame'] if isinstance(c, dict) else c.frame
        env = c['env'] if isinstance(c, dict) else c.sym
        rec_code, rec_type = self.visit(ast.receiver, Access(frame, env, False))
        
        struct_name = rec_type.name
        is_struct = struct_name in self.structTypes
        
        method = None
        if is_struct:
            methods = self.structMethods[struct_name]
            method = methods.get(ast.metName)
        else:
            interface_type = self.interfaceTypes[struct_name]
            method = next((proto for proto in interface_type.methods if proto.name == ast.metName), None)
        
        args_code = rec_code
        for arg in ast.args:
            arg_code, _ = self.visit(arg, Access(frame, env, False))
            args_code += arg_code
        
        params = method.fun.params if is_struct else method.params
        return_type = method.fun.retType if is_struct else method.retType
        
        param_types = []
        for param in params:
            param_type = param.parType if is_struct else param
            if isinstance(param_type, StringType):
                param_types.append(ClassType("String_MiniGo"))
            elif self.check_array_type(param_type, StringType):
                param_types.append(ArrayType(param_type.dimens, ClassType("String_MiniGo")))
            else:
                param_types.append(param_type)
        
        if isinstance(return_type, StringType):
            return_type = ClassType("String_MiniGo")
        elif self.check_array_type(return_type, StringType):
            return_type = ArrayType(return_type.dimens, ClassType("String_MiniGo"))
        
        method_type = MType(param_types, return_type)
        call_code = (self.emit.emitINVOKEVIRTUAL(f"{struct_name}/{ast.metName}", method_type, frame)
                    if is_struct else
                    self.emit.emitINVOKEINTERFACE(f"{struct_name}/{ast.metName}", method_type, frame, len(params) + 1))
        
        return args_code + call_code, return_type

    def visitArrayLiteral(self, ast, c):
        frame = c.frame
        env = c.sym
        isArrayFloat = c.isArrayFloat
        result = []
        if isinstance(ast.eleType, IntType) and isArrayFloat:
                ast.eleType = FloatType()
        if isinstance(ast.eleType, StringType):
            ast.eleType = ClassType("String_MiniGo")
        for dim in ast.dimens:
            dim_code, _ = self.visit(dim, Access(frame, env, False))
            result += [dim_code]
        
        if len(ast.dimens) > 1:
            array_type = ArrayType(ast.dimens, ast.eleType)
            result += [self.emit.emitNEWARRAY(array_type, frame)]
        else:
            if isinstance(ast.eleType, (IntType, FloatType, BoolType)):
                result += [self.emit.jvm.emitNEWARRAY(self.emit.getFullType(ast.eleType))]
            else:
                result += [self.emit.emitNEWARRAY(ast, frame)]
        
        def init_nested_array(values, current_indices=[]):
            if not isinstance(values, list):
                result.append(self.emit.jvm.emitDUP())
                
                for i, idx in enumerate(current_indices[:-1]):
                    result.append(self.emit.emitPUSHICONST(idx, frame))
                    result.append(self.emit.jvm.emitAALOAD())
                
                result.append(self.emit.emitPUSHICONST(current_indices[-1], frame))
                
                val_code, val_type = self.visit(values, Access(frame, env, False))
                result.append(val_code)
                
                if isinstance(ast.eleType, FloatType) and isinstance(val_type, IntType):
                    result.append(self.emit.emitI2F(frame))
                
                if isinstance(ast.eleType, IntType):
                    result.append(self.emit.jvm.emitIASTORE())
                elif isinstance(ast.eleType, BoolType):
                    result.append(self.emit.jvm.emitBASTORE())
                elif isinstance(ast.eleType, FloatType):
                    result.append(self.emit.jvm.emitFASTORE())
                elif isinstance(ast.eleType, (StringType, ArrayType, ClassType)):
                    result.append(self.emit.jvm.emitAASTORE())
                else:
                    result.append(self.emit.jvm.emitAASTORE())
                return
            
            for i, item in enumerate(values):
                init_nested_array(item, current_indices + [i])
        
        init_nested_array(ast.value)
        
        return ''.join(result), ArrayType(ast.dimens, ast.eleType)

    def visitStructLiteral(self, ast, c):
        frame = c.frame
        env = c.sym
        result = []
        result += [self.emit.emitNEW(ast.name, frame), 
                   self.emit.emitDUP(frame),
                   self.emit.emitINVOKESPECIAL(frame, f"{ast.name}/<init>", MType([], VoidType()))]
        
        initialized_fields = {field_name: field_expr for field_name, field_expr in ast.elements}
        if ast.name in self.structTypes:
            struct_def = self.structTypes[ast.name]
            
            for field_name, field_type in struct_def.elements:
                if field_name not in initialized_fields:
                    if isinstance(field_type, (Id, ArrayType)):
                        continue
                    
                    result += [self.emit.emitDUP(frame)]
                    
                    default_val = self.get_default_val(field_type)
                    default_code, _ = self.visit(default_val, Access(frame, env, False))
                    result += [default_code]
                    
                    if isinstance(field_type, Id):
                        field_type = ClassType(field_type.name)
                    if isinstance(field_type, StringType):
                        field_type = ClassType("String_MiniGo")
                        
                    result += [self.emit.emitPUTFIELD(f"{ast.name}/{field_name}", field_type, frame)]
                else:
                    result += [self.emit.emitDUP(frame)]
                    expr_code, expr_type = self.visit(initialized_fields[field_name], Access(frame, env, False))
                    result += [expr_code]
                    
                    if isinstance(field_type, FloatType) and isinstance(expr_type, IntType):
                        result += [self.emit.emitI2F(frame)]
                    if isinstance(field_type, Id):
                        field_type = ClassType(field_type.name)
                    if isinstance(field_type, StringType):
                        result += [self.emit.emitPUTFIELD(f"{ast.name}/{field_name}",ClassType("String_MiniGo"), frame)]
                        continue
                    result += [self.emit.emitPUTFIELD(f"{ast.name}/{field_name}", field_type, frame)]
            
        return ''.join(result), ClassType(ast.name)

    def visitIntLiteral(self, ast, c):
        val = ast.value
        if isinstance(val, str):
            if val.startswith("0b") or val.startswith("0B"):
                val = int(val, 2)
            elif val.startswith("0o") or val.startswith("0O"):
                val = int(val, 8)
            elif val.startswith("0x") or val.startswith("0X"):
                val = int(val, 16)
        return self.emit.emitPUSHICONST(val, c.frame), IntType()

    def visitFloatLiteral(self, ast, c):
        return self.emit.emitPUSHFCONST(str(ast.value), c.frame), FloatType()

    def visitStringLiteral(self, ast, c):
        frame = c.frame
        result = []
        result += [self.emit.emitNEW("String_MiniGo", frame),
                self.emit.emitDUP(frame),
                self.emit.emitPUSHCONST(ast.value, StringType(), frame),
                self.emit.emitINVOKESPECIAL(frame, "String_MiniGo/<init>", MType([StringType()], VoidType()))]
        return ''.join(result), ClassType("String_MiniGo")

    def visitBooleanLiteral(self, ast, c):
        value = ast.value
        if isinstance(value, str):
            value = value.lower() == 'true'
        return self.emit.emitPUSHICONST(1 if value else 0, c.frame), BoolType()

    def visitNilLiteral(self, ast, c):
        return self.emit.jvm.emitPUSHNULL(), VoidType()

    def visitId(self, ast, c):
        frame = c.frame
        env = c.sym
        isLeft = c.isLeft
        for scope in env:
            for sym in scope:
                if sym.name == ast.name and not isinstance(sym.mtype, (VarDecl, ConstDecl)):
                    if isinstance(sym.mtype, Id):
                        sym.mtype = ClassType(sym.mtype.name)

                    if isLeft:
                        if isinstance(sym.value, Index):
                            return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, frame), sym.mtype
                        else:
                            return self.emit.emitPUTSTATIC(f"{sym.value.value}/{sym.name}", sym.mtype, frame), sym.mtype
                    else:  
                        if isinstance(sym.value, Index):
                            return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, frame), sym.mtype
                        else:
                            return self.emit.emitGETSTATIC(f"{sym.value.value}/{sym.name}", sym.mtype, frame), sym.mtype

    def visitStructType(self, ast, c): pass