# -*- coding: utf-8 -*-
def mult2(x, y):
    print('{0} is multiplied by {1}'.format(x, y))
    return x * y

print(mult2(2, 7))

a = 12
print(mult2(a, 6))

b = 11
print(mult2(a, b))



print("\n------ foo -------\n")
def foo(x):
	x[2] = 99  # Modifies a because it's a mutable type!

a = [1, 2, 3, 4]

foo(a)

print(a[2])

print(a)

print("\n------ foo 2 -------\n")

def foo2(x):   # x = a
	print(x)  # hello
	x = x.upper()   # Reassigns x, but doesn't modify a--strings are immutable!
	print(x)  # HELLO

a = "hello"

foo2(a)

print(a)  # hello


print("\n------ centered_average -------\n")

# Return the "centered" average of an array of positive or negative ints, which
# we'll say is the mean average of the values, except ignoring the largest and
# smallest values in the array. The array can be out of order. The array will
# have at least 3 numbers. Use integer division to compute the average.
## centered_average([1, 2, 3, 4, 100]) → 3
## centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
## centered_average([1, 2, 3, 4]) -> (2+3)/2 = 5/2 = 2
## centered_average([1, 1, 1]) -> 1

import math

def centered_average(a):
	a.sort()

	middle = a[1:-1]

	total = 0
	for v in middle:
		total += v

	return total // len(middle)

def centered_average2(a):
	a.remove(max(a))
	a.remove(min(a))

	total = 0
	for v in a:
		total += v

	return total // len(a)

def centered_average3(a):
	total = 0
	for v in a:
		total += v

	total -= min(a)
	total -= max(a)

	return total // (len(a) - 2)

def centered_average4(a):
	total = 0
    # mx = -math.inf
	# mn = math.inf
	mx = -324231432142341241243243242342342423
	mn = 345989489879878977979897888686

	for v in a:
		if v < mn:
			mn = v

		if v > mx:
			mx = v

		total += v

	total -= mn
	total -= mx

	return total // (len(a) - 2)

print(centered_average4([1, 1, 5, 5, 10, 8, 7]))
#print(centered_average([1, 1, 2, 3, 3]))