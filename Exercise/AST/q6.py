from functools import reduce
class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return self.visit(ctx.exp())

    def visitExp(self,ctx:MPParser.ExpContext):
        terms = ctx.term()[::-1]
        ops = ctx.ASSIGN()[::-1]
        lst = zip(terms[1:], ops)
        return reduce(lambda x,y : Binary(y[1].getText(), self.visit(y[0]), x), lst, self.visit(terms[0]))

    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.COMPARE():
            return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1))) 
        return self.visit(ctx.factor(0))

    def visitFactor(self,ctx:MPParser.FactorContext):
        operands = ctx.operand()
        ops = ctx.ANDOR()
        lst = zip(operands[1:], ops)
        return reduce(lambda x,y : Binary(y[1].getText(),x, self.visit(y[0]) ), lst, self.visit(operands[0]))

    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLIT():
            return BooleanLiteral(True if ctx.BOOLIT().getText() == 'True' else False)
        return self.visit(ctx.exp())
