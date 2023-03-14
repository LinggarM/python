import numpy as np

# Example 1
def create_generator():
    mylist = np.arange(3,6,1)
    for i in mylist:
        yield i*i

mygenerator = create_generator() # create a generator
print(mygenerator) # mygenerator is an object!
for i in mygenerator:
	print(i)

# Example 2
def grepper_gen():
  yield "add"
  yield "grepper"
  yield "answer"

grepper = grepper_gen()
print(type(grepper))
print(next(grepper))
print(next(grepper))
print(next(grepper))