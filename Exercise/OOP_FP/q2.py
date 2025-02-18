from abc import ABC

class Exp(ABC):
    def eval(self):
        pass

    def printPrefix(self):
        pass

class BinExp(Exp):
    def __init__(self, left: Exp, op: str, right: Exp):
        self.left = left
        self.op = op
        self.right = right
    
    def eval(self):
        left_val = self.left.eval()
        right_val = self.right.eval()
        
        if self.op == '+':
            return left_val + right_val
        elif self.op == '-':
            return left_val - right_val
        elif self.op == '*':
            return left_val * right_val
        elif self.op == '/':
            return left_val / right_val
        else:
            raise ValueError("Unsupported operator")
        
    def printPrefix(self):
        return self.op + " " + self.left.printPrefix() + " " + self.right.printPrefix()

class UnExp(Exp):
    def __init__(self, op: str, operand: Exp):
        self.op = op
        self.operand = operand
    
    def eval(self):
        operand_val = self.operand.eval()
        
        if self.op == '+':
            return +operand_val
        elif self.op == '-':
            return -operand_val
        else:
            raise ValueError("Unsupported unary operator")
        
    def printPrefix(self):
        return self.op + ". " + self.operand.printPrefix()

class IntLit(Exp):
    def __init__(self, value: int):
        self.value = value
    
    def eval(self):
        return self.value
    
    def printPrefix(self):
        return str(self.value)
    
class FloatLit(Exp):
    def __init__(self, value: float):
        self.value = value
    
    def eval(self):
        return self.value
    
    def printPrefix(self):
        return str(self.value)
    
x6 = BinExp(UnExp('-', IntLit(4)), '+', BinExp(IntLit(3), '*', IntLit(2))) # x6 = -4 + 3 * 2
print(x6.printPrefix()) # Expected output: + - 4 * 3 2
