a = int(input(''))
b = int(input(''))
def s(a, b):
    return a + b
def v(a, b):
    return a - b
def u(a, b):
    return a * b
def d(a, b):
    if b == 0:
        return 'er1: деление на ноль'
    return a / b
print(s(a, b))
print(v(a, b))
print(u(a, b))
print(d(a, b))
