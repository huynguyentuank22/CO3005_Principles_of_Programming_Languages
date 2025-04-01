from abc import ABC, abstractmethod
class Program: #decl:List[VarDecl],exp:Exp
    pass
class VarDecl: #name:str,typ:Type
    pass
class Type(ABC): #abstract class
    pass
class IntType(Type):
    pass
class FloatType(Type):
    pass
class BoolType(Type):
    pass
class Exp(ABC): #abstract class
    pass
class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=
    pass
class UnOp(Exp): #op:str,e:Exp #op is -, !
    pass
class IntLit(Exp): #valIntType()    
    pass
class FloatLit(Exp): #val FloatType()    
    pass
class BoolLit(Exp): #valBooBoolType()    
    pass
class Id(Exp): #name:str
    pass

from functools import reduce
class StaticCheck(Visitor):
    def visitProgram(self, ctx:Program, o):
        o = []
        o = reduce(lambda acc, ele: self.visit(ele, acc), ctx.decl, o)
        return self.visit(ctx.exp, o)

    def visitVarDecl(self, ctx:VarDecl, o):
        if ctx.name in [x[0] for x in o]:
            raise Redeclared(ctx)
        return o + [(ctx.name, ctx.typ)]

    def visitBinOp(self, ctx:BinOp, o): 
        e1 = self.visit(ctx.e1, o)
        e2 = self.visit(ctx.e2, o)
        
        if ctx.op in ['+', '-', '*']:
            if not (isinstance(e1, (IntType, FloatType)) and isinstance(e2, (IntType, FloatType))):
                raise TypeMismatchInExpression(ctx)
            return FloatType() if isinstance(e1, FloatType) or isinstance(e2, FloatType) else IntType()
        
        elif ctx.op == '/':
            if not (isinstance(e1, (IntType, FloatType)) and isinstance(e2, (IntType, FloatType))):
                raise TypeMismatchInExpression(ctx)
            return FloatType()
            
        elif ctx.op in ['&&', '||']:
            if not (isinstance(e1, BoolType) and isinstance(e2, BoolType)):
                raise TypeMismatchInExpression(ctx)
            return BoolType()
            
        elif ctx.op in ['>', '<', '==', '!=']:
            if type(e1) != type(e2):
                raise TypeMismatchInExpression(ctx)
            return BoolType()
            
        raise TypeMismatchInExpression(ctx)

    def visitUnOp(self, ctx:UnOp, o):
        e = self.visit(ctx.e, o)
        if ctx.op == '-':
            if not isinstance(e, (IntType, FloatType)):
                raise TypeMismatchInExpression(ctx)
            return e
        elif ctx.op == '!':
            if not isinstance(e, BoolType):
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        raise TypeMismatchInExpression(ctx)
        
    def visitIntLit(self, ctx:IntLit, o): 
        return IntType()
    
    def visitFloatLit(self, ctx, o): 
        return FloatType()    
    
    def visitBoolLit(self, ctx, o):
        return BoolType()
    
    def visitIntType(self, ctx:IntType, o):
        return IntType()

    def visitFloatType(self, ctx:FloatType, o):
        return FloatType()

    def visitBoolType(self, ctx:BoolType, o):
        return BoolType()

    def visitId(self, ctx, o):
        var = next((x for x in o if x[0] == ctx.name), None)
        if var is None:
            raise UndeclaredIdentifier(ctx.name)
        return var[1]