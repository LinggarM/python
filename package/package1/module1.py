from abc import ABC, abstractmethod 

def func1():
	print("This is func1")

class Animal(ABC):
	@abstractmethod
	def sound():
		pass

	@abstractmethod
	def habitat():
		pass

class Cat(Animal):
	def sound(self):
		print("Miaw")

	def habitat(self):
		print("Darat")