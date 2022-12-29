
#Functions
# example 1

# def great():
#     print("Good Morning")
#     # return
#     print("Good Afternoon")
# msg=great()

#example 2
#Class
# class Student:
#  def __init__(self,name):
#         self.name=name
#  def display(self):
#         print(self.name)
    # a=10
    # b=20
    # c=a+b
    # print(c)
# obj=Student("rajesh")
# del obj

#Example 3
# def wish(name):
#         print("Hello ",name, "Good Evening")
# wish("rajesh")



# Example 4
# Write a function to take number as input and print square as output
# def sqr(num):
#         print("The square of ", num ,"is ", num*num)
# sqr(4)
# sqr(5)
# sqr(6)

# Example 5
# a= "Rajesh"
# for i in range(len(a)):
#         print(i)

#Example 6
# a="Rajesh"
# b="Deshbandhu"
# c=a+b
# print(c)
# print(type(c))
# print(len(c))
# c[0]
# print(c.index("j"))
# print(c.lower())
# print(c.upper())

#Example 7
# def add(a,b):
#         print(a+b)
# add(10,20)

#Example 8
# def am():
#        global a
#        a=10
#        print(a)
# am()

#Example 9: Perform addition and subtraction and taking values from user
# class Maths:
#
#     def add(self):
#         x= int(input("Enter first number: "))
#         y= int(input("Enter second number: "))
#         print (x+y)
#     def sub(self):
#         x = int(input("Enter first number: "))
#         y = int(input("Enter second number: "))
#         print (x - y)
# maths=Maths()
# maths.add()
# maths.sub()

#Example 10: Performing addition and substraction using input and if else condition
# class Maths:
#     x = int(input("Enter first number: "))
#     y= int(input("Enter second number: "))
#     sub= str(input("choose operation +/-: "))
#     if(sub== "+"):
#         print("Addition: ",x+y)
#     elif (sub=="-"):
#         print("Substraction: ", x - y)
#     else:
#         print("Please enter valid operator")
#
#Example 11
# class Student:
#
#     def __init__(self,x,z,y):
#         self.name=x
#         self.rolno=y
#         self.marks=z
#
#     def display(self):
#         print("Student Name: {}\nRoll No: {}\nMarks: {}".format(self.name,self.rolno,self.marks))
# s=Student("Rajesh",1021,455)
# s.display()

#Example 12
# class Empoyee:
#
#     def __init__(self):
#         self.eno= 1021
#         self.ename="Rajesh"
#
#     def m1(self):
#         self.esal=45000   # We can declare instance variables inside instance method using self variable
# e=Empoyee()
# e.m1()
# e.eaddr="Bhopal"  # We can declare instance variables outside of the class by using object referece variable
# print(e.__dict__)
#

#Example 13
# class Employee2:
#     def __init__(self,eid,ename):
#         self.eid=eid
#         self.ename=ename
#         print(self.eid)
#         print(self.ename)
# # e=Employee2(1021,"Rajesh")
# # e1=Employee2(1022,"Amit")
#

#Example 14
# class Test:
#     a=10
#
#     def __init__(self):
#         Test.b=20
#     def m1(self):
#         Test.c=30
#     @classmethod
#     def m2(cls):
#         Test.d=40
#         cls.e=50
#     @staticmethod
#     def m3():
#         Test.f=60
# # print(Test.__dict__)
# t=Test()
# t.m1()
# t.m2()
# t.m3()
# print(Test.__dict__)
#
#
# print("Fabunacci series using for loop")
# x=0
# y=1
# t=int(input("Enter series values: "))
# print("Fabunacci series: ",x,y, end=" ")
# for i in range (0,t):
#     z=x+y
#     x=y
#     y=z
#     print(z,end=" ")
#
# print("\nFabunacci series using while loop")
# n=int(input("Enter series value: "))
# a=0
# b=1
# c=0
# count=1
# print("Fabunacci series: ", end=" ")
# while( count <=n):
#     count +=1
#     print(c, end=" ")
#     a=b
#     b=c
#     c = a + b

# class maths:
#     def add(self,x,y):
#         # x=10
#         # y=20
#         return (x+y)
# m=maths()
#
# print("Result: {}".format(m.add(10,20)))
#
# def fun(x,y):
#   return (x+y)
#
# res = fun(10,20)
# print("Result: {}".format(res))
#
# def greet(name):
#     return "Hello " + name # function returns a value does not print it
# greeting = greet("Rajesh")  # storing return value in greeting variable and printing it
# print(greeting)

# Printing means showing a value in the console.
# Returning means giving back a value from a function.



#Example-1
# def add():
#     x=10
#     y=20
#     z=x+y
#     print("Addition; ",z)
# add()


# Function
# def add(x,y): #remove self from parameter
#
#         z = x + y
#         print("Addition: ",z)
# add(15,20)
# add(25,54)

#
# class Add:
#     def add(self,x,y):  # Method
#         z = x + y
#
#         print("Addition: ",z)
#     # add(15,20)
#     # add(25,54)
# a1=Add()
# a1.add(10,20)
#
#
# class Add1:
#     def add(self,x,y):  # Method
#         self.x=x  # typecasting local to class level variable
#         self.y=y
#         z = x + y
#         self.z=z
#         print("Addition: ",self.z)
#     # add(15,20)
#     # add(25,54)
# a1=Add1()
# a1.add(40,20)
#
# class Arr:
#     def __init__(self):
#         x=10
#         y=10
#         z=x+y
#         print(z)
# ar = Arr()



# class Arr:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         z=x+y
#         self.z=z
#         print("Addition: ",self.z)
# ar = Arr(14,23)

# class Test1:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def pp(self):
#         print("Result: ",self.a + self.b)
# test = Test1(10,20)
# test.pp()
#
# Define a class Pen and print prize and color using constructor and method
# class Pen:
#
#     def __init__(self,prize,color):
#         self.prize = prize
#         self.color = color
#     def show(self):
#         print("Prize of Pen is: ",self.prize,"Rs.")
#         print("Color of Pen is: ", self.color)
# pen= Pen(10,"Red")
# pen.show()
#
#
# class Parent:
#
#     def hair_color(self,color):
#         color = "Brown"
#         print("Hair color of Parent: ",color)
#
#
# class Child(Parent):
#
#     def skin_color(self):
#         scolor = "brown"
#         print("Skin color of child1: ",scolor)
#     def hair_color(self,color):
#         color = "light brown"
#         print("Hair Color of Child1: ",color)
#
# class Child2(Parent):
#
#     def hair_color(self,color):
#         color="Black"
#         print("Hair color of Child2: ",color)
#
# p= Parent()
# p.hair_color()
# ch2=Child2()
# ch1=Child()
# ch1.hair_color()
# ch2.hair_color()
# ch1.skin_color()

#
# class Ad:
#     def __init__(self,color,size):
#         self.color = color
#         self.size=size
#
#     def xy(self):
#         print("Color: ",  self.color)
#         print("Size: ",self.size)
#
# class Bd(Ad):
#
#     def __init__(self,color,size,price,len):
#         super().__init__(color,size)
#         self.price=price
#         self.len=len
#     def show(self):
#         print("Price: ",self.price)
#         print("Length: ",self.len)
# bd=Bd("Red","0.5","Rs 20","10cm")
# bd.show()
# bd.xy()
# print("********")
# ad=Ad("Green","0.5")
# ad.xy()
# print("********")
# bd.xy()

# Multi level inheritance
# class Alpha:
#
#     def m1(self):
#         color = "Red"
#         Cls = "Alpha"
#         print("Color; ",color)
#         print("Class: ",Cls)
#
#     @classmethod
#     def clsmethod(cls):
#         color ="Vilot"
#         Cls="clsmethod"
#         print("Color: ",color)
#         print("Class method of Alpha: ",Cls)
#
# class Beta(Alpha):
#     def m2(self):
#         color="Green"
#         Cls ="Beta"
#         print("Color: ",color)
#         print("Class: ",Cls)
# class Gamma(Beta):
#     def m3(self):
#         color ="Blue"
#         Cls="Gamma"
#         print("Color: ", color)
#         print("Class: ",Cls)
#
# gamma = Gamma()
# gamma.m3()
# print("**********")
# gamma.m2()
# print("**********")
# gamma.m1()
# print("**********")
# gamma.clsmethod()

#
# class GF:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def m1(self):
#         print("Name of GF: ",self.name)
#         print("Age of GF: ",self.age)
#
#     # def m1(self,name,age):
#     #     self.name=name
#     #     self.age=age
#     #     print("Name of GF: ",self.name)
#     #     print("Age of GF: ",self.age)
#
# class P(GF):
#
#     def __init__(self, name, age): # Constructor
#         self.name = name # Type casting of local variable to class level variable
#         self.age = age   # same type casting
#
#     def m2(self): # method
#         print("Name of P: ", self.name)
#         print("Age of P: ", self.age)
#
#     # def m2(self,name,age):
#     #     self.name=name
#     #     self.age=age
#     #     print("Name of P: ",self.name)
#     #     print("Age of P: ",self.age)
# class C(P):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def m3(self):
#         print("Name of C: ", self.name)
#         print("Age of C: ", self.age)
#
#     # def m3(self,name,age):
#     #     self.name=name
#     #     self.age=age
#     #     print("Name of C: ",self.name)
#     #     print("Age of C: ",self.age)
# # c=C()
# # c.m3("Rahul",20)
# # print('************')
# # c.m2("Kishan",45)
# # print('************')
# # c.m1("Jagmohan",70)
#
# c=C("Rahul",20)
# c.m3()
# c=P("Kishan",45)
# c.m2()
# c=GF("Jagmohan",70)
# c.m1()
#



