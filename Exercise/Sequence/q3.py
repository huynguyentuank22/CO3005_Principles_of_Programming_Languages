    def visitFor(self,ctx,o):
        o.frame.enterLoop()
    
        frame = o.frame
        labelBreak = frame.getBreakLabel()
        labelContinue = frame.getContinueLabel()
        labelFor = frame.getNewLabel()
        idx = ctx.idx
    
        #% visit(exp1)
        init_code, _ = self.visit(ctx.ini, Access(frame, o.sym, False))
        self.emit.printout(init_code)
        #% Assign value to index
        idx_code, _ = self.visit(idx, Access(frame, o.sym, True))
        self.emit.printout(idx_code)
        #* _______________________FOR_LOOP_______________________
        #% emitLABEL(LabelFor)
        self.emit.printout(self.emit.emitLABEL(labelFor, frame))
    
        #% Check index
        idx_code, _ = self.visit(idx, Access(frame, o.sym, False))
        self.emit.printout(idx_code)
        #% visit(exp2)
        cond_code, _ = self.visit(ctx.end, Access(frame, o.sym, False))
        self.emit.printout(cond_code)
        #% If Index <= exp2
        compare_code = self.emit.emitREOP('<=', IntType(), frame)
        self.emit.printout(compare_code)
        
        #% emitIFFALSE(LabelExit)
        self.emit.printout(self.emit.emitIFFALSE(labelBreak, frame))
    
        #% visit(stmt)
        self.visit(ctx.stmt, o)
    
        #% emitLABEL(LabelContinue)
        self.emit.printout(self.emit.emitLABEL(labelContinue, frame))
    
        #% visit(exp3)
        update_code, _ = self.visit(ctx.upd, Access(frame, o.sym, False))
        self.emit.printout(update_code)
    
        #% Take Index
        idx_code, _ = self.visit(idx, Access(frame, o.sym, False))
        self.emit.printout(idx_code)
    
        #% +
        add_code = self.emit.emitADDOP('+', IntType(), frame)
        self.emit.printout(add_code)
    
        #% Assign value to index
        idx_code, _ = self.visit(idx, Access(frame, o.sym, True))
        self.emit.printout(idx_code)
    
        #% emitGOTO(LabelFor)
        self.emit.printout(self.emit.emitGOTO(labelFor, frame))
        #* _______________________FOR_LOOP_______________________
        
        #% emitLABEL(LabelExit)
        self.emit.printout(self.emit.emitLABEL(labelBreak, frame))
        
        o.frame.exitLoop()
        return None, None