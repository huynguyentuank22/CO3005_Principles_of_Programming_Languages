class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return self.visit(ctx.exp())

    def visitExp(self,ctx:MPParser.ExpContext):

        return Binary(ctx.ASSIGN().getText(), self.visit(ctx.term()), self.visit(ctx.exp())) if ctx.exp() else self.visit(ctx.term())

    def visitTerm(self,ctx:MPParser.TermContext): 

        return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1))) if ctx.COMPARE() else self.visit(ctx.factor(0))

    def visitFactor(self,ctx:MPParser.FactorContext):

        return Binary(ctx.ANDOR().getText(), self.visit(ctx.factor()), self.visit(ctx.operand())) if ctx.factor() else self.visit(ctx.operand())

    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLIT():
            return BooleanLiteral(True if ctx.BOOLIT().getText() == 'True' else False)
        return self.visit(ctx.exp())
