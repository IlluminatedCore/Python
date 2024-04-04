#creating a sub from main statement

#indexing
full_name = "Kedar Goud"

first_name = full_name[0:5]

last_name = full_name[6:10]

print(first_name)
print(last_name)
print(" ")

first_name = full_name[:5]
last_name = full_name[6:]

print(first_name)
print(last_name)

middle = full_name[2:7]

print(middle)

reversed = full_name[::-1]

print(reversed)

#slicing

website1 = "https://Google.com"
website2 = "https://Github.com"

slice = slice(8,-4)

print(website1[slice])
print(website2[slice])