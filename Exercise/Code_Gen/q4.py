    def visitId(self, ctx, o):
        name = ctx.name
        sym = o.sym
        for s in sym:
            if s.name == name:
                if type(s.value) is Index:
                    # Local variable
                    codegen = self.emit.emitREADVAR(name, s.mtype, s.value.value, o.frame)
                else:
                    # Global variable
                    codegen = self.emit.emitGETSTATIC(s.value.value + '/' + name, s.mtype, o.frame)
                return codegen, s.mtype