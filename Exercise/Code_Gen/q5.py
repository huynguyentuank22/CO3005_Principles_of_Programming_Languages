    def visitBinExpr(self, ctx, o):
        op = ctx.op
        exp1, typ1 = self.visit(ctx.e1, o)
        exp2, typ2 = self.visit(ctx.e2, o)
    
        # Check mtype
        if isinstance(typ1, FloatType) or isinstance(typ2, FloatType):
            mType = FloatType()
        else:
            mType = IntType()
        if op == '/':
            mType = FloatType()
        if type(typ1) is IntType and type(mType) != type(typ1):
            exp1 = exp1 + self.emit.emitI2F(o.frame)
        if type(typ2) is IntType and type(mType) != type(typ2):
            exp2 = exp2 + self.emit.emitI2F(o.frame)
    
        # Check op
        #@ emitREOP(self, op, inType, frame)
        #@ emitADDOP(self,lexeme, inType, frame)
        if op in ['>','<','>=','<=','!=','==']:
            return exp1 + exp2 + self.emit.emitREOP(op, mType, o.frame), BoolType()
        elif op in ['+', '-']:
            return exp1 + exp2 + self.emit.emitADDOP(op, mType, o.frame), mType
        elif op in ['*', '/']:
            return exp1 + exp2 + self.emit.emitMULOP(op, mType, o.frame), mType