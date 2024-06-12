# print("Print all the factors of a given number");
# print("---------------------------------------");

# num = int(input("Enter a number : "));

# factorial = 1;

# if num < 0: print("Please enter positive number")
# elif num == 0: print("Factorial of zero is 1")
# else: 
#     for i in range(1, num+1): factorial = factorial * i 
#     print("The factorial of a given number is : ", num, " = ", factorial)

# print("*******************************************");
# print("\n")
# print("Print if the two given strings are equal or unequal");
# print("---------------------------------------------------");
# str1 = str(input("Enter a first string : "));
# str2 = str(input("Enter a second string : "));
# if(str1 == str2) : print("Strings are equal") 
# else: print("Strings are not equal")
# if(str1.casefold() == str2.casefold()) : print("Strings are equal") 
# else: print("Strings are not equal")

# print("*******************************************");
# print("\n")
# print("Print the frequency of the given character in the given string");
# print("---------------------------------------------------");
# str1 = str(input("Enter a string : "));
# d = {}
# for i in str1:
#     if i in d : d[i] += 1 
#     else: d[i]=1
# print(d)

# print("*******************************************");
# print("\n")
# print("Print the number of vowels in a given string.");
# print("---------------------------------------------------");
# str1 = str(input("Enter a string : "));
# # .fromkeys(x, y) : its a key and value pair
# d = {}.fromkeys('aeiou', 0)
# for i in str1.casefold():
#     if i in 'aeiou': d[i] += 1 
# print(d)

# print("*******************************************");
# print("\n")
# print("Print all the numbers divisible by a given number in the range");
# print("---------------------------------------------------");
# a=int(input("Enter lower no.:"))
# b=int(input("Enter upper no.:"))
# num=int(input("Enter the no. to be divided by:"))
# for i in range(a,b+1):
#     if(i%num==0):
#         print(i, end=" ");

# print("*******************************************");
# print("\n")
# print("Print “Welcome” if your name is present in the list and “See you next time” if names is not present");
# print("---------------------------------------------------");
# newnames=["a", "B", "c"]
# name=input("Enter a name : ")
# if name.casefold() in newnames: print("Welcome")
# else: print("See you next time");

# print("*******************************************");
# print("\n")
# print("Find the factorial of a number with recursion");
# print("-------------------------------------------------------------------");
# def fact(n):
#  if int(n)>1: return int(n)*fact(int(n)-1)
#  else: return 1;

# factorial=input("Enter a number : ")
# print("Factorial of a number is ", fact(factorial));


# print("*******************************************");
# print("\n")
# print(". Display the Fibonacci series with recursion");
# print("-------------------------------------------------------------------");
# def fibonacci(n):
#    if int(n) <= 1:
#        return int(n)
#    else:
#        return(fibonacci(int(n)-1) + fibonacci(int(n)-2))
# fibo=input("Enter a number : ")
# if int(fibo) <= 0:
#    print("Plese enter a positive integer")
# else:
#    for i in range(int(fibo)):
#        print(fibonacci(i), end=" ")


# print("*******************************************");
# print("\n")
# print("Find if the given number is prime");
# print("-------------------------------------------------------------------");
# n=int(input("Enter a number : "))
# if n > 1:
#     for i in range(2, (n//2)+1):
#         if (n % i) == 0:
#             print(n, " is not a prime number")
#             break
#     else:
#         print(n, " is a prime number")


# print("*******************************************");
# print("\n")
# print("Print the list of prime numbers in the  given range");
# print("-------------------------------------------------------------------");
# n1=int(input("Enter a Starting number : "))
# n2=int(input("Enter a Ending number : "))
# if n1 > 1 and n2 > 1:
#     for i in range(n1, n2):
#         j= n1
#         while (j <= (n2/2)):
#             if (i%j == 0): break
#     j += 1
#     if(j>i/j): print (i, " is a prime number")

# def get_choices():
#     player = "Rahul"
#     student ="Sai"
    
#     return player

# choices = get_choices();
# print("************", choices)

# dict ={"name": "A", "color": "red"}

# def get_choices():
#     player_choice = input("Enter a player choice : ")
#     computer_choice ="computer"
#     choices = {"player": player_choice, "computer": computer_choice}
#     return choices

# choices=get_choices();
# print(choices)

import random
food = ["A", "B", "C"]
dinner = random.choice(food)
print(dinner)

def revStr(str1, str2):
    if str1 == str2[::-1]:
        print(f"{str1} == {str2} is a palindrome")
    else: print("Not palindrome")

string1 = str(input("Enter first string :"));    
string2 = str(input("Enter second string :"));    
revStr(string1, string2)