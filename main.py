# print("hello python ") 

# a = 'hello'
# print(a[0:4:2])

   
# b = "vs code"



#question1 
# number = int(input("enter your age :"))
# print(f"your age is {number}")


#compound assignment operator
# a = 10
# a += 5
# print(a)

# print(ord("R"))
# print(ord("T"))

# print ("R" > "T")  
# cannot compare string with an integer 

#conditional statements questions 

#1
# num1 = int(input("enter first number :"))
# num2 = int(input("enter second number :"))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# else:
#     print(f"{num2} is greater than {num1}")



#2
# user = input("enter your gender (male/female):")

# if user == 'male':
#     print ("good Morning sir ")
# else:
#     print("good Morning ma'am")



#3
# num = int(input("enter a number :"))

# if num % 2 == 0:
#     print(f"{num} is even number")
# else:
#     print(f"{num} is odd number")


#4
# name = input("enter your name :")
# age = int(input("enter your age :"))

# if age >= 18:
#     print(f"Hello {name} you are a valid voter")
# else:
#     print(f"Hello {name} you are not a valid voter")


#5 
# year = int(input("enter a year :"))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


#6
# temp = int(input("enter temperature :"))

# if temp == 0:
#     print ("freezing cold ")
# elif temp > 0 and temp <= 10:
#     print("very cold")
# elif temp > 10 and temp <= 20:
#     print("cold")
# elif temp > 20 and temp <= 30:
#     print("pleasant")
# elif temp > 30 and temp <= 40:
#     print("hot")
# else:
#     print("very hot")


#loops 

#1
# num = int(input("enter number of times you want to execute  :"))
# for i in range(num):
#     print("hello world")


#2
# num = int(input("enter a number :"))

# for i in range (1, num+1):
#     print (i)



#3
# num = int(input("enter a number :"))

# for i in range (num, 0, -1):
#     print (i)



#4
# num = int(input("enter a number :"))

# for i in range (1, 11):
#     print (f"{num} x {i} = {num*i}")



#5
# num = int(input("enter a number :"))
# sum = 0
# for i in range (1, num+1):
#     sum = sum + i

# print (f"the sum is {sum}")



#6
# num = int(input("enter a number :"))
# fac = 1
# for i in range (1, num+1):
#     fac = fac * i

# print (f"the factorial is {fac}")



#7
# num = int(input("enter a number :"))
# even =0
# odd = 0
# for i in range (1, num+1):
#     if i % 2 ==0:
#         even = even + i
#     else:
#         odd = odd + i

# print (f"even and odd sum is {even} and {odd}")



#8
# num = int(input("enter a number :"))
# for i in range (1, num+1):
#     if num % i == 0:
#         print (i)



#9
# num = int(input("enter a number to find out if its perfect or not  :"))
# sum = 0
# for i in range (1, num):
#     if num % i == 0:
#         sum = sum + i
# if sum == num:
#     print(f"{num} is a perfect number")
# else:
#     print(f"{num} is not a perfect number")



#10
# num = int(input("enter a number to find out if its prime or not  :"))
# count = 0
# for i in range (1, num+1):
#     if num % i ==0:
#         count = count + 1

# if count == 2:
#     print(f"number is a prime number {num}")
# else:
#     print(f"{num} is not a prime number")



#11
# string = input("enter a string you want to reverse :")
# inLine = ""
# for i in range(len(string)-1, -1, -1):
#     inLine = inLine + string[i]
# print(inLine)


#12
# string = input("enter a string you want to reverse :")
# inLine = ""
# for i in range(len(string)-1, -1, -1):
#     inLine = inLine + string[i]

# if string == inLine:
#     print(f"{string} is a palindrome")
# else:
#     print(f"{string} is not a palindrome")



#13
# word = input("enter something :")
# char = 0
# dig = 0
# spchar= 0

# for i in word :
#     if i.isalpha():
#         char = char + 1
#     elif i.isdigit():
#         dig = dig + 1
#     else:
#         spchar = spchar + 1

# print(f"characters {char} \ndigits {dig} \n special characters {spchar}")



#while loop 


#1
#to extract digits of a number
# a = int(input("enter a number :"))
# while a > 0:
#     print(a%10)
#     a = a//10


#2
#extract number to print in reverse order 
# a = int(input("enter a number :"))
# rev = 0
# while a > 0:
#     rev = rev * 10 + (a % 10)
#     a = a//10
# print(rev)


#3
# a = int(input("enter a number :"))
# copy = a
# rev = 0
# while a > 0:
#     rev = rev * 10 + (a % 10)
#     a = a//10

# if copy == rev:
#     print(f"{copy} is a palindromic number")
# else:
#     print(f"{copy} is not a palindromic number ")



#game 
#craete a number guessing game
# import random
# number = random.randint(1, 10)
# print(number)
# tries = 0


# while True :
#     guess = int(input("guess a number between 1 to 10 :"))
#     if guess < number:
#         print("too low ")
#         tries += 1
#     elif guess > number:
#         print("too high ")
#         tries += 1
#     else:
#         print(f"congratulations you guessed it right in {tries} tries")
#         tries += 1
#         break

#functions 
 
# def pallindrome (string):
#     rev = ""
#     for i in range(len(string)-1, -1, -1):
#         rev = rev + string[i]   

#     if string == rev:
#         print(f"{string} is a palindrome")
#     else:
#         print(f"{string} is not a palindrome")

# pallindrome("barcelona")


#Data Structures

# list
# list traversing methods 

# 1 ,using index  (prefersable )
# a = [1, 2, 3, 4, 5]
# for i in range(len(a)):
#     print(a[i])

# 2 ,using directly on value 
# for i in a:
#     print(i)    

# methods in list 

# a = [1, 2, 3, 4, 5]
# a.append(6)
# print(a)    
# a.insert(0, 0)
# print(a)    
# a.extend( [7, 8, 9]) 
# print(a)    
# a.remove(3)
# print(a)    
# popped_item = a.pop(6)  #removes last element
# print(popped_item)
# print(a)
# print(a.index(4))
  
# print(a.count(2))

# a.sort()
# print(a)
    
# a.reverse()
# print(a)

# new_a = a.copy()
# print(a) 
# print(new_a)  

# a.clear()
# print(a)    

 
#1
# list = [12,86,-90,65,45,-32,78,-12]

# print ("positive numbers are :")
# for i in list:
#     if i >= 0:
#         print(i)

# print("negative numbers are :")
# for i in list:
#     if i < 0:
#         print(i)

#2

# list = int(input("enter number of elements you want in list :"))
# a = []
# for i in range(list):
#     num = int(input("enter a number :"))
#     a.append(num)
# print(a)

# mean = sum(a)/len(a)
# print(f"mean is {mean}")


#3
# a = [12,86,-90,65,45,657,-32,78,-12]
# #ro find the largest element in the list
# largest = a[0]
# index = 0
# for i in range(len(a)):
#     if a[i] > largest:
#         largest = a[i]
#         index = i
# print(f"largest number is {largest} and its index is {index}")

#4
#to find the second largest element in the list
# a = [11,56,43,23]
# largest = a[0]
# index1= 0
# second_largest = a[0]
# index2 = 0
# for i in a:
#     if i > largest:
#         second_largest = largest
#         largest = i
        
#     elif i > second_largest:
#         second_largest = i
#         index2 = a.index(i)

# print(f"second largest number is {second_largest} and its index is {index2}")


#5
#to find the sortest list 
# a = [1,3,9,5,6]

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("list is not sorted")
#         break   
# else:
#     print("list is sorted")

#tuple 

#unpacking of tuple
# a,b,c = (1, 2, 3)

#set 
# a = {1, 2, 3, 4, 5} 

#set methods 

# set = {1,2,3,4,5}

# set.add(6)
# print(set)
# set.remove(3)
# print(set)
# set.discard(4)
# print(set)
# set.pop()  #removes random element
# print(set)
# set.clear()
# print(set)


# other methods
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# union
# set = a.union(b)  #print(a | b)  to add both the sets 

# intersection
# intersaction = a.intersection(b)  #print(a & b) to find out common elements in both sets

# difference
# difference = a.difference(b)  #print(a - b) to find elements in a but not in b
# difference = b.difference(a)  #print(b - a) to find elements in b but not in a

# symmetric difference
# symmetric_difference = a.symmetric_difference(b)  #print(a ^ b) to find elements in a and b but not in both 


# dictionary
# key value pair 
 
# key cannot be changed
# value can be changed

# d= {10:100 , 20:200, 30:300, 40:400}

# d.update ({50:500})   # you cannot update keys in dictionary
# print(d)

# d[60] = 600
# print(d)     

# del d[30]

# d = {10:100 , 20:200, 30:300, 40:400}

# for i in d:
#     print (d[i]) # to print values of dictionary
#     print(i)   # to print keys of dictionary


# methods
# d = {10:100 , 20:200, 30:300, 40:400}

# # d.clear()

# a = d.copy() # shallow copy
# print(a)

# print(d.get(20)) # to get value of a key
# print(d.items()) # to get all items in the form of tuples


# 1 merging two dictionaries

# d1 = {10:100 , 20:200 , 30:300}
# d2 = {40:400 , 50:500 , 60:600}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)

#2 sum all the values in the dictionary
# d = {10:100 , 20:200 , 30:300}
# sum = 0
# for i in d:
#     sum = sum + d[i]

# print(f"sum of all values is {sum}")


#3 counting frequency of each element in list 
# a = [1,1,1,2,2,3,3,3,4,4,4,4]
# freq = {}
# for i in a:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# print(freq)

#combining two dictionaries adding values of common keys 
# d1 = {10:100 , 20:200 , 40:300}
# d2 = {40:400 , 50:500 , 60:600}

# for i in d2:
#     if i in d1:
#         d1[i] = d1[i] + d2[i]
#     else:
#         d1[i] = d2[i]

# print(d1)

#exceptions handling


# a = int (input("enter a number :"))

# try:
#     print(10/a)
# except ZeroDivisionError:
#     print("cannot divide by zero ")
# else:
#     print("no error")
# finally:
#     print("i will run no matter what")
# print("hello")

#raise exception

# file handeling 

# p = open('main.py')
# print(p.read())  # reads the whole file

# r = open('ironman.txt', 'a') 
# r.write("i am ironman ")
# r.write('appending file')  # w for write mode , r for read mode , a for append mode
# r.close()

# oops in python

# imperative appraoch 
# a = 2
# b = 5
# print(a+b)


# functional approach 
# def add (a, b):
#     return a + b   
 
# print(add(2, 5))


# class 
# class Car:
#     a = 12  # class attribute
#     def hello():   # method 
#         print("hello car")

#     print("im getting printed when class is defined")

# # print(a) # will give error because a is not defined in this scope
# print(Car().a)  # to access class attribute
# Car.hello()  # to access method

# obj = Car()  # creating object of class
# print(obj.a)  # accessing class attribute using object
# obj.hello()  # accessing method using object


# constructor
# class Factory :
#     def __init__(self, material , zips , pockets ): # constructor use as parameter and self as location of object
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
    
#     def show (self):
#         print(f"ojects details are  {self.material} , zips are {self.zips} , pockets are {self.pockets}")

# reebok = Factory("leather", 5, 4)
# nike = Factory("jeans", 3, 2)

# print(reebok.material)
# print(nike.zips)
# reebok.show()
# nike.show() 


# types of attributes

# class Car:
#     wheels = 4 # class attribute

#     def __init__(self, color):
#         self.color = color  # instance attribute

#     def show (self):    # instance method
#         print ("How have you been ?")

#     @classmethod
#     def hello(cls):
#         print ("hello car")  # class method

#     @staticmethod
#     def greet():
#         print("good morning")  # static method  

# obj = Car("red")
 
# obj.show()  # instance method called using object
# Car.hello()  # class method called using class name
# Car.greet()  # static method called using class name
# print(obj.color)  # instance attribute called using object
# print(Car.wheels)  # class attribute called using class name


# inheritance

# single level inheritance

# class FactoryDelhi :  # parent class/super class
#     a = "I am delhi factory"
#     def hello (self):
#         print("i make perfumes in delhi factory")

# class FactoryMumbai(FactoryDelhi):  # child class /sub class
#     pass

# obj = FactoryDelhi()  # object of delhi factory
# obj2 = FactoryMumbai()  # object of mumbai factory
# print(obj2.a)


# class Animal : # parent class
#     def __init__(self,name):
#         self.name = name

#     def show (self):
#         print(f" name is {self.name}")

# class Human(Animal) : #child class
#     def __init__(self, name, age ):
#         super().__init__(name)  # to call constructor of parent class
#         self.age = age

#     def show (self):
#         print(f" name is {self.name},{self.age}")

# animal1 = Animal("tiger")  #instance of parent class
# person1 = Human("Sarthak",23)  #instance of child class

# animal1.show()
# person1.show()




# multilevel inheritance


# class Animal :
#     name1 = "lion"

# class Human :
#     name2 = "Sarthak"
    
# class Robots (Human, Animal):  # multiple inheritance
#     name3 = "robo"

# obj = Robots()

# print(obj.name1, obj.name2, obj.name3)



# class Factory :
#     def __init__(self,material ,zips ):
#         self.material = material 
#         self.zips = zips 

# class BhopalFactory (Factory):
#     def __init__(self, material, zips, color):
#         super().__init__(material, zips)
#         self.color = color 
       
# class PuneFactory(BhopalFactory):
#     def __init__(self, material, zips, color, pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets 



# obj =PuneFactory()


# polymorphism 


#overriding
# class Animal :
#     def show (self):
#         print("hello im Sarthak")

# class Human (Animal):
#     def show(self):
#         print("How are you ?")

# obj = Human()
# obj.show()  #method overriding 


# duck typing

# class Animal :
#     def show (self):
#         print("im showing")

# class Human(Animal):
#     def show(self):
#         print("hellp im also showing")

# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show()  #separated by classes 


 
 #encapsulation 

#proctected attributes and methods 

# naming convention to tell developers that this is protected 

# class Factory :
#     _a = "pune "  # proctected 

#     def _show (self):
#         print("hello im pune factory ")

# class Bhopal (Factory):
#     def show2(self):
#         print(super()._a)  # trying to accessing protected 

  
# obj = Bhopal()
# obj.show2()



# private attributes and methods


# class Factory :
#     __a = "pune "  # private  __

#     def _show (self):
#         print("hello im pune factory ")

# class Bhopal (Factory):
#     def show2(self):
#         print(super().__a)  # trying to accessing private content 

  
# obj = Bhopal()
# obj.show2()



# abstraction

# from abc import ABC, abstractmethod 


# class abstract(ABC):
#     @abstractmethod
#     def perimeter (self):
#         pass
     
#     @abstractmethod
#     def area (self):
#         pass


# class Square(abstract):
#     def __init__(self,side):
#         self.side = side

#     def perimeter (self):
#         print("i have created")

#     def area (self):
#         print("i have created this too")

# class Circle (abstract):
#     def __init__(self,radius):
#         self.radius = radius
        
#     def perimeter (self):
#         print("i have created")

#     def area (self):
#         print("i have created this too")


# obj = Circle (7)
# obj2 = Square(12)

    



#Dunder methods
# start and end with double underscore

# class Animal :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"hello how are you and your name is {self.name}"
    
#     def __add__ (self, other):
#         sum = 0
#         for i in other:
#             sum = sum + i.age
#         return f"your sum of ages are {self.age + sum}"

    
# obj = Animal("whale",12)
# obj2 = Animal("dolphin", 5)
# obj3 = Animal("tiger",3)


# print(obj + (obj2,obj3))



# decorator 


# def decorate(func):
#     def wrapper ():
#         print("i will print myself before the function hello ")
#         func()
#         print("i will print after the function")
#     return wrapper

# @decorate
# def hello( ) :
#     print("hello im Sarthak sharma")

# hello()



# def decorate(func):
#     def wrapper (a,b):
#         print("Addition to your numbers are ")
#         func(a,b)
#         print("thankyou")
#     return wrapper

# @decorate
# def Addition(a,b) :
#     print(f"your total is {a + b}")

# Addition(23,26)



# args and kwargs 


#args

# def addition (*args):  #storing multiple arguments in tuple form 
#     sum = 0
#     for i in args:
#         sum = sum +i 
#     print (sum)

# addition (12,12.658856456545)

# #kwargs 
# #keyword arguments 

# def info(**kwargs):
#     print("your information is : \n")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")



# info (name = "sarthak", age = 23 , designation = "ai/ml")





# def decorate(func):
#     def wrapper (*args ,**kwargs):
#         print("Addition to your numbers are ")
#         func(*args, **kwargs)
#         print("thankyou")
#     return wrapper

# @decorate
# def Addition(a,b) :
#     print(f"your total is {a + b}")

# Addition(23,26)




# ternary operation 
# a = 13

# print ("even ") if a %2 == 0 else print("odd")



#comprehension 


# l = [i for i in range(1,21) if i %2==0]  #list comprehension
# print(l)


# l = {i : i**2 for i in range(1,21)}  #dictionary comprehension
# print(l)


# l = {i*i for i in range(10) if i %2==0} #set comprehension
# print(l)


#Lamda Function 

# addition = lambda a,b : a+b 

# print(addition(12,12))




# addition = lambda a : "even" if a %2 == 0 else "odd"

# print(addition(23))




# map filter and zip


# a = [1,2,3,4,5]

# result = map (lambda x : x*2, a )
# or
# def double (x):
#     return x*2

# result = map(double,a)


# map works better with lambda 

# print (list(result))


# filter
# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# a = [1,2,3,4,5,6,7,8,9]

# # result= filter(even ,a)
# #or
# result = filter (lambda x :True if x%2 == 0 else False ,a)

# print(list(result))



# modules and packages 

# module is a single file containing code to use this file in other file 

# import maths

# print(maths.addition(12,12)) #calling from another file 




# packages 
# contain one or more modules 

from packages import hello ,maths

# if folder in folder 

# from foldername.foldername import hello , maths 