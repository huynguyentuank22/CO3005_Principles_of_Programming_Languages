class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return self.visit(ctx.mptype())

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return self.visit(ctx.primtype()) if ctx.primtype() else self.visit(ctx.arraytype())
        
        
    def visitArraytype(self,ctx:MPParser.ArraytypeContext):
        if ctx.primtype():
            return ArrayType(self.visit(ctx.dimen()),self.visit(ctx.primtype()))
        inner_type = self.visit(ctx.arraytype())
            # Combine the current dimension with the inner type using UnionType
        return ArrayType(UnionType(inner_type.indexType, self.visit(ctx.dimen())), inner_type.eleType)

    def visitPrimtype(self,ctx:MPParser.PrimtypeContext): 

        return IntType() if ctx.INTTYPE() else FloatType()

    def visitDimen(self,ctx:MPParser.DimenContext):
        first = self.visit(ctx.num(0))
        second = self.visit(ctx.num(1))
        return RangeType(first, second)
        

    def visitNum(self,ctx:MPParser.DimenContext):
        return int(ctx.INTLIT().getText()) if ctx.getChildCount() == 1 else int(ctx.INTLIT().getText())*-1