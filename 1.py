A = 24 * 5
print(A)
B = "Hello Manjunaath"
print(B)
B.split();
# 31 May 2024 (List and Tuples)
# prompt: create list with 5 elements and print it

# Create a list with 5 elements and print the list
my_list = [1, 2, 3, 4, 5]
print(my_list)

newList = [10, 20, 30, 10, 40, 50, 20]
print(newList)
newList.sort();
print(newList)
newList.reverse();
print(newList);

import sys

print(sys.version)

if 5 > 2:
  print("Five is greater than two!")
  
if 5 > 2:print("Five is greater than two!") 
if 5 > 2:print("Five is greater than two!") 
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
h="msg"
ttt = h.capitalize();
print(ttt)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y.capitalize())
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

sent = "I am good"
sent1 = sent.split();

str1 = "Welcome\nto\nTutorialspoint"

print("The given string is")
print(str1)

print("The resultant string split at newline is")
print(str1.splitlines())

splitWords = "I am good boy";
print(splitWords.replace(" ", "\n"));
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# Global variables
x = "awesome"

def myfunc():
  print("Hello")
  print("Python is " + x)

myfunc()

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = set(("apple", "banana", "cherry"))
print(x)
x = frozenset(("apple", "banana", "cherry"))
print(x)

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)
print(a)

import random

print(random.randrange(1, 10))
a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)
  
  txt = "The best things in life are free!"
print("free" in txt)

b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

age = 36
txt = f"My name is John, I am {age}"
print(txt)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
  x = 200
print(isinstance(x, int))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

list1 = ["abc", 34, True, 40, "male"]
list2 = [1,3,2]
print(len(list1));
print(list2.sort())
list2.insert(2, 10);
print(list2)
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x, end=" ")
  
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x.endswith("a"))

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 2
  
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

print("************\n")

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

def myfunc(n):
  return abs(n)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.upper)
print(thislist)

thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
  print("\n")

thistuple = ("apple", "banana", "cherry")
i = 1
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

