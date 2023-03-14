dummy_list = [1, 3, 5, 7]
def func(a):
	return a * a

# Traditional declaration
out = list()
for i in dummy_list:
	now = func(i)
	out.append(now)

# Using map()
out_2 = list(map(func, dummy_list))

print("Using traditional declaration: ", out)
print("Using map(): ", out_2)