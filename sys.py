import sys

if len(sys.argv) < 3:
    print("Usage: python script.py <first_name> <last_name>")
    sys.exit(1)

first_name = sys.argv[1]
last_name = sys.argv[2]
city_name = sys.argv[3]
hero_name = sys.argv[4]

print("First name:", first_name)
print("Last name:", last_name)
print("City name:", city_name)
print("fav hero:", hero_name)

