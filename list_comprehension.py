# its a way to create a new list with less lines of code
# can mimic certain lambda functions, easier to read.
#list = [expression for item in iterable]
#list = [expression for item in iterable if conditional]
#list = [expression if/else for item in iterable]


numbers = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

#passed = list(filter(lambda i: i >= 60 , numbers)) or

#passed = [i for i in numbers if i  >= 60] or

passed = [i if i >= 60 else "Failed" for i in numbers]

print(passed)