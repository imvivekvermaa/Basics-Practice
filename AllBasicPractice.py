# user_city = input("Please enter the city name you grew up in!\n")
# user_pet= input("please enter your pet name!\n")

# print(f"your band name could be {user_city +' ' + user_pet}")

# a=20
# b=10

# c=a
# a=b
# b=c
# print(a)
# print(b)

# bill_value= int(input("what was the total bill?\n"))
# number_of_people= int(input("How many people to split the bill?\n"))
# tip= int(input("what percentage tip would your like to give?"))
# tip_value= (bill_value*tip)/100

# final_price= (bill_value + tip_value) /number_of_people

# print((f"Each person should pay {final_price}"))

# user_input= input("Please give us a random number!")
# print(user_input)
# a= int(user_input[0])
# b=int(user_input[1])
# print(a+b)

# user_input= int(input("Type a year!\n"))

# if user_input % 4 == 0:
#   if user_input % 100==0:

#     if user_input % 400 ==0:
#       print("it's a leap year!")
#     else:
#       print("Not a leap year")
#   else:
#     print("leap year")
# else:
#   print("Not a leap year")

# import random

# number=random.random()*5
# print(number)

# list=["computer","tablet","phones","smartphones", "laptop"]
# print(len(list))
# list.append("jacket")
# # [] is important to add bundle of items in a list
# list.extend(["shoes","socks" ,"gloves"])
# # to break a word like "work" into "w","o","r","k" in a list, use only .extend(). that's it.
# list.extend("jeans")
# print(list)

# a=[]
# for x in range(1,100):
#   a.append(x)
# print(a)

# # Diff. example of printing a list with range

# a=list(range(1,100))
# print(a)

# s=""
# for k in a:
#   s+= str(k)
# print(s)

# name= "Vivek me, you us they, those"
# print(name.split(","))

# name= "Vivek me, you us they, those"
# new_name= name.split(", ")
# print(new_name)

# 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Very important👇
#list itmes counting is always 1 less than length

# vertical= int(position[0])
# horizontal= int(position[1])

# print(vertical)
# print(horizontal)

# map[vertical-1][horizontal-1]=' X'
# print(f"{row1}\n{row2}\n{row3}")

# user_input= input("Please enter the list of students heights ").split()

# nof_people=0
# for i in range(0,len(user_input)):
#   nof_people+=1
#   user_input[i]= int(user_input[i])
# print(user_input)


# sum_height=0
# for a in user_input:
#   sum_height+=a

# print(sum_height)

# average_height= sum_height/nof_people

# print(average_height)

# students_score= input("input a list of students score ").split()

# for i in range(0,len(students_score)):
#   students_score[i]= int(students_score[i])
# print(students_score)

# max=0
# for score in students_score:
#   if max<score:
#     max=score

# print(max)


# to make a list easily--->

# a=[]
# for i in range(0,100,3):
#   a.append(i)
# print(a)

# b=""
# for j in a:
#   b+= str(j)
# print(b)

# a=list(range(1,101))
# print(a)

# for i in range(1,101):
#   if i%3==0 and i%5==0:
#     print("fizzBuzz")
#   elif i%3==0:
#     print("fizz")
#   elif i%5==0:
#     print("buzz")
#   else:
#     print(i)

#Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))


# random.shuffle(letters)
# random.shuffle(numbers)
# random.shuffle(symbols)

# l=[]
# for i in range(0, nr_letters):
#   l+=letters[i]

# s=[]
# for i in range(0, nr_symbols):
#   s+=symbols[i]

# n=[]
# for i in range(0, nr_numbers):
#   n+=numbers[i]

# new_password=l+s+n
# random.shuffle(new_password)


# final_password=""
# for p in new_password:
#   final_password+= str(p)
# print(final_password)
# n= int(input("How many times you want to print?"))

# def testing(n):
#   for i in range(n):
#     print("It Worked")

# # testing(20)
# testing(n)

# def prime_checker(number):
#   is_prime= True  
#   for i in range(2,number):    
#     if number%i==0:
#       is_prime = False
#   if is_prime:
#     print("It's a prime number")
#   else:
#     print("It's not a prime number")



# def prime_checker(number):
#   is_prime= True
#   for i in range(2,number):
#     if number%i==0:
#       is_prime= False
#   if is_prime:
#     print("It's a prime number")
#   else:
#     print("It's not a prime number")

# n=int(input("check this number: "))    
# prime_checker(number=n)


# a, b, c, n = [int(raw_input()) for _ in xrange(4)]

# print [x,y,z for x in xrange(a + 1) for y in xrange(b + 1) for z in xrange(c + 1) if x + y + z != n]

# a=0
# for i in range(1,11):
#   a+=1
#   if a==3:
#     print("_")
#   if a[1]==3:
#     print("a")

#  print(a)
# i=1
# a=23
# b=str(a)
# print(type(int(b[1])))
# print(a)

# number=0
# for i in range(1,51):
#   number+=1
#   string=str(number)
#   new_num1= int(string[0])
#   if new_num1==3:
#     new_num1+=1
#     n=str(new_num1)
#   print(new_num1)

# print(("My name is vivek").split())

# n= int(input('Check your number here!'))
# def prime_checker(number=n):
#     is_prime= True
#     for i in range(2, number):        
#         if number % i ==0:
#             is_prime= False            
#     if is_prime:
#         print("its a prime number")
#     else:
#         print("its not a prime number")
        
# prime_checker(number=n)

# i=1
# while i <= 10:
#     a= "Testing"
#     i+=1
#     print(a)

# print(a)

# n=3
# a = 0
# b=[]
# while n > a:
#     a+=1
#     b.append(a)
    
# print(sum(b))
# n=3

# n=3

# j=0
# for i in range(1, n+1):
#     j+=i
# print(j)

# e=2
# def count():
#     return e+1
# print(count())



# def check():
#     i=5
#     if  i> 0:
#         print("hi")
#         return 0
# print(check())


# l= [10,20,30,40,50]
# print(l[:4])

# l= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def oddeven(l):
#     a= [x for x in range(1,11) if x % 2== 0]
#     p= [y for y in range(1,11) if y % 2!= 0]

#     return a,p

# a,p =oddeven(l)

# print(a)
# print(p)

# l= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a= [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# d= dict(zip(l,a))
# print(d)

l= [2, 7, 8, 9, 100, 100, 200]

def checklist(l):
    a=0
    for x in range(len(l)):
        if l[x]>= a:
            a= l[x]
        else:
            return False
    return True

if checklist(l):
    print("Index is sorted")
else:
    print("index is not sorted")

# def getseclar(l):
#     lar=l[0]
#     if len(l)<=1:
#         secl=None
#         return -1
#     for x in l:
#         if x> lar:
#             secl= lar
#             lar= x
#         elif x!= lar:
#             if secl == None or secl <x:
#                 secl = x
    
#     return secl

# print(getseclar(l))