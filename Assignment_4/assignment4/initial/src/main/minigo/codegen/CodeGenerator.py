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
# import warnings
from copy import deepcopy

# warnings.filterwarnings("ignore", category=DeprecationWarning)

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

# for lib
class CName(Val):
    def __init__(self, value):
        self.value = value


class ClassType(Type): # for struct type
    def __init__(self, name):
        #value: Id
        self.name = name
    def __str__(self):
        return "Class{0}".format(self.name)
    def accept(self, v, param): return None
    
    

# when visit function use it
class SubBody(): # for body of function
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
        self.isArrayFloat = isArrayFloat # for array of float type
        
# for first scan
class PreCodeGen(BaseVisitor):
    def __init__(self, astTree, env):
        self.astTree = astTree
        self.env = env
        self.className = "MiniGoClass"    
        self.structTypes = {} # for struct
        self.structMethods = {}
        self.interfaceTypes = {}
    
    
    def visitProgram(self, ast, c): 
        e = SubBody(None, self.env)
        # first scan catch all func, struct, type
        for decl in ast.decl:
            if isinstance(decl, FuncDecl) or isinstance(decl, StructType) or isinstance(decl, InterfaceType) or isinstance(decl, VarDecl) or isinstance(decl, ConstDecl):
                e = self.visit(decl, e)
        
        # second scan get method decl 
        for decl in ast.decl:
            if isinstance(decl, MethodDecl):
                e = self.visit(decl, e)
    
        self.env = e.sym
        return c

    def visitVarDecl(self, ast, c):
        c.sym.append(Symbol(ast.varName, ast, CName(self.className)))
        return c
    def visitConstDecl(self, ast, c):
        c.sym.append(Symbol(ast.conName, ast, CName(self.className)))
        return c
    
    def visitFuncDecl(self, ast, c): 
        returnType = ast.retType
        paramTypes = [param.parType for param in ast.params]
        if isinstance(returnType, StringType):
            returnType = ClassType("GoString")
        c.sym.append(Symbol(ast.name, MType(paramTypes, returnType), CName(self.className)))
        return c
    
    def visitStructType(self, ast, c): 
        self.structTypes[ast.name] = ast
        c.sym.append(Symbol(ast.name, ClassType(ast.name), CName(self.className)))
        return c
    
    def visitInterfaceType(self, ast, c): 
        self.interfaceTypes[ast.name] = ast
        c.sym.append(Symbol(ast.name, ClassType(ast.name), CName(self.className)))
        return c
    
    # receiver: str, recType: Type, fun: FuncDecl
    
    def visitMethodDecl(self, ast, c): 
        # Find the struct for this method
        structName = ast.recType.name
        if structName not in self.structMethods:
            self.structMethods[structName] = {}
            
        # Add method to struct
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
        gl = self.init() # got list of symbol io funcs
        preprocess = PreCodeGen(ast, gl)
        preprocess.visit(ast, None) # preprocess got all list of symbol function, struct with their methods, interface 
        gc = CodeGenVisitor(ast, preprocess.env, path, preprocess.structTypes, preprocess.structMethods, preprocess.interfaceTypes)
        gc.visit(ast, None)
    
    


""" 
structTypes: dict
    key: name of struct
    value: ast of StructType()

structMethods: dict of dict 
    key: name of struct
    value: dict 
            key: name of method
            value: MethodDecl()

interfaceTypes: dict
    key: name of interface
    value: ast of InterfaceType()

"""
class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path, structTypes, structMethods, interfaceTypes):
        self.className = "MiniGoClass"
        self.astTree = astTree
        self.env = env # list[list[Symbol]]
        self.path = path
        self.emit = Emitter(path + "/" + self.className + ".j")
        self.structTypes = structTypes
        self.structMethods = structMethods
        self.interfaceTypes = interfaceTypes
    def isReferenceType(self, typ):
        return (isinstance(typ, StringType) or 
                isinstance(typ, ClassType) or  # structs and interfaces
                isinstance(typ, ArrayType))
        
    def genGoStringType(self):
        # Create a separate .j file for GoString class
        goStringFile = self.path + "/GoString.j"
        strEmitter = Emitter(goStringFile)
        
        # Generate class prologue
        strEmitter.printout(strEmitter.emitPROLOG("GoString", "java/lang/Object"))
        
        # Add a field for holding the string value
        strEmitter.printout(".field private value Ljava/lang/String;\n\n")
        
        # Generate default constructor
        frame = Frame("<init>", VoidType())
        strEmitter.printout(strEmitter.emitMETHOD("<init>", MType([], VoidType()), False, frame))
        frame.enterScope(True)
        
        # Generate code to initialize this
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitINVOKESPECIAL(frame))
        
        # Initialize value field to empty string
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitPUSHCONST("\"\"", StringType(), frame))
        strEmitter.printout(strEmitter.emitPUTFIELD("GoString/value", StringType(), frame))
        
        # End constructor
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitRETURN(VoidType(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()
        
        # Generate constructor with string parameter
        frame = Frame("<init>", VoidType())
        strEmitter.printout(strEmitter.emitMETHOD("<init>", MType([StringType()], VoidType()), False, frame))
        frame.enterScope(True)
        
        # Generate code for this and parameter
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "str", StringType(), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        
        # Initialize
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitINVOKESPECIAL(frame))
        
        # Set value field to parameter
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitREADVAR("str", StringType(), 1, frame))
        strEmitter.printout(strEmitter.emitPUTFIELD("GoString/value", StringType(), frame))
        
        # End constructor
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitRETURN(VoidType(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()
        
        # Generate compare method
        frame = Frame("compare", IntType())
        strEmitter.printout(strEmitter.emitMETHOD("compare", MType([ClassType("GoString")], IntType()), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "other", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        
        # Get this.value
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("GoString/value", StringType(), frame))
        
        # Get other.value
        strEmitter.printout(strEmitter.emitREADVAR("other", ClassType("GoString"), 1, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("GoString/value", StringType(), frame))
        
        # Invoke compareTo
        strEmitter.printout(strEmitter.emitINVOKEVIRTUAL("java/lang/String/compareTo", 
                                                    MType([StringType()], IntType()), frame))
        
        # Return result
        strEmitter.printout(strEmitter.emitRETURN(IntType(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()
        
        # Generate concat method
        frame = Frame("concat", ClassType("GoString"))
        strEmitter.printout(strEmitter.emitMETHOD("concat", MType([ClassType("GoString")], ClassType("GoString")), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "other", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        
        # Create new GoString
        strEmitter.printout(strEmitter.emitNEW("GoString", frame))
        strEmitter.printout(strEmitter.emitDUP(frame))
        
        # Get this.value
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("GoString/value", StringType(), frame))
        
        # Get other.value
        strEmitter.printout(strEmitter.emitREADVAR("other", ClassType("GoString"), 1, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("GoString/value", StringType(), frame))
        
        # Concatenate strings
        strEmitter.printout(strEmitter.emitINVOKEVIRTUAL("java/lang/String/concat", 
                                                    MType([StringType()], StringType()), frame))
        
        # Initialize new GoString with result
        strEmitter.printout(strEmitter.emitINVOKESPECIAL(frame, "GoString/<init>", 
                                                    MType([StringType()], VoidType())))
        
        # Return new GoString
        strEmitter.printout(strEmitter.emitRETURN(ClassType("GoString"), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()
        
        # Generate toString method
        frame = Frame("toString", StringType())
        strEmitter.printout(strEmitter.emitMETHOD("toString", MType([], StringType()), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        
        # Return value field directly
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("GoString/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitRETURN(StringType(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()
        
        # Generate getValue method
        frame = Frame("getValue", StringType())
        strEmitter.printout(strEmitter.emitMETHOD("getValue", MType([], StringType()), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        
        # Return value field directly
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitGETFIELD("GoString/value", StringType(), frame))
        
        strEmitter.printout(strEmitter.emitRETURN(StringType(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()
        
        # Generate setValue method
        frame = Frame("setValue", VoidType())
        strEmitter.printout(strEmitter.emitMETHOD("setValue", MType([StringType()], VoidType()), False, frame))
        frame.enterScope(True)
        
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "this", ClassType("GoString"), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitVAR(frame.getNewIndex(), "str", StringType(), 
                        frame.getStartLabel(), frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitLABEL(frame.getStartLabel(), frame))
        
        # Set value field
        strEmitter.printout(strEmitter.emitREADVAR("this", ClassType("GoString"), 0, frame))
        strEmitter.printout(strEmitter.emitREADVAR("str", StringType(), 1, frame))
        strEmitter.printout(strEmitter.emitPUTFIELD("GoString/value", StringType(), frame))
        
        # Return
        strEmitter.printout(strEmitter.emitLABEL(frame.getEndLabel(), frame))
        strEmitter.printout(strEmitter.emitRETURN(VoidType(), frame))
        strEmitter.printout(strEmitter.emitENDMETHOD(frame))
        frame.exitScope()
        
        # Close the file
        strEmitter.emitEPILOG()
        
        
        
    def inferValueConstant(self, ast): 
        if isinstance(ast, IntLiteral):
            if type(ast.value) is str:
                if ast.value.startswith("0x") or ast.value.startswith("0X"):
                    return int(ast.value, 16)
                elif ast.value.startswith("0b") or ast.value.startswith("0B"):
                    return int(ast.value, 2)
                elif ast.value.startswith("0o") or ast.value.startswith("0O"):
                    return int(ast.value, 8)
                return int(ast.value)
            return int(ast.value)
        elif isinstance(ast, FloatLiteral):
            return ast.value
        elif isinstance(ast, StringLiteral):
            return ast.value
        elif isinstance(ast, BooleanLiteral):
            return ast.value
        elif isinstance(ast, ArrayLiteral):
            return [self.inferValueConstant(x) for x in ast.value]
        elif isinstance(ast, BinaryOp):
            left = self.inferValueConstant(ast.left)
            right = self.inferValueConstant(ast.right)
            if ast.op == '+':
                return left + right
            elif ast.op == '-':
                return left - right
            elif ast.op == '*':
                return left * right
            elif ast.op == '/':
                return left / right
            elif ast.op == '%':
                return left % right
            elif ast.op == '==':
                return left == right
            elif ast.op == '!=':
                return left != right
            elif ast.op == '<':
                return left < right
            elif ast.op == '<=':
                return left <= right
            elif ast.op == '>':
                return left > right
            elif ast.op == '>=':
                return left >= right
        elif isinstance(ast, UnaryOp):
            value = self.inferValueConstant(ast.body)
            if ast.op == '-':
                return -value
            elif ast.op == '!':
                return not value
            
    def getDefaultValue(self, typ):
        if isinstance(typ, IntType):
            return IntLiteral(0)
        elif isinstance(typ, FloatType):
            return FloatLiteral(0.0)
        elif isinstance(typ, StringType):
            return StringLiteral("\"\"")
        elif isinstance(typ, BoolType):
            return BooleanLiteral(False)
        else:
            return NilLiteral()
    
    # FuncDecl: name, params List[ParamDecl], retType: Type ParamDecl: parName, parType: Type
    def checkPrototype(self, method: FuncDecl, proto: Prototype):
        if method.name != proto.name: return False
        if len(method.params) != len(proto.params): return False
        for p, q in zip(method.params, proto.params):
            if not type(p.parType) is type(q): return False
        if not type(method.retType) is type(proto.retType): return False
        return True
    # InterfaceType: name, methods: list[Prototype] Prototype: name, params: list[Types], rettype: Type
    # struct Methods: method: MethodDecl receiver: str, recType: Type, fun: FuncDecl
    def getInterfaceForStruct(self, structName):
        # structName: str
        # return list of interface name that struct implements
        
        structMethods = self.structMethods.get(structName, {}) # dict of method name and method decl
        implemented_interfaces = []
        for interfaceName, interface_ast in self.interfaceTypes.items():
            lst_proto = interface_ast.methods # list of prototype in interface
            flag = False
            for proto in lst_proto:
                for methodName, method in structMethods.items():
                    if methodName == proto.name and not self.checkPrototype(method.fun, proto):
                        flag = True
                        break
                if flag: break
            if not flag:
                implemented_interfaces.append(interfaceName)
        return implemented_interfaces
                
    
            
    def genInterface(self, interfaceName, methods, path):
        interfaceFile = self.path + "/" + interfaceName + ".j"
        interfaceEmit = Emitter(interfaceFile)
        
        # Generate interface class declaration
        interfaceEmit.printout(interfaceEmit.emitPROLOG(interfaceName, "java/lang/Object", isInterface=True))
        
        # Set class access flags for interface (.interface .public)
        interfaceEmit.printout(".class public abstract interface " + interfaceName + "\n")
        interfaceEmit.printout(".super java/lang/Object\n\n")
        
        # Generate method signatures for each method in the interface
        interface_ast = self.interfaceTypes[interfaceName]
        
        for method in interface_ast.methods:
            # Get method return type and parameters
            returnType = method.retType
            if isinstance(returnType, StringType):
                returnType = ClassType("GoString")
            elif isinstance(returnType, ArrayType) and isinstance(returnType.eleType, StringType):
                returnType.eleType = ClassType("GoString")
            paramTypes = []
            for p in method.params:
                typ = p
                if isinstance(typ, StringType):
                    typ = ClassType("GoString")
                elif isinstance(typ, ArrayType) and isinstance(typ.eleType, StringType):
                    typ.eleType = ClassType("GoString")
                paramTypes.append(typ)

            # Create method type object
            methodType = MType(paramTypes, returnType)
            
            # Create temporary frame for method
            tempFrame = Frame(method.name, returnType)
            
            # Generate method declaration manually with abstract keyword
            # This line replaces the call to emitMETHOD
            method_signature = ".method public abstract " + method.name + interfaceEmit.getJVMType(methodType) + "\n"
            interfaceEmit.printout(method_signature)
            
            # Generate method end directive
            interfaceEmit.printout(".end method\n\n")
        
        # Close the file
        interfaceEmit.emitEPILOG()
          
    def genStructClass(self, structName, fields, methods, path):
        classFile = self.path + "/" + structName + ".j"
        structEmit = Emitter(classFile)
        
        # Check if this struct implements any interfaces
        implemented_interfaces = self.getInterfaceForStruct(structName)
        structEmit.printout(structEmit.emitPROLOG(structName, "java/lang/Object", implemented_interfaces))
        
        # Generate fields
        for field in fields:
            fieldName, fieldType = field
            if isinstance(fieldType, StringType):
                fieldType = ClassType("GoString")
            if isinstance(fieldType, ArrayType) and isinstance(fieldType.eleType, StringType):
                fieldType.eleType = ClassType("GoString")
            structEmit.printout(structEmit.emitATTRIBUTE(fieldName, fieldType, True, False, None, isStruct=True))
        
        # Generate constructor
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
        # Generate methods
        for method in methods.values():
            # print("Method: ", method.fun.name)
            self.genStructMethod(method, structName, structEmit)
        
        structEmit.emitEPILOG()
    
    # MethodDecl: receiver: str, recType, fun: FuncDecl
    def genStructMethod(self, method, structName: str, structEmit: Emitter): 
        # method: MethodDecl
        # structName: str
        # structEmit: Emitter
        original_emitter = self.emit
        self.emit = structEmit
        original_className = self.className
        self.className = structName
        
        # Set up frame for method
        frame = Frame(method.fun.name, method.fun.retType)
        env = {}
        env[ENV] = [[]] + [self.env]  # list of symbol
        env[FRAME] = frame
        
        # Generate method code (similar to instance method in Java)
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
            intyp.append(param.parType)
            
        self.emit.printout(self.emit.emitMETHOD(method.fun.name, MType(intyp, ret), False, frame))
        
        frame.enterScope(True)
        
        # Add 'this' parameter as first parameter (receiver)
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this" , ClassType(structName), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        # Add other parameters
        for param in method.fun.params:
            idx = frame.getNewIndex()
            if isinstance(param.parType, StringType):
                param.parType = ClassType("GoString")
            self.emit.printout(self.emit.emitVAR(idx, param.parName, param.parType, frame.getStartLabel(), frame.getEndLabel(), frame))
            env[ENV][0] = [Symbol(param.parName, param.parType, Index(idx))] + env[ENV][0]
        
        # Add receiver parameter to environment
        env[ENV][0] = [Symbol(method.receiver, ClassType(structName), Index(0))] + env[ENV][0]
        
        # Generate method body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        
        # printSymbolList(env[ENV])
        # Visit method body
        self.visit(method.fun.body, env)
        
        # End of method
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        
        # If no explicit return statement in void method, add return
        if isinstance(method.fun.retType, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
            
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        
        # restore original emitter and class name
        self.emit = original_emitter
        self.className = original_className
    
    # this function is used to generate the method for function
    def genMethod(self, ast, o, frame): 
        # ast is FuncDecl
        # o : any
        # frame: Frame
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
            self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame)) # emit method init
        
        frame.enterScope(True) # enter scope of method
        glenv = o
        
        if isInit: # then init this
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isClinit: # for global var
            # print('Debug')
            # printSymbolList(o[ENV])
            marked = {}
            # printSymbolList(o[ENV])
            for global_var in o[ENV][-1]: 
                if global_var.name in marked: continue
                if isinstance(global_var.mtype, VarDecl):
                    init = global_var.mtype.varInit if global_var.mtype.varInit else self.getDefaultValue(global_var.mtype.varType)
                    if (isinstance(init, NilLiteral)): 
                        marked[global_var.name] = True
                        continue
                    code_init, type_init = self.visit(init, Access(frame, o[ENV], False))
                    if not global_var.mtype.varType:
                        global_var.mtype.varType = type_init
                    if type(global_var.mtype.varType) is Id:
                        global_var.mtype.varType = ClassType(global_var.mtype.varType.name)
                    code_init += self.emit.emitPUTSTATIC(f"{self.className}/{global_var.name}", global_var.mtype.varType, frame)
                    self.emit.printout(code_init)
                    # print("Code: ", code_init)
                    marked[global_var.name] = True
                elif isinstance(global_var.mtype, ConstDecl):
                    code_init, type_init = self.visit(global_var.mtype.iniExpr, Access(frame, o[ENV], False))
                    ast.conType = type_init
                    code_init += self.emit.emitPUTSTATIC(f"{self.className}/{global_var.name}", global_var.mtype.conType, frame)
                    self.emit.printout(code_init)
                    marked[global_var.name] = True
                
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else: # for normal function 
            # process parameters
            for param in ast.params:
                idx = frame.getNewIndex()
                if isinstance(param.parType, Id): # interface or struct
                    param.parType = ClassType(param.parType.name) 
                if isinstance(param.parType, StringType): # string type
                    param.parType = ClassType("GoString")
                if isinstance(param.parType, ArrayType) and isinstance(param.parType.eleType, StringType):
                    param.parType.eleType = ClassType("GoString")
                self.emit.printout(self.emit.emitVAR(idx, param.parName, param.parType, frame.getStartLabel(), frame.getEndLabel(), frame))
                o[ENV][0].append(Symbol(param.parName, param.parType, Index(idx)))
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame)) # start label
        if isInit: # for init method, we need to call super class constructor
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame)) # read this
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame)) # call super class constructor
        if not isClinit:
            body = ast.body
            self.visit(body, o) # visit body of function
            
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame)) # end label
        if type(return_typ) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame)) # end method
        frame.exitScope() # exit scope of method
            
    
    def visitProgram(self, ast, c):
        env = {}
        env[ENV] = [self.env] # list of symbol
        # temp_for_clinit = deepcopy(env) # for clinit method   
        self.genGoStringType() # generate GoString class
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        for decl in ast.decl:
            if isinstance(decl, VarDecl) or isinstance(decl, ConstDecl):
                env = self.visit(decl, env)
                # printSymbolList(env[ENV])
        for interfaceName, interface_ast in self.interfaceTypes.items():
            self.genInterface(interfaceName, interface_ast.methods, self.path)
        # Generate struct classes
        for structName, structDef in self.structTypes.items():
            self.genStructClass(structName, structDef.elements, self.structMethods.get(structName, {}), self.path)
        # Visit all declarations
        # gen for global var, const
        env[ENV] = [[]] + env[ENV] # add global var, const to the first scope
        for decl in ast.decl:
            if isinstance(decl, VarDecl) or isinstance(decl, ConstDecl):
                name_ = decl.varName if isinstance(decl, VarDecl) else decl.conName
                sym = None
                for s in env[ENV][-1]:
                    if s.name == name_ and (not isinstance(s.mtype, VarDecl) and not isinstance(s.mtype, ConstDecl)):
                        sym = s
                        break
                env[ENV][0].append(sym)  
            elif not isinstance(decl, StructType) and not isinstance(decl, MethodDecl) and not isinstance(decl, InterfaceType):
                env = self.visit(decl, env)
        # printSymbolList(env[ENV])
        self.genMethod(FuncDecl("<init>", [], VoidType(), Block([])), env, Frame("<init>", VoidType()))
        # Generate clinit method
        # for global var, const
        # printSymbolList(env[ENV])
        self.genMethod(FuncDecl("<clinit>", [], VoidType(), Block([])), env, Frame("<clinit>", VoidType()))
        # Close file
        # print(self.emit.buff)
        self.emit.printout(self.emit.emitEPILOG())
        return env


    # FuncDecl: name, params, retType, body
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
                params.append(param.parType)
            mtype = MType(params, ret)
        # Add function to environment
        c[ENV][0].append(Symbol(ast.name, mtype, CName(self.className)))
        c[FRAME] = frame
        self.genMethod(ast, c, frame) # generate method code
        
        return c
    
    def visitParamDecl(self, ast, o):
        idx = o[FRAME].getNewIndex()
        o[ENV][0] = [Symbol(ast.parName, ast.parType, Index(idx))] + o[ENV][0]
        return idx
    # Block: member: list[BlockMember]
    def visitBlock(self, ast, o):
        env = o.copy()
        frame = env[FRAME]
        env[ENV] = [[]] + env[ENV] # access block of function has another scope
        frame.enterScope(False) # enter scope of blockcl
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # Visit each statement in the block
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
                # if expr_code:  # Some statements return code directly
                #     self.emit.printout(expr_code)
            # print(stmt)
            # printSymbolList(env[ENV])
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
        
    def visitStructType(self, ast, o): pass
    
    # VarDecl: varName, varType, varInit
    def visitVarDecl(self, ast, o):
        if FRAME not in o: # global variable
            if ast.varInit:
                temp_frame = Frame("<init>", VoidType())
                # printSymbolList(o[ENV])
                code, typ = self.visit(ast.varInit, Access(temp_frame, o[ENV], False))
                if not ast.varType:
                    # print("Code: ", code)
                    ast.varType = typ
                if isinstance(ast.varType, StringType):
                    ast.varType = ClassType("GoString")
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, ""))
            o[ENV][0].append(Symbol(ast.varName, ast.varType, CName(self.className)))
        else: # local variable
            frame = o[FRAME]
            idx = frame.getNewIndex()
            code, typ = "", None
            if ast.varType and isinstance(ast.varType, ArrayType) and not ast.varInit:
                # Emit variable declaration
                if isinstance(ast.varType.eleType, StringType):
                    ast.varType.eleType = ClassType("GoString")
                self.emit.printout(self.emit.emitVAR(idx, ast.varName, ast.varType, 
                                frame.getStartLabel(), frame.getEndLabel(), frame))
                
                # Get dimensions from the array type
                dimensions = ast.varType.dimens
                element_type = ast.varType.eleType
                # Create array with default values
                if len(dimensions) == 1:
                    # For 1D array
                    size = dimensions[0].value if hasattr(dimensions[0], 'value') else dimensions[0]
                    # Push size onto stack
                    if isinstance(size, Id):
                        size = self.visit(size, Access(frame, o[ENV], False))[0]
                        self.emit.printout(size)
                    else:
                        self.emit.printout(self.emit.emitPUSHICONST(size, frame))
                    if isinstance(element_type, IntType) or isinstance(element_type, BoolType):
                        self.emit.printout(self.emit.jvm.emitNEWARRAY(self.emit.getFullType(element_type)))
                    elif isinstance(element_type, FloatType):
                        self.emit.printout(self.emit.jvm.emitNEWARRAY(self.emit.getFullType(element_type)))
                    else:
                        # Reference types
                        # print(element_type)
                        self.emit.printout(self.emit.jvm.emitANEWARRAY(self.emit.getFullType(element_type)))
                else:
                    # For multi-dimensional arrays (if needed)
                    # Push all dimensions onto stack
                    for dim in dimensions:
                        dim_value = dim.value if hasattr(dim, 'value') else dim
                        if isinstance(dim_value, Id):
                            dim_value = self.visit(dim_value, Access(frame, o[ENV], False))[0]
                            self.emit.printout(dim_value)
                        else:
                            self.emit.printout(self.emit.emitPUSHICONST(dim_value, frame))
                    
                    # Create multi-dimensional array
                    self.emit.printout(self.emit.emitNEWARRAY(ast.varType, frame))
                
                # Store array reference in local variable
                self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, idx, frame))
                
                # Add to environment
                o[ENV][0].append(Symbol(ast.varName, ast.varType, Index(idx)))
                return o
                
            # for struct type
            if ast.varType and isinstance(ast.varType, Id): # interface or struct
                # Convert Id to ClassType
                struct_name = ast.varType.name
                ast.varType = ClassType(struct_name)
                isStruct = struct_name in self.structTypes
                # Declare the variable
                self.emit.printout(self.emit.emitVAR(idx, ast.varName, ast.varType, 
                              frame.getStartLabel(), frame.getEndLabel(), frame))
                if not isStruct and not ast.varInit:
                    o[ENV][0].append(Symbol(ast.varName, ast.varType, Index(idx)))
                    return o
                if ast.varInit:
                    # If we have an initializer, use it directly
                    init_code, init_type = self.visit(ast.varInit, Access(frame, o[ENV], False))
                    self.emit.printout(init_code)
                elif isStruct:
                    # If no initializer, create default instance of struct
                    self.emit.printout(self.emit.emitNEW(struct_name, frame))
                    self.emit.printout(self.emit.emitDUP(frame))
                    self.emit.printout(self.emit.emitINVOKESPECIAL(frame, f"{struct_name}/<init>", MType([], VoidType())))
                    
                
                # Store struct reference in local variable
                self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, idx, frame))
                
                # Add to environment
                o[ENV][0].append(Symbol(ast.varName, ast.varType, Index(idx)))
                return o
                
            # For other types of variable declarations
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
            # Initialize if needed
            self.emit.printout(code)
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, idx, frame))
            o[ENV][0].append(Symbol(ast.varName, ast.varType, Index(idx)))
        return o
    
    def visitConstDecl(self, ast, o):
        if FRAME not in o: # global constant
            temp_frame = Frame("<init>", VoidType())
            code, typ = self.visit(ast.iniExpr, Access(temp_frame, o[ENV], False))
            ast.conType = typ
            self.emit.printout(self.emit.emitATTRIBUTE(ast.conName, ast.conType, True, True, ""))
            o[ENV][0].append(Symbol(ast.conName, ast.conType, CName(self.className)))
        else: # local constant
            frame = o[FRAME]
            idx = frame.getNewIndex()
            # Initialize
            code, typ_ = self.visit(ast.iniExpr, Access(frame, o[ENV], False))
            if isinstance(typ_, ArrayType) and isinstance(typ_.eleType, StringType):
                typ_.eleType = ClassType("GoString")
            ast.conType = typ_
            self.emit.printout(self.emit.emitVAR(idx, ast.conName, ast.conType, 
                              frame.getStartLabel(), frame.getEndLabel(), frame))
            self.emit.printout(code)
            self.emit.printout(self.emit.emitWRITEVAR(ast.conName, ast.conType, idx, frame))
                
            # Add to environment
            o[ENV][0] = [Symbol(ast.conName, ast.conType, Index(idx))] + o[ENV][0]
        return o
    
    
    
    
    def visitAssign(self, ast, o):
        frame = o[FRAME]
        env = o[ENV]
        # print(ast)
        # Special case for array cell assignments
        if isinstance(ast.lhs, ArrayCell):
            # Generate code for right-hand side value first (will be on stack)
            rc, rt = self.visit(ast.rhs, Access(frame, env, False))
            
            # Generate code for the array access (as LValue)
            lc, lt = self.visit(ast.lhs, Access(frame, env, True))
            # print("Left")
            # print(lc, lt)
            # print("Right")
            # print(rc, rt)
            # Type conversion if needed
            if isinstance(lt, FloatType) and isinstance(rt, IntType):
                rc += self.emit.emitI2F(frame)
            
            
            if isinstance(rt, ArrayType):
                # For array assignment, we need to store the value in the array cell
                # Load the array reference and index from the stack
                # print("lcode: ", lc)
                # print("rcode: ", rc)
                # Store the value in the array cell
                store_code = self.emit.emitASTORE(rt, frame)
                # Generate code to store the value in the array cell
                return lc + rc + store_code, VoidType()
            store_code = self.emit.emitASTORE(lt, frame) 
                
            return lc + rc + store_code, VoidType()
        
        if isinstance(ast.lhs, FieldAccess): 
            """ format of store with field access 
            a_load -> load addr of obj
            rhs code -> load value of rhs
            putField -> store value in field
            lc return as [aload, putField]
            rc return as [list(code to calculate value of rhs)]
            """
            rc, rt = self.visit(ast.rhs, Access(frame, env, False))
            lc, lt = self.visit(ast.lhs, Access(frame, env, True))
            # print(rc)
            # print(lc)
            # print(type(lc))
            # print(type(rc))
            lst_codes = lc.split('\n')
            # print(lst_codes)
            if isinstance(rt, ClassType) and rt.name == "GoString":
                rc, rt = self.visit(ast.rhs, Access(frame, env, False))
                lc, lt = self.visit(ast.lhs, Access(frame, env, False))
                lst_codes = lc.split('\n')
                struct_name = lst_codes[1].split(' ')[1].split('/')[0]
                get_field = self.emit.emitGETFIELD(f"{struct_name}/{ast.lhs.field}", rt, frame)
                get_val = self.emit.emitINVOKEVIRTUAL(f"{rt.name}/getValue", MType([], StringType()), frame)
                set_val = self.emit.emitINVOKEVIRTUAL(f"{rt.name}/setValue", MType([StringType()], VoidType()), frame)
                return lst_codes[0] + "\n " + get_field + "\n" + rc + "\n"+get_val +"\n" + set_val + "\n", VoidType()
            rst_codes = rc.split('\n')
            load = lst_codes[0]
            store = lst_codes[1]
            # print(load + "\n" + val + "\n" + store + "\n")
            return load + "\n" + rc + "\n" + store + "\n", VoidType()
            
            
        # Regular variable assignment handling (no changes)
        # Generate code for right-hand side
        rc, rt = self.visit(ast.rhs, Access(frame, env, False))
        
        # Check if LHS is an implicit declaration
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
        # ensure that the type of LHS and RHS are compatible
        if not flag and isinstance(ast.lhs, Id): # implicit declaration
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, ast.lhs.name, rt, 
                              frame.getStartLabel(), frame.getEndLabel(), frame))
            env[0].append(Symbol(ast.lhs.name, rt, Index(idx)))
            code = self.emit.emitWRITEVAR(ast.lhs.name, rt, idx, frame)
            return rc + code, rt
        else: # normal assignment
            lc, lt = self.visit(ast.lhs, Access(frame, env, True))
            if isinstance(lt, ArrayType) and isinstance(rt, ArrayType):
                i2f = (isinstance(lt.eleType, FloatType) and isinstance(rt.eleType, IntType))
                rc, rt = self.visit(ast.rhs, Access(frame, env, False, i2f))
                return rc + lc, VoidType()
            if isinstance(lt, ClassType) and lt.name == "GoString":
                lc, _ = self.visit(ast.lhs, Access(frame, env, False))
                rc, rt = self.visit(ast.rhs, Access(frame, env, False))
                # dup_ = self.emit.emitDUP(frame)
                get_val = self.emit.emitINVOKEVIRTUAL(f"{lt.name}/getValue", MType([], StringType()), frame)
                set_val = self.emit.emitINVOKEVIRTUAL(f"{lt.name}/setValue", MType([StringType()], VoidType()), frame)
                return lc + rc  + get_val + set_val, VoidType()
            # Type conversion if needed
            if isinstance(lt, FloatType) and isinstance(rt, IntType):
                rc += self.emit.emitI2F(frame)
                
            return rc + lc, VoidType()
        
        
        
        
    def visitIf(self, ast, o):
        frame = o[FRAME]
        env = o[ENV]
        
        # Generate code for condition
        cond_code, cond_type = self.visit(ast.expr, Access(frame, env, False))
        self.emit.printout(cond_code)
        
        # Labels for branching
        falseLabel = frame.getNewLabel()
        endLabel = frame.getNewLabel()
        
        # If false, jump to falseLabel
        self.emit.printout(self.emit.emitIFFALSE(falseLabel, frame))
        
        # Generate code for 'then' branch
        if isinstance(ast.thenStmt, Block):
            # For block statements, we need to create a new label for the block
            blockLabel = frame.getNewLabel()
            self.emit.printout(self.emit.emitLABEL(blockLabel, frame))
            self.visit(ast.thenStmt, o)
        else:
            self.visit(ast.thenStmt, o)
        
        # Jump to end after executing 'then'
        if ast.elseStmt:
            self.emit.printout(self.emit.emitGOTO(endLabel, frame))
            
            # False label - this is where we jump if condition is false
            self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
            
            if isinstance(ast.elseStmt, If):
                # Handle "else if" by visiting the If statement directly
                # The nested If will handle its own labels
                self.visit(ast.elseStmt, o)
            elif isinstance(ast.elseStmt, Block):
                # For block statements, we need to create a new label for the block
                blockLabel = frame.getNewLabel()
                self.emit.printout(self.emit.emitLABEL(blockLabel, frame))
                self.visit(ast.elseStmt, o)
            else:
                # Handle regular else statements
                self.visit(ast.elseStmt, o)
            
            # End label - all branches jump here when done
            self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        else:
            # No else branch, so false condition jumps to end
            self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
            # For completeness/clarity, also emit the end label
            self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        
        return o
        
    
    # cond: Expr, loop: Block
    def visitForBasic(self, ast, o):
        frame = o[FRAME]
        env = o[ENV]
        
        # Enter loop
        frame.enterLoop()
        
        # Get labels
        continueLabel = frame.getContinueLabel()
        breakLabel = frame.getBreakLabel()
        
        # Start label
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
        
        # Condition check
        cond_code, _ = self.visit(ast.cond, Access(frame, env, False))
        self.emit.printout(cond_code)
        self.emit.printout(self.emit.emitIFFALSE(breakLabel, frame))
        
        # Loop body
        self.visit(ast.loop, o)
        
        # Go back to start
        self.emit.printout(self.emit.emitGOTO(continueLabel, frame))
        
        # Break label
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))
        
        # Exit loop
        frame.exitLoop()
        
        return o
    
    
    def visitForStep(self, ast, o):
        # Get the frame from the environment
        frame = o[FRAME]
        
        # Enter loop in the frame
        frame.enterLoop()
        
        # Create a new frame for the loop to ensure proper variable scoping
        loop_start_label = frame.getNewLabel()
        loop_end_label = frame.getNewLabel()
        # print(loop_start_label, loop_end_label)
        cond_label = frame.getNewLabel()
        body_label = frame.getNewLabel()
        update_label = frame.getContinueLabel()
        end_label = frame.getBreakLabel()
        
        # Create a new environment with a new scope for the loop
        # This is critical to ensure variables in the loop don't conflict with outer variables
        loop_env = {}
        loop_env[FRAME] = frame
        loop_env[ENV] = [[]] + o[ENV]
        
        # Start the loop scope
        self.emit.printout(self.emit.emitLABEL(loop_start_label, frame))
        name_i = ast.init.varName if isinstance(ast.init, VarDecl) else ast.init.lhs.name
        if isinstance(ast.init, VarDecl):
            rc, rt = self.visit(ast.init.varInit, Access(frame, loop_env, False))
            ast.init.varType = rt
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, name_i, rt, loop_start_label, loop_end_label, frame))
            loop_env[ENV][0].append(Symbol(name_i, rt, Index(idx)))
            code = self.emit.emitWRITEVAR(name_i, rt, idx, frame)
            self.emit.printout(rc + code)
        else:
            rc, rt = self.visit(ast.init.rhs, Access(frame, loop_env, False))
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, name_i, rt, loop_start_label, loop_end_label, frame))
            loop_env[ENV][0].append(Symbol(name_i, rt, Index(idx)))
            code = self.emit.emitWRITEVAR(name_i, rt, idx, frame)
            self.emit.printout(rc + code)
            
        # Condition check
        self.emit.printout(self.emit.emitLABEL(cond_label, frame))
        cond_code, _ = self.visit(ast.cond, Access(frame, loop_env[ENV], False))
        self.emit.printout(cond_code)
        self.emit.printout(self.emit.emitIFFALSE(end_label, frame))
        self.emit.printout(self.emit.emitGOTO(body_label, frame))
        
        # Update statement (continue jumps here)
        self.emit.printout(self.emit.emitLABEL(update_label, frame))
        update_code, _ = self.visit(ast.upda, loop_env)  # Use loop environment
        self.emit.printout(update_code)
        self.emit.printout(self.emit.emitGOTO(cond_label, frame))
        
        # Body
        self.emit.printout(self.emit.emitLABEL(body_label, frame))
        
        if isinstance(ast.loop, Block):
            self.visit(ast.loop, loop_env)
        
        # After body execution, go to update
        self.emit.printout(self.emit.emitGOTO(update_label, frame))
        
        # End labels
        self.emit.printout(self.emit.emitLABEL(end_label, frame))
        self.emit.printout(self.emit.emitLABEL(loop_end_label, frame))
        
        # Exit loop
        frame.exitLoop()
        
        # Keep original environment unchanged
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
        
        # If return has expression, generate code for it
        if ast.expr:
            expr_code, expr_type = self.visit(ast.expr, Access(frame, env, False))
            # print(expr_code, expr_type)
            result.append(expr_code)
            # Type conversion if needed (int to float)
            if isinstance(frame.returnType, FloatType) and isinstance(expr_type, IntType):
                result.append(self.emit.emitI2F(frame))
            # Return value
            if isinstance(frame.returnType, Id):
                frame.returnType = ClassType(frame.returnType.name)
            result.append(self.emit.emitRETURN(frame.returnType, frame))
            self.emit.printout(''.join(result))
        
    # FieldAccess: receiver: Expr, field: str
    def visitFieldAccess(self, ast, o):
        frame = o.frame
        env = o.sym
        isLeft = o.isLeft
        
        # Visit receiver to get object reference
        rec_code, rec_type = self.visit(ast.receiver, Access(frame, env, False))
        
        # Get field information
        struct_name = rec_type.name if isinstance(rec_type, ClassType) else rec_type.name
        field_type = None
        
        # Find field type in struct
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
        
        # Generate appropriate field access code
        if isLeft:  # LHS (write)
            return rec_code + self.emit.emitPUTFIELD(f"{struct_name}/{ast.field}", field_type, frame), field_type
        else:  # RHS (read)
            return rec_code + self.emit.emitGETFIELD(f"{struct_name}/{ast.field}", field_type, frame), field_type
        
    def visitBinaryOp(self, ast, o):
        frame = o.frame
        env = o.sym
        # Short circuit for boolean operators
        if ast.op == '&&' or ast.op == '||':
            end_label = frame.getNewLabel()
            
            # Generate code for left operand
            left_code, left_type = self.visit(ast.left, Access(frame, env, False))
            result = []
            result.append(left_code)
            
            # Duplicate the result of left operand for final result
            result.append(self.emit.emitDUP(frame))
            
            if ast.op == '&&':
                # For AND: If left is false, skip right operand (short-circuit to end)
                result.append(self.emit.emitIFFALSE(end_label, frame))
                
                # Pop the duplicate value (we'll replace it with the final result)
                result.append(self.emit.emitPOP(frame))
                
                # Evaluate right operand
                right_code, right_type = self.visit(ast.right, Access(frame, env, False))
                result.append(right_code)
            else:  # ast.op == '||'
                # For OR: If left is true, skip right operand (short-circuit to end)
                result.append(self.emit.emitIFTRUE(end_label, frame))
                
                # Pop the duplicate value (we'll replace it with the final result)
                result.append(self.emit.emitPOP(frame))
                
                # Evaluate right operand
                right_code, right_type = self.visit(ast.right, Access(frame, env, False))
                result.append(right_code)
                
            
            # End label for short-circuit paths
            result.append(self.emit.emitLABEL(end_label, frame))
            
            return ''.join(result), BoolType()
        # Generate code for operands
        left_code, left_type = self.visit(ast.left, Access(frame, env, False))
        right_code, right_type = self.visit(ast.right, Access(frame, env, False))
        
        # Determine result type
        result_type = left_type
        if isinstance(left_type, FloatType) or isinstance(right_type, FloatType):
            result_type = FloatType()
            
            # Type conversion if needed
            if isinstance(left_type, IntType):
                left_code += self.emit.emitI2F(frame)
            if isinstance(right_type, IntType):
                right_code += self.emit.emitI2F(frame)
                
        # Generate operator code
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
        
        # Generate code for operand
        body_code, body_type = self.visit(ast.body, Access(frame, env, False))
        # Generate operator code
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
        # Find function in environment
        func_sym = None
        for scope in env:
            for sym in scope:
                if sym.name == ast.funName:
                    func_sym = sym
                    break
            if func_sym:
                break
        # Generate code for arguments
        args_code = ""
        for arg in ast.args:
            arg_code, arg_type = self.visit(arg, Access(frame, env, False, False))
            if isinstance(arg_type, ClassType) and arg_type.name == "GoString" and (ast.funName == "putString" or ast.funName =="putStringLn"): arg_code += self.emit.emitINVOKEVIRTUAL("GoString/getValue", MType([], StringType()), frame)
            args_code += arg_code
            # Type conversion if needed
            if len(func_sym.mtype.partype) > 0 and isinstance(func_sym.mtype.partype[0], FloatType) and isinstance(arg_type, IntType):
                args_code += self.emit.emitI2F(frame)
        
        # Call function
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
            # ensure o is dict
            frame = o[FRAME]
            env = o[ENV]
            return {ENV: env, FRAME: frame}
        else:
            return (args_code + call_code, func_sym.mtype.rettype)
        
    def visitMethCall(self, ast, o):
        frame = o[FRAME] if isinstance(o, dict) else o.frame
        env = o[ENV] if isinstance(o, dict) else o.sym
        # Generate code for receiver
        rec_code, rec_type = self.visit(ast.receiver, Access(frame, env, False))
        
        # Find method in struct
        struct_name = rec_type.name if isinstance(rec_type, ClassType) else rec_type.name
        
        method = None
        isStruct = struct_name in self.structTypes
        
        # #interfaceTypes: dict
        # key: name of interface
        # value: ast of InterfaceType()
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
            
        # Generate code for arguments
        arg_codes = [rec_code]  # First argument is receiver
        for arg in ast.args:
            arg_code, arg_type = self.visit(arg, Access(frame, env, False))
            arg_codes.append(arg_code)
            
            # Type conversion if needed - would need to check parameter types
            
        # Combine argument codes
        args_code = ''.join(arg_codes)
        method_type = None
        ret = None
        # Get method type
        if isStruct:
            inp = []
            for param in method.fun.params:
                if isinstance(param.parType, StringType):
                    inp.append(ClassType("GoString"))
                elif isinstance(param.parType, ArrayType) and isinstance(param.parType.eleType, StringType):
                    inp.append(ArrayType(param.parType.dimens, ClassType("GoString")))
                else:
                    inp.append(param.parType)
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
                    inp.append(ClassType("GoString"))
                elif isinstance(param, ArrayType) and isinstance(param.eleType, StringType):
                    inp.append(ArrayType(param.dimens, ClassType("GoString")))
                else:
                    inp.append(param)
            ret = method.retType
            if isinstance(ret, StringType):
                ret = ClassType("GoString")
            elif isinstance(ret, ArrayType) and isinstance(ret.eleType, StringType):
                ret = ArrayType(ret.dimens, ClassType("GoString"))
            method_type = MType(inp, ret)
        # Call method
        if isStruct:
            call_code = self.emit.emitINVOKEVIRTUAL(
                f"{struct_name}/{ast.metName}", method_type, frame)
        else: 
            call_code = self.emit.emitINVOKEINTERFACE(
                f"{struct_name}/{ast.metName}", method_type, frame, len(method.params) + 1)
        if isStruct:
            return args_code + call_code, ret
        else:
            return args_code + call_code, ret
            
    # ArrayCell: arr: Expr, idx: List[Expr]
    def visitArrayCell(self, ast, o):
        frame = o.frame
        env = o.sym
        isLeft = o.isLeft
        
        # Get the array reference and its type
        arr_code, arr_type = self.visit(ast.arr, Access(frame, env, False))
        result = arr_code
        
        # For multi-dimensional arrays
        current_type = arr_type
        # print("ArrayCell: ", current_type)  
        if type(current_type.eleType) is StringType:
            current_type.eleType = ClassType("GoString")
        
        # Process each dimension
        for i in range(len(ast.idx)):
            # Generate code for this index
            idx_code, _ = self.visit(ast.idx[i], Access(frame, env, False))
            result += idx_code
            
            # If not the last index, load the subarray
            if i < len(ast.idx) - 1:
                result += self.emit.emitALOAD(current_type, frame)
                # Update current_type for the next dimension
                # if isinstance(current_type, ArrayType):
                #     current_type = current_type.eleType
        
        # For loading (reading): array reference → index → value
        # For storing (writing): array reference → index → value to store
        # For RHS (reading), add the load instruction
        # For LHS (writing), don't add the load - we'll store the value later
        if not isLeft:
            if isinstance(current_type, ArrayType):
                result += self.emit.emitALOAD(current_type.eleType, frame)
                return result, current_type.eleType
            else:
                result += self.emit.emitALOAD(current_type, frame)
                return result, current_type
        
        # Return the element type for writing operations
        if isinstance(current_type, ArrayType):
            return result, current_type.eleType
        else:
            return result, current_type
    
    
    # ArrayLiteral: dimens: List[Expr], eleType: Type, value: NestedList 
    def visitArrayLiteral(self, ast, o):
        frame = o.frame
        env = o.sym
        isArrayFloat = o.isArrayFloat
        result = []
        if isinstance(ast.eleType, IntType) and isArrayFloat:
                ast.eleType = FloatType()
        if isinstance(ast.eleType, StringType):
            ast.eleType = ClassType("GoString")
        # Push dimensions onto stack - for multianewarray
        for dim in ast.dimens:
            dim_code, _ = self.visit(dim, Access(frame, env, False))
            result.append(dim_code)
        
        # Create the array with all dimensions at once
        if len(ast.dimens) > 1:
            # Multi-dimensional array
            array_type = ArrayType(ast.dimens, ast.eleType)
            result.append(self.emit.emitNEWARRAY(array_type, frame))
        else:
            # 1D array
            if isinstance(ast.eleType, (IntType, FloatType, BoolType)):
                # Primitive type array
                result.append(self.emit.jvm.emitNEWARRAY(self.emit.getFullType(ast.eleType)))
            else:
                # print(ast.eleType)
                # Reference type array
                result.append(self.emit.emitNEWARRAY(ast, frame))
        
        # Helper function to initialize array elements recursively
        def init_nested_array(values, current_indices=[]):
            if not isinstance(values, list):
                # Base case: this is a value to store
                # Duplicate the array reference
                result.append(self.emit.jvm.emitDUP())
                
                # Navigate to the right position in the array
                for i, idx in enumerate(current_indices[:-1]):
                    result.append(self.emit.emitPUSHICONST(idx, frame))
                    result.append(self.emit.jvm.emitAALOAD())
                
                # Push the final index
                result.append(self.emit.emitPUSHICONST(current_indices[-1], frame))
                
                # Push the value and store it
                val_code, val_type = self.visit(values, Access(frame, env, False))
                result.append(val_code)
                
                # Type conversion if needed
                if isinstance(ast.eleType, FloatType) and isinstance(val_type, IntType):
                    result.append(self.emit.emitI2F(frame))
                
                # Store the value
                if isinstance(ast.eleType, IntType):
                    result.append(self.emit.jvm.emitIASTORE())
                elif isinstance(ast.eleType, BoolType):
                    result.append(self.emit.jvm.emitBASTORE())
                elif isinstance(ast.eleType, FloatType):
                    result.append(self.emit.jvm.emitFASTORE())
                elif isinstance(ast.eleType, StringType) or isinstance(ast.eleType, ArrayType) or isinstance(ast.eleType, ClassType):
                    result.append(self.emit.jvm.emitAASTORE())
                else:
                    result.append(self.emit.jvm.emitAASTORE())
                return
            
            # Recursive case: handle nested arrays
            for i, item in enumerate(values):
                init_nested_array(item, current_indices + [i])
        
        # Start initialization from the outermost array
        init_nested_array(ast.value)
        
        return ''.join(result), ArrayType(ast.dimens, ast.eleType)
    
    # StructLiteral: name, elements: List[Tuple[str, Expr]]
    def visitStructLiteral(self, ast, o):
        frame = o.frame
        env = o.sym
        result = []
        
        # Create a new struct instance
        # new -> dup -> invoke special init
        result.append(self.emit.emitNEW(ast.name, frame))
        result.append(self.emit.emitDUP(frame))
        result.append(self.emit.emitINVOKESPECIAL(frame, f"{ast.name}/<init>", MType([], VoidType())))
        
        # Create a dictionary of explicitly initialized fields
        initialized_fields = {field_name: field_expr for field_name, field_expr in ast.elements}
        # print(initialized_fields)
        # Get all fields from the struct definition
        if ast.name in self.structTypes:
            struct_def = self.structTypes[ast.name]
            
            # Initialize all fields in the struct, using default values for uninitialized primitive types
            for field_name, field_type in struct_def.elements:
                # Check if field should be initialized (skip uninitialized complex types)
                if field_name not in initialized_fields:
                    # Skip default initialization for complex types (structs, interfaces, arrays)
                    if isinstance(field_type, Id) or isinstance(field_type, ArrayType):
                        continue
                    
                    # For primitive types, initialize with default values
                    result.append(self.emit.emitDUP(frame))  # Duplicate struct reference
                    
                    # Generate default value based on field type
                    default_val = self.getDefaultValue(field_type)
                    default_code, default_type = self.visit(default_val, Access(frame, env, False))
                    result.append(default_code)
                    
                    if isinstance(field_type, Id):
                        field_type = ClassType(field_type.name)
                    if isinstance(field_type, StringType):
                        field_type = ClassType("GoString")
                        
                    # Store default value in field
                    result.append(self.emit.emitPUTFIELD(f"{ast.name}/{field_name}", field_type, frame))
                else:
                    # Field is explicitly initialized, use the provided value
                    result.append(self.emit.emitDUP(frame))  # Duplicate struct reference
                    # print(initialized_fields[field_name])
                    # Generate field value
                    expr_code, expr_type = self.visit(initialized_fields[field_name], Access(frame, env, False))
                    result.append(expr_code)
                    
                    # Find field type
                    if isinstance(field_type, FloatType) and isinstance(expr_type, IntType):
                        result.append(self.emit.emitI2F(frame))
                    if isinstance(field_type, Id):
                        field_type = ClassType(field_type.name)
                    if isinstance(field_type, StringType):
                        result.append(self.emit.emitPUTFIELD(f"{ast.name}/{field_name}",ClassType("GoString"), frame))
                        continue
                    # Store field
                    result.append(self.emit.emitPUTFIELD(f"{ast.name}/{field_name}", field_type, frame))
            
        return ''.join(result), ClassType(ast.name)
        
    def visitId(self, ast, o):
        frame = o.frame
        env = o.sym
        isLeft = o.isLeft
        # printSymbolList(env)
        # Find the identifier in the environment
        for scope in env:
            for sym in scope:
                if sym.name == ast.name and not isinstance(sym.mtype, VarDecl) and not isinstance(sym.mtype, ConstDecl):
                    if type(sym.mtype) is Id:
                        sym.mtype = ClassType(sym.mtype.name)

                    if isLeft:  # LHS (write)
                        if isinstance(sym.value, Index):
                            return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, frame), sym.mtype
                        else:
                            return self.emit.emitPUTSTATIC(f"{sym.value.value}/{sym.name}", sym.mtype, frame), sym.mtype
                    else:  # RHS (read)
                        if isinstance(sym.value, Index):
                            return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, frame), sym.mtype
                        else:
                            return self.emit.emitGETSTATIC(f"{sym.value.value}/{sym.name}", sym.mtype, frame), sym.mtype
        
    def visitIntLiteral(self, ast, o):
        val_ = ast.value
        if isinstance(val_, str):
            if val_.startswith("0x") or val_.startswith("0X"):
                val_ = int(val_, 16)
            elif val_.startswith("0b") or val_.startswith("0B"):
                val_ = int(val_, 2)
            elif val_.startswith("0o") or val_.startswith("0O"):
                val_ = int(val_, 8)
        return self.emit.emitPUSHICONST(val_, o.frame), IntType()
        
    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), FloatType()
        
    def visitStringLiteral(self, ast, o):
        frame = o.frame
        # Create a new GoString with the string literal
        result = []
        result.append(self.emit.emitNEW("GoString", frame))
        result.append(self.emit.emitDUP(frame))
        result.append(self.emit.emitPUSHCONST(ast.value, StringType(), frame))
        result.append(self.emit.emitINVOKESPECIAL(frame, "GoString/<init>", MType([StringType()], VoidType())))
        return ''.join(result), ClassType("GoString")
        
    def visitBooleanLiteral(self, ast, o):
        # Handle both string 'true'/'false' and boolean True/False
        value = ast.value
        if isinstance(value, str):
            value = value.lower() == 'true'
        return self.emit.emitPUSHICONST(1 if value else 0, o.frame), BoolType()
    def visitNilLiteral(self, ast, o):
        return self.emit.jvm.emitPUSHNULL(), VoidType()
    def visitForEach(self, ast, o): return o

