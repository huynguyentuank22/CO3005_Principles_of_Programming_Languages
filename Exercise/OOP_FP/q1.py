from abc import ABC

class Exp(ABC):
    def eval(self):
        return

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

class IntLit(Exp):
    def __init__(self, value: int):
        self.value = value
    
    def eval(self):
        return self.value

class FloatLit(Exp):
    def __init__(self, value: float):
        self.value = value
    
    def eval(self):
        return self.value

x6 = Exp()
print(x6.eval())  
