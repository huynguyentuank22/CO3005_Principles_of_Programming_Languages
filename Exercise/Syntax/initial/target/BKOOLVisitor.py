# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decl.
    def visitVar_decl(self, ctx:BKOOLParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var.
    def visitVar(self, ctx:BKOOLParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#func_decl.
    def visitFunc_decl(self, ctx:BKOOLParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#params.
    def visitParams(self, ctx:BKOOLParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body.
    def visitBody(self, ctx:BKOOLParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stm.
    def visitStm(self, ctx:BKOOLParser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assign_stm.
    def visitAssign_stm(self, ctx:BKOOLParser.Assign_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#call_stm.
    def visitCall_stm(self, ctx:BKOOLParser.Call_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_stm.
    def visitReturn_stm(self, ctx:BKOOLParser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#operand.
    def visitOperand(self, ctx:BKOOLParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#func.
    def visitFunc(self, ctx:BKOOLParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#types.
    def visitTypes(self, ctx:BKOOLParser.TypesContext):
        return self.visitChildren(ctx)



del BKOOLParser