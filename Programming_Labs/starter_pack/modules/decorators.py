import functools
from time import time
from contextlib import ContextDecorator


def decTime(func = None,  min_seconds = 0):
	"""Decorator that will measure function proceeeding time"""
	def inner_wrap(func):
		@functools.wraps(func)
		def wrapper(debug = False):
				startTime = time()
				func()
				endTime = time()
				runTime = endTime - startTime
				if debug:
					if runTime < min_seconds:
						print("RunTime is less than min_seconds")
					else: 
						print(f"{runTime:.4f} seconds elapsed")
		return wrapper
	if func is None:
		return inner_wrap
	else:
		return inner_wrap(func)


class timeit(ContextDecorator):
	"""Both context manager and decorator"""
	def __enter__(self):
		self.start = time()
		return self		

	def __exit__(self, *exc):
		self.end = time()
		time_elapsed = self.end - self.start
		print(f"Ending for {time_elapsed:.6f} seconds")
		return False

