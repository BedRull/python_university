# import random
# import itertools

# from itertools import chain

# Cubes mapping
# first_dict = {x: x**3 for x in range(100)}
# print("1st:", first_dict, '\n')

# Combining two lists
# a = random.sample(range(20),5)
# b = random.sample(range(20,40),5)
# print("2nd:\na:", a, '\nb:', b)
# combine_dict = {k: v for k,v in zip(a,b)}
# print(combine_dict, '\n')

# dict merging
d1, d2 = dict(k1=[2, 3], k2=[4]), dict(k2=[5], k3=[6, 7])
dicts = list(d1.keys())
for k in d2.keys():
	dicts.append(k)

d3 = { for i in d1}

# for d in dicts:
	# for k,v in d.items():
		# for i in v:
			# d3[k].append(v)
print(d3)
# z = {k: v for k,v in d1 for k,v in d2}
# print(z)

# d3 = {k: v for k, v in chain(d1.items(), d2.items())}

