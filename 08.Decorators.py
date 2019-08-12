import functools
from time import sleep, time
from contextlib import ContextDecorator

class timeit(ContextDecorator):
	"""docstring"""
	def __enter__(self):
		self.start = time()
		return self		

	def __exit__(self, *exc):
		self.end = time()
		time_elapsed = self.end - self.start
		print(f"Ending for {time_elapsed:.6f} seconds")

# @timeit()
# def proceedFunc():
# 	sleep(1)

# with timeit():
# 	sleep(1)


def decTime(func = None,  min_seconds = 0):
	def inner_wrap(func):
		@functools.wraps(func)
		def wrapper(*args, debug = False, **kwargs):
				startTime = time()
				res = func(*args,**kwargs)
				endTime = time()
				runTime = endTime - startTime
				if debug:
					if runTime < min_seconds:
						print("runTime is less than min_seconds")
					else: 
						print(f"It took {runTime:.4f} seconds to")
				return res
		return wrapper
	if func is None:
		return inner_wrap
	else:
		return inner_wrap(func)

@decTime()
def proceedFunc(seconds):
	"""Function that need some time..."""
	sleep(seconds)
	return seconds

help(proceedFunc)
print(proceedFunc(seconds=2, debug=True))
