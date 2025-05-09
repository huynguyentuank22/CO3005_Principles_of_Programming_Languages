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

FRAME = 'frame'
ENV = 'env'
ACCESS = 'access'

def printSymbolList(symbols):
    for i, scope in enumerate(symbols):
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
    
class SubBody():
    def __init__(self, frame, sym):
        # frame: Frame
        # sym: list[Symbol]
        self.frame = frame
        self.sym = sym
        

class Access():
    def __init__(self, frame, sym, isLeft, isArrayFloat = False):
        #frame: Frame
        #sym: Symbol
        #isLeft: Boolean
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isArrayFloat = isArrayFloat
        
class PreCodeGen(BaseVisitor):
    def __init__(self, astTree, env):
        self.astTree = astTree
        self.env = env
        self.className = "MiniGoClass"    
        self.structTypes = {} 
        self.structMethods = {}
        self.interfaceTypes = {}
    
    def visitProgram(self, ast, c): 
        e = SubBody(None, self.env)
        for decl in ast.decl:
            if isinstance(decl, FuncDecl) or isinstance(decl, StructType) or isinstance(decl, InterfaceType) or isinstance(decl, VarDecl) or isinstance(decl, ConstDecl):
                e = self.visit(decl, e)
        
        for decl in ast.decl:
            if isinstance(decl, MethodDecl):
                e = self.visit(decl, e)
    
        self.env = e.sym
        return c

    def visitVarDecl(self, ast, c):
        c.sym += [Symbol(ast.varName, ast, CName(self.className))]
        return c
    def visitConstDecl(self, ast, c):
        c.sym += [Symbol(ast.conName, ast, CName(self.className))]
        return c
    
    def visitFuncDecl(self, ast, c): 
        returnType = ast.retType
        paramTypes = [param.parType for param in ast.params]
        if isinstance(returnType, StringType):
            returnType = ClassType("GoString")
        c.sym += [Symbol(ast.name, MType(paramTypes, returnType), CName(self.className))]
        return c
    
    def visitStructType(self, ast, c): 
        self.structTypes[ast.name] = ast
        c.sym += [Symbol(ast.name, ClassType(ast.name), CName(self.className))]
        return c
    
    def visitInterfaceType(self, ast, c): 
        self.interfaceTypes[ast.name] = ast
        c.sym += [Symbol(ast.name, ClassType(ast.name), CName(self.className))]
        return c
        
    def visitMethodDecl(self, ast, c): 
        structName = ast.recType.name
        if structName not in self.structMethods:
            self.structMethods[structName] = {}
            
        self.structMethods[structName][ast.fun.name] = ast
        return c
    
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
        gl = self.init() 
        preprocess = PreCodeGen(ast, gl)
        preprocess.visit(ast, None) 
        gc = CodeGenVisitor(ast, preprocess.env, path, preprocess.structTypes, preprocess.structMethods, preprocess.interfaceTypes)
        gc.visit(ast, None)

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path, structTypes, structMethods, interfaceTypes):
        self.className = "MiniGoClass"
        self.astTree = astTree
        self.env = env 
        self.path = path
        self.emit = Emitter(path + "/" + self.className + ".j")
        self.structTypes = structTypes
        self.structMethods = structMethods
        self.interfaceTypes = interfaceTypes

    def isReferenceType(self, typ):
        return (isinstance(typ, StringType) or isinstance(typ, ClassType) or isinstance(typ, ArrayType))
        
    def gen_default_constructor(self, strEmitter):
        frame = Frame("<init>", VoidType())
        strEmitter.printout(strEmitter.emitMETHOD("<init>", MType([], VoidType()), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitINVOKESPECIAL(frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitPUSHCONST("\"\"", StringType(), frame))
        strEmitter.printout(strEmitter.emitPUTFIELD("GoString/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitRETURN(VoidType(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()

    def gen_constructor_with_str_param(self, strEmitter):
        frame = Frame("<init>", VoidType())
        strEmitter.printout(strEmitter.emitMETHOD("<init>", MType([StringType()], VoidType()), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "str", StringType(), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitINVOKESPECIAL(frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitREADVAR("str", StringType(), 1, frame))
        strEmitter.printout(strEmitter.emitPUTFIELD("GoString/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitRETURN(VoidType(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()

    def gen_compare_method(self, strEmitter):
        frame = Frame("compare", IntType())
        strEmitter.printout(strEmitter.emitMETHOD("compare", MType([ClassType("GoString")], IntType()), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "other", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("GoString/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("other", ClassType("GoString"), 1, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("GoString/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitINVOKEVIRTUAL("java/lang/String/compareTo", 
                                                    MType([StringType()], IntType()), frame))
        
        strEmitter.printout(strEmitter.emitRETURN(IntType(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()

    def gen_concat_method(self, strEmitter):
        frame = Frame("concat", ClassType("GoString"))
        strEmitter.printout(strEmitter.emitMETHOD("concat", MType([ClassType("GoString")], ClassType("GoString")), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "other", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        
        strEmitter.printout(strEmitter.emitNEW("GoString", frame))
        strEmitter.printout(strEmitter.emitDUP(frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("GoString/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("other", ClassType("GoString"), 1, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("GoString/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitINVOKEVIRTUAL("java/lang/String/concat", 
                                                    MType([StringType()], StringType()), frame))
        
        strEmitter.printout(strEmitter.emitINVOKESPECIAL(frame, "GoString/<init>", 
                                                    MType([StringType()], VoidType())))
        
        strEmitter.printout(strEmitter.emitRETURN(ClassType("GoString"), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()

    def gen_toString_method(self, strEmitter):
        frame = Frame("toString", StringType())
        strEmitter.printout(strEmitter.emitMETHOD("toString", MType([], StringType()), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("GoString/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitRETURN(StringType(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()

    def gen_getValue_method(self, strEmitter):
        frame = Frame("getValue", StringType())
        strEmitter.printout(strEmitter.emitMETHOD("getValue", MType([], StringType()), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("GoString/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitRETURN(StringType(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()

    def gen_setValue_method(self, strEmitter):
        frame = Frame("setValue", VoidType())
        strEmitter.printout(strEmitter.emitMETHOD("setValue", MType([StringType()], VoidType()), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "str", StringType(), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitREADVAR("str", StringType(), 1, frame))
        strEmitter.printout(strEmitter.emitPUTFIELD("GoString/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitRETURN(VoidType(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()

    def genGoStringType(self):
        goStringFile = self.path + "/GoString.j"
        strEmitter = Emitter(goStringFile)
        
        strEmitter.printout(strEmitter.emitPROLOG("GoString", "java/lang/Object"))
        strEmitter.printout(".field private value Ljava/lang/String;\n\n")
        
        self.gen_default_constructor(strEmitter)
        self.gen_constructor_with_str_param(strEmitter)
        self.gen_compare_method(strEmitter)
        self.gen_concat_method(strEmitter)
        self.gen_toString_method(strEmitter)
        self.gen_getValue_method(strEmitter)
        self.gen_setValue_method(strEmitter)
        
        strEmitter.emitEPILOG()
        
    def inferValueConstant(self, ast): 
        if isinstance(ast, IntLiteral):
            if isinstance(ast.value, str):
                if ast.value.startswith("0b") or ast.value.startswith("0B"):
                    return int(ast.value, 2)
                elif ast.value.startswith("0o") or ast.value.startswith("0O"):
                    return int(ast.value, 8)
                elif ast.value.startswith("0x") or ast.value.startswith("0X"):
                    return int(ast.value, 16)
                return int(ast.value)
            return int(ast.value)
        elif isinstance(ast, (FloatLiteral, StringLiteral, BooleanLiteral)):
            return ast.value
        elif isinstance(ast, ArrayLiteral):
            return [self.inferValueConstant(x) for x in ast.value]
        elif isinstance(ast, BinaryOp):
            left = self.inferValueConstant(ast.left)
            right = self.inferValueConstant(ast.right)
            op_dict = { '+': lambda x, y: x + y,
                        '-': lambda x, y: x - y,
                        '*': lambda x, y: x * y,
                        '/': lambda x, y: x / y,
                        '%': lambda x, y: x % y,
                        '==': lambda x, y: x == y,
                        '!=': lambda x, y: x != y,
                        '<': lambda x, y: x < y,
                        '<=': lambda x, y: x <= y,
                        '>': lambda x, y: x > y,
                        '>=': lambda x, y: x >= y }
            if ast.op in op_dict:
                return op_dict[ast.op](left, right)
        elif isinstance(ast, UnaryOp):
            value = self.inferValueConstant(ast.body)
            if ast.op == '-':
                return -value
            elif ast.op == '!':
                return not value
            
    def getDefaultValue(self, type):
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
    
    def checkPrototype(self, method, prototype):
        if method.name != prototype.name: return False
        if len(method.params) != len(prototype.params): return False
        for p, q in zip(method.params, prototype.params):
            if not type(p.parType) is type(q): return False
        if not type(method.retType) is type(prototype.retType): return False
        return True

    def getInterfaceForStruct(self, structName):
        structMethods = self.structMethods.get(structName, {}) 
        implemented_interfaces = []
        for interfaceName, interface_ast in self.interfaceTypes.items():
            lst_prototype = interface_ast.methods 
            flag = False
            for prototype in lst_prototype:
                for methodName, method in structMethods.items():
                    if methodName == prototype.name and not self.checkPrototype(method.fun, prototype):
                        flag = True
                        break
                if flag: break
            if not flag:
                implemented_interfaces += [interfaceName]
        return implemented_interfaces
                
    def genInterface(self, interfaceName):
        interfaceFile = self.path + "/" + interfaceName + ".j"
        interfaceEmit = Emitter(interfaceFile)
        
        interfaceEmit.printout(interfaceEmit.emitPROLOG(interfaceName, "java/lang/Object", isInterface=True))
        
        interfaceEmit.printout(".class public abstract interface " + interfaceName + "\n")
        interfaceEmit.printout(".super java/lang/Object\n\n")
        
        interface_ast = self.interfaceTypes[interfaceName]
        
        for method in interface_ast.methods:
            returnType = method.retType
            if isinstance(returnType, StringType):
                returnType = ClassType("GoString")
            elif isinstance(returnType, ArrayType) and isinstance(returnType.eleType, StringType):
                returnType.eleType = ClassType("GoString")
            paramTypes = []
            for param in method.params:
                type = param
                if isinstance(type, StringType):
                    type = ClassType("GoString")
                elif isinstance(type, ArrayType) and isinstance(type.eleType, StringType):
                    type.eleType = ClassType("GoString")
                paramTypes += [type]

            methodType = MType(paramTypes, returnType)
                        
            method_signature = ".method public abstract " + method.name + interfaceEmit.getJVMType(methodType) + "\n"
            interfaceEmit.printout(method_signature)
            
            interfaceEmit.printout(".end method\n\n")
        
        interfaceEmit.emitEPILOG()
          
    def genStructClass(self, structName, fields, methods):
        classFile = self.path + "/" + structName + ".j"
        structEmit = Emitter(classFile)
        
        implemented_interfaces = self.getInterfaceForStruct(structName)
        structEmit.printout(structEmit.emitPROLOG(structName, "java/lang/Object", implemented_interfaces))
        
        for field in fields:
            fieldName, fieldType = field
            if isinstance(fieldType, StringType):
                fieldType = ClassType("GoString")
            if isinstance(fieldType, ArrayType) and isinstance(fieldType.eleType, StringType):
                fieldType.eleType = ClassType("GoString")
            structEmit.printout(structEmit.emitATTRIBUTE(fieldName, fieldType, True, False, None, isStruct=True))
        
        self.genStructConstructor(structName, structEmit)
        for method in methods.values():
            self.genStructMethod(method, structName, structEmit)
        
        structEmit.emitEPILOG()
    
    def genStructConstructor(self, structName, structEmit):
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

    def genStructMethod(self, method, structName: str, structEmit: Emitter): 
        original_emitter = self.emit
        self.emit = structEmit
        original_className = self.className
        self.className = structName
        
        frame = Frame(method.fun.name, method.fun.retType)
        env = {}
        env[ENV] = [[]] + [self.env] 
        env[FRAME] = frame
        
        ret = method.fun.retType if not isinstance(method.fun.retType, Id) else ClassType(method.fun.retType.name)
        if isinstance(ret, StringType):
            ret = ClassType("GoString")
        elif isinstance(ret, ArrayType) and isinstance(ret.eleType, StringType):
            ret.eleType = ClassType("GoString")
        intyp = []
        for param in method.fun.params:
            if isinstance(param.parType, Id):
                param.parType = ClassType(param.parType.name)
            if isinstance(param.parType, StringType):
                param.parType = ClassType("GoString")
            if isinstance(param.parType, ArrayType) and isinstance(param.parType.eleType, StringType):
                param.parType.eleType = ClassType("GoString")
            intyp += [param.parType]
            
        self.emit.printout(self.emit.emitMETHOD(method.fun.name, MType(intyp, ret), False, frame))
        
        frame.enterScope(True)
        
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this" , ClassType(structName), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        for param in method.fun.params:
            idx = frame.getNewIndex()
            if isinstance(param.parType, StringType):
                param.parType = ClassType("GoString")
            self.emit.printout(self.emit.emitVAR(idx, param.parName, param.parType, frame.getStartLabel(), frame.getEndLabel(), frame))
            env[ENV][0] = [Symbol(param.parName, param.parType, Index(idx))] + env[ENV][0]
        
        env[ENV][0] = [Symbol(method.receiver, ClassType(structName), Index(0))] + env[ENV][0]
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        self.visit(method.fun.body, env)
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        
        if isinstance(method.fun.retType, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
            
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        
        self.emit = original_emitter
        self.className = original_className
    
    def genMethod(self, ast, o, frame): 
        isInit = ast.name == '<init>'
        isClinit = ast.name == '<clinit>'
        isMain = ast.name == 'main' and len(ast.params) == 0 and ast.retType == VoidType()
        return_typ = VoidType() if isInit or isClinit else (ast.retType if not isinstance(ast.retType, Id) else ClassType(ast.retType.name))
        if isinstance(return_typ, StringType):
            return_typ = ClassType("GoString")
        elif isinstance(return_typ, ArrayType) and isinstance(return_typ.eleType, StringType):
            return_typ.eleType = ClassType("GoString")
        methodName = '<init>' if isInit else ast.name
        inType = [ArrayType([None], StringType())] if isMain else [param.parType for param in ast.params]
        isStruct = not (self.className == 'MiniGoClass')
        if not isMain or isStruct:
            for i, t in enumerate(inType):
                if isinstance(t, StringType):
                    inType[i] = ClassType("GoString")
                elif isinstance(t, ArrayType) and isinstance(t.eleType, StringType):
                    inType[i].eleType = ClassType("GoString")
        mtype = MType(inType, return_typ)
        
        if isStruct:
            self.emit.printout(self.emit.emitMETHOD(methodName, mtype, False, frame))
        else:
            self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame)) 
        
        frame.enterScope(True) 
        
        if isInit: 
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isClinit:
            marked = {}
            for global_var in o[ENV][-1]: 
                if global_var.name in marked: continue
                if isinstance(global_var.mtype, VarDecl):
                    init = global_var.mtype.varInit if global_var.mtype.varInit else self.getDefaultValue(global_var.mtype.varType)
                    if isinstance(init, NilLiteral): 
                        marked[global_var.name] = True
                        continue
                    code_init, type_init = self.visit(init, Access(frame, o[ENV], False))
                    if not global_var.mtype.varType:
                        global_var.mtype.varType = type_init
                    if type(global_var.mtype.varType) is Id:
                        global_var.mtype.varType = ClassType(global_var.mtype.varType.name)
                    code_init += self.emit.emitPUTSTATIC(f"{self.className}/{global_var.name}", global_var.mtype.varType, frame)
                    self.emit.printout(code_init)
                    marked[global_var.name] = True
                elif isinstance(global_var.mtype, ConstDecl):
                    code_init, type_init = self.visit(global_var.mtype.iniExpr, Access(frame, o[ENV], False))
                    ast.conType = type_init
                    code_init += self.emit.emitPUTSTATIC(f"{self.className}/{global_var.name}", global_var.mtype.conType, frame)
                    self.emit.printout(code_init)
                    marked[global_var.name] = True
                
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else: 
            for param in ast.params:
                idx = frame.getNewIndex()
                if isinstance(param.parType, Id): 
                    param.parType = ClassType(param.parType.name) 
                if isinstance(param.parType, StringType): 
                    param.parType = ClassType("GoString")
                if isinstance(param.parType, ArrayType) and isinstance(param.parType.eleType, StringType):
                    param.parType.eleType = ClassType("GoString")
                self.emit.printout(self.emit.emitVAR(idx, param.parName, param.parType, frame.getStartLabel(), frame.getEndLabel(), frame))
                o[ENV][0] += [Symbol(param.parName, param.parType, Index(idx))]
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame)) 
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame)) 
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame)) 
        if not isClinit:
            body = ast.body
            self.visit(body, o) 
            
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame)) 
        if type(return_typ) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame)) 
        frame.exitScope() 
            
    
    def visitProgram(self, ast, c):
        env = {}
        env[ENV] = [self.env] 
        self.genGoStringType() 
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        for decl in ast.decl:
            if isinstance(decl, VarDecl) or isinstance(decl, ConstDecl):
                env = self.visit(decl, env)
        for interfaceName, interface_ast in self.interfaceTypes.items():
            self.genInterface(interfaceName)
        for structName, structDef in self.structTypes.items():
            self.genStructClass(structName, structDef.elements, self.structMethods.get(structName, {}))
        env[ENV] = [[]] + env[ENV] 
        for decl in ast.decl:
            if isinstance(decl, VarDecl) or isinstance(decl, ConstDecl):
                name_ = decl.varName if isinstance(decl, VarDecl) else decl.conName
                sym = None
                for s in env[ENV][-1]:
                    if s.name == name_ and not isinstance(s.mtype, (VarDecl, ConstDecl)):
                        sym = s
                        break
                env[ENV][0] += [sym]
            elif not isinstance(decl, (StructType, MethodDecl, InterfaceType)):
                env = self.visit(decl, env)
        self.genMethod(FuncDecl("<init>", [], VoidType(), Block([])), env, Frame("<init>", VoidType()))
        self.genMethod(FuncDecl("<clinit>", [], VoidType(), Block([])), env, Frame("<clinit>", VoidType()))
        self.emit.printout(self.emit.emitEPILOG())
        return env

    def visitFuncDecl(self, ast, c):
        frame = Frame(ast.name, ast.retType)
        isMain = ast.name == "main"
        
        mtype = None
        
        if isMain:
            mtype = MType([ArrayType([None], StringType())], VoidType())
        else:
            ret = ast.retType if not isinstance(ast.retType, Id) else ClassType(ast.retType.name)
            if isinstance(ret, StringType):
                ret = ClassType("GoString")
            elif isinstance(ret, ArrayType) and isinstance(ret.eleType, StringType):
                ret.eleType = ClassType("GoString")
            params = []
            for param in ast.params:
                if isinstance(param.parType, Id):
                    param.parType = ClassType(param.parType.name)
                if isinstance(param.parType, StringType):
                    param.parType = ClassType("GoString")
                params += [param.parType]
            mtype = MType(params, ret)
        c[ENV][0] += [Symbol(ast.name, mtype, CName(self.className))]
        c[FRAME] = frame
        self.genMethod(ast, c, frame)
        
        return c
    
    def visitParamDecl(self, ast, o):
        idx = o[FRAME].getNewIndex()
        o[ENV][0] = [Symbol(ast.parName, ast.parType, Index(idx))] + o[ENV][0]
        return idx

    def visitBlock(self, ast, o):
        env = o.copy()
        frame = env[FRAME]
        env[ENV] = [[]] + env[ENV] 
        frame.enterScope(False) 
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        for stmt in ast.member:
            if isinstance(stmt, VarDecl) or isinstance(stmt, ConstDecl):
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
                    temp_frame = env[0][FRAME]
                    temp_env = env[0][ENV]
                    env = {ENV: temp_env, FRAME: temp_frame}
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
        
    def visitStructType(self, ast, o): pass
    
    def visitVarDecl(self, ast, o):
        if FRAME not in o: 
            if ast.varInit:
                temp_frame = Frame("<init>", VoidType())
                code, typ = self.visit(ast.varInit, Access(temp_frame, o[ENV], False))
                if not ast.varType:
                    ast.varType = typ
                if isinstance(ast.varType, StringType):
                    ast.varType = ClassType("GoString")
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, ""))
            o[ENV][0] += [Symbol(ast.varName, ast.varType, CName(self.className))]
        else: 
            frame = o[FRAME]
            idx = frame.getNewIndex()
            code, typ = "", None
            if ast.varType and isinstance(ast.varType, ArrayType) and not ast.varInit:
                if isinstance(ast.varType.eleType, StringType):
                    ast.varType.eleType = ClassType("GoString")
                self.emit.printout(self.emit.emitVAR(idx, ast.varName, ast.varType, 
                                frame.getStartLabel(), frame.getEndLabel(), frame))
                
                dimensions = ast.varType.dimens
                element_type = ast.varType.eleType
                if len(dimensions) == 1:
                    size = dimensions[0].value if hasattr(dimensions[0], 'value') else dimensions[0]
                    if isinstance(size, Id):
                        size = self.visit(size, Access(frame, o[ENV], False))[0]
                        self.emit.printout(size)
                    else:
                        self.emit.printout(self.emit.emitPUSHICONST(size, frame))
                    if isinstance(element_type, (IntType, BoolType, FloatType)):
                        self.emit.printout(self.emit.jvm.emitNEWARRAY(self.emit.getFullType(element_type)))
                    else:
                        self.emit.printout(self.emit.jvm.emitANEWARRAY(self.emit.getFullType(element_type)))
                else:
                    for dim in dimensions:
                        dim_value = dim.value if hasattr(dim, 'value') else dim
                        if isinstance(dim_value, Id):
                            dim_value = self.visit(dim_value, Access(frame, o[ENV], False))[0]
                            self.emit.printout(dim_value)
                        else:
                            self.emit.printout(self.emit.emitPUSHICONST(dim_value, frame))
                    
                    self.emit.printout(self.emit.emitNEWARRAY(ast.varType, frame))
                
                self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, idx, frame))
                
                o[ENV][0] += [Symbol(ast.varName, ast.varType, Index(idx))]
                return o
                
            if ast.varType and isinstance(ast.varType, Id):
                struct_name = ast.varType.name
                ast.varType = ClassType(struct_name)
                isStruct = struct_name in self.structTypes
                self.emit.printout(self.emit.emitVAR(idx, ast.varName, ast.varType, 
                              frame.getStartLabel(), frame.getEndLabel(), frame))
                if not isStruct and not ast.varInit:
                    o[ENV][0] += [Symbol(ast.varName, ast.varType, Index(idx))]
                    return o
                if ast.varInit:
                    init_code, _ = self.visit(ast.varInit, Access(frame, o[ENV], False))
                    self.emit.printout(init_code)
                elif isStruct:
                    self.emit.printout(self.emit.emitNEW(struct_name, frame))
                    self.emit.printout(self.emit.emitDUP(frame))
                    self.emit.printout(self.emit.emitINVOKESPECIAL(frame, f"{struct_name}/<init>", MType([], VoidType())))
                    
                self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, idx, frame))
                
                o[ENV][0] += [Symbol(ast.varName, ast.varType, Index(idx))]
                return o
                
            init_val = ast.varInit if ast.varInit else self.getDefaultValue(ast.varType)
            code, typ = "", None
            if isinstance(ast.varType, ArrayType) and isinstance(ast.varType.eleType, StringType):
                ast.varType.eleType = ClassType("GoString")
            if not isinstance(init_val, NilLiteral):
                if type(ast.varType) is ArrayType and isinstance(init_val, ArrayLiteral):
                    i2f = (isinstance(ast.varType.eleType, FloatType) and isinstance(init_val.eleType, IntType))
                    code, typ = self.visit(init_val, Access(frame, o[ENV], False, i2f))
                else:
                    code, typ = self.visit(init_val, Access(frame, o[ENV], False))
            if not ast.varType and not isinstance(typ, VoidType):
                if isinstance(typ, ArrayType) and isinstance(typ.eleType, StringType):
                    typ.eleType = ClassType("GoString")
                ast.varType = typ  
            elif isinstance(ast.varType, Id):
                name_ = ast.varType.name
                ast.varType = ClassType(name_)
            elif isinstance(ast.varType, StringType):
                ast.varType = ClassType("GoString")
            self.emit.printout(self.emit.emitVAR(idx, ast.varName, ast.varType, 
                              frame.getStartLabel(), frame.getEndLabel(), frame))
            self.emit.printout(code)
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, idx, frame))
            o[ENV][0] += [Symbol(ast.varName, ast.varType, Index(idx))]
        return o
    
    def visitConstDecl(self, ast, o):
        if FRAME not in o: 
            temp_frame = Frame("<init>", VoidType())
            code, typ = self.visit(ast.iniExpr, Access(temp_frame, o[ENV], False))
            ast.conType = typ
            self.emit.printout(self.emit.emitATTRIBUTE(ast.conName, ast.conType, True, True, ""))
            o[ENV][0] += [Symbol(ast.conName, ast.conType, CName(self.className))]
        else: 
            frame = o[FRAME]
            idx = frame.getNewIndex()
            code, typ_ = self.visit(ast.iniExpr, Access(frame, o[ENV], False))
            if isinstance(typ_, ArrayType) and isinstance(typ_.eleType, StringType):
                typ_.eleType = ClassType("GoString")
            ast.conType = typ_
            self.emit.printout(self.emit.emitVAR(idx, ast.conName, ast.conType, 
                              frame.getStartLabel(), frame.getEndLabel(), frame))
            self.emit.printout(code)
            self.emit.printout(self.emit.emitWRITEVAR(ast.conName, ast.conType, idx, frame))
                
            o[ENV][0] = [Symbol(ast.conName, ast.conType, Index(idx))] + o[ENV][0]
        return o
    
    def visitAssign(self, ast, o):
        frame = o[FRAME]
        env = o[ENV]
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
            if isinstance(rt, ClassType) and rt.name == "GoString":
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
            temp_flag1 = False
            temp_flag2 = False
            if ret is not None:
                temp_flag1 = True
            for scope in env[:-1]:
                for sym in scope:
                    if sym.name == ast.lhs.name:
                        temp_flag2 = True
                        break
                if temp_flag2: break

            flag = temp_flag1 and temp_flag2
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
            if isinstance(lt, ClassType) and lt.name == "GoString":
                lc, _ = self.visit(ast.lhs, Access(frame, env, False))
                rc, rt = self.visit(ast.rhs, Access(frame, env, False))
                get_val = self.emit.emitINVOKEVIRTUAL(f"{lt.name}/getValue", MType([], StringType()), frame)
                set_val = self.emit.emitINVOKEVIRTUAL(f"{lt.name}/setValue", MType([StringType()], VoidType()), frame)
                return lc + rc  + get_val + set_val, VoidType()
            if isinstance(lt, FloatType) and isinstance(rt, IntType):
                rc += self.emit.emitI2F(frame)
                
            return rc + lc, VoidType()
           
    def visitIf(self, ast, o):
        frame = o[FRAME]
        env = o[ENV]
        
        cond_code, _ = self.visit(ast.expr, Access(frame, env, False))
        self.emit.printout(cond_code)
        
        falseLabel = frame.getNewLabel()
        endLabel = frame.getNewLabel()
        
        self.emit.printout(self.emit.emitIFFALSE(falseLabel, frame))
        
        if isinstance(ast.thenStmt, Block):
            blockLabel = frame.getNewLabel()
            self.emit.printout(self.emit.emitLABEL(blockLabel, frame))
            self.visit(ast.thenStmt, o)
        else:
            self.visit(ast.thenStmt, o)
        
        if ast.elseStmt:
            self.emit.printout(self.emit.emitGOTO(endLabel, frame))
            
            self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
            
            if isinstance(ast.elseStmt, If):
                self.visit(ast.elseStmt, o)
            elif isinstance(ast.elseStmt, Block):
                blockLabel = frame.getNewLabel()
                self.emit.printout(self.emit.emitLABEL(blockLabel, frame))
                self.visit(ast.elseStmt, o)
            else:
                self.visit(ast.elseStmt, o)
            
            self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        else:
            self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
            self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        
        return o
        
    def visitForBasic(self, ast, o):
        frame = o[FRAME]
        env = o[ENV]
        
        frame.enterLoop()
        
        continueLabel = frame.getContinueLabel()
        breakLabel = frame.getBreakLabel()
        
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
        
        cond_code, _ = self.visit(ast.cond, Access(frame, env, False))
        self.emit.printout(cond_code)
        self.emit.printout(self.emit.emitIFFALSE(breakLabel, frame))
        
        self.visit(ast.loop, o)
        
        self.emit.printout(self.emit.emitGOTO(continueLabel, frame))
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))
        
        frame.exitLoop()
        
        return o
    
    
    def visitForStep(self, ast, o):
        frame = o[FRAME]
        
        frame.enterLoop()
        
        loop_start_label = frame.getNewLabel()
        loop_end_label = frame.getNewLabel()
        cond_label = frame.getNewLabel()
        body_label = frame.getNewLabel()
        update_label = frame.getContinueLabel()
        end_label = frame.getBreakLabel()
        
        loop_env = {}
        loop_env[FRAME] = frame
        loop_env[ENV] = [[]] + o[ENV]
        
        self.emit.printout(self.emit.emitLABEL(loop_start_label, frame))
        name_i = ast.init.varName if isinstance(ast.init, VarDecl) else ast.init.lhs.name
        if isinstance(ast.init, VarDecl):
            rc, rt = self.visit(ast.init.varInit, Access(frame, loop_env, False))
            ast.init.varType = rt
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, name_i, rt, loop_start_label, loop_end_label, frame))
            loop_env[ENV][0] += [Symbol(name_i, rt, Index(idx))]
            code = self.emit.emitWRITEVAR(name_i, rt, idx, frame)
            self.emit.printout(rc + code)
        else:
            rc, rt = self.visit(ast.init.rhs, Access(frame, loop_env, False))
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, name_i, rt, loop_start_label, loop_end_label, frame))
            loop_env[ENV][0] += [Symbol(name_i, rt, Index(idx))]
            code = self.emit.emitWRITEVAR(name_i, rt, idx, frame)
            self.emit.printout(rc + code)
            
        self.emit.printout(self.emit.emitLABEL(cond_label, frame))
        cond_code, _ = self.visit(ast.cond, Access(frame, loop_env[ENV], False))
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
        
        return o
        
    def visitBreak(self, ast, o):
        frame = o[FRAME]
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))
        return o
        
    def visitContinue(self, ast, o):
        frame = o[FRAME]
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))
        return o
        
    def visitReturn(self, ast, o):
        frame = o[FRAME]
        env = o[ENV]
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
        
    def visitFieldAccess(self, ast, o):
        frame = o.frame
        env = o.sym
        isLeft = o.isLeft
        
        rec_code, rec_type = self.visit(ast.receiver, Access(frame, env, False))
        
        struct_name = rec_type.name if isinstance(rec_type, ClassType) else rec_type.name
        field_type = None
        
        if struct_name in self.structTypes:
            struct_def = self.structTypes[struct_name]
            for field_name, field_typ in struct_def.elements:
                if field_name == ast.field:
                    field_type = field_typ
                    if isinstance(field_type, StringType):
                        field_type = ClassType("GoString")
                    if isinstance(field_type, ArrayType) and isinstance(field_type.eleType, StringType):
                        field_type.eleType = ClassType("GoString")
                    break
        
        if isLeft:
            return rec_code + self.emit.emitPUTFIELD(f"{struct_name}/{ast.field}", field_type, frame), field_type
        else:  
            return rec_code + self.emit.emitGETFIELD(f"{struct_name}/{ast.field}", field_type, frame), field_type
        
    def visitBinaryOp(self, ast, o):
        frame = o.frame
        env = o.sym
        if ast.op == '&&' or ast.op == '||':
            end_label = frame.getNewLabel()
            
            left_code, left_type = self.visit(ast.left, Access(frame, env, False))
            result = []
            result += [left_code, self.emit.emitDUP(frame)]
                        
            if ast.op == '&&':
                result += [self.emit.emitIFFALSE(end_label, frame), self.emit.emitPOP(frame)]
                
                right_code, right_type = self.visit(ast.right, Access(frame, env, False))
                result += [right_code]
            else:
                result += [self.emit.emitIFTRUE(end_label, frame), self.emit.emitPOP(frame)]
                
                right_code, right_type = self.visit(ast.right, Access(frame, env, False))
                result += [right_code]
                
            result += [self.emit.emitLABEL(end_label, frame)]
            return ''.join(result), BoolType()
        
        left_code, left_type = self.visit(ast.left, Access(frame, env, False))
        right_code, right_type = self.visit(ast.right, Access(frame, env, False))
        result_type = left_type
        if isinstance(left_type, FloatType) or isinstance(right_type, FloatType):
            result_type = FloatType()
            
            if isinstance(left_type, IntType):
                left_code += self.emit.emitI2F(frame)
            if isinstance(right_type, IntType):
                right_code += self.emit.emitI2F(frame)
                
        op_code = ""
        if ast.op in ['+', '-']:
            if isinstance(left_type, ClassType) and isinstance(right_type, ClassType) and left_type.name == right_type.name and left_type.name == "GoString":
                op_code = self.emit.emitINVOKEVIRTUAL("GoString/concat", MType([ClassType("GoString")], ClassType("GoString")), frame)
            else:
                op_code = self.emit.emitADDOP(ast.op, result_type, frame)
        elif ast.op in ['*', '/']:
            op_code = self.emit.emitMULOP(ast.op, result_type, frame)
        elif ast.op == '%':
            op_code = self.emit.emitMOD(frame)
        elif ast.op in ['&&', '||']:
            op_code = self.emit.emitANDOP(frame) if ast.op == '&&' else self.emit.emitOROP(frame)
            result_type = BoolType()
        elif ast.op in ['==', '!=', '<', '<=', '>', '>=']:
            op_code = self.emit.emitREOP(ast.op, left_type, frame)
            result_type = BoolType()
        
        return left_code + right_code + op_code, result_type
        
    def visitUnaryOp(self, ast, o):
        frame = o.frame
        env = o.sym
        
        body_code, body_type = self.visit(ast.body, Access(frame, env, False))
        if ast.op == '-':
            return body_code + self.emit.emitNEGOP(body_type, frame), body_type
        elif ast.op == '!':
            return body_code + self.emit.emitNOT(body_type, frame), BoolType()
            
        return body_code, body_type
        
    def visitFuncCall(self, ast, o):
        frame = o[FRAME] if isinstance(o, dict) else o.frame
        env = o[ENV] if isinstance(o, dict) else o.sym
        if ast.funName in ["getInt", "getFloat", "getBool", "getString"]:
            func_sym = next((s for s in env[-1] if s.name == ast.funName), None)
            typ_ = func_sym.mtype.rettype
            default_ = self.getDefaultValue(typ_)
            code, typ_ = self.visit(default_, Access(frame, env, False))
            return code, typ_
        func_sym = None
        for scope in env:
            for sym in scope:
                if sym.name == ast.funName:
                    func_sym = sym
                    break
            if func_sym:
                break
        args_code = ""
        for arg in ast.args:
            arg_code, arg_type = self.visit(arg, Access(frame, env, False, False))
            if isinstance(arg_type, ClassType) and arg_type.name == "GoString" and (ast.funName == "putString" or ast.funName =="putStringLn"): arg_code += self.emit.emitINVOKEVIRTUAL("GoString/getValue", MType([], StringType()), frame)
            args_code += arg_code
            if len(func_sym.mtype.partype) > 0 and isinstance(func_sym.mtype.partype[0], FloatType) and isinstance(arg_type, IntType):
                args_code += self.emit.emitI2F(frame)
        
        if ast.funName == "putString" or ast.funName == "putStringLn":
            call_code = self.emit.emitINVOKESTATIC(
                f"{func_sym.value.value}/{ast.funName}", func_sym.mtype, frame)
        else:
            for i, t in enumerate(func_sym.mtype.partype):
                if isinstance(t, StringType):
                    func_sym.mtype.partype[i] = ClassType("GoString")
            call_code = self.emit.emitINVOKESTATIC(
                f"{func_sym.value.value}/{ast.funName}", func_sym.mtype, frame)
        if type(func_sym.mtype.rettype) is VoidType:
            self.emit.printout(args_code + call_code)
        elif ast.funName in ["getInt", "getFloat", "getBool", "getString"]:
            return o
        if isinstance(o, dict) and type(func_sym.mtype.rettype) is VoidType:
            frame = o[FRAME]
            env = o[ENV]
            return {ENV: env, FRAME: frame}
        else:
            return (args_code + call_code, func_sym.mtype.rettype)
        
    def visitMethCall(self, ast, o):
        frame = o[FRAME] if isinstance(o, dict) else o.frame
        env = o[ENV] if isinstance(o, dict) else o.sym
        rec_code, rec_type = self.visit(ast.receiver, Access(frame, env, False))
        
        struct_name = rec_type.name if isinstance(rec_type, ClassType) else rec_type.name
        
        method = None
        isStruct = struct_name in self.structTypes
        
        if isStruct:
            methods = self.structMethods[struct_name]
            if ast.metName in methods:
                method = methods[ast.metName]
        else:
            interface_ = self.interfaceTypes[struct_name]
            protos = interface_.methods
            for proto in protos:
                if proto.name == ast.metName:
                    method = proto
                    break
            
        arg_codes = [rec_code]  
        for arg in ast.args:
            arg_code, _ = self.visit(arg, Access(frame, env, False))
            arg_codes += [arg_code]
                        
        args_code = ''.join(arg_codes)
        method_type = None
        ret = None
        if isStruct:
            inp = []
            for param in method.fun.params:
                if isinstance(param.parType, StringType):
                    inp += [ClassType("GoString")]
                elif isinstance(param.parType, ArrayType) and isinstance(param.parType.eleType, StringType):
                    inp += [ArrayType(param.parType.dimens, ClassType("GoString"))]
                else:
                    inp += [param.parType]
            ret = method.fun.retType
            if isinstance(ret, StringType):
                ret = ClassType("GoString")
            elif isinstance(ret, ArrayType) and isinstance(ret.eleType, StringType):
                ret = ArrayType(ret.dimens, ClassType("GoString"))
            
            method_type = MType(inp, ret)
        else: 
            inp = []
            for param in method.params:
                if isinstance(param, StringType):
                    inp += [ClassType("GoString")]
                elif isinstance(param, ArrayType) and isinstance(param.eleType, StringType):
                    inp += [ArrayType(param.dimens, ClassType("GoString"))]
                else:
                    inp += [param]
            ret = method.retType
            if isinstance(ret, StringType):
                ret = ClassType("GoString")
            elif isinstance(ret, ArrayType) and isinstance(ret.eleType, StringType):
                ret = ArrayType(ret.dimens, ClassType("GoString"))
            method_type = MType(inp, ret)
        if isStruct:
            call_code = self.emit.emitINVOKEVIRTUAL(
                f"{struct_name}/{ast.metName}", method_type, frame)
        else: 
            call_code = self.emit.emitINVOKEINTERFACE(
                f"{struct_name}/{ast.metName}", method_type, frame, len(method.params) + 1)
        return args_code + call_code, ret
            
    def visitArrayCell(self, ast, o):
        frame = o.frame
        env = o.sym
        isLeft = o.isLeft
        
        arr_code, arr_type = self.visit(ast.arr, Access(frame, env, False))
        result = arr_code
        
        current_type = arr_type
        if type(current_type.eleType) is StringType:
            current_type.eleType = ClassType("GoString")
        
        for i in range(len(ast.idx)):
            idx_code, _ = self.visit(ast.idx[i], Access(frame, env, False))
            result += idx_code
            
            if i < len(ast.idx) - 1:
                result += self.emit.emitALOAD(current_type, frame)
        if not isLeft:
            if isinstance(current_type, ArrayType):
                result += self.emit.emitALOAD(current_type.eleType, frame)
                return result, current_type.eleType
            else:
                result += self.emit.emitALOAD(current_type, frame)
                return result, current_type
        
        if isinstance(current_type, ArrayType):
            return result, current_type.eleType
        else:
            return result, current_type
    
    def visitArrayLiteral(self, ast, o):
        frame = o.frame
        env = o.sym
        isArrayFloat = o.isArrayFloat
        result = []
        if isinstance(ast.eleType, IntType) and isArrayFloat:
                ast.eleType = FloatType()
        if isinstance(ast.eleType, StringType):
            ast.eleType = ClassType("GoString")
        for dim in ast.dimens:
            dim_code, _ = self.visit(dim, Access(frame, env, False))
            result.append(dim_code)
        
        if len(ast.dimens) > 1:
            array_type = ArrayType(ast.dimens, ast.eleType)
            result.append(self.emit.emitNEWARRAY(array_type, frame))
        else:
            if isinstance(ast.eleType, (IntType, FloatType, BoolType)):
                result.append(self.emit.jvm.emitNEWARRAY(self.emit.getFullType(ast.eleType)))
            else:
                result.append(self.emit.emitNEWARRAY(ast, frame))
        
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
    
    def visitStructLiteral(self, ast, o):
        frame = o.frame
        env = o.sym
        result = []
        result.append(self.emit.emitNEW(ast.name, frame))
        result.append(self.emit.emitDUP(frame))
        result.append(self.emit.emitINVOKESPECIAL(frame, f"{ast.name}/<init>", MType([], VoidType())))
        
        initialized_fields = {field_name: field_expr for field_name, field_expr in ast.elements}
        if ast.name in self.structTypes:
            struct_def = self.structTypes[ast.name]
            
            for field_name, field_type in struct_def.elements:
                if field_name not in initialized_fields:
                    if isinstance(field_type, Id) or isinstance(field_type, ArrayType):
                        continue
                    
                    result.append(self.emit.emitDUP(frame))  
                    
                    default_val = self.getDefaultValue(field_type)
                    default_code, _ = self.visit(default_val, Access(frame, env, False))
                    result.append(default_code)
                    
                    if isinstance(field_type, Id):
                        field_type = ClassType(field_type.name)
                    if isinstance(field_type, StringType):
                        field_type = ClassType("GoString")
                        
                    result.append(self.emit.emitPUTFIELD(f"{ast.name}/{field_name}", field_type, frame))
                else:
                    result.append(self.emit.emitDUP(frame))  
                    expr_code, expr_type = self.visit(initialized_fields[field_name], Access(frame, env, False))
                    result.append(expr_code)
                    
                    if isinstance(field_type, FloatType) and isinstance(expr_type, IntType):
                        result.append(self.emit.emitI2F(frame))
                    if isinstance(field_type, Id):
                        field_type = ClassType(field_type.name)
                    if isinstance(field_type, StringType):
                        result.append(self.emit.emitPUTFIELD(f"{ast.name}/{field_name}",ClassType("GoString"), frame))
                        continue
                    result.append(self.emit.emitPUTFIELD(f"{ast.name}/{field_name}", field_type, frame))
            
        return ''.join(result), ClassType(ast.name)
        
    def visitId(self, ast, o):
        frame = o.frame
        env = o.sym
        isLeft = o.isLeft
        for scope in env:
            for sym in scope:
                if sym.name == ast.name and not isinstance(sym.mtype, (VarDecl, ConstDecl)):
                    if type(sym.mtype) is Id:
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
        
    def visitIntLiteral(self, ast, o):
        val = ast.value
        if isinstance(val, str):
            if val.startswith("0b") or val.startswith("0B"):
                val = int(val, 2)
            elif val.startswith("0o") or val.startswith("0O"):
                val = int(val, 8)
            elif val.startswith("0x") or val.startswith("0X"):
                val = int(val, 16)
        return self.emit.emitPUSHICONST(val, o.frame), IntType()
        
    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), FloatType()
        
    def visitStringLiteral(self, ast, o):
        frame = o.frame
        result = []
        result.append(self.emit.emitNEW("GoString", frame))
        result.append(self.emit.emitDUP(frame))
        result.append(self.emit.emitPUSHCONST(ast.value, StringType(), frame))
        result.append(self.emit.emitINVOKESPECIAL(frame, "GoString/<init>", MType([StringType()], VoidType())))
        return ''.join(result), ClassType("GoString")
        
    def visitBooleanLiteral(self, ast, o):
        value = ast.value
        if isinstance(value, str):
            value = value.lower() == 'true'
        return self.emit.emitPUSHICONST(1 if value else 0, o.frame), BoolType()

    def visitNilLiteral(self, ast, o):
        return self.emit.jvm.emitPUSHNULL(), VoidType()

    def visitForEach(self, ast, o): return o

