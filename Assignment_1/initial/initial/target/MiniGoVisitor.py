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


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign.
    def visitAssign(self, ctx:MiniGoParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call.
    def visitCall(self, ctx:MiniGoParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl.
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#args.
    def visitArgs(self, ctx:MiniGoParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method.
    def visitMethod(self, ctx:MiniGoParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param_list.
    def visitParam_list(self, ctx:MiniGoParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#types.
    def visitTypes(self, ctx:MiniGoParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literals.
    def visitLiterals(self, ctx:MiniGoParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_type.
    def visitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_array.
    def visitAssign_array(self, ctx:MiniGoParser.Assign_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_decl.
    def visitArray_decl(self, ctx:MiniGoParser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimensions.
    def visitDimensions(self, ctx:MiniGoParser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ele_list.
    def visitEle_list(self, ctx:MiniGoParser.Ele_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ele.
    def visitEle(self, ctx:MiniGoParser.EleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#access_struct.
    def visitAccess_struct(self, ctx:MiniGoParser.Access_structContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_struct.
    def visitAssign_struct(self, ctx:MiniGoParser.Assign_structContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_decl.
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_type.
    def visitStruct_type(self, ctx:MiniGoParser.Struct_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fields.
    def visitFields(self, ctx:MiniGoParser.FieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_lit.
    def visitField_lit(self, ctx:MiniGoParser.Field_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_type.
    def visitInterface_type(self, ctx:MiniGoParser.Interface_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_decl.
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primary_expr.
    def visitPrimary_expr(self, ctx:MiniGoParser.Primary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#asm_stmt.
    def visitAsm_stmt(self, ctx:MiniGoParser.Asm_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt.
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
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


    # Visit a parse tree produced by MiniGoParser#range_clause.
    def visitRange_clause(self, ctx:MiniGoParser.Range_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_stmt.
    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
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



del MiniGoParser