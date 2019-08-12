import numpy as np

# sort
a = np.random.randint(-20,20,10,int)
print("Before: {0}".format(a))
a.sort()
print("After: {0}\n".format(a))

# mean
b = np.random.randint(-20,20,20,int)
print("{0}\nMean: {1:.3f}\n".format(b,np.mean(b)))

# array 2x2x2
c = np.random.rand(2,2,2)
print("{0}\n".format(c))

# 4x4 matrix
d = np.random.randint(0,9,(4,4),int)
print("{0}\n".format(d))

# arrays intersection
e = np.intersect1d(a,b)
print("Intersection of a and b arrays: {0}\n".format(e))

# find nearest
def nearest(arr, value):
	print("Trying to find {0}...".format(value))
	return (np.abs(arr - value)).argmin()

f = np.random.randint(0,100,5)
print(f)
print("The nearest value is {0}".format(f[nearest(f,10)]))