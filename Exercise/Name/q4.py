from abc import ABC, abstractmethod

class Program: #decl:List[Decl]
    pass
class Decl(ABC): #abstract class
    pass
class VarDecl(Decl): #name:str,typ:Type
    pass
class ConstDecl(Decl): #name:str,val:Lit
    pass
class FuncDecl(Decl): #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])
    pass
class Type(ABC): #abstract class
    pass
class IntType(Type):
    pass
class FloatType(Type):
    pass
class Expr(ABC): #abstract class
    pass
class Lit(Expr): #abstract class
    pass
class IntLit(Lit): #val:int
    pass
class Id(Expr): #name:str
    pass

class RedeclaredVariable(Exception): #name:str
    pass
class RedeclaredConstant(Exception): #name:str
    pass
class RedeclaredFunction(Exception): #name:str
    pass
class UndeclaredIdentifier(Exception): #name:str
    pass

from functools import reduce
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o:object):
        reduce(lambda acc, ele: self.visit(ele,acc), ctx.decl, [[]])

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredVariable(ctx.name)
        return [o[0] + [ctx.name]] + o[1:]
    
    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredConstant(ctx.name)
        return [o[0] + [ctx.name]] + o[1:]
    
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredFunction(ctx.name)
        env = [[]] + [o[0] + [ctx.name]] + o[1:]
        env = reduce(lambda acc, ele: self.visit(ele,acc), ctx.param + ctx.body[0], env)
        reduce(lambda acc, ele: self.visit(ele,env), ctx.body[1], env)
        return [o[0] + [ctx.name]] + o[1:]
    
    def visitIntType(self,ctx:IntType,o:object):
        pass
    def visitFloatType(self,ctx:FloatType,o:object):
        pass
    def visitIntLit(self,ctx:IntLit,o:object):
        pass
    def visitId(self,ctx:Id,o:object):
        env = next(filter(lambda x: ctx.name in x, o), False)
        if not env:
            raise UndeclaredIdentifier(ctx.name)