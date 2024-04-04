#lambda function is written in 1 line using lambda keyword
#accepts any no.of arguments but only has one expression.
# useful if needed for short period of time, its a shortcut.

multiply = lambda x : x * x

print(multiply(5))

add = lambda x, y : x +y

print(add(5, 6))

age_check = lambda age: True if age >= 18 else False

print(age_check(18))
