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






