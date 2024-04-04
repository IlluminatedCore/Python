#They are the arguments preceded by an identifier when we pass them to 
# a function, the order of the arguments doesnt matter unlike
#positional arguments


def username(first, middle, last):
    print("Hello {} {} {}".format(first, middle, last))


username(middle='Ramesh', first='Sachin', last='Tendulkar')
