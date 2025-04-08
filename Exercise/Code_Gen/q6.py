    def visitVarDecl(self,ctx,o):
        varName = ctx.name
        varType = ctx.typ
        if o.frame is None:
            codegen = self.emit.emitATTRIBUTE(varName, varType, False)
            self.emit.printout(codegen)
            return Symbol(varName, varType, CName(self.className))
        index = o.frame.getNewIndex()
        startLabel = o.frame.getStartLabel()
        endLabel = o.frame.getEndLabel()
        codegen = self.emit.emitVAR(index, varName, varType, startLabel, endLabel)
        self.emit.printout(codegen)
        return Symbol(varName, varType, Index(index))