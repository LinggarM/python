from bigO import BigO

def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1

def my_generator_for(n):

    for i in range (n):
        yield i

for value in my_generator(3):

    # print each value produced by generator
    print(value)

for value in my_generator_for(3):

    # print each value produced by generator
    print(value)

lib = BigO()
complexity = lib.test_all(my_generator)
complexity = lib.test_all(my_generator_for)