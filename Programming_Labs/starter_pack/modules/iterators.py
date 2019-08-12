#Fibonacci
class fib:
    def __init__(self, limit):
        self.values = []
        self.limit = limit
        self.step = 0

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if self.step > self.limit - 1:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.step += 1
        return fib	

	
# Geometric Progression
class GP:
    """class for generating geometric progression
    At initializing demands length of sequence and ratio between two near placed numbers
    The progression starts with 1"""
    def __init__(self, length, ratio):
        self.value = 1
        self.ratio = ratio
        self.length = length
        self.passed = 0

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.passed >= self.length:
            raise StopIteration
        elif self.passed == 0:
            self.passed +=1 
            return 1

        self.value *= self.ratio
        self.passed += 1
        return self.value


#Countdown
class countdown:
    def __init__(self, start):
        self.value = start
        self.value_rev = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value <= 0:
            raise StopIteration
        self.value -= 1
        return self.value + 1

    # Reversed countdown
    def __reversed__(self):
        while self.value_rev < self.value:
            yield self.value_rev
            self.value_rev += 1 


if __name__ == "__main__":
    print("iterators.py ran")