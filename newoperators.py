Age = int(input("What is your age?\n"))

if Age == 18:
    print("Congrats, you are adult!")
elif Age < 18:
    print("You are still a teen")
elif Age > 18:
    print("You are a man!")
elif Age == 0:
    print("You are not born yet!")
else:
    print("You are a child")
