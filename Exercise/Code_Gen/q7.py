    def visitId(self, ctx, o):
        name = ctx.name
        sym = o.sym
        #print([(x.name,x.value) for x in sym])
        for s in sym:
            #print(type(s.value))
            if s.name == name:
                if o.isLeft:
                    if type(s.value) is Index:
                        # Local variable
                        codegen = self.emit.emitWRITEVAR(name, s.mtype, s.value.value, o.frame)
                    else:
                        # Global variable
                        codegen = self.emit.emitPUTSTATIC(s.value.value + '/' + name, s.mtype, o.frame)
                else:
                    if type(s.value) is Index:
                        # Local variable
                        codegen = self.emit.emitREADVAR(name, s.mtype, s.value.value, o.frame)
                    else:
                        # Global variable
                        codegen = self.emit.emitGETSTATIC(s.value.value + '/' + name, s.mtype, o.frame)
                return codegen, s.mtype