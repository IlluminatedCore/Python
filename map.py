# map applies a function to each item in an  iterable list, tuple etc

store = [
    ("shirt", 20),
    ("Pant", 30),
    ("Socks", 5),
    ("Jacket", 50)
]

to_dollars = lambda value : (value[0], round(value[1]/.82))
dollar_store = map(to_dollars, store)

for i in dollar_store:
    print(i)