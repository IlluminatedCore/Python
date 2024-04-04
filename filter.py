#filter creates a collection of elements from a list which are iterable for which 
#a funciton returns true.
#filter(function, items)


friends = [
    ("Rachel", 18),
    ("Monica", 20),
    ("Phoebe", 16),
    ("Joey", 14),
    ("Chandler", 20)
]

age = lambda data: data[1] >= 18

above = filter(age, friends)

for i in above:
    print(i[0], end=" ")