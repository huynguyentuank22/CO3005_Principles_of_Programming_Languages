# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#many_decl.
    def visitMany_decl(self, ctx:MiniGoParser.Many_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl.
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl_var_type_init.
    def visitDecl_var_type_init(self, ctx:MiniGoParser.Decl_var_type_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl_var_init.
    def visitDecl_var_init(self, ctx:MiniGoParser.Decl_var_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl_var_type.
    def visitDecl_var_type(self, ctx:MiniGoParser.Decl_var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_decl.
    def visitArray_decl(self, ctx:MiniGoParser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl_arr.
    def visitDecl_arr(self, ctx:MiniGoParser.Decl_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimensions.
    def visitDimensions(self, ctx:MiniGoParser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dim.
    def visitDim(self, ctx:MiniGoParser.DimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ele_list.
    def visitEle_list(self, ctx:MiniGoParser.Ele_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#many_ele.
    def visitMany_ele(self, ctx:MiniGoParser.Many_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ele.
    def visitEle(self, ctx:MiniGoParser.EleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_decl.
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_type.
    def visitStruct_type(self, ctx:MiniGoParser.Struct_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#many_fields.
    def visitMany_fields(self, ctx:MiniGoParser.Many_fieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fields.
    def visitFields(self, ctx:MiniGoParser.FieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_elements.
    def visitStruct_elements(self, ctx:MiniGoParser.Struct_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_ele.
    def visitStruct_ele(self, ctx:MiniGoParser.Struct_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_type.
    def visitInterface_type(self, ctx:MiniGoParser.Interface_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#many_interface_field.
    def visitMany_interface_field(self, ctx:MiniGoParser.Many_interface_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_field.
    def visitInterface_field(self, ctx:MiniGoParser.Interface_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param_list.
    def visitParam_list(self, ctx:MiniGoParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#id_list.
    def visitId_list(self, ctx:MiniGoParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#many_stmt.
    def visitMany_stmt(self, ctx:MiniGoParser.Many_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_decl.
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method.
    def visitMethod(self, ctx:MiniGoParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#types.
    def visitTypes(self, ctx:MiniGoParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_lit.
    def visitPrimitive_lit(self, ctx:MiniGoParser.Primitive_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literals.
    def visitLiterals(self, ctx:MiniGoParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_type.
    def visitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primary_expr.
    def visitPrimary_expr(self, ctx:MiniGoParser.Primary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr_list.
    def visitExpr_list(self, ctx:MiniGoParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#operand.
    def visitOperand(self, ctx:MiniGoParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl_stmt.
    def visitDecl_stmt(self, ctx:MiniGoParser.Decl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#asm_stmt.
    def visitAsm_stmt(self, ctx:MiniGoParser.Asm_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#asm.
    def visitAsm(self, ctx:MiniGoParser.AsmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_elem.
    def visitArray_elem(self, ctx:MiniGoParser.Array_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#many_index_ops.
    def visitMany_index_ops(self, ctx:MiniGoParser.Many_index_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_elem.
    def visitStruct_elem(self, ctx:MiniGoParser.Struct_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#many_struct_ops.
    def visitMany_struct_ops(self, ctx:MiniGoParser.Many_struct_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_ops.
    def visitStruct_ops(self, ctx:MiniGoParser.Struct_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rhs.
    def visitRhs(self, ctx:MiniGoParser.RhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt.
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#many_else_if_stmt.
    def visitMany_else_if_stmt(self, ctx:MiniGoParser.Many_else_if_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_if_stmt.
    def visitElse_if_stmt(self, ctx:MiniGoParser.Else_if_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt.
    def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_clause.
    def visitFor_clause(self, ctx:MiniGoParser.For_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fully_clause.
    def visitFully_clause(self, ctx:MiniGoParser.Fully_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init.
    def visitInit(self, ctx:MiniGoParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl_var_type_init_for.
    def visitDecl_var_type_init_for(self, ctx:MiniGoParser.Decl_var_type_init_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#update.
    def visitUpdate(self, ctx:MiniGoParser.UpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#asm_for.
    def visitAsm_for(self, ctx:MiniGoParser.Asm_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#range_clause.
    def visitRange_clause(self, ctx:MiniGoParser.Range_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_stmt.
    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_stmt.
    def visitCall_stmt(self, ctx:MiniGoParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_elem_call.
    def visitStruct_elem_call(self, ctx:MiniGoParser.Struct_elem_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#many_struct_ops_call.
    def visitMany_struct_ops_call(self, ctx:MiniGoParser.Many_struct_ops_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_ops_call.
    def visitStruct_ops_call(self, ctx:MiniGoParser.Struct_ops_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_stmt.
    def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#boolean_ops.
    def visitBoolean_ops(self, ctx:MiniGoParser.Boolean_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arithmetic_ops.
    def visitArithmetic_ops(self, ctx:MiniGoParser.Arithmetic_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#relational_ops.
    def visitRelational_ops(self, ctx:MiniGoParser.Relational_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_ops.
    def visitAssign_ops(self, ctx:MiniGoParser.Assign_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#index_ops.
    def visitIndex_ops(self, ctx:MiniGoParser.Index_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#eos.
    def visitEos(self, ctx:MiniGoParser.EosContext):
        return self.visitChildren(ctx)



del MiniGoParser