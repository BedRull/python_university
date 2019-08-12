def getValueName(class_type, value):
	"""helper function for ShowAccess descriptor"""
	return [k for k,v in class_type.__dict__.items() if v is value][0]

class ShowAccess(object):
	"""It's a descriptor"""
	def __init__(self,  value = 0):
		self.value = value
	def __get__(self, instance, owner):
		value_name = getValueName(owner, self)
		print(f"Receiving {value_name}...")
		return self.value
	def __set__(self, instance, value):
		value_name = getValueName(instance.__class__, self)
		print(f"Setting {value_name}...")
		self.value = value
	def __delete__(self, instance):
		value_name = getValueName(instance.__class__, self)
		print(f"Deleting {value_name}...")
		del self.value

class Temperature():
	celcius = ShowAccess()
	fahrenheit = ShowAccess()

