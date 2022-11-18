# reduce is available in functools
from functools import reduce

lst = [2, 4, 3, 2, 3, 5, 6, 45, 33, 67, 56]

evens = list(filter(lambda n : n%2==0, lst))
print(evens)

double = list(map(lambda n : n*2, evens))
print(double)

sum = reduce(lambda a, b:a+b, double)
print(sum)


