#Fibonacci
class Fib:
    def __init__(self, limit):
        self.values = []
        self.limit = limit

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.limit:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib	

for f in Fib(100):
    print(f)

	
# Geometric Progression
class GP:
    def __init__(self, ratio, limit):
        self.value = 1
        self.ratio = ratio
        self.limit = limit
        print(self.value)

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.value > self.limit:
            raise StopIteration
        self.value *= self.ratio
        return 
    
for i in GP(3,200):
    print(i)
	
#Countdown
class Countdown:
    def __init__(self, start):
        self.value = start
        print(self.value)
    
    def __iter__(self):
        return(self)
    
    def __next__(self):
        if self.value <= 0:
            raise StopIteration
        self.value -= 1
        return self.value
    
for i in Countdown(200):
    print(i)
	
# Reversed Countdown
class Countdown:
    def __init__(self, start):
        self.value = start
        self.value_rev = 0
    
    def __iter__(self):
        return(self)
    
    def __next__(self):
        if self.value == 0:
            raise StopIteration
        self.value -= 1
        return self.value
    
    def __reversed__(self):
        while self.value_rev <= self.value:
            yield self.value_rev
            self.value_rev += 1

CD_rev = reversed(Countdown(200))
for i in CD_rev:
    print(i)