#The following program emphasizes the dynamic type system of Python.

#In a dynamically typed language, a variable is simply a value bound to a name.

#The value of what is being referenced by the variable has a type like int or float or str, but the variable itself has no type.

#!/usr/bin/env python3
x = 10
tab = " \t"

print(x, tab, type(x), tab, id(x))
y = x
print(y, tab, type(y), tab, id(y))
x = 25.7
print(x, tab, type(x), tab, id(x))
x = "Hello"
print(x, tab, type(x), tab, id(x))
