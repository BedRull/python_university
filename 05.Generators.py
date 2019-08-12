# fibonacci
def fib():
    a = 0
    b = 1
    while True:
        yield a
        a,b = b, a + b

g = fib()
for i in range(10):
    print(next(g))

# Geometric Progression
def GeomProg(Start, Ratio):
    Result = Start
    while True:
        yield Result
        Result *= Ratio

g = GeomProg(200,5)
for i in range(10):
    print(next(g))
	
#CountDown
def countdown(n):
    Current = n
    while Current:
        yield Current
        Current -= 1

genCountDown = countdown(200)
print(*genCountDown, sep='\n')