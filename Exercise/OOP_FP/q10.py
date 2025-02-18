from functools import reduce

def compose(*args):
    if len(args) < 2:
        raise TypeError()
    return lambda x:reduce(lambda v, f: f(v), reversed(args), x)

def increase(x):
    return x + 1

def square(x):
    return x ** 2

f = compose(increase,square)
print(f(3)) #increase(square(3)) = 10