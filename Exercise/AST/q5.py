class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        # Collect all VarDecl objects from each vardecl and wrap them in a Program node
        vardecls = [self.visit(vardecl) for vardecl in ctx.vardecl()]
        # Flatten the list of lists into a single list of VarDecl objects
        flattened_vardecls = [var for sublist in vardecls for var in sublist]
        return Program(flattened_vardecls)

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return [VarDecl(x, self.visit(ctx.mptype())) for x in self.visit(ctx.ids())]

    def visitMptype(self,ctx:MPParser.MptypeContext):
        
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(x.getText()) for x in ctx.ID()]
