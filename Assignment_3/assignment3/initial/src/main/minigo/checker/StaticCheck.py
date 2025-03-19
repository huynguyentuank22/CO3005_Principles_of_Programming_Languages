"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
# from Utils import Utils
from StaticError import *
from functools import reduce

"""
c = [Local(0), NonLocal(1), NonLocal(2),..., Global(N), BuiltIn()]
Local(i) = [Symbol(1), Symbol(2),..., Symbol(n)]
"""
class Utils:
    def lookupRedeclared(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None
    
    def lookupUndeclared(self,name,lst,func):
        for x in lst:
            for y in x:
                if name == func(y):
                    return y
        return None
    
    def printStack(self, env):
        print('======STACK======')
        for i in env:
            print('======')
            for j in i:
                print(str(j))
    
class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [Symbol("getInt",MType([],IntType())),
                            Symbol("putInt",MType([IntType()],VoidType())),
                            Symbol("putIntLn",MType([IntType()],VoidType())),
                            Symbol("getFloat",MType([],FloatType())),
                            Symbol("putFloat",MType([FloatType()],VoidType())),
                            Symbol("putFloatLn",MType([FloatType()],VoidType())),
                            Symbol("getBool",MType([],BoolType())),
                            Symbol("putBool",MType([BoolType()],VoidType())),
                            Symbol("putBoolLn",MType([BoolType()],VoidType())),
                            Symbol("getString",MType([],StringType())),
                            Symbol("putString",MType([StringType()],VoidType())),
                            Symbol("putStringLn",MType([StringType()],VoidType())),
                            Symbol("putLn",MType([],VoidType()))]
 
    
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        env = [[]] + [c]
        scope = reduce(lambda acc,ele: self.visit(ele,acc), ast.decl, env)
        # print("\n=== Global Scope Symbols ===")
        # for x in scope:
        #     print(str(x))
        # return [c] 

    def visitVarDecl(self, ast, c):
        res = self.lookupRedeclared(ast.varName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.varName) 
        if ast.varInit:
            initType = self.visit(ast.varInit, c)
            if ast.varType is None:
                ast.varType = initType
            if not type(ast.varType) is type(initType):
                raise TypeMismatch(ast)
        return [c[0] + [Symbol(ast.varName, ast.varType)]] + c[1:]
        
    def visitConstDecl(self, ast, c):
        res = self.lookupRedeclared(ast.conName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Constant(), ast.conName)
        conType = self.visit(ast.iniExpr, c)
        if ast.conType is None:
            ast.conType = conType
        return [c[0] + [Symbol(ast.conName, ast.conType,ast.iniExpr)]] + c[1:]

    def visitFuncDecl(self,ast, c):
        res = self.lookupRedeclared(ast.name, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)
        
        # add func name to env
        env = [c[0] + [Symbol(ast.name, ast.retType)]] + c[1:]
        if ast.params:
            env = [[]] + env
            env = reduce(lambda acc, ele: self.visit(ele, acc), ast.params, env)

        self.visit(ast.body, env)
        return env

    def visitMethodDecl(self,ast, c):
        try:
            self.visit(ast.fun, c)
        except Redeclared:
            raise Redeclared(Method(), ast.fun.name)

        # res = self.lookupUndeclared(ast.recType, c, lambda x: x.name)
        # if res:
            # flag = self.lookupRedeclared(ast.fun.name, res.mtype, lambda x: x)
            # if flag:
            #     raise Redeclared(Method(), flag)
            # res.mtype += ast.fun.name
        # self.printStack(c)
        for _, x in enumerate(c):
            for _, y in enumerate(x):
                # print(ast.recType)
                if ast.recType.name == y.name:
                    for _, z in enumerate(y.mtype):
                        if ast.fun.name == z.partype:
                            raise Redeclared(Method(), ast.fun.name)
                    y.mtype.append(MType(ast.fun.name, ast.fun.retType))
                    break
        # self.printStack(c)
        # env = [c[0] + [Symbol(ast.fun.name, ast.fun.retType)]] + c[1:]
        # if ast.fun.params:
        #     env = [[]] + env
        #     env = reduce(lambda acc, ele: self.visit(ele, acc), ast.fun.params, env)

        # self.visit(ast.fun.body, env)
        # return [c[0] + [Symbol(ast.fun.name, ast.fun.retType)]] + c[1:]        

        return c
        

    def visitStructType(self,ast, c):
        if self.lookupRedeclared(ast.name, c[0], lambda x: x.name):
            raise Redeclared(Type(), ast.name)
        
        env = [c[0] + [Symbol(ast.name, ast.methods)]] + c[1:]
        for mem in ast.elements:
            if self.lookupRedeclared(mem[0], env[0][-1].mtype, lambda x: x.partype):
                raise Redeclared(Field(), mem[0])
            env[0][-1].mtype.append(MType(mem[0], mem[1])) 

        return env

    def visitInterfaceType(self,ast, c):
        if self.lookupRedeclared(ast.name, c[0], lambda x: x.name):
            raise Redeclared(Type(), ast.name)
        
        env = [c[0] + [Symbol(ast.name, ast.methods)]] + c[1:]
        scope = reduce(lambda acc, ele: self.visit(ele, acc), ast.methods, [])
        env[0][-1].mtype = scope
        return env
    
    def visitParamDecl(self,ast, c):
        res = self.lookupRedeclared(ast.parName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Parameter(), ast.parName)
        return [c[0] + [Symbol(ast.parName, ast.parType)]] + c[1:]
    
    def visitPrototype(self,ast, c):
        res = self.lookupRedeclared(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Prototype(), ast.name)
        return c + [Symbol(ast.name, MType(ast.params, ast.retType))]
        # return [c[0] + [Symbol(ast.name, MType(ast.params, ast.retType))]] + c[1:]
    
    def visitBlock(self, ast, c):
        env = [[]] + c
        reduce(lambda acc, ele: self.visit(ele, acc), ast.member, env)
        # return env

    def visitFuncCall(self,ast, c):
        res = self.lookupUndeclared(ast.funName, c, lambda x: x.name)
        if res is None:
            raise Undeclared(Function(), ast.funName)
    
    def visitMethCall(self,ast, c):
        res = self.lookupUndeclared(ast.metName, c, lambda x: x.name)
        if res is None:
            raise Undeclared(Method(), ast.metName)

    def visitIntLiteral(self,ast, c):
        return IntType()
    
    def visitFloatLiteral(self,ast, c):
        return FloatType()
    
    def visitStringLiteral(self,ast, c):
        return StringType()
    
    def visitBooleanLiteral(self,ast, c):
        return BoolType()
    
    def visitId(self,ast,c):
        res = self.lookupUndeclared(ast.name, c, lambda x: x.name) # ast.name in x
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        return res.mtype

    def visitReturn(self,ast,c):
        pass