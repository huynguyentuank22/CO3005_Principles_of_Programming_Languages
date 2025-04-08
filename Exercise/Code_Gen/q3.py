    def visitBinExpr(self,ctx,o):
        expr1, expr1_type = self.visit(ctx.e1,o)
        expr2, expr2_type = self.visit(ctx.e2,o)
        if ctx.op in ['+', '-']: 
            codegen =expr1 + expr2 + self.emit.emitADDOP(ctx.op, IntType(), o.frame)
            return codegen, IntType()
        if ctx.op in ['*', '/']: 
            codegen =expr1 + expr2 + self.emit.emitMULOP(ctx.op, IntType(), o.frame)
            return codegen, IntType()
        if ctx.op in ['+.', '-.']:
            codegen = expr1 + expr2 + self.emit.emitADDOP(ctx.op[0], FloatType(), o.frame)
            return codegen, FloatType()
        if ctx.op in ['*.', '/.']:
            codegen = expr1 + expr2 + self.emit.emitMULOP(ctx.op[0], FloatType(), o.frame)
            return codegen, FloatType()
    
    
    #op: str 
    # e1 and e2: Expr
    def visitBinExpr(self,ctx,o):
        e1, t1 = self.visit(ctx.e1, o)
        e2, t2  = self.visit(ctx.e2, o)
        op = None
        finalType = IntType() if len(ctx.op) != 2 else FloatType()  
        
        if ctx.op in ['+', '+.']:
            op = self.emit.emitADDOP(ctx.op[0], finalType, o.frame)
            
        elif ctx.op in ['-', '-.']:
            op = self.emit.emitADDOP(ctx.op[0], finalType, o.frame)
        
        elif ctx.op in ['*', '*.']:
            op = self.emit.emitMULOP(ctx.op[0], finalType, o.frame)
        
        elif ctx.op in ['/', '/.']:
            op = self.emit.emitMULOP(ctx.op[0], finalType, o.frame)
            
        jvm_code = e1 + e2 + op
        
        return jvm_code, finalType