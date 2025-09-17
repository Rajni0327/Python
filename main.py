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
num = int(input("enter a number :"))

for i in range (1, num+1):
    print (i)
