class Class1():
	def info(self):
		print("This is Class 1")

class Class2(Class1):
	pass

class Class3(Class1):
	def info(self):
		print("This is Class 3")

class Class4(Class2, Class3):
	pass

obj = Class4()
obj.info()