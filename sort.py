list = ["Squidword", "Spongebob", "Patrick", "Sandy", "Dave"]

list.sort()

#print(list) or

for i in list:
    print(i)
####################
#.sort() works for list, and fails if its a tuple, so 
#we use sorted function.
    
print(" ")
    
newlist = ("Squidword", "Spongebob", "Patrick", "Sandy", "Dave")

x = sorted(newlist)

for i in x:
    print(i)
print(" ")
########################################
Students = [
    ("Squidword", "F", 60),
    ("Spongebob", "A", 16),
    ("Patrick", "B", 12),
     ("Sandy", "C", 25),
     ("Dave", "B", 20)]

grades = lambda grade : grade[1]
Students.sort(key=grades)


for i in Students:
    print(i)

###
# To arrange in reverse order
print(" ")
Students.sort(key=grades, reverse=True)
for i in Students:
    print(i)


### if the given state is in a tuple
print(" ")

Students = (
    ("Squidword", "F", 60),
    ("Spongebob", "A", 16),
    ("Patrick", "B", 12),
     ("Sandy", "C", 25),
     ("Dave", "B", 20))

ages = lambda age : age[2]

sorted_students = sorted(Students,key=ages)

for i in sorted_students:
    print(i)