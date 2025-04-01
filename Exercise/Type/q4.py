class IntType: pass
class FloatType: pass
class BoolType: pass
class StaticCheck(Visitor):
    #@ class Program: #decl:List[VarDecl],stmts:List[Stmt]
    #@ class Stmt(ABC): #abstract class
    def visitProgram(self,ctx:Program,o):
        o=[]
        for decl in ctx.decl:
            o.append(self.visit(decl,o))
        for stmt in ctx.stmts:
            self.visit(stmt,o)

    #@ class VarDecl: #name:str
    def visitVarDecl(self,ctx:VarDecl,o): 
        # print all values in o
        # print(o)
        for i in o:
            if ctx.name == i[0]:
                raise Redeclared(ctx) 
        return [ctx.name, None]

    # class Block(Stmt): #decl:List[VarDecl],stmts:List[Stmt]
    def visitBlock(self,ctx:Block,o):
        o1 = []
        for decl in ctx.decl:
            # redeclare only in the newest scope
            o1.append(self.visit(decl,o1))
        for stmt in ctx.stmts:
            # check the newest scope to old scope
            self.visit(stmt,o1 + o)

    #@ class Assign: #lhs:Id,rhs:Exp
    def visitAssign(self,ctx:Assign,o): 
        rhs_type = self.visit(ctx.rhs,o)
        lhs_type = self.visit(ctx.lhs,o)
        if lhs_type and rhs_type:
            if type(lhs_type) is not type(rhs_type):
                raise TypeMismatchInStatement(ctx)
        elif (not lhs_type) and rhs_type:
            #update type for Id
            o.append(rhs_type)
            self.visit(ctx.lhs,o)
        elif lhs_type and (not rhs_type):
            o.append(lhs_type)
            self.visit(ctx.rhs,o)
        else:
            raise TypeCannotBeInferred(ctx)

        

    #@ class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    def visitBinOp(self,ctx:BinOp,o): 
        left = self.visit(ctx.e1, o)
        right = self.visit(ctx.e2, o)
        op = ctx.op
        accept_type = None
        return_type = None
        if op in ['+', '-', '*', '/']:
            accept_type = IntType()
            return_type = IntType()
        elif op in ['+.','-.','*.','/.']:
            accept_type = FloatType()
            return_type = FloatType()
        elif op in ['>','=']:
            accept_type = IntType()
            return_type = BoolType()
        elif op in ['>.','=.']:
            accept_type = FloatType()
            return_type = BoolType()
        elif op in ['!', '&&', '||', '>b','=b']:
            accept_type = BoolType()
            return_type = BoolType()

        if left and right:
            if type(left) == type(accept_type) and type(right) == type(accept_type):
                return return_type
            raise TypeMismatchInExpression(ctx)
        #update_typ for Id
        elif not left:
            o.append(accept_type)
            self.visit(ctx.e1,o)
            if not right:
                o.append(accept_type)
                self.visit(ctx.e2,o)
            elif type(right) is not type(accept_type):
                raise TypeMismatchInExpression(ctx)
        elif not right:
            if type(left) is not type(accept_type):
                raise TypeMismatchInExpression(ctx)
            o.append(accept_type)
            self.visit(ctx.e2,o)
        return return_type

    #@ class UnOp(Exp): #op:str,e:Exp #op is -,-., !,i2f, floor
    def visitUnOp(self,ctx:UnOp,o): 
        value = self.visit(ctx.e,o)
        accept_type = None
        return_type = None
        if ctx.op == "-":
            accept_type = IntType()
            return_type = IntType()
        elif ctx.op == "-.":
            accept_type = FloatType()
            return_type = FloatType()
        elif ctx.op == "!":
            accept_type = BoolType()
            return_type = BoolType()
        elif ctx.op == "i2f":
            accept_type = IntType()
            return_type = FloatType()
        elif ctx.op == "floor":
            accept_type = FloatType()
            return_type = IntType()
            
        if value:    
            if type(value) == type(accept_type):
                return return_type
            raise TypeMismatchInExpression(ctx)
        else:
            #update_typ for Id
            o.append(accept_type)
            self.visit(ctx.e,o)
        return return_type


    #@ class IntLit(Exp): #val:int
    def visitIntLit(self,ctx:IntLit,o): 
        return IntType() 

    #@ class FloatLit(Exp): #val:float
    def visitFloatLit(self,ctx,o): 
        return FloatType()

    #@ class BoolLit(Exp): #val:bool
    def visitBoolLit(self,ctx,o): 
        return BoolType()
    
    #@ class Id(Exp): #name:str
    def visitId(self,ctx:Id,o): 
        for id in o:
            if id[0] == ctx.name:
                if type(o[-1]) in (IntType,FloatType,BoolType): 
                    id[1] = o.pop()
                    return None
                else:
                    return id[1]
        raise UndeclaredIdentifier(ctx.name)