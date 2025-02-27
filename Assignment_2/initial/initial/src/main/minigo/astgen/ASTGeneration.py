from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    # program: many_decl EOF;
    def visitProgram(self,ctx:MiniGoParser.ProgramContext):
        tokens = self.visit(ctx.many_decl())
        return Program(tokens)

    #  many_decl: decl many_decl | decl;
    def visitMany_decl(self,ctx:MiniGoParser.Many_declContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.decl())]
        return [self.visit(ctx.decl())] + self.visit(ctx.many_decl())

    # decl: var_decl | const_decl | struct_decl | interface_decl | func_decl | method_decl;
    def visitDecl(self,ctx:MiniGoParser.DeclContext):
        return self.visit(ctx.getChild(0))
        
    # var_decl: (decl_var_type_init | decl_var_init | decl_var_type) eos;
    def visitVar_decl(self,ctx:MiniGoParser.Var_declContext):
        if ctx.decl_var_type_init():
            return self.visit(ctx.decl_var_type_init())
        if ctx.decl_var_init():
            return self.visit(ctx.decl_var_init())
        if ctx.decl_var_type():
            return self.visit(ctx.decl_var_type())
    
    # decl_var_type_init: VAR IDENTIFIER types DECLARE_ASSIGN expr;
    def visitDecl_var_type_init(self,ctx:MiniGoParser.Decl_var_type_initContext):
        id = ctx.IDENTIFIER().getText()
        typ = self.visit(ctx.types())
        expr = self.visit(ctx.expr())
        return VarDecl(id,typ,expr)
    
    # decl_var_init: VAR IDENTIFIER DECLARE_ASSIGN expr;
    def visitDecl_var_init(self,ctx:MiniGoParser.Decl_var_initContext):
        id = ctx.IDENTIFIER().getText()
        expr = self.visit(ctx.expr())
        return VarDecl(id,None,expr)
    
    # decl_var_type: VAR IDENTIFIER types;
    def visitDecl_var_type(self,ctx:MiniGoParser.Decl_var_typeContext):
        id = ctx.IDENTIFIER().getText()
        typ = self.visit(ctx.types())
        return VarDecl(id,typ,None)
    
    # const_decl: CONST IDENTIFIER types? DECLARE_ASSIGN expr eos;
    def visitConst_decl(self,ctx:MiniGoParser.Const_declContext):
        id = ctx.IDENTIFIER().getText()
        typ = self.visit(ctx.types()) if ctx.types() else None
        expr = self.visit(ctx.expr())
        return ConstDecl(id,typ,expr)   
    
    # array_type: dimensions (primitive_type | IDENTIFIER);
    def visitArray_type(self,ctx:MiniGoParser.Array_typeContext):
        dimens = self.visit(ctx.dimensions())
        typ = self.visit(ctx.primitive_type()) if ctx.primitive_type() else Id(ctx.IDENTIFIER().getText())
        return ArrayType(dimens,typ)
    
    # dimensions: dim dimensions | dim;
    def visitDimensions(self,ctx:MiniGoParser.DimensionsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.dim())]
        return [self.visit(ctx.dim())] + self.visit(ctx.dimensions())

    # dim: LSB expr RSB;
    def visitDim(self,ctx:MiniGoParser.DimContext):
        return self.visit(ctx.expr())
    
    # array_literal: array_type ele_list;
    def visitArray_literal(self,ctx:MiniGoParser.Array_literalContext):
        array_type = self.visit(ctx.array_type())
        dim, typ = array_type.dimens, array_type.eleType
        ele = self.visit(ctx.ele_list())
        return ArrayLiteral(dim,typ,ele)

    # ele_list: LCB many_ele RCB;
    def visitEle_list(self,ctx:MiniGoParser.Ele_listContext):
        return self.visit(ctx.many_ele())
    
    # many_ele: ele COMMA many_ele | ele;
    def visitMany_ele(self,ctx:MiniGoParser.Many_eleContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.ele())]
        return [self.visit(ctx.ele())] + self.visit(ctx.many_ele())
    
    # ele: ele_list | primitive_lit;
    def visitEle(self,ctx:MiniGoParser.EleContext):
        if ctx.ele_list():
            return self.visit(ctx.ele_list())
        if ctx.primitive_lit():
            return self.visit(ctx.primitive_lit())
        
    # struct_decl: TYPE IDENTIFIER struct_type eos;
    def visitStruct_decl(self,ctx:MiniGoParser.Struct_declContext):
        id = ctx.IDENTIFIER().getText()
        elements = []
        methods = []
        for ele in self.visit(ctx.struct_type()):
            if ele.__class__.__name__ == "MethodDecl":
                methods.append(ele)
            else:
                elements.append(ele)
        return StructType(id,elements,methods)
    
    # struct_type: STRUCT LCB many_fields RCB;
    def visitStruct_type(self,ctx:MiniGoParser.Struct_typeContext):
        return self.visit(ctx.many_fields())
    
    # many_fields: fields many_fields | fields;
    def visitMany_fields(self,ctx:MiniGoParser.Many_fieldsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.fields())]
        return [self.visit(ctx.fields())] + self.visit(ctx.many_fields())
    
    # fields: ele_field eos;
    def visitFields(self,ctx:MiniGoParser.FieldsContext):
        return self.visit(ctx.getChild(0))
    
    # ele_field: IDENTIFIER (primitive_type | array_type | IDENTIFIER);
    def visitEle_field(self,ctx:MiniGoParser.FieldsContext):
        id = ctx.IDENTIFIER(0).getText()
        if ctx.primitive_type():
            typ = self.visit(ctx.primitive_type())
        elif ctx.array_type():
            typ = self.visit(ctx.array_type())
        else:
            typ = Id(ctx.IDENTIFIER(1).getText())
        return (id,typ)

    # struct_literal: IDENTIFIER LCB struct_elements? RCB;
    def visitStruct_literal(self,ctx:MiniGoParser.Struct_literalContext):
        id = ctx.IDENTIFIER().getText()
        if ctx.struct_elements():
            elements = self.visit(ctx.struct_elements())
        else:
            elements = []
        return StructLiteral(id,elements)
    
    # struct_elements: struct_ele COMMA struct_elements | struct_ele;
    def visitStruct_elements(self,ctx:MiniGoParser.Struct_elementsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.struct_ele())]
        return [self.visit(ctx.struct_ele())] + self.visit(ctx.struct_elements())
    
    # struct_ele: IDENTIFIER ':' expr;
    def visitStruct_ele(self,ctx:MiniGoParser.Struct_eleContext):
        id = ctx.IDENTIFIER().getText()
        expr = self.visit(ctx.expr())
        return (id,expr)
    
    # interface_decl: TYPE IDENTIFIER interface_type eos;
    def visitInterface_decl(self,ctx:MiniGoParser.Interface_declContext):
        id = ctx.IDENTIFIER().getText()
        methods = self.visit(ctx.interface_type())
        return InterfaceType(id,methods)
    
    # interface_type: INTERFACE LCB many_interface_field RCB;
    def visitInterface_type(self,ctx:MiniGoParser.Interface_typeContext):
        return self.visit(ctx.many_interface_field())
    
    # many_interface_field: interface_field many_interface_field | interface_field;
    def visitMany_interface_field(self,ctx:MiniGoParser.Many_interface_fieldContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.interface_field())]
        return [self.visit(ctx.interface_field())] + self.visit(ctx.many_interface_field())
    
    # interface_field: IDENTIFIER LB param_list? RB types? eos;
    def visitInterface_field(self,ctx:MiniGoParser.Interface_fieldContext):
        id = ctx.IDENTIFIER().getText()
        if ctx.param_list():
            param_lst = self.visit(ctx.param_list())
            params = [typ for (id, typ) in param_lst]
        else:
            params = []
        if ctx.types():
            ret_typ = self.visit(ctx.types())
        else:
            ret_typ = VoidType()
        return Prototype(id,params,ret_typ)
    
    # func_decl: FUNC IDENTIFIER LB param_list? RB types? block eos;
    def visitFunc_decl(self,ctx:MiniGoParser.Func_declContext):
        id = ctx.IDENTIFIER().getText()
        if ctx.param_list():
            param_lst = self.visit(ctx.param_list())
            params = [ParamDecl(parName,parType) for (parName,parType) in param_lst]
        else:
            params = []
        if ctx.types():
            ret_typ = self.visit(ctx.types())
        else:
            ret_typ = VoidType()
        block = self.visit(ctx.block())
        return FuncDecl(id,params,ret_typ,block)
    
    # param_list: param COMMA param_list | param;
    def visitParam_list(self,ctx:MiniGoParser.Param_listContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.param())
        return self.visit(ctx.param()) + self.visit(ctx.param_list())
    
    # param: id_list types;
    def visitParam(self,ctx:MiniGoParser.ParamContext):
        ids = self.visit(ctx.id_list())
        typ = self.visit(ctx.types())
        return [(id,typ) for id in ids]
    
    # id_list: IDENTIFIER COMMA id_list | IDENTIFIER;
    def visitId_list(self,ctx:MiniGoParser.Id_listContext):
        if ctx.getChildCount() == 1:
            return [ctx.IDENTIFIER().getText()]
        return [ctx.IDENTIFIER().getText()] + self.visit(ctx.id_list())
    
    # block: LCB many_stmt RCB;
    def visitBlock(self,ctx:MiniGoParser.BlockContext):
        stmts = self.visit(ctx.many_stmt())
        return Block(stmts)
    
    # many_stmt: stmt many_stmt | stmt;
    def visitMany_stmt(self,ctx:MiniGoParser.Many_stmtContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.stmt())]
        return [self.visit(ctx.stmt())] + self.visit(ctx.many_stmt())
    
    # method_decl: FUNC method IDENTIFIER LB param_list? RB types? block eos;
    def visitMethod_decl(self,ctx:MiniGoParser.Method_declContext):
        recv, recv_typ = self.visit(ctx.method())

        id = ctx.IDENTIFIER().getText()
        if ctx.param_list():
            param_lst = self.visit(ctx.param_list())
            params = [ParamDecl(parName,parType) for (parName,parType) in param_lst]
        else:
            params = []
        if ctx.types():
            ret_typ = self.visit(ctx.types())
        else:
            ret_typ = VoidType()
        block = self.visit(ctx.block())

        fun = FuncDecl(id,params,ret_typ,block)
        return MethodDecl(recv,recv_typ,fun)
    
    # method: LB IDENTIFIER IDENTIFIER RB;
    def visitMethod(self,ctx:MiniGoParser.MethodContext):
        recv = ctx.IDENTIFIER(0).getText()
        recv_typ = Id(ctx.IDENTIFIER(1).getText())
        return (recv,recv_typ)

    # types: primitive_type | array_type | IDENTIFIER;
    def visitTypes(self,ctx:MiniGoParser.TypesContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        if ctx.array_type():
            return self.visit(ctx.array_type())
        return Id(ctx.IDENTIFIER().getText())
    
    # primitive_lit: INT_LITERAL | FLOAT_LITERAL | STRING_LITERAL | BOOLEAN_LITERAL | NIL_LITERAL;
    def visitPrimitive_lit(self,ctx:MiniGoParser.Primitive_litContext):
        if ctx.INT_LITERAL():
            return IntLiteral(int(ctx.INT_LITERAL().getText()))
        if ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        if ctx.STRING_LITERAL():
            return StringLiteral(str(ctx.STRING_LITERAL().getText()))
        if ctx.BOOLEAN_LITERAL():
            return BooleanLiteral(ctx.BOOLEAN_LITERAL().getText())
        return NilLiteral()
    
    # literals: primitive_lit | array_literal | struct_literal;
    def visitLiterals(self,ctx:MiniGoParser.LiteralsContext):
        if ctx.primitive_lit():
            return self.visit(ctx.primitive_lit())
        if ctx.array_literal():
            return self.visit(ctx.array_literal())
        return self.visit(ctx.struct_literal())
    
    # primitive_type: INT | FLOAT | STRING | BOOLEAN;
    def visitPrimitive_type(self,ctx:MiniGoParser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        if ctx.BOOLEAN():
            return BoolType()

    # func_call: IDENTIFIER LB expr_list? RB;
    def visitFunc_call(self,ctx:MiniGoParser.Func_callContext):
        funName = ctx.IDENTIFIER().getText()
        if ctx.expr_list():
            args = self.visit(ctx.expr_list())
        else:
            args = []
        return FuncCall(funName,args)
    
    # expr: expr OR expr1 | expr1;
    def visitExpr(self,ctx:MiniGoParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1())
        else:
            op = ctx.OR().getText()
            left = self.visit(ctx.expr())
            right = self.visit(ctx.expr1())
            return BinaryOp(op,left,right)
        
    # expr1: expr1 AND expr2 | expr2;
    def visitExpr1(self,ctx:MiniGoParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2())
        else:
            op = ctx.AND().getText()
            left = self.visit(ctx.expr1())
            right = self.visit(ctx.expr2())
            return BinaryOp(op,left,right)
        
    # expr2: expr2 relational_ops expr3 | expr3;
    def visitExpr2(self,ctx:MiniGoParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        else:
            op = self.visit(ctx.relational_ops())
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            return BinaryOp(op,left,right)
        
    # expr3: expr3 (ADD | SUB) expr4 | expr4;
    def visitExpr3(self,ctx:MiniGoParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            return BinaryOp(op,left,right)
        
    # expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
    def visitExpr4(self,ctx:MiniGoParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr4())
            right = self.visit(ctx.expr5())
            return BinaryOp(op,left,right)
        
    # expr5: (NOT | SUB) expr5 | primary_expr;
    def visitExpr5(self,ctx:MiniGoParser.Expr5Context):
        if ctx.primary_expr():
            return self.visit(ctx.primary_expr())
        else:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.expr5())
            return UnaryOp(op,body)

    # primary_expr: primary_expr many_index_ops
            # | primary_expr DOT IDENTIFIER
            # | primary_expr DOT IDENTIFIER LB expr_list? RB
            # | operand
            # ;
    def visitPrimary_expr(self,ctx:MiniGoParser.Primary_exprContext):
        if ctx.operand():
            return self.visit(ctx.operand())
        if ctx.primary_expr() and ctx.many_index_ops():
            primary_expr = self.visit(ctx.primary_expr())
            many_index_ops = self.visit(ctx.many_index_ops())
            return ArrayCell(primary_expr, many_index_ops)
        primary_expr = self.visit(ctx.primary_expr())
        if ctx.LB():
            func_name = ctx.IDENTIFIER().getText()
            expr_list = self.visit(ctx.expr_list()) if ctx.expr_list() else []
            return MethCall(primary_expr,func_name,expr_list)
        return FieldAccess(primary_expr, ctx.IDENTIFIER().getText())
            

    # expr_list: expr COMMA expr_list | expr;
    def visitExpr_list(self,ctx:MiniGoParser.Expr_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.expr_list())
    
    # operand:  literals | IDENTIFIER | func_call | LB expr RB ;
    def visitOperand(self,ctx:MiniGoParser.OperandContext):
        if ctx.literals():
            return self.visit(ctx.literals())
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        if ctx.func_call():
            return self.visit(ctx.func_call())
        return self.visit(ctx.expr())
    
    # stmt: decl_stmt | asm_stmt | if_stmt | for_stmt | break_stmt | continue_stmt | call_stmt | return_stmt ;
    def visitStmt(self,ctx:MiniGoParser.StmtContext):
        return self.visit(ctx.getChild(0))
    
    # decl_stmt: var_decl | const_decl | array_decl;
    def visitDecl_stmt(self,ctx:MiniGoParser.Decl_stmtContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        if ctx.const_decl():
            return self.visit(ctx.const_decl())
        return self.visit(ctx.array_decl())
    
    # asm_stmt: asm eos;
    def visitAsm_stmt(self,ctx:MiniGoParser.Asm_stmtContext):
        return self.visit(ctx.asm())
    
    # asm: lhs assign_ops rhs;
    def visitAsm(self,ctx:MiniGoParser.AsmContext):
        lhs = self.visit(ctx.lhs())
        assign_ops = self.visit(ctx.assign_ops())
        if assign_ops == ":=":
            return Assign(lhs,self.visit(ctx.rhs()))
        op = assign_ops[0]
        rhs = BinaryOp(op,lhs,self.visit(ctx.rhs()))
        return Assign(lhs,rhs)
    
    # lhs: IDENTIFIER | array_elem | struct_elem;
    def visitLhs(self,ctx:MiniGoParser.LhsContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        if ctx.array_elem():
            return self.visit(ctx.array_elem())
        return self.visit(ctx.struct_elem())
    
    # array_elem: expr many_index_ops;
    def visitArray_elem(self,ctx:MiniGoParser.Array_elemContext):
        arr = self.visit(ctx.expr()) # expr???
        idx = self.visit(ctx.many_index_ops())
        if isinstance(arr,ArrayCell):
            return ArrayCell(arr.arr,arr.idx + idx)
        return ArrayCell(arr,idx)
    
    # many_index_ops: index_ops many_index_ops | index_ops;
    def visitMany_index_ops(self,ctx:MiniGoParser.Many_index_opsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.index_ops())]
        return [self.visit(ctx.index_ops())] + self.visit(ctx.many_index_ops())
    
    # struct_elem: expr DOT IDENTIFIER;
    def visitStruct_elem(self,ctx:MiniGoParser.Struct_elemContext):
        receiver = self.visit(ctx.expr())
        field = ctx.IDENTIFIER().getText()
        return FieldAccess(receiver,field)

    # rhs: expr;
    def visitRhs(self,ctx:MiniGoParser.RhsContext):
        return self.visit(ctx.expr())
    
    # if_stmt: IF LB expr RB block if_tail? eos;
    def visitIf_stmt(self,ctx:MiniGoParser.If_stmtContext):
        expr = self.visit(ctx.expr())
        then = self.visit(ctx.block())
        if ctx.if_tail():
            return If(expr,then,self.visit(ctx.if_tail()))
        return If(expr,then,None)
    
    # if_tail: else_if_stmt if_tail | else_if_stmt | else_stmt; 
    def visitIf_tail(self,ctx:MiniGoParser.If_tailContext):
        if ctx.if_tail():
            else_if = self.visit(ctx.else_if_stmt())
            return If(else_if.expr, else_if.thenStmt, self.visit(ctx.if_tail()))
        if ctx.else_if_stmt():
            else_if = self.visit(ctx.else_if_stmt())
            return If(else_if.expr, else_if.thenStmt, None)
        return self.visit(ctx.else_stmt())

    # else_if_stmt: ELSE IF LB expr RB block;
    def visitElse_if_stmt(self,ctx:MiniGoParser.Else_if_stmtContext):
        expr = self.visit(ctx.expr())
        block = self.visit(ctx.block())
        return If(expr,block,None)
    
    # else: ELSE block;
    def visitElse_stmt(self,ctx:MiniGoParser.Else_stmtContext):
        return self.visit(ctx.block())

    # for_stmt: for_basic | for_step | for_each;
    def visitFor_stmt(self,ctx:MiniGoParser.For_stmtContext):
        return self.visit(ctx.getChild(0))
    
    # for_basic: FOR expr block eos;
    def visitFor_basic(self,ctx:MiniGoParser.For_basicContext):
        cond = self.visit(ctx.expr())
        block = self.visit(ctx.block())
        return ForBasic(cond,block)
    
    # for_step: FOR fully_clause block eos;
    def visitFor_step(self,ctx:MiniGoParser.For_stepContext):
        init,cond,update = self.visit(ctx.fully_clause())
        block = self.visit(ctx.block())
        return ForStep(init,cond,update,block)
    
    # for_each: FOR range_clause block eos;
    def visitFor_each(self,ctx:MiniGoParser.For_eachContext):
        idx,value,arr = self.visit(ctx.range_clause())
        block = self.visit(ctx.block())
        return ForEach(idx,value,arr,block)
    
    # fully_clause: init eos expr eos update;
    def visitFully_clause(self,ctx:MiniGoParser.Fully_clauseContext):
        init = self.visit(ctx.init())
        cond = self.visit(ctx.expr())
        update = self.visit(ctx.update())
        return (init,cond,update)
    
    # init: asm_for | decl_var_init | decl_var_type_init_for;
    def visitInit(self,ctx:MiniGoParser.InitContext):
        if ctx.asm_for():
            return self.visit(ctx.asm_for())
        if ctx.decl_var_init():
            return self.visit(ctx.decl_var_init())
        return self.visit(ctx.decl_var_type_init_for())
    
    # asm_for: IDENTIFIER assign_ops rhs;
    def visitAsm_for(self,ctx:MiniGoParser.Asm_forContext):
        lhs = Id(ctx.IDENTIFIER().getText())
        assign_ops = ctx.assign_ops().getText()
        if assign_ops == ":=":
            return Assign(lhs,self.visit(ctx.rhs()))
        op = assign_ops[0]
        rhs = self.visit(ctx.rhs())
        return Assign(lhs,BinaryOp(op,lhs,rhs))
    
    # decl_var_type_init_for: VAR IDENTIFIER primitive_type DECLARE_ASSIGN expr;
    def visitDecl_var_type_init_for(self,ctx:MiniGoParser.Decl_var_type_init_forContext):
        id = ctx.IDENTIFIER().getText()
        typ = self.visit(ctx.primitive_type())
        expr = self.visit(ctx.expr())
        return VarDecl(id,typ,expr)
    
    # update: asm_for;
    def visitUpdate(self,ctx:MiniGoParser.UpdateContext):
        return self.visit(ctx.asm_for())
    
    # range_clause: (IDENTIFIER | '_') COMMA IDENTIFIER ASSIGN RANGE expr;
    def visitRange_clause(self,ctx:MiniGoParser.Range_clauseContext):
        if ctx.IDENTIFIER(1):
            idx = Id(ctx.IDENTIFIER(0).getText())
            value = Id(ctx.IDENTIFIER(1).getText())
        else:
            idx = Id("_")
            value = Id(ctx.IDENTIFIER(0).getText())
        arr = self.visit(ctx.expr())
        return (idx,value,arr)
    
    # break_stmt: BREAK eos;
    def visitBreak_stmt(self,ctx:MiniGoParser.Break_stmtContext):
        return Break()
    
    # continue_stmt: CONTINUE eos;
    def visitContinue_stmt(self,ctx:MiniGoParser.Continue_stmtContext):
        return Continue()
    
    # call_stmt: (func_call | method_call) eos;
    def visitCall_stmt(self,ctx:MiniGoParser.Call_stmtContext):
        if ctx.func_call():
            return self.visit(ctx.func_call())
        return self.visit(ctx.method_call())
    
    # method_call: expr DOT func_call;
    def visitMethod_call(self,ctx:MiniGoParser.Method_callContext):
        receiver = self.visit(ctx.expr())
        func = self.visit(ctx.func_call())
        metName = func.funName
        args = func.args
        return MethCall(receiver,metName,args)
    
    # return_stmt: RETURN expr? eos;
    def visitReturn_stmt(self,ctx:MiniGoParser.Return_stmtContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return(None)
    
    # relational_ops: EQ | NEQ | GT | GE | LT | LE;
    def visitRelational_ops(self,ctx:MiniGoParser.Relational_opsContext):
        return ctx.getChild(0).getText()
    
    # assign_ops: ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | MULT_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;
    def visitAssign_ops(self,ctx:MiniGoParser.Assign_opsContext):
        return ctx.getChild(0).getText()
    
    # index_ops: LSB expr RSB;
    def visitIndex_ops(self,ctx:MiniGoParser.Index_opsContext):
        return self.visit(ctx.expr())
    


