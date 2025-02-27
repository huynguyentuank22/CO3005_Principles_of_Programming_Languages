class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return Program(self.visit(ctx.vardecls()))

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail()) if ctx.vardecl() else []

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        
        return [VarDecl(x, self.visit(ctx.mptype())) for x in self.visit(ctx.ids())] 

    def visitMptype(self,ctx:MPParser.MptypeContext):

        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):

        return [Id(ctx.ID().getText())] + self.visit(ctx.ids()) if ctx.ids() else [Id(ctx.ID().getText())]