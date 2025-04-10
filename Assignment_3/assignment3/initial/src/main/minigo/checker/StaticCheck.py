"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
# from Utils import Utils
from StaticError import *
from functools import reduce
from copy import deepcopy

"""
c = [Local(0), NonLocal(1), NonLocal(2),..., Global(N) + BuiltIn()]
Local(i) = [Symbol(1), Symbol(2),..., Symbol(n)]
Global -> var, const, func, struct, interface
"""
class Utils:
    def lookupRedeclared(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None
    
    def lookupUndeclared(self,name,lst,func):
        for x in lst:
            for y in x:
                if name == func(y):
                    return y
        return None
    
    def lookup(self, lst, *name_func):
        for x in lst:
            for y in x:
                if all([z == fun(y) for z, fun in name_func]):
                    return y
        return None
    
    def getType(self, res):
        return res[0] if isinstance(res, tuple) else res
    
    def getValue(self, res):
        if isinstance(res, tuple):
            if isinstance(res[1], (int, float)):
                return res[1]
        return None
    
    def smart_int(self, value):
        return int(value, 0) if isinstance(value, str) else int(value)
    
    def compareType(self, type1, type2):
        if type(type1) is type(type2):
            if isinstance(type1, Id) and isinstance(type2, Id):
                return type1.name == type2.name
            return True
        return False
        
    def checkAssignType(self, type_lhs, type_rhs, ast, c):
        env = c[0]
        if not ((type(type_lhs) is type(type_rhs)) or (isinstance(type_lhs, FloatType) and isinstance(type_rhs, IntType))):
            raise TypeMismatch(ast)
        if type(type_lhs) is ArrayType and type(type_rhs) is ArrayType:
            if len(type_lhs.dimens) != len(type_rhs.dimens):
                raise TypeMismatch(ast)
            # check value each dimens in array type between lhs and rhs
            dims_lhs = [self.getValue(self.visit(x, c)) for x in type_lhs.dimens]
            dims_rhs = [self.getValue(self.visit(x, c)) for x in type_rhs.dimens]
            if any([x != y for x, y in zip(dims_lhs, dims_rhs)]):
                raise TypeMismatch(ast)
            if not ((self.compareType(type_lhs.eleType, type_rhs.eleType)) or (isinstance(type_lhs.eleType, FloatType) and isinstance(type_rhs.eleType, IntType))):
                raise TypeMismatch(ast)
        if isinstance(type_lhs, Id) and isinstance(type_rhs, Id):
            if type_lhs.name == type_rhs.name:
                return
            res_lhs = self.lookup(env, (type_lhs.name, lambda x: x.name), ('INTERFACE', lambda x: x.value))
            res_rhs = self.lookup(env, (type_rhs.name, lambda x: x.name), ('STRUCT', lambda x: x.value))
            if res_lhs and res_rhs:
                struct_methods = [method for method in res_rhs.mtype if method.value == 'METHOD']
                interface_methods = [method for method in res_lhs.mtype if method.value == 'METHOD']
                struct_method_dict = {method.name: method for method in struct_methods}

                # Duyệt qua từng method trong interface
                for intf_method in interface_methods:
                    struct_method = struct_method_dict.get(intf_method.name)
                    # Kiểm tra xem method có tồn tại trong struct không
                    if struct_method is None:
                        raise TypeMismatch(ast)
                    
                    # Kiểm tra kiểu tham số (partype)
                    if len(struct_method.mtype.partype) != len(intf_method.mtype.partype):
                        raise TypeMismatch(ast)  # Số lượng tham số không khớp
                    
                    # So sánh từng kiểu tham số
                    if any([type(struct_param) is not type(intf_param) for struct_param, intf_param in zip(struct_method.mtype.partype, intf_method.mtype.partype)]):
                        raise TypeMismatch(ast)  # Kiểu tham số không khớp
                    
                    # Kiểm tra kiểu trả về (rettype)
                    if type(struct_method.mtype.rettype) is not type(intf_method.mtype.rettype):
                        raise TypeMismatch(ast)  # Kiểu trả về không khớp
            else: raise TypeMismatch(ast)
    
    def checkSameType(self, type1, type2, c):
        if type(type1) is type(type2):
            if isinstance(type1, Id) and isinstance(type2, Id):
                return type1.name == type2.name
            if isinstance(type1, ArrayType) and isinstance(type2, ArrayType):
                if len(type1.dimens) != len(type2.dimens):
                    return False
                # check value each dimens in array type between lhs and rhs
                dims_lhs = [self.getValue(self.visit(x, c)) for x in type1.dimens]
                dims_rhs = [self.getValue(self.visit(x, c)) for x in type2.dimens]
                if any([x != y for x, y in zip(dims_lhs, dims_rhs)]):
                    return False
                if not ((self.compareType(type1.eleType, type2.eleType)) or (isinstance(type1.eleType, FloatType) and isinstance(type2.eleType, IntType))):
                    return False
                return True
            return True
        return False
    
    def printStack(self, env):
        print('======STACK======')
        for i in env:
            print('======')
            for j in i:
                print(str(j))
    
class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [Symbol("getInt",MType([],IntType()), 'FUNCTION'),
                            Symbol("putInt",MType([IntType()],VoidType()), 'FUNCTION'),
                            Symbol("putIntLn",MType([IntType()],VoidType()), 'FUNCTION'),
                            Symbol("getFloat",MType([],FloatType()), 'FUNCTION'),
                            Symbol("putFloat",MType([FloatType()],VoidType()), 'FUNCTION'),
                            Symbol("putFloatLn",MType([FloatType()],VoidType()), 'FUNCTION'),
                            Symbol("getBool",MType([],BoolType()), 'FUNCTION'),
                            Symbol("putBool",MType([BoolType()],VoidType()), 'FUNCTION'),
                            Symbol("putBoolLn",MType([BoolType()],VoidType()), 'FUNCTION'),
                            Symbol("getString",MType([],StringType()), 'FUNCTION'),
                            Symbol("putString",MType([StringType()],VoidType()), 'FUNCTION'),
                            Symbol("putStringLn",MType([StringType()],VoidType()), 'FUNCTION'),
                            Symbol("putLn",MType([],VoidType()), 'FUNCTION')]
    
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        builtin_env = [c] 
        # check redeclared global
        global_ast = [x for x in ast.decl if not isinstance(x, MethodDecl)]
        # global_ast = [x for x in ast.decl if isinstance(x, (StructType, InterfaceType, FuncDecl))]
        global_env = reduce(lambda acc,ele: self.visit(ele, (acc, True)), global_ast, builtin_env)

        # real env
        global_ast = [x for x in ast.decl if isinstance(x, (StructType, InterfaceType, FuncDecl))]
        global_env = reduce(lambda acc,ele: self.visit(ele, (acc, True)), global_ast, builtin_env)
        
        methods = [x for x in ast.decl if isinstance(x, (MethodDecl, StructType))]
        global_env = reduce(lambda acc, ele: self.visit(ele, (acc, True)) if isinstance(ele, MethodDecl) else self.visit(ele, (acc, False)), methods, global_env)
        # ids = [x for x in ast.decl if isinstance(x, (VarDecl, ConstDecl))]
        # global_env = reduce(lambda acc, ele: self.visit(ele, (acc, 'global')), ids, global_env)

        body = [x for x in ast.decl if isinstance(x, (VarDecl, ConstDecl, FuncDecl, MethodDecl))]
        reduce(lambda acc, ele: self.visit(ele, (acc, False)), body, global_env)

    def visitVarDecl(self, ast, c):
        env, isGlobal = c
        if str(isGlobal) == str(True):
            res = self.lookupRedeclared(ast.varName, env[0], lambda x: x.name)
            if res:
                raise Redeclared(Variable(), ast.varName)
            # check array type
            # if isinstance(ast.varType, ArrayType):
            #     res = self.visit(ast.varType, c)
            return [env[0] + [Symbol(ast.varName, ast.varType)]] + env[1:]
        # elif isGlobal == 'global':
        #     if ast.varInit:
        #         c = (env, 'expr')
        #         init = self.visit(ast.varInit, c)
        #         initType = init if not isinstance(init, tuple) else init[0]  # Lấy kiểu từ tuple nếu có
        #         initValue = None if not isinstance(init, tuple) else init[1]  # Lấy giá trị nếu có
        #         if ast.varType is None:
        #             ast.varType = initType
        #             for _, i in enumerate(env):
        #                 for _, j in enumerate(i):
        #                     if j.name == ast.varName:
        #                         j.mtype = initType
        #                         j.value = initValue                            
        #         if not type(ast.varType) is type(initType):
        #             raise TypeMismatch(ast)
        #     return env
        else:
            res = self.lookupRedeclared(ast.varName, env[0], lambda x: x.name)
            if res:
                raise Redeclared(Variable(), ast.varName)
            initValue = None
            # check array type
            if isinstance(ast.varType, ArrayType):
                res = self.visit(ast.varType, c)
            if ast.varInit:
                c = (env, 'expr')
                init = self.visit(ast.varInit, c)
                initType = self.getType(init) # Lấy kiểu từ tuple nếu có
                initValue = self.getValue(init)  # Lấy giá trị nếu có
                if ast.varType is None:
                    ast.varType = initType
                # if not (type(ast.varType) is type(initType) or (isinstance(ast.varType, FloatType) and isinstance(initType, IntType))):
                #     raise TypeMismatch(ast)
                self.checkAssignType(ast.varType, initType, ast, c)
            initValue = 0 if initValue is None and isinstance(ast.varType, IntType) else initValue
            return [env[0] + [Symbol(ast.varName, ast.varType, initValue)]] + env[1:]
        
    def visitConstDecl(self, ast, c):
        env, isGlobal = c
        if str(isGlobal) == str(True):
            res = self.lookupRedeclared(ast.conName, env[0], lambda x: x.name)
            if res:
                raise Redeclared(Constant(), ast.conName)
            return [env[0] + [Symbol(ast.conName, ast.conType)]] + env[1:]
        # elif isGlobal == 'global':
        #     c = (env, 'expr')
        #     init = self.visit(ast.iniExpr, c)
        #     conType = init if not isinstance(init, tuple) else init[0]  # Lấy kiểu từ tuple nếu có
        #     initValue = None if not isinstance(init, tuple) else init[1]  # Lấy giá trị nếu có
        #     if ast.conType is None:
        #         for _, i in enumerate(env):
        #             for _, j in enumerate(i):
        #                 if j.name == ast.conName:
        #                     j.mtype = conType
        #                     j.value = initValue
        #     return env
        else:
            res = self.lookupRedeclared(ast.conName, env[0], lambda x: x.name)
            if res:
                raise Redeclared(Constant(), ast.conName)
            c = (env, 'expr')
            initValue = None
            init = self.visit(ast.iniExpr, c)
            conType = self.getType(init)  # Lấy kiểu từ tuple nếu có
            initValue = self.getValue(init)  # Lấy giá trị nếu có
            if ast.conType is None:
                ast.conType = conType
            return [env[0] + [Symbol(ast.conName, ast.conType, initValue)]] + env[1:]
        
    def visitStructType(self,ast, c):
        env, isGlobal = c
        if isGlobal:
            if self.lookupRedeclared(ast.name, env[0], lambda x: x.name):
                raise Redeclared(Type(), ast.name)
            return [env[0] + [Symbol(ast.name, [], 'STRUCT')]] + env[1:]
        else:
            # fields = []
            # self.printStack(env)
            for _, x in enumerate(env): # env [[Symbol]]
                for _, y in enumerate(x): # x [Symbol]
                    # y Symbol
                    if ast.name == y.name:
                        for name, typ in ast.elements:
                            for _, z in enumerate(y.mtype):
                                if name == z.name:
                                    # print(name, z.name)
                                    raise Redeclared(Field(), name)
                            y.mtype.append(Symbol(name, typ, 'FIELD'))
                        if ast.methods:
                            for method in ast.methods:
                                for _, z in enumerate(y.mtype):
                                    if method.fun.name == z.name:
                                        raise Redeclared(Method(), method.fun.name)
                                parTypes = []
                                if method.fun.params:
                                    param = reduce(lambda acc, ele: self.visit(ele, (acc, isGlobal)), method.fun.params, parTypes)
                                    parTypes = [x[1] for x in param]
                                    # parTypes = parTypes[1:] # Bỏ qua receiver
                                y.mtype.append(Symbol(method.fun.name, MType(parTypes, method.fun.retType), 'METHOD'))
                            #     if ast.fun.name == z.name:
                            #         raise Redeclared(Method(), ast.fun.name)
                            # parTypes = []
                            # if ast.fun.params:
                            #     param = reduce(lambda acc, ele: self.visit(ele, (acc, isGlobal)), ast.fun.params, [(ast.receiver, ast.recType)])
                            #     parTypes = [x[1] for x in param]
                            #     parTypes = parTypes[1:] # Bỏ qua receiver
                            # y.mtype.append(Symbol(ast.fun.name, MType(parTypes, ast.fun.retType), 'METHOD'))
            # self.printStack(env)
            return env
        
        

    def visitInterfaceType(self,ast, c):
        # prototype: list of Symbol
        env, isGlobal = c
        if self.lookupRedeclared(ast.name, env[0], lambda x: x.name):
            raise Redeclared(Type(), ast.name)
        
        prototype = reduce(lambda acc, ele: self.visit(ele, acc), ast.methods, [])
        return [env[0] + [Symbol(ast.name, prototype, 'INTERFACE')]] + env[1:]
    
    def visitPrototype(self,ast, c):
        res = self.lookupRedeclared(ast.name, c, lambda x: x.name)
        if res:
            raise Redeclared(Prototype(), ast.name)
        return c + [Symbol(ast.name, MType(ast.params, ast.retType), 'METHOD')]

    def visitFuncDecl(self,ast, c):
        env, isGlobal = c
        if isGlobal:
            res = self.lookupRedeclared(ast.name, env[0], lambda x: x.name)
            if res:
                raise Redeclared(Function(), ast.name)
            parTypes = []
            if ast.params:
                params = reduce(lambda acc, ele: self.visit(ele, (acc, isGlobal)), ast.params, [])
                parTypes = [x[1] for x in params]
            return [env[0] + [Symbol(ast.name, MType(parTypes, ast.retType), 'FUNCTION')]] + env[1:]
        else:
            local_env = deepcopy(env)
            if ast.params:
                local_env = reduce(lambda acc, ele: self.visit(ele, (acc, isGlobal)), ast.params, [[]] + local_env)
            self.visit(ast.body, ([[]] + local_env, ast.retType))
            return env

    def visitParamDecl(self,ast, c):
        env, isGlobal = c
        if isGlobal:
            res = self.lookupRedeclared(ast.parName, env, lambda x: x[0])
            if res:
                raise Redeclared(Parameter(), ast.parName)
            return env + [(ast.parName ,ast.parType)]
        else:
            return [env[0] + [Symbol(ast.parName, ast.parType)]] + env[1:]
    
    def visitMethodDecl(self,ast, c):
        env, isGlobal = c
        if isGlobal:
            for _, x in enumerate(env): # env [[Symbol]]
                for _, y in enumerate(x): # x [Symbol]
                    # y Symbol
                    if ast.recType.name == y.name:
                        for _, z in enumerate(y.mtype):
                            if ast.fun.name == z.name:
                                raise Redeclared(Method(), ast.fun.name)
                        parTypes = []
                        if ast.fun.params:
                            param = reduce(lambda acc, ele: self.visit(ele, (acc, isGlobal)), ast.fun.params, parTypes)
                            parTypes = [x[1] for x in param]
                            # parTypes = parTypes[1:] # Bỏ qua receiver
                        y.mtype.append(Symbol(ast.fun.name, MType(parTypes, ast.fun.retType), 'METHOD'))
                        return env
            return env
        else:
            local_env = deepcopy(env)
            local_env = [[Symbol(ast.receiver, ast.recType)]] + local_env
            if ast.fun.params:
                local_env = reduce(lambda acc, ele: self.visit(ele, (acc, isGlobal)), ast.fun.params, [[]] + local_env)
            self.visit(ast.fun.body, ([[]] + local_env, ast.fun.retType))
            return env        
    
    def visitBlock(self, ast, c):
        env, isGlobal = c
        # if str(isGlobal) == 'for':
        reduce(lambda acc, ele: self.visit(ele, (acc, isGlobal)), ast.member, env)
        # else:
        #     reduce(lambda acc, ele: self.visit(ele, (acc, isGlobal)), ast.member, [[]] + env)
        return env

    def visitFuncCall(self,ast, c):
        env, isGlobal = c
        c = (env, 'expr')
        # self.printStack(env)
        res = self.lookupUndeclared(ast.funName, env, lambda x: x.name)
        if (res is None) or (res and res.value != 'FUNCTION'):
            raise Undeclared(Function(), ast.funName)
        if res and res.value == 'FUNCTION':
            if len(ast.args) != len(res.mtype.partype):
                raise TypeMismatch(ast)
            # print('args', ast.args)
            if any([not self.checkSameType(self.getType(self.visit(x, c)), res.mtype.partype[i], c) for i, x in enumerate(ast.args)]):
                raise TypeMismatch(ast)
            # print(isGlobal)
            if str(isGlobal) == 'expr':
                if isinstance(res.mtype.rettype, VoidType):
                    raise TypeMismatch(ast)
                return res.mtype.rettype
            else:
                if not isinstance(res.mtype.rettype, VoidType):
                    raise TypeMismatch(ast)
                return env
    
    def visitMethCall(self, ast, c):
        env, isGlobal = c
        c = (env, 'expr')
        # Xử lý receiver để lấy kiểu của nó
        if isinstance(ast.receiver, MethCall):
            recv_type = self.visitMethCall(ast.receiver, c)  # Đệ quy cho MethCall lồng nhau
        elif isinstance(ast.receiver, Id):
            # Tìm Id trong môi trường
            res = self.lookupUndeclared(ast.receiver.name, env, lambda x: x.name)
            if res is None:
                raise Undeclared(Identifier(), ast.receiver.name)
            recv_type = res.mtype  # Kiểu của Id (có thể là Id, struct, hoặc interface)
        elif isinstance(ast.receiver, FieldAccess):
            recv_type = self.visitFieldAccess(ast.receiver, c)  # Xử lý FieldAccess
        elif isinstance(ast.receiver, ArrayCell):
            recv_type = self.visitArrayCell(ast.receiver, c)
        elif isinstance(ast.receiver, FuncCall):
            recv_type = self.visitFuncCall(ast.receiver, c)
        else:
            raise TypeMismatch(ast)
        # Kiểm tra xem recv_type có phải là struct hoặc interface không
        if isinstance(recv_type, Id):
            type_symbol = self.lookupUndeclared(recv_type.name, env, lambda x: x.name)
            if type_symbol is None or type_symbol.value not in ['STRUCT', 'INTERFACE']:
                raise TypeMismatch(ast)
            methods = [x for x in type_symbol.mtype if x.value == 'METHOD']
        else:
            raise TypeMismatch(ast)
        # Tìm method trong danh sách methods
        method_symbol = self.lookupRedeclared(ast.metName, methods, lambda x: x.name)
        if method_symbol is None:
            raise Undeclared(Method(), ast.metName)
        if len(ast.args) != len(method_symbol.mtype.partype):
            raise TypeMismatch(ast)
        if any([not self.checkSameType(self.getType(self.visit(x, c)), method_symbol.mtype.partype[i], c) for i, x in enumerate(ast.args)]):
            raise TypeMismatch(ast)
        # print(isGlobal)
        if str(isGlobal) == 'expr':
            if isinstance(method_symbol.mtype.rettype, VoidType):
                raise TypeMismatch(ast)
            return method_symbol.mtype.rettype  # Trả về kiểu trả về của method 
        else: 
            if not isinstance(method_symbol.mtype.rettype, VoidType):
                raise TypeMismatch(ast)
            return env

    def visitFieldAccess(self, ast, c):
        # print(c)
        env = c[0]
        # c = (env, 'expr')
        # Xử lý receiver để lấy kiểu của nó
        if isinstance(ast.receiver, FieldAccess):
            recv_type = self.visitFieldAccess(ast.receiver, c)  # Đệ quy để lấy kiểu của receiver
        elif isinstance(ast.receiver, Id):
            # Tìm Id trong môi trường
            res = self.lookupUndeclared(ast.receiver.name, env, lambda x: x.name)
            if res is None:
                raise Undeclared(Identifier(), ast.receiver.name)
            recv_type = res.mtype  # Kiểu của Id (có thể là Id hoặc struct)
        elif isinstance(ast.receiver, MethCall):
            recv_type = self.visitMethCall(ast.receiver, c)
        elif isinstance(ast.receiver, ArrayCell):
            recv_type = self.visitArrayCell(ast.receiver, c)
        else:
            raise TypeMismatch(ast)

        # Kiểm tra xem recv_type có phải là struct không
        if isinstance(recv_type, Id):
            struct_symbol = self.lookupUndeclared(recv_type.name, env, lambda x: x.name)
            if struct_symbol is None or struct_symbol.value != 'STRUCT':
                raise TypeMismatch(ast)
            fields = [x for x in struct_symbol.mtype if x.value == 'FIELD']
        else:
            raise TypeMismatch(ast)

        # Tìm field trong danh sách fields
        field_symbol = self.lookupRedeclared(ast.field, fields, lambda x: x.name)
        if field_symbol is None:
            raise Undeclared(Field(), ast.field)
        
        return field_symbol.mtype  # Trả về kiểu của field để dùng ở mức trên
    
    def visitArrayCell(self, ast, c):
        # c = (c[0], 'expr')
        arr_type = self.getType(self.visit(ast.arr, c))
        idx = [self.visit(x, c) for x in ast.idx]
        if not isinstance(arr_type, ArrayType):
            raise TypeMismatch(ast)
        if any([not isinstance(self.getType(x), IntType) for x in idx]):
            raise TypeMismatch(ast)
        if len(idx) == len(arr_type.dimens):
            return arr_type.eleType
        if len(arr_type.dimens) > len(idx):
            remain_idx = arr_type.dimens[len(idx):]
            return ArrayType(remain_idx, arr_type.eleType)
        # return arr_type.eleType
    
    def visitNilLiteral(self, ast, c):
        return (VoidType(), None)
    
    def visitIntLiteral(self, ast, c):
        return (IntType(), self.smart_int(ast.value))

    def visitFloatLiteral(self, ast, c):
        return (FloatType(), float(ast.value))

    def visitStringLiteral(self, ast, c):
        return (StringType(), ast.value)

    def visitBooleanLiteral(self, ast, c):
        return (BoolType(), ast.value)
    
    def visitArrayLiteral(self, ast, c):
        dim_types = [self.getType(self.visit(x, c)) for x in ast.dimens]
        if any([not isinstance(x, IntType) for x in dim_types]):
            raise TypeMismatch(ast)
        def flatten_array(arr):
            """Làm phẳng mảng bằng generator."""
            return [x for item in arr for x in (flatten_array(item) if isinstance(item, (list, tuple)) else [item])]
        flat_values = flatten_array(ast.value)
        if any([not self.compareType(self.getType(self.visit(x, c)), ast.eleType) for x in flat_values]):
            raise TypeMismatch(ast)
        return (ArrayType(ast.dimens, ast.eleType), None)
    
    def visitArrayType(self, ast, c):
        # self.printStack(c[0])
        dim_types = [self.getType(self.visit(x, c)) for x in ast.dimens]
        if any([not isinstance(x, IntType) for x in dim_types]):
            raise TypeMismatch(ast)
        return (ArrayType(ast.dimens, ast.eleType), None)

    def visitStructLiteral(self, ast, c):
        env, isGlobal = c
        res = self.lookup(env, (ast.name, lambda x: x.name), ('STRUCT', lambda x: x.value))
        fields = []
        for field, expr in ast.elements:
            if field in fields:
                raise Redeclared(Field(), field)
            # typ = self.getType(self.visit(expr, c))
            ress = self.lookupRedeclared(field, res.mtype, lambda x: x.name)
            if ress is None:
                raise Undeclared(Field(), field)
            # if ress
            fields.append(field)
        return (Id(ast.name), None) 

    def visitAssign(self, ast, c):
        env, isGlobal = c
        # if isinstance(ast.lhs, Id):
        #     res = self.lookupRedeclared(ast.lhs.name, env[0], lambda x: x.name)
        #     if res is None:
        #         try:
        #             c = (env, 'expr')
        #             rhs = self.visit(ast.rhs, c)
        #             type_rhs = self.getType(rhs)
        #             val_rhs = self.getValue(rhs)
        #             return [env[0] + [Symbol(ast.lhs.name, type_rhs, val_rhs)]] + env[1:]

        #         except Undeclared as e:
        #             if ast.lhs.name == e.n:
        #                 raise TypeMismatch(ast)
        #             raise Undeclared(e.k, e.n)
        if isinstance(ast.lhs, Id):
            res = self.lookupRedeclared(ast.lhs.name, env[0], lambda x: x.name)
            ress = self.lookupUndeclared(ast.lhs.name, env, lambda x: x.name)
            if ress is None:
                if isinstance(ast.rhs, BinaryOp):
                    if isinstance(ast.rhs.left, Id):
                        if ast.rhs.left.name == ast.lhs.name:
                            raise Undeclared(Identifier(), ast.lhs.name)
                try:
                    c = (env, 'expr')
                    rhs = self.visit(ast.rhs, c)
                    type_rhs = self.getType(rhs)
                    val_rhs = self.getValue(rhs)
                    return [env[0] + [Symbol(ast.lhs.name, type_rhs, val_rhs)]] + env[1:]

                except Undeclared as e:
                    if ast.lhs.name == e.n:
                        print('hi')
                        raise TypeMismatch(ast)
                    raise Undeclared(e.k, e.n)
            elif ress and res is None:
                try:
                    c = (env, 'expr')
                    rhs = self.visit(ast.rhs, c)
                    type_rhs = self.getType(rhs)
                    val_rhs = self.getValue(rhs)
                    if type(ress.mtype) is not type(type_rhs):
                        return [env[0] + [Symbol(ast.lhs.name, type_rhs, val_rhs)]] + env[1:]

                except Undeclared as e:
                    if ast.lhs.name == e.n:
                        print('hi')
                        raise TypeMismatch(ast)
                    raise Undeclared(e.k, e.n)
                
        c = (env, 'expr')   
        lhs = self.visit(ast.lhs, c)
        rhs = self.visit(ast.rhs, c)
        type_lhs = self.getType(lhs)
        type_rhs = self.getType(rhs)
        if isinstance(type_lhs, VoidType):
            raise TypeMismatch(ast)
        # if not ((type(type_lhs) is type(type_rhs)) or (isinstance(type_lhs, FloatType) and isinstance(type_rhs, IntType))):
        #     raise TypeMismatch(ast)
        # if type(type_lhs) is ArrayType and type(type_rhs) is ArrayType:
        #     if len(type_lhs.dimens) != len(type_rhs.dimens):
        #         raise TypeMismatch(ast)
        #     # check value each dimens in array type between lhs and rhs
        #     dims_lhs = [self.getValue(self.visit(x, c)) for x in type_lhs.dimens]
        #     dims_rhs = [self.getValue(self.visit(x, c)) for x in type_rhs.dimens]
        #     if any([x != y for x, y in zip(dims_lhs, dims_rhs)]):
        #         raise TypeMismatch(ast)
        #     if not ((type(type_lhs.eleType) is type(type_rhs.eleType)) or (isinstance(type_lhs.eleType, FloatType) and isinstance(type_rhs.eleType, IntType))):
        #         raise TypeMismatch(ast)
        # if isinstance(type_lhs, Id) and isinstance(type_rhs, Id):
        #     res_lhs = self.lookup(env, (type_lhs.name, lambda x: x.name), ('INTERFACE', lambda x: x.value))
        #     res_rhs = self.lookup(env, (type_rhs.name, lambda x: x.name), ('STRUCT', lambda x: x.value))
        #     if  res_lhs and res_rhs:
        #         struct_methods = [method for method in res_rhs.mtype if method.value == 'METHOD']
        #         interface_methods = [method for method in res_lhs.mtype if method.value == 'METHOD']
        #         struct_method_dict = {method.name: method for method in struct_methods}

        #         # Duyệt qua từng method trong interface
        #         for intf_method in interface_methods:
        #             struct_method = struct_method_dict.get(intf_method.name)
        #             # Kiểm tra xem method có tồn tại trong struct không
        #             if struct_method is None:
        #                 raise TypeMismatch(ast)
                    
        #             # Kiểm tra kiểu tham số (partype)
        #             if len(struct_method.mtype.partype) != len(intf_method.mtype.partype):
        #                 raise TypeMismatch(ast)  # Số lượng tham số không khớp
                    
        #             # So sánh từng kiểu tham số
        #             if any([type(struct_param) is not type(intf_param) for struct_param, intf_param in zip(struct_method.mtype.partype, intf_method.mtype.partype)]):
        #                 raise TypeMismatch(ast)  # Kiểu tham số không khớp
                    
        #             # Kiểm tra kiểu trả về (rettype)
        #             if type(struct_method.mtype.rettype) is not type(intf_method.mtype.rettype):
        #                 raise TypeMismatch(ast)  # Kiểu trả về không khớp
        self.checkAssignType(type_lhs, type_rhs, ast, c)
        return env
    
    def visitId(self,ast,c):
        env = c[0]
        res = self.lookupUndeclared(ast.name, env, lambda x: x.name) # ast.name in x
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        return (res.mtype, res.value)
    
    def visitIf(self,ast,c):
        env, isGlobal = c
        expr_typ = self.visit(ast.expr, c)
        if not isinstance(self.getType(expr_typ), BoolType):
            raise TypeMismatch(ast)
        
        self.visit(ast.thenStmt, ([[]] + env, isGlobal))
        if ast.elseStmt:
            self.visit(ast.elseStmt, c)

        return env

    def visitForBasic(self,ast,c):
        env, isGlobal = c
        cond_typ = self.getType(self.visit(ast.cond, c))
        if not isinstance(cond_typ, BoolType):
            raise TypeMismatch(ast)
        
        self.visit(ast.loop, ([[]] + env, isGlobal))

        return env
    
    def visitForStep(self,ast,c):
        env, isGlobal = c
        local_env = deepcopy(env)
        local_env = self.visit(ast.init, ([[]] + local_env, isGlobal))
        cond_typ = self.getType(self.visit(ast.cond, (local_env, isGlobal)))
        if not isinstance(cond_typ, BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.upda, (local_env, isGlobal))
        self.visit(ast.loop, (local_env, isGlobal))
        return env
    
    def visitForEach(self,ast,c):
        env, isGlobal = c
        local_env = deepcopy(env)
        # local_env = [[]] + local_env
        # if ast.idx.name != '_':
        #     local_env = [local_env[0] + [Symbol(ast.idx.name, IntType())]] + local_env[1:]
        # res = self.lookupRedeclared(ast.value.name, local_env[0], lambda x: x.name)
        # if res: 
        #     raise Redeclared(Variable(), ast.value.name)
        arr_typ = self.getType(self.visit(ast.arr, c))
        if not isinstance(arr_typ, ArrayType):
            raise TypeMismatch(ast)
        
        if ast.idx.name != '_':
            idx_typ = self.getType(self.visit(ast.idx, c))
            if not isinstance(idx_typ, IntType):
                raise TypeMismatch(ast)
        val_typ = self.getType(self.visit(ast.value, c))
        if not type(val_typ) is type(arr_typ.eleType):
            raise TypeMismatch(ast)
        
        local_env = [local_env[0] + [Symbol(ast.value.name, arr_typ.eleType)]] + local_env[1:]
        self.visit(ast.loop, ([[]] + local_env, isGlobal))
        return env

    def visitBreak(self,ast,c):
        return c[0]

    def visitContinue(self,ast,c):
        return c[0]

    def visitReturn(self,ast,c):
        env, func_name = c
        c = (env, 'expr')
        typ_expr = VoidType() if ast.expr is None else self.getType(self.visit(ast.expr, c))
        # print(typ_expr)
        # res_func = self.lookup(env, (func_name, lambda x: x.name), ('FUNCTION', lambda x: x.value))
        # res_meth = self.lookup(env, (func_name, lambda x: x.name), ('METHOD', lambda x: x.value))
        # if res_func:
        #     if not type(res_func.mtype.rettype) is type(typ_expr):
        #         raise TypeMismatch(ast)
        # if res_meth:
        #     if not type(res_meth.fun.mtype.rettype) is type(typ_expr):
        #         raise TypeMismatch(ast)
        # print(func_name)
        # print(typ_expr, func_name)
        if not self.checkSameType(typ_expr, func_name, c):
            raise TypeMismatch(ast)
        # if func_name.startswith('ArrayType('):
        #     # print('ArrayType')
        #     if not isinstance(typ_expr, ArrayType):
        #         raise TypeMismatch(ast)
        # if func_name.startswith('Id('):
        #     # print('Id')
        #     if not isinstance(typ_expr, Id):
        #         raise TypeMismatch(ast)
        #     if typ_expr.name != func_name[3:-1]:
        #         raise TypeMismatch(ast)
        # # if not isinstance(typ_expr, func_name):
        # #     raise TypeMismatch(ast)
        # dict = { 'VoidType': VoidType, 'IntType': IntType, 'FloatType': FloatType, 'StringType': StringType, 'BoolType': BoolType }
        # if func_name in dict:
        #     if not isinstance(typ_expr, dict[func_name]):
        #         raise TypeMismatch(ast)
        
        return env
             
    def visitBinaryOp(self, ast, c):
        # + Addition int/float/string
        # - Subtraction int/float 
        # * Multiplication int/float 
        # / Division int/float
        # % Modulus int
        # == Equal int/float/string 
        # != Not equal int/float/string 
        # < Less than int/float/string 
        # > Greater than int/float/string 
        # <= Less than or equal int/float/string 
        # >= Greater than or equal int/float/string
        # ! Negation boolean 
        # && Conjunction (AND) boolean 
        # || Disjunction (OR) boolean
        # c = (c[0], 'expr')
        # print(c)
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)

        # Xử lý tuple từ visit (có thể từ Id hoặc literal)
        left_type = self.getType(left)
        left_value = left[1] if isinstance(left, tuple) else None
        right_type = self.getType(right)
        right_value = right[1] if isinstance(right, tuple) else None

        # Kiểm tra xem có thể tính toán giá trị không
        can_compute = (left_value is not None and right_value is not None and 
                    isinstance(left_value, (int, float)) and isinstance(right_value, (int, float)))

        if ast.op == '+':
            if not (isinstance(left_type, (IntType, FloatType, StringType)) and isinstance(right_type, (IntType, FloatType, StringType))):
                # print('cho nay')
                raise TypeMismatch(ast)
            if type(left_type) is StringType and type(right_type) is StringType:
                return StringType()
            if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
                result_type = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
                if can_compute:
                    left_val = float(left_value) if isinstance(left_type, FloatType) else left_value
                    right_val = float(right_value) if isinstance(right_type, FloatType) else right_value
                    result = left_val + right_val
                    return (result_type, result)
                return result_type

        if ast.op in ['-', '*', '/']:
            if not isinstance(left_type, (IntType, FloatType)) or not isinstance(right_type, (IntType, FloatType)):
                raise TypeMismatch(ast)
            result_type = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
            if can_compute:
                left_val = float(left_value) if isinstance(left_type, FloatType) else left_value
                right_val = float(right_value) if isinstance(right_type, FloatType) else right_value
                if ast.op == '-':
                    result = left_val - right_val
                elif ast.op == '*':
                    result = left_val * right_val
                elif ast.op == '/':
                    if right_val != 0:
                        result = left_val / right_val
                    else: result = None
                return (result_type, result)
            return result_type

        if ast.op == '%':
            if not isinstance(left_type, IntType) or not isinstance(right_type, IntType):
                raise TypeMismatch(ast)
            if can_compute:
                return (IntType(), int(left_value) % int(right_value))
            return IntType()

        if ast.op in ['==', '!=', '<', '>', '<=', '>=']:
            if not (isinstance(left_type, (IntType, FloatType, StringType)) and isinstance(right_type, (IntType, FloatType, StringType))):
                raise TypeMismatch(ast)
            if not type(left_type) is type(right_type):
                raise TypeMismatch(ast)
            return BoolType()

        if ast.op in ['&&', '||']:
            if not isinstance(left_type, BoolType) or not isinstance(right_type, BoolType):
                raise TypeMismatch(ast)
            return BoolType()

        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast, c):
        # c = (c[0], 'expr')
        body = self.visit(ast.body, c)
        
        # Xử lý tuple từ visit
        body_type = self.getType(body)
        body_value = body[1] if isinstance(body, tuple) else None

        # Kiểm tra xem có thể tính toán không
        can_compute = body_value is not None and isinstance(body_value, (int, float))

        if ast.op == '-':
            if not isinstance(body_type, (IntType, FloatType)):
                raise TypeMismatch(ast)
            result_type = FloatType() if isinstance(body_type, FloatType) else IntType()
            if can_compute:
                value = float(body_value) if isinstance(body_type, FloatType) else body_value
                result = -value
                return (result_type, result)
            return result_type

        if ast.op == '!':
            if not isinstance(body_type, BoolType):
                raise TypeMismatch(ast)
            return BoolType()

        raise TypeMismatch(ast)