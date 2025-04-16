    def visitWhile(self,ctx,o):
        # Enter the loop and get the label for breaking out of it
        o.frame.enterLoop()
        labelExit = o.frame.getBreakLabel()
    
        # Emit a label for continuing the loop
        self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(),o.frame))
    
        # Evaluate the loop condition and jump to the end if false
        if_exprCode, if_exprType = ctx.expr.accept(self, Access(o.frame, o.sym, False))
        self.emit.printout(if_exprCode)
        self.emit.printout(self.emit.emitIFFALSE(labelExit,o.frame))
    
        # Visit the statement inside the loop and jump back to the beginning
        ctx.stmt.accept(self,o)
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(),o.frame))
    
        # Emit a label for exiting the loop and exit the frame
        self.emit.printout(self.emit.emitLABEL(labelExit,o.frame))
        o.frame.exitLoop()