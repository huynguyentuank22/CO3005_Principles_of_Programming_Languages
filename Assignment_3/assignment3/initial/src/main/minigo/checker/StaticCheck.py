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
    
    def getType(self, res):
        # if isinstance(res, tuple):
        #     print(res[0])
        # else: print(res)
        return res[0] if isinstance(res, tuple) else res
    
    def getValue(self, res):
        # print(res)
        if isinstance(res, tuple):
            if isinstance(res[1], (int, float)):
                return res[1]
        return None
    
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
        self.global_envi = [Symbol("getInt",MType([],IntType())),
                            Symbol("putInt",MType([IntType()],VoidType())),
                            Symbol("putIntLn",MType([IntType()],VoidType())),
                            Symbol("getFloat",MType([],FloatType())),
                            Symbol("putFloat",MType([FloatType()],VoidType())),
                            Symbol("putFloatLn",MType([FloatType()],VoidType())),
                            Symbol("getBool",MType([],BoolType())),
                            Symbol("putBool",MType([BoolType()],VoidType())),
                            Symbol("putBoolLn",MType([BoolType()],VoidType())),
                            Symbol("getString",MType([],StringType())),
                            Symbol("putString",MType([StringType()],VoidType())),
                            Symbol("putStringLn",MType([StringType()],VoidType())),
                            Symbol("putLn",MType([],VoidType()))]
 
    
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        # check var, const, struct, interface, func (name, param type)
        builtin_env = [c] # [[]] +
        global_ast = [x for x in ast.decl if not isinstance(x, MethodDecl)]
        global_env = reduce(lambda acc,ele: self.visit(ele, (acc, True)), global_ast, builtin_env)

        methods = [x for x in ast.decl if isinstance(x, MethodDecl)]
        global_env = reduce(lambda acc, ele: self.visit(ele, (acc, True)), methods, global_env)
        # if not global_env:
        #     print('global_env is None')

        ids = [x for x in ast.decl if isinstance(x, (VarDecl, ConstDecl))]
        global_env = reduce(lambda acc, ele: self.visit(ele, (acc, 'global')), ids, global_env)

        body = [x for x in ast.decl if isinstance(x, FuncDecl) or isinstance(x, MethodDecl)]
        # list(map(lambda x: self.visit(x, (global_env, False)), funcs))
        reduce(lambda acc, ele: self.visit(ele, (acc, False)), body, global_env)

    def visitVarDecl(self, ast, c): #!!!!!!!!!!!!!!
        env, isGlobal = c
        if isGlobal == True:
            res = self.lookupRedeclared(ast.varName, env[0], lambda x: x.name)
            if res:
                raise Redeclared(Variable(), ast.varName)
            return [env[0] + [Symbol(ast.varName, ast.varType)]] + env[1:]
        elif isGlobal == 'global':
            if ast.varInit:
                init = self.visit(ast.varInit, c)
                initType = init if not isinstance(init, tuple) else init[0]  # Lấy kiểu từ tuple nếu có
                initValue = None if not isinstance(init, tuple) else init[1]  # Lấy giá trị nếu có
                if ast.varType is None:
                    ast.varType = initType
                    for _, i in enumerate(env):
                        for _, j in enumerate(i):
                            if j.name == ast.varName:
                                j.mtype = initType
                                j.value = initValue

                if not type(ast.varType) is type(initType):
                    raise TypeMismatch(ast)
            return env
        else:
            res = self.lookupRedeclared(ast.varName, env[0], lambda x: x.name)
            if res:
                raise Redeclared(Variable(), ast.varName)
            initValue = None
            if ast.varInit:
                init = self.visit(ast.varInit, c)
                initType = init if not isinstance(init, tuple) else init[0]  # Lấy kiểu từ tuple nếu có
                initValue = None if not isinstance(init, tuple) else init[1]  # Lấy giá trị nếu có
                # print(initValue)
                if ast.varType is None:
                    ast.varType = initType
                if not type(ast.varType) is type(initType):
                    raise TypeMismatch(ast)
            return [env[0] + [Symbol(ast.varName, ast.varType, initValue)]] + env[1:]
        
    def visitConstDecl(self, ast, c):
        env, isGlobal = c
        if isGlobal == True:
            res = self.lookupRedeclared(ast.conName, env[0], lambda x: x.name)
            if res:
                raise Redeclared(Constant(), ast.conName)
            return [env[0] + [Symbol(ast.conName, ast.conType)]] + env[1:]
        elif isGlobal == 'global':
            init = self.visit(ast.iniExpr, c)
            conType = init if not isinstance(init, tuple) else init[0]  # Lấy kiểu từ tuple nếu có
            initValue = None if not isinstance(init, tuple) else init[1]  # Lấy giá trị nếu có
            if ast.conType is None:
                for _, i in enumerate(env):
                    for _, j in enumerate(i):
                        if j.name == ast.conName:
                            j.mtype = conType
                            j.value = initValue
            return env
        else:
            res = self.lookupRedeclared(ast.conName, env[0], lambda x: x.name)
            if res:
                raise Redeclared(Constant(), ast.conName)
            initValue = None
            init = self.visit(ast.iniExpr, c)
            conType = init if not isinstance(init, tuple) else init[0]  # Lấy kiểu từ tuple nếu có
            initValue = None if not isinstance(init, tuple) else init[1]  # Lấy giá trị nếu có
            if ast.conType is None:
                ast.conType = conType
            return [env[0] + [Symbol(ast.conName, ast.conType, initValue)]] + env[1:]
        

    def visitStructType(self,ast, c):
        env = c[0]
        if self.lookupRedeclared(ast.name, env[0], lambda x: x.name):
            raise Redeclared(Type(), ast.name)
        
        fields = []
        for name, typ in ast.elements:
            if self.lookupRedeclared(name, fields, lambda x: x.name):
                raise Redeclared(Field(), name)
            fields.append(Symbol(name, typ, 'FIELD'))
        
        # env = [env[0] + [Symbol(ast.name, ast.methods)]] + env[1:]
        # for mem in ast.elements:
        #     if self.lookupRedeclared(mem[0], env[0][-1].mtype, lambda x: x.partype):
        #         raise Redeclared(Field(), mem[0])
        #     env[0][-1].mtype.append(MType(mem[0], mem[1])) 

        return [env[0] + [Symbol(ast.name, fields, 'STRUCT')]] + env[1:]

    def visitInterfaceType(self,ast, c):
        # prototype: list of Symbol
        env, isGlobal = c
        if self.lookupRedeclared(ast.name, env[0], lambda x: x.name):
            raise Redeclared(Type(), ast.name)
        
        # env = [env[0] + [Symbol(ast.name, ast.methods)]] + env[1:]
        # scope = reduce(lambda acc, ele: self.visit(ele, (acc, isGlobal)), ast.methods, [])
        # env[0][-1].mtype = scope
        prototype = reduce(lambda acc, ele: self.visit(ele, acc), ast.methods, [])
        return [env[0] + [Symbol(ast.name, prototype, 'INTERFACE')]] + env[1:]
    
    def visitPrototype(self,ast, c):
        res = self.lookupRedeclared(ast.name, c, lambda x: x.name)
        if res:
            raise Redeclared(Prototype(), ast.name)
        return c + [Symbol(ast.name, MType(ast.params, ast.retType), 'METHOD')]
        # return [c[0] + [Symbol(ast.name, MType(ast.params, ast.retType))]] + c[1:]

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
                # local_env = [[]] + local_env
                local_env = reduce(lambda acc, ele: self.visit(ele, (acc, isGlobal)), ast.params, [[]] + local_env)
            # env = [[]] + env
            self.visit(ast.body, (local_env, isGlobal))
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
        # try:
        #     print(c)
        #     self.visit(ast.fun, c)
        # except Redeclared:
        #     raise Redeclared(Method(), ast.fun.name)

        # res = self.lookupUndeclared(ast.recType, c, lambda x: x.name)
        # if res:
            # flag = self.lookupRedeclared(ast.fun.name, res.mtype, lambda x: x)
            # if flag:
            #     raise Redeclared(Method(), flag)
            # res.mtype += ast.fun.name
        # self.printStack(c)
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
                            parTypes = reduce(lambda acc, ele: self.visit(ele, (acc, isGlobal)), ast.fun.params, [])
                        y.mtype.append(Symbol(ast.fun.name, MType(parTypes, ast.fun.retType), 'METHOD'))
                        return env
            return env
        else:
            local_env = deepcopy(env)
            if ast.fun.params:
                # local_env = [[]] + local_env
                local_env = reduce(lambda acc, ele: self.visit(ele, (acc, isGlobal)), ast.fun.params, [[]] + local_env)
            # env = [[]] + env
            self.visit(ast.fun.body, (local_env, isGlobal))
            return env
        


        # print('==BEFORE==')
        # self.printStack(env)
        # for _, x in enumerate(env):
        #     for _, y in enumerate(x):
        #         print(ast.recType.name, y.name)
        #         if ast.recType.name == y.name:
        #             print('==FOUND==')
        #             for _, z in enumerate(y.mtype):
        #                 if ast.fun.name == z.partype:
        #                     print('vcl', ast.fun.name, z.partype)
        #                     raise Redeclared(Method(), ast.fun.name)
        #             y.mtype.append(MType(ast.fun.name, ast.fun.retType))
        #             break
        # print('==AFTER==')
        # self.printStack(env)
        # env = [c[0] + [Symbol(ast.fun.name, ast.fun.retType)]] + c[1:]
        # if ast.fun.params:
        #     env = [[]] + env
        #     env = reduce(lambda acc, ele: self.visit(ele, acc), ast.fun.params, env)

        # self.visit(ast.fun.body, env)
        # return [c[0] + [Symbol(ast.fun.name, ast.fun.retType)]] + c[1:]        

        # return env
        

    
    def visitBlock(self, ast, c):
        env, isGlobal = c
        # env = [[]] + env
        reduce(lambda acc, ele: self.visit(ele, (acc, isGlobal)), ast.member, [[]] + env)
        return env

    def visitFuncCall(self,ast, c):
        env = c[0]
        res = self.lookupUndeclared(ast.funName, env, lambda x: x.name)
        if (res is None) or (res and res.value != 'FUNCTION'):
            raise Undeclared(Function(), ast.funName)
        if res and res.value == 'FUNCTION':
            if len(ast.args) != len(res.mtype.partype):
                raise TypeMismatch(ast)
            if any([type(self.visit(x, c)) is not type(res.mtype.partype[i]) for i, x in enumerate(ast.args)]):
                raise TypeMismatch(ast)
            return res.mtype.rettype
    
    def visitMethCall(self, ast, c):
        env = c[0]
        # Xử lý receiver để lấy kiểu của nó
        if isinstance(ast.receiver, MethCall):
            recv_type = self.visitMethCall(ast.receiver, c)  # Đệ quy cho MethCall lồng nhau
        elif isinstance(ast.receiver, Id):
            # Tìm Id trong môi trường
            # self.printStack(env)
            # print(str(env[0][0].mtype[0]))
            res = self.lookupUndeclared(ast.receiver.name, env, lambda x: x.name)
            if res is None:
                raise Undeclared(Identifier(), ast.receiver.name)
            recv_type = res.mtype  # Kiểu của Id (có thể là Id, struct, hoặc interface)
        elif isinstance(ast.receiver, FieldAccess):
            recv_type = self.visitFieldAccess(ast.receiver, c)  # Xử lý FieldAccess
        elif isinstance(ast.receiver, ArrayCell):
            recv_type = self.visitArrayCell(ast.receiver, c)
        else:
            raise TypeMismatch(ast)
        # Kiểm tra xem recv_type có phải là struct hoặc interface không
        if isinstance(recv_type, Id):
            type_symbol = self.lookupUndeclared(recv_type.name, env, lambda x: x.name)
            if type_symbol is None or type_symbol.value not in ['STRUCT', 'INTERFACE']:
                raise TypeMismatch(ast)
            methods = [x for x in type_symbol.mtype if x.value == 'METHOD']
        # elif isinstance(recv_type, list):  # Nếu recv_type là danh sách từ struct/interface
        #     methods = [x for x in recv_type if x.value == 'METHOD']
        else:
            raise TypeMismatch(ast)
        # Tìm method trong danh sách methods
        method_symbol = self.lookupRedeclared(ast.metName, methods, lambda x: x.name)
        if method_symbol is None:
            raise Undeclared(Method(), ast.metName)
        if len(ast.args) != len(method_symbol.mtype.partype):
            raise TypeMismatch(ast)
        if any([type(self.getType(self.visit(x, c))) is not type(method_symbol.mtype.partype[i]) for i, x in enumerate(ast.args)]):
            raise TypeMismatch(ast)
        return method_symbol.mtype.rettype  # Trả về kiểu trả về của method
        

    def visitFieldAccess(self, ast, c):
        env = c[0]
        
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
        # elif isinstance(recv_type, list):  # Nếu recv_type là danh sách fields từ struct
        #     fields = [x for x in recv_type if x.value == 'FIELD']
        else:
            raise TypeMismatch(ast)

        # Tìm field trong danh sách fields
        field_symbol = self.lookupRedeclared(ast.field, fields, lambda x: x.name)
        if field_symbol is None:
            raise Undeclared(Field(), ast.field)
        
        return field_symbol.mtype  # Trả về kiểu của field để dùng ở mức trên
    
    def visitArrayCell(self, ast, c):
        arr_type = self.visit(ast.arr, c)
        idx = [self.visit(x, c) for x in ast.idx]
        if not isinstance(self.getType(arr_type), ArrayType):
            raise TypeMismatch(ast)
        if any([not isinstance(self.getType(x), IntType) for x in idx]):
            raise TypeMismatch(ast)
        return arr_type[0].eleType if isinstance(arr_type, tuple) else arr_type.eleType
    
    def visitIntLiteral(self, ast, c):
        return (IntType(), int(ast.value))

    def visitFloatLiteral(self, ast, c):
        return (FloatType(), float(ast.value))

    def visitStringLiteral(self, ast, c):
        return (StringType(), ast.value)

    def visitBooleanLiteral(self, ast, c):
        return (BoolType(), ast.value)
    
    def visitArrayLiteral(self, ast, c):
        # if len(ast.value) == 0:
        #     return ArrayType(None, [])
        # eleType = self.visit(ast.value[0], c)
        # if any([type(self.visit(x, c)) is not type(eleType) for x in ast.value]):
        #     raise TypeMismatch(ast)
        # return ArrayType(eleType, [])
        pass

    def visitStructLiteral(self, ast, c):
        pass

    def visitAssign(self, ast, c):
        env, isGlobal = c
        if isinstance(ast.lhs, Id):
            print('Id')
            res = self.lookupUndeclared(ast.lhs.name, env, lambda x: x.name)
            if res is None:
                try:
                    rhs = self.visit(ast.rhs, c)
                    type_rhs = self.getType(rhs)
                    val_rhs = self.getValue(rhs)
                    return [env[0] + [Symbol(ast.lhs.name, type_rhs, val_rhs)]] + env[1:]

                except Undeclared as e:
                    if ast.lhs.name == e.n:
                        raise TypeMismatch(ast)
                    raise Undeclared(e.k, e.n)
            
            
        lhs = self.visit(ast.lhs, c)
        rhs = self.visit(ast.rhs, c)
        type_lhs = self.getType(lhs)
        type_rhs = self.getType(rhs)
        print(type_lhs, type_rhs)
        if isinstance(type_lhs, VoidType):
            print('void')
            raise TypeMismatch(ast)
        if not ((type(type_lhs) is type(type_rhs)) or (isinstance(type_lhs, FloatType) and isinstance(type_rhs, IntType))):
            print('ko cung loai')
            raise TypeMismatch(ast)
        if type(type_lhs) is ArrayType and type(type_rhs) is ArrayType:
            print('array')
            if len(type_lhs.dimens) != len(type_rhs.dimens):
                print('khac so phan tu')
                raise TypeMismatch(ast)
            int_check_lhs = all([isinstance(self.getType(self.visit(x, c)), IntType) for x in type_lhs.dimens])
            int_check_rhs = all([isinstance(self.getType(self.visit(x, c)), IntType) for x in type_rhs.dimens])
            if not int_check_lhs or not int_check_rhs:
                print('ko phai int')
                raise TypeMismatch(ast)
            # check value each dimens in array type between lhs and rhs
            dims_lhs = [self.getValue(self.visit(x, c)) for x in type_lhs.dimens]
            dims_rhs = [self.getValue(self.visit(x, c)) for x in type_rhs.dimens]
            print(dims_lhs, dims_rhs)
            if any([x != y for x, y in zip(dims_lhs, dims_rhs)]):
                print('khac phan tu')
                raise TypeMismatch(ast)
            if not ((type(type_lhs.eleType) is type(type_rhs.eleType)) or (isinstance(type_lhs.eleType, FloatType) and isinstance(type_rhs.eleType, IntType))):
                raise TypeMismatch(ast)
        # if isinstance(type_lhs, InterfaceType) and isinstance(type_rhs, StructType):
        return env
    
    def visitId(self,ast,c):
        env = c[0]
        res = self.lookupUndeclared(ast.name, env, lambda x: x.name) # ast.name in x
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        return (res.mtype, res.value) # !!!!!!!
    
    def visitIf(self,ast,c):
        env, isGlobal = c
        expr_typ = self.visit(ast.expr, c)
        if not isinstance(self.getType(expr_typ), BoolType):
            raise TypeMismatch(ast)
        
        self.visit(ast.thenStmt, c)
        if ast.elseStmt:
            self.visit(ast.elseStmt, c)

        return env

    def visitForBasic(self,ast,c):
        env = c[0]
        cond_typ = self.visit(ast.cond, c)
        if not isinstance(cond_typ, BoolType):
            raise TypeMismatch(ast)
        
        self.visit(ast.loop, c)

        return env
    
    def visitForStep(self,ast,c):
        env, isGlobal = c
        local_env = deepcopy(env)
        local_env = self.visit(ast.init, ([[]] + local_env, isGlobal))
        cond_typ = self.visit(ast.cond, (local_env, isGlobal))
        if not isinstance(cond_typ, BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.upda, (local_env, isGlobal))
        self.visit(ast.loop, (local_env, isGlobal))
        return env
    
    def visitForEach(self,ast,c):
        env, isGlobal = c
        local_env = deepcopy(env)
        local_env = [[]] + local_env
        if ast.idx.name != '_':
            local_env = [local_env[0] + [Symbol(ast.idx.name, IntType())]] + local_env[1:]
        res = self.lookupRedeclared(ast.value.name, local_env[0], lambda x: x.name)
        if res: 
            raise Redeclared(Variable(), ast.value.name)
        
        arr_typ = self.visit(ast.arr, c)
        if not isinstance(arr_typ, ArrayType):
            raise TypeMismatch(ast)
        
        local_env = [local_env[0] + [Symbol(ast.value.name, arr_typ.eleType)]] + local_env[1:]
        self.visit(ast.loop, (local_env, isGlobal))
        return env

    def visitBreak(self,ast,c):
        pass

    def visitContinue(self,ast,c):
        pass

    def visitReturn(self,ast,c):
        env = c[0]
        typ_expr = VoidType() if ast.expr is None else self.visit(ast.expr, c)
        res = self.lookupUndeclared('FUNCTION', env, lambda x: x.value)
        if res:
            if not type(res.mtype.rettype) is type(self.getType(typ_expr)):
                raise TypeMismatch(ast)
            
    # def visitBinaryOp(self, ast, c):
    #     # + Addition int/float/string
    #     # - Subtraction int/float 
    #     # * Multiplication int/float 
    #     # / Division int/float
    #     # % Modulus int
    #     # == Equal int/float/string 
    #     # != Not equal int/float/string 
    #     # < Less than int/float/string 
    #     # > Greater than int/float/string 
    #     # <= Less than or equal int/float/string 
    #     # >= Greater than or equal int/float/string
    #     # ! Negation boolean 
    #     # && Conjunction (AND) boolean 
    #     # || Disjunction (OR) boolean
    #     left = self.visit(ast.left, c)
    #     right = self.visit(ast.right, c)

    #     is_literal = isinstance(ast.left, (IntLiteral, FloatLiteral)) and isinstance(ast.right, (IntLiteral, FloatLiteral))
    #     if ast.op == '+':
    #         if not (isinstance(left, (IntType, FloatType, StringType)) and isinstance(right, (IntType, FloatType, StringType))):
    #             raise TypeMismatch(ast)
    #         if type(left) is StringType and type(right) is StringType:
    #             return StringType()
    #         if isinstance(left, (IntType, FloatType)) and isinstance(right, (IntType, FloatType)):
    #             result_type = FloatType() if isinstance(left, FloatType) or isinstance(right, FloatType) else IntType()
    #             if is_literal:
    #                 left_val = float(ast.left.value) if isinstance(left, FloatType) else int(ast.left.value)
    #                 right_val = float(ast.right.value) if isinstance(right, FloatType) else int(ast.right.value)
    #                 return FloatLiteral(left_val + right_val) if type(result_type) is FloatType else IntLiteral(left_val + right_val)
    #             return result_type
    #     if ast.op in ['-', '*', '/']:
    #         if not isinstance(left, (IntType, FloatType)) or not isinstance(right, (IntType, FloatType)):
    #             raise TypeMismatch(ast)
    #         result_type = FloatType() if type(left) is FloatType or type(right) is FloatType else IntType()
    #         if is_literal:
    #             left_val = float(ast.left.value) if isinstance(left, FloatType) else int(ast.left.value)
    #             right_val = float(ast.right.value) if isinstance(right, FloatType) else int(ast.right.value)
    #             if ast.op == '-':
    #                 result = left_val - right_val
    #             elif ast.op == '*':
    #                 result = left_val * right_val
    #             elif ast.op == '/':
    #                 result = left_val / right_val
    #             return FloatLiteral(result) if result_type is FloatType else IntLiteral(result)
    #         return result_type
    #     if ast.op == '%':
    #         if not isinstance(left, IntType) or not isinstance(right, IntType):
    #             raise TypeMismatch(ast)
    #         if is_literal:
    #             return IntLiteral(int(ast.left.value) % int(ast.right.value))
    #         return IntType()
    #     if ast.op in ['==', '!=', '<', '>', '<=', '>=']:
    #         if not (isinstance(left, (IntType, FloatType, StringType)) and isinstance(right, (IntType, FloatType, StringType))):
    #             raise TypeMismatch(ast)
    #         if not type(left) is type(right):
    #             raise TypeMismatch(ast)
    #         return BoolType()
    #     if ast.op in ['&&', '||']:
    #         if not isinstance(left, BoolType) or not isinstance(right, BoolType):
    #             raise TypeMismatch(ast)
    #         return BoolType()
    #     raise TypeMismatch(ast)
    
    def visitBinaryOp(self, ast, c):
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
                    # print('compute')
                    left_val = float(left_value) if isinstance(left_type, FloatType) else left_value
                    right_val = float(right_value) if isinstance(right_type, FloatType) else right_value
                    result = left_val + right_val
                    # print(result)
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
                    result = left_val / right_val
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

    # def visitUnaryOp(self, ast, c):
    #     # - Negation int/float 
    #     # ! Negation boolean
    #     body = self.visit(ast.body, c)
    #     is_literal = isinstance(ast.body, (IntLiteral, FloatLiteral))
    #     if ast.op == '-':
    #         if not isinstance(body, (IntType, FloatType)):
    #             raise TypeMismatch(ast)
    #         result_type = FloatType() if type(body) is FloatType else IntType()
    #         if is_literal:
    #             value = float(ast.body.value) if isinstance(body, FloatType) else ast.body.value
    #             return FloatLiteral(-float(value)) if result_type is FloatType else IntLiteral(-int(value))
    #         return 
    #     if ast.op == '!':
    #         if not isinstance(body, BoolType):
    #             raise TypeMismatch(ast)
    #         return BoolType()
    #     raise TypeMismatch(ast)

    def visitUnaryOp(self, ast, c):
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
                return (FloatLiteral(result) if isinstance(result_type, FloatType) else IntLiteral(int(result)), result)
            return result_type

        if ast.op == '!':
            if not isinstance(body_type, BoolType):
                raise TypeMismatch(ast)
            return BoolType()

        raise TypeMismatch(ast)