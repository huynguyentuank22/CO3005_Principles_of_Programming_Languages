def powGen(x):
    def inner(y):
        return y ** x
    return inner

square = powGen(2)
print(square(4))