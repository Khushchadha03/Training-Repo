# print("hello","hola")
"""
name = "khush"
print(name)
print("my name is", name)
age = 23
print("my age is", age)
age2 = age
print("my age2 is", age2)
print(type(name))
print(type(age))
print(type(age2))
old = False
a = None
print(type(old))
print(type(a))
a = 2000
b = 300
Sum = a+b
print(Sum)
"""

# Operators 

# Arithemetic Operators
# a = 2000
# b = 300
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b) #a^b

# Relational / comparision Operators 
# a = 20
# b = 30
# print (a==b)
# print (a!=b)
# print (a>=b)
# print (a<=b)

# Assignment Operators
# num = 10
# num +=10  #num = num+10
# num -=10  #num = num-10
# num *=10  #num = num*10
# num /=10  #num = num/10
# num %=10  #num = num%10
# num **=10  #num = num%10
# print (num)

#Logical Operarors
# a = 30
# b = 10   
# print(not True)
# print(not (a>b))
# val1 = True
# val2 = False
# print(val1 and val2)
# print(val1 or val2)

# Type Conversion 
# a = 2   # you can't add float and string if a = "2"
# b = 4.25
# print (a+b) 
# Type casting 
# a = int("2")
# b = 4.25
# print(type(a))
# print (a+b) 
# a = 3.14
# a = str(a)

# taking input
# name = int(input("name:")) # input is always going to be string so use type casting
# print("Welcome",name)

# num1 = int(input())
# num2 = int(input())
# print(num1 + num2)

# a = int(input("side of Sq: "))
# print("Area of Sq:",a*a)

# a = float(input("a: "))
# b = float(input("b: "))
# print ("Average =", (a+b)/2)


# num1 = int(input())
# num2 = int(input())
# print(num1>=num2)

# Strings
# str1 = "String 1"
# str2 = ' String 2'
# str3 = '''String 3'''
# str4 = "String 4 \-ntry to next line"
# print(str4)
# str5 = "String 5 \ttry to next line"
# print(str5)
# concatenation 
# str1 = "String 1"
# str2 = ' String 2'
# final_str = str1+str2
# print (final_str)
# Length of string
# str1 = "String 1"
# len1 = str1
# print(len(str1))
# Indexing - accessing a character and we can't manipulate the character
# str1 = "String 1"
# ch = str1[3]
# print(ch)

#Slicing - acessing the part of the string
# str = "String 1"
# a=str[1:3] #not take 3
# b=str[:3]
# c=str[3:] #for last string we can also write only len(str)
# print(a)
# print(b)
# print(c)
# negative index or backward counting
# str = "String 1"
# a=str[-4:-1] #not take 4
# print(a)

# String Functions 
# str = "hello my name is khush chadha"
# print(str.endswith("ha"))
# str = print(str.capitalize()) # for doing changes in main string
# str = "hello my name is khush chadha"
# print(str.replace("o","a"))
# str = "hello my name is khush chadha"
# print(str.find("name"))
# str = "hello my name is khush chadha"
# print(str.count("h"))
# name = input("user name:")
# print(len(name))
# str = input("String : ") 
# print(str.count("$"))

# Conditional Statements - if-else
# age = 16
# if(age>=18):
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")
# marks = 70
# if(marks>=90):
#     grade = ("A")
# elif(80<=marks and marks<90):
#     grade = ("B")
# elif(70<=marks and marks<80):
#     grade = ("C")
# elif(70<=marks and marks<80):
#     grade = ("D")
# elif(60<=marks and marks<70):
#     grade = ("E")
# else:
#     grade = ("Fail")

# nesting - if mein if
# age = 15
# if(age >=18):
#     if(age<=80):
#         print("can drive")
#     else:
#         print("can not drive")
# else:
#     print("can not drive")  

# num = int(input("Enter a number: "))
# num = num%2 == 0
# if(num):
#     print("Number is Even")
# else:
#     print("Number is Odd")
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# if(a>b and a>c):
#     print("a is the largest number")
# elif(b>c):
#     print("b is the largest number")
# else:
#     print("c is the largest number")
# num = int(input("enter the number: "))
# num %= 7
# if(num ==0):
#     print("num is divisible")
# if(num !=0):
#     print("num is not divisible")

# Lists #Strings are immutable and lists are mutable 
# marks = [12,"khush",45,56,"ram",78,89.5]
# print(marks[0])
# print(marks[1],marks[2])
# print(len(marks))
# marks[2] = "Chadha"
# print(marks)
# # print(marks[7]) #out of index error

# List Slicing # ending index is not included
# marks = [12,"khush",45,56,"ram",78,89.5]
# print(marks[1:4])
# print(marks[:4])
# print(marks[3:])
# print(marks[-5:-1])

# List Methods
# list = [2,4,3]
# list = ['a','g','u','r']
# list.append('y')
# list.sort() # ascending method
# list.sort(reverse=True) # descending method
# list.reverse()
# list.insert(1,5)
# list.remove('u')
# list.pop(3)
# print(list)

# Tuples  # immutable
# tup = (1,5,7,9,4)
# tup = (1,) # if not  comma it will be understood as an interger
# tup = ()
# print(tup[3])

# Tuple Slicing 
# tup = (1,5,7,9,4)
# print(tup[1:3])
# print(tup[:3])
# print(tup[2:])
# print(tup[-4:-1])

# Tuple methods
# tup = (1,5,7,9,4,1,3,4,5,1)
# print(tup.index(9))
# print(tup.count(1))

# movies = []
# m1 = input("Favourite movie 1: ")
# m2 = input("Favourite movie 2: ")
# m3 = input("Favourite movie 3: ")
# movies.append(m1)
# movies.append(m2)
# movies.append(m3)
# print(movies)
# print(type(movies))

# movies = []
# m = input("Favourite movie 1: ")
# movies.append(m)
# m = input("Favourite movie 2: ")
# movies.append(m)
# m = input("Favourite movie 3: ")
# movies.append(m)
# print(movies)
# print(type(movies))

# movies = []
# movies.append(input("Favourite movie 1: "))
# movies.append(input("Favourite movie 2: "))
# movies.append(input("Favourite movie 3: "))
# print(movies)
# print(type(movies))

# list = [1,2,3,2,7]
# copy_list = list.copy()
# copy_list.reverse()
# if(list == copy_list):
#     print("palindrome")
# else:
#     print("not palindrome")
# grade = ('C','D','A','A','B','B','A')
# print(grade.count('A'))
# grade = ['C','D','A','A','B','B','A']
# grade.sort()
# print(grade)

# Dictionary # unordered, mutable,
# info = {
#     "key" : "value",
#     "subject" : ["python","c","JAVA"],
#     "topics" : ("dict","set"),
#     "name" : "khush",
#     "learning" : "coding",
#     "age" : "21",
# }
# print(info["name"])
# print(info["subject"])
# null_dict = {}  # empty dictionary
# info["name"] = "khush chadha"
# info["surname"] = "JI"
# print(info)

# Nested Dictionary
# student ={
#     "name" : "khush",
#     "subjects" : {
#         "phy" : 97,
#         "chem" : 99,
#         "maths" : 89
#     }
# }
# print(student["subjects"]["chem"])

# Dictionary methods
# student ={
#     "name" : "khush",
#     "subjects" : {
#         "phy" : 97,
#         "chem" : 99,
#         "maths" : 89
#     }
# }
# print(list(student.keys()))
# print(len(student.keys()))
# print(list(student.values()))
# pairs = list(student.items())
# print(pairs[1])
# print(student["name"]) #if the value is not there it will give error
# print(student.get("name")) #if the value is not there it will give none
# student.update({"city":"Delhi"})
# new_dict = {"city":"Delhi","age":13}
# student.update(new_dict)
# print(student)

#Set #Unique and immutable, Unordered, ignore duplicate values
# Collection = {1,2,2,3,4}
# print(Collection)
# print(len(Collection))
# collection = set() #empty set syntax
#set methods # sets are mutable but the elements of sets are immutable

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.remove(1)
# collection.add("khush")
# collection.add((1,2,3,4))#cannot pass a list in the set
# collection.clear()
# collection.pop() # Generating Random Value from set
# print(collection)
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set = set1.union(set2)
# print(set)
# print(set1)
# print(set2)
# set = set1.intersection(set2)
# print(set)

# dictionary = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture" ,"list of facts & figures"]
# }
# print(dictionary)

# list = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
# print(len(list))

# marks ={}
# x = int(input("marks "))
# marks.update({"phy" : x})
# x = int(input("marks "))
# marks.update({"m" : x})
# x = int(input("marks "))
# marks.update({"c" : x})
# print(marks)

# value = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(value)

# loops
# count = 1
# while count<=5:
#     print("hii")
#     count+=1
# print(count)
# i = 1
# while i<=5:
#     print(i)
#     i+=1
# i=5
# while i>=1:
#     print(i)
#     i-=1
# i = 100
# while i>=1:
#     print(i)
#     i-=1
# i=1
# while i<=10:
#     print(i*3)
#     i+=1
# list = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i<=len(list)-1:
#     print(list[i])
#     i+=1
# tup = (1,4,9,16,25,36,49,64,81,100)
# num = int(input("num"))
# i=0
# while i<=len(tup)-1:
#     if(tup[i]==num):
#         print(i)
#     i+=1
#Break and Continue
# i = 1
# while i<=10:
#     if(i==3):
#         i+=1
#         continue
#     if(i==5):
#         break
#     print(i)
#     i+=1
# list = "khush_chadha hey"
# for i in list:
#     print(i)
# num = (1,4,9,16,25,36,49,64,81,100,36)
# x = 36
# idx = 0
# for i in num:
#     if(i==x):
#         print(idx)
#     idx +=1
# seq = range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])
# for i in range(5):
#     print(i)
#range(start(op or it will take 0),stop(compulsary),step(op or it will take 1))
# for i in range(10):
#     print(i)
# for i in range(2,10):
#     print(i)
# for i in range(2,10,2):
#     print(i)
# for i in range(1,101):
#     print(i)
# for i in range(100,0,-1):
#     print(i).
# n=int(input("enter number: "))
# for i in range(1,11):
#     print(n*i)
# pass
# for i in range(8):
#     pass # also used in if else
# print("hola")
# num = int(input("to which number : "))
# sum = 0
# i=0
# while i<=num:
#     sum +=i
#     i+=1
# for i in range(num+1):
#     sum += i 
# print(sum)

# num = int(input("to which number : "))
# mul = 1
# for i in range(1, num+1):
#     mul*=i
# print(mul)

#Functions
# def cal_sum(a,b): # function defination & Parameters
#     sum = a+b
#     print(sum)
#     return sum
# cal_sum(4,5)# calling the function & (4,5) are the arguments
# def cal_sum(a,b):
#     return a+b
# print(cal_sum(1,2))
# def cal_avg(a, b, c):
#     avg = (a+b+c)/3
#     print(avg)
#     # return avg
# cal_avg(3,4,6)

# print("hello",end=" ")
# print("heyy!!")

# def cal_mul(a=1,b=4,c=6): #you can use default parameters so that is the value is not going to define there than the function will also going to work
# # and if you want to use some default values do it with last value so that the function will not give any error def cal_mul(a,b,c=6) in this also if you will not give the value of C it will work
#     return a*b*c
# mul = cal_mul(2,3,5)
# print(mul)
# mul1 = cal_mul()
# print(mul1)
# cities = ["delhi", "gurugram", "noida"]
# def len_list(a):
#     for i in range(len(a)):
#         print(a[i])
#     return i
# len_list(cities)
# cities = ["delhi", "gurugram", "noida"]
# def len_list(a):
#     for i in range(len(a)):
#         print(a[i],end = " ")
#     return i
# len_list(cities)
# def fac(a):
#     fact = 1
#     for i in range(1, a+1):
#         fact *= i
#     print(fact)
# fac(5)
# def conv(a):
#     b = a*83
#     print(b)
# conv(8)
# def check(n):
#     if(n % 2 == 0):
#         print("Even")
#     else:
#         print("Odd")
# check(8)

# Recursion # Reccurance Relation
# def show(n):
#     if(n==0): #Base Case
#         return
#     print(n)
#     show(n-1)
#     print("END")
# show(5)
# def fac(n):
#     if (n==0 or n==1):
#         return 1
#     return fac(n-1)*n
# ans = fac(5)
# print(ans)
# def sum(n):
#     if(n == 0):
#         return 0
#     return sum(n-1)+n
# total_sum = sum(5)
# print(total_sum)
# def list(a,ind = 0):
#     if(ind == len(a)):
#         return
#     print(a[ind])
#     list(a, ind+1)
# fruits = ["mango", "grapes", "guava", "pomegranate"]
# list(fruits)
#File I/O
# f = open("demo.txt", "r")
# # data = f.read(5)
# data = f.readline()
# print(data)
# f.close()
# f = open("demo.txt", "a")
# f.write("\n i m khush chadha")
# f.close()
# f = open("sample.txt","w") # for creating a file
# f.close()

# with Syntax
# with open("demo.txt","r") as f: #automatiically close
#     data = f.read()
#     print (data)
# import os
# os.remove("demo.txt")

#OOPS
#creating class
# class Student:
#     name = "Khush" 
#creating objects
# s1 = Student()
# print(s1.name)
# s2 = Student()
# print(s2.name) 

#Constructors
# class Student:
#     #default constructors
#     def __init__(self):
#         pass
#         #Parameterized Constructors
#     def __init__(self,name, marks):
#         self.name = name
#         self.marks = marks
# s1 = Student("Khush" , 99)
# print(s1.name, s1.marks)

# class students:
#     college_name = "VIT"
#     def __init__(self , name, state, marks):
#         self.name = name
#         self.state = state
#         self.marks = marks
#         print(name)
#     def welcome(self):
#         print("welcome student")
#     def get_marks(self):
#         return self.marks
# s1 = students("khush" , "Delhi",99)
# s1.welcome()
# print (s1.get_marks())

# class students:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         # print(name , marks)
#     def avg_marks(self):
#         sum = 0
#         for i in self.marks:
#             sum+=i
#         avg = sum/len(self.marks)
#         print(avg)
# s1 = students("Khush1", [34,56,78])
# s1.avg_marks()

# Static Methods
# @staticmethod #decorator

# class Acc:
#     def __init__(self, balance, acc_no):
#         self.balance = balance
#         self.acc_no = acc_no
#     def debit(self, debit):
#         self.balance -= debit  
#         print("total balance is: ",self.print_bal())
#     def credit(self, credit):
#         self.balance += credit
#         print("total balance is: ",self.print_bal())
#     def print_bal(self):
#         # print(self.balance)
#         return self.balance
# s1 = Acc(10000,1)
# s1.debit(500)
# s1.credit(200)

# Del keyword
# class Student:
#     def __init__(self, name):
#         self.name = name
# s1 = Student("Khush")
# del s1
# print(s1)

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass #double underscore is for making it private we cant use outside the class
# acc1 = Account(12345, 3456)
# print(acc1.acc_no)
# print(acc1.__acc_pass)#it will show error

# Inheritance
# Single Inheritance
# class car:
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped..")
# class toyotacar(car): #for showinf inheritance
#     def __init__(self, name):
#         self.name = name
# car1 = toyotacar("fortuner")
# car2 = toyotacar("prius")
# print(car1.name)
# print(car1.start())

# Multi Level Inhertance
# class car:
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped..")
# class toyotacar(car): #for showing inheritance
#     def __init__(self, brand):
#         self.brand = brand
# class fortuner(toyotacar):
#     def __init__(self, type):
#         self.type = type
# car1 = fortuner("diesel")
# car1.start()

# Multiple Inheritance
# class A:
#     varA = "ClassA"
# class B:
#     varB = "ClassB"
# class C(A,B):
#     varC = "ClassC"
# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

# Super Method
# class car:
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped..")
# class toyotacar(car): #for showing inheritance
#     def __init__(self, name,type):
#         self.name = name
#         super().__init__(type)
#         super().start()
# car1 = toyotacar("fortuner", "Electric")
# print(car1.type)

# class person:
#     name = "anonymous"
#     def changename(self,name):
#         # self.__class__.name = name # for doing changes in class other method
#         # person.name = name # for doing changes in class 
#         # self.name = name #it will not make changes in class
# p1 = person()
# name = p1.changename("Khush")
# print(p1.name)
# print(person.name)
# class person:
#     name = "anonymous"
#     @classmethod
#     def changename (cls,name):
#         cls.name = name
# p1 = person()
# name = p1.changename("Khush")
# print(p1.name)
# print(person.name)

#Property decorator
# class Student:
#     def __init__(self, phy, chem, math):
#         self.math = math
#         self.phy = phy
#         self.chem = chem
#     def cal_percent(self):
#         self.percentage = str((self.math + self.phy + self.chem)/3) + "%"
# stu1 = Student(78, 89, 99)
# print(stu1.percentage)
# stu1.phy = 76
# print(stu1.phy)
# stu1.cal_percent()
# print(stu1.cal_percent)

# class Student:
#     def __init__(self, phy, chem, math):
#         self.math = math
#         self.phy = phy
#         self.chem = chem
#     # def cal_percent(self):
#     #     self.percentage = str((self.math + self.phy + self.chem)/3) + "%"
#     @property
#     def percentage(self):
#         return str((self.math + self.phy + self.chem)/3) + "%"
# stu1 = Student(78, 89, 99)
# print(stu1.percentage)
# stu1.phy = 76
# print(stu1.percentage)

# Polymorphism
# print(1+2)
# print("Khush" + "Chadha")
# print([1,2,3]+[4,5,6])
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
#     def show(self):
#         print(self.real, "i +", self.img, "j")
#     def __add__(self, num2):# dunder function
#         newReal = self.real +num2.real
#         newImg = self.img +num2.img
#         return Complex(newReal, newImg)
#     def __sub__(self, num2):# dunder function
#         newReal = self.real -num2.real
#         newImg = self.img -num2.img
#         return Complex(newReal, newImg)
# num1 = Complex(1, 3)
# num1.show()
# num2 = Complex(3, 5)
# num2.show()
# num3 = num1+num2
# num3.show()
# num4 = num1-num2
# num4.show()

# class circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return (22/7)*self.radius**2# for squares
#     def peri(self):
#         return 2*(22/7)*self.radius
# c1 = circle(21)
# print(c1.area())
# print(c1.peri())

# class employee:
#     def __init__(self, role, dept, sal):
#         self.role = role
#         self.dept = dept
#         self.sal = sal
#     def show_details(self):
#         print("your role",self.role,"and department", self.dept, "salary is", self.sal)
# class engineer(employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Eng", "IT", "50000")
# eng1 = engineer("khush", 21)
# eng1.show_details()

# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price
#     def __gt__(self, ord2):
#         return self.price > ord2.price

# ord1 = Order("masala", "98")
# print("item is", ord1.item, "price is", ord1.price)
# ord2 = Order("Masala Chips", "50")
# print("item is", ord2.item, "price is", ord2.price)
# print(ord1 < ord2)