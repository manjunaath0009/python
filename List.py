# list is ordered, changeable and duplicates are allowed
a = list(('a', 'b','c'))
b = list(('a', 'b','c'))
print(a)
print(a[1])
print(a[-1])
print(a[1:3])
print(a[:3])
print(a[1:])
a[1]="d"
print(a)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
thislist.remove("apple")
print(thislist)
thislist.append("Hello")
thislist.insert(3, "Hello")
print(thislist)
a.extend(b)
print(a)
thislist = ["apple", "banana", "cherry"]
del thislist
thislist = ["apple", "banana", "cherry"]
del thislist[1]
print("del thislist[1]", thislist)
thislist=["Sai", "Sai Samarth", "Sohan", "Sai"]
for x in thislist:
    if(len(x) == 3):
        print(x)

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
#50, 0, 15, 32, 27
thislist.sort(key = myfunc)
print(thislist)

def myfunc(n):
  return abs(n)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
print(list(list1 + list2))
print(list1 + list2)
print(list2, list1)
for x in list2:
  list1.append(x)

print(list1)