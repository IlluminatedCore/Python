#scope = The region that a variable is recognized.
#That variable is only avaialble from inside the region it is created.
#Global and local scoped versions of a variable can be created.

name = "Bro" #global, these are available inside and outside of a func

def username():
    #name = "manideep" #local variable
    #global name
    print(f"Hello {name}")
username()

#print(name)

