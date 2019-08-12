import random

# Squares
print("1st:", [x**2 for x in range(100)], '\n')

# Divided by 3
print("2nd:", [x for x in range(100) if  x%3 == 0 and x], '\n')

# Only Positive
random_values = random.sample(range(-50, 50), 20)
print("3rd:", random_values)
only_positive = [x for x in random_values if x>0]
print("    ", only_positive, '\n')

# Last Letters
sentence = "Given a sentence, produce a list of last letters of every word"
print("4th:", sentence.split())
last_letters = [x[-1] for x in sentence.split()]
print("    ", last_letters, '\n')

# Pairs
a = ['a1', 'a2']
b = ['b1', 'b2', 'b3']
pairs = [(x,y) for x in a for y in b]
print("5th:", pairs, '\n')

# List of lists
lists = [random.sample(range(1,7),1) for i in range(5)]
print("6th:", lists)