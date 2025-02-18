from abc import ABC, abstractmethod

class Exp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class BinExp(Exp):
    def __init__(self, left: Exp, op: str, right: Exp):
        self.left = left
        self.op = op
        self.right = right

    def accept(self, visitor):
        return visitor.visitBinExp(self)

class UnExp(Exp):
    def __init__(self, op: str, operand: Exp):
        self.op = op
        self.operand = operand

    def accept(self, visitor):
        return visitor.visitUnExp(self)

class IntLit(Exp):
    def __init__(self, value: int):
        self.value = value
    
    def accept(self, visitor):
        return visitor.visitIntLit(self)
    
class FloatLit(Exp):
    def __init__(self, value: float):
        self.value = value

    def accept(self, visitor):
        return visitor.visitFloatLit(self)
    
class Visitor(ABC):
    @abstractmethod
    def visitBinExp(self, binExp: BinExp):
        pass

    @abstractmethod
    def visitUnExp(self, unExp: UnExp):
        pass

    @abstractmethod
    def visitIntLit(self, intLit: IntLit):
        pass

    @abstractmethod
    def visitFloatLit(self, floatLit: FloatLit):
        pass

class Eval(Visitor):
    def visitBinExp(self, binExp: BinExp):
        left_val = binExp.left.accept(self)
        right_val = binExp.right.accept(self)
        
        if binExp.op == '+':
            return left_val + right_val
        elif binExp.op == '-':
            return left_val - right_val
        elif binExp.op == '*':
            return left_val * right_val
        elif binExp.op == '/':
            return left_val / right_val
        else:
            raise ValueError("Unsupported operator")

    def visitUnExp(self, unExp: UnExp):
        operand_val = unExp.operand.accept(self)
        
        if unExp.op == '+':
            return +operand_val
        elif unExp.op == '-':
            return -operand_val
        else:
            raise ValueError("Unsupported unary operator")

    def visitIntLit(self, intLit: IntLit):
        return intLit.value

    def visitFloatLit(self, floatLit: FloatLit):
        return floatLit.value
    
class PrintPrefix(Visitor):
    def visitBinExp(self, binExp: BinExp):
        return binExp.op + " " + binExp.left.accept(self) + " " + binExp.right.accept(self)

    def visitUnExp(self, unExp: UnExp):
        return unExp.op + ". " + unExp.operand.accept(self)

    def visitIntLit(self, intLit: IntLit):
        return str(intLit.value)

    def visitFloatLit(self, floatLit: FloatLit):
        return str(floatLit.value)
    
class PrintPostfix(Visitor):
    def visitBinExp(self, binExp: BinExp):
        return binExp.left.accept(self) + " " + binExp.right.accept(self) + " " + binExp.op

    def visitUnExp(self, unExp: UnExp):
        return unExp.operand.accept(self) + " " + unExp.op + "."

    def visitIntLit(self, intLit: IntLit):
        return str(intLit.value)

    def visitFloatLit(self, floatLit: FloatLit):
        return str(floatLit.value)

x6 = BinExp(UnExp('-', IntLit(4)), '+', BinExp(IntLit(3), '*', IntLit(2))) # x6 = -4 + 3 * 2
print(x6.accept(PrintPrefix())) # Expected output: + - 4 * 3 2
