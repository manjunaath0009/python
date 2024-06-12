# list is ordered, changeable and duplicates are allowed
a = list(('a', 'b','c'))
b = list(('a', 'b','c'))
mytuple = ('a', 'b', 'c')
print(mytuple)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
x = ("apple", "banana", "cherry")
print(x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
fruits = ("apple", "banana", "cherry")

(a, b, c) = fruits

print(a)
print(b)
print(c)
print(set(a+b+c))