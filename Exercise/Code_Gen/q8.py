    def visitAssign(self, ctx, o):
        left_access = Access(o.frame, o.sym, True)
        right_access = Access(o.frame, o.sym, False)
        rhs = ctx.rhs.accept(self, right_access)
        lhs = ctx.lhs.accept(self, left_access)
        return self.emit.printout(rhs[0] + lhs[0])