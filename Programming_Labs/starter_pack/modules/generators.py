# Fibonacci
def fib():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

# Geometric Progression
def GeomProg(ratio):
    result = 1
    while True:
        yield result
        result *= ratio

# CountDown
def countdown(n):
    current = n
    while current:
        yield current
        current -= 1
