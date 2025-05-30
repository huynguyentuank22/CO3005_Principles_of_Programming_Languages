from abc import ABC, abstractmethod

class Program: #decl:List[Decl]
    pass
class Decl(ABC): #abstract class
    pass
class VarDecl(Decl): #name:str,typ:Type
    pass
class ConstDecl(Decl): #name:str,val:Lit
    pass
class Type(ABC): #abstract class
    pass
class IntType(Type):
    pass
class FloatType(Type):
    pass
class Lit(ABC): #abstract class
    pass
class IntLit(Lit): #val:int
    pass

class RedeclaredVariable(Exception): #name:str
    pass
class RedeclaredConstant(Exception): #name:str
    pass

from functools import reduce
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o:object):
        reduce(lambda acc, ele: self.visit(ele,acc), ctx.decl, [])

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        return o + [ctx.name]
    
    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        return o + [ctx.name]
    
    def visitIntType(self,ctx:IntType,o:object):
        pass
    def visitFloatType(self,ctx:FloatType,o:object):
        pass
    def visitIntLit(self,ctx:IntLit,o:object):
        pass