# Descending digit sequence
print("***Descending digit sequence***")
import random
random_values = random.sample(range(1000), 20)
print("List before:", random_values)
random_values.sort(reverse = True)
print("List after:", random_values, '\n')


# Sort strings. Case sensitive
print("***Sort strings case sensitive***")
words_list = list(("one", "two", "Three", "four", "Five", "six", "Seven", "eight", "nine", "ten", "Eleven", "Twelve", "thirteen"))
print("List before:", words_list)
words_list.sort()
print("List after:", words_list, '\n')


# Sort strings by last letter
print("***Order by last letter***")
words_list = list(("One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen"))
print("List before:", words_list)
words_list.sort(key=lambda x: str(x[-1]))
print("List after:", words_list, '\n')


# Sort strings by length
print("***Sort strings by length***")
words_list = list(("One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen"))
print("List before:", words_list)
words_list.sort(key = len)
print("List after:", words_list)