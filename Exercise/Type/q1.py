from abc import ABC, abstractmethod

class Exp(ABC): #abstract class
    pass
class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=
    pass
class UnOp(Exp): #op:str,e:Exp #op is -, !
    pass
class IntLit(Exp): #val:int
    pass
class FloatLit(Exp): #val:float
    pass
class BoolLit(Exp): #val:bool
    pass

class StaticCheck(Visitor):

    def visitBinOp(self,ctx:BinOp,o): 
        e1 = self.visit(ctx.e1,o)
        e2 = self.visit(ctx.e2,o)
        if ctx.op in ['+','-','*']:
            if e1 not in ['int','float'] or e2 not in ['int','float']:
                raise TypeMismatchInExpression(ctx)
            return 'float' if 'float' in [e1,e2] else 'int'
        if ctx.op in ['/']:
            if e1 not in ['int','float'] or e2 not in ['int','float']:
                raise TypeMismatchInExpression(ctx)
            return 'float'
        if ctx.op in ['&&', '||']:
            if e1 != 'bool' or e2 != 'bool':
                raise TypeMismatchInExpression(ctx)
            return 'bool'
        if ctx.op in ['>', '<', '==', '!=']:
            if e1 != e2:
                raise TypeMismatchInExpression(ctx)
            return 'bool'

    def visitUnOp(self,ctx:UnOp,o):
        if ctx.op == '-':
            e = self.visit(ctx.e,o)
            if e not in ['int','float']:
                raise TypeMismatchInExpression(ctx)
            return e
        if ctx.op == '!':
            e = self.visit(ctx.e,o)
            if e != 'bool':
                raise TypeMismatchInExpression(ctx)
            return 'bool'
        
    def visitIntLit(self,ctx:IntLit,o): 
        return 'int'
    def visitFloatLit(self,ctx,o): 
        return 'float'
    def visitBoolLit(self,ctx,o):
        return 'bool'