"""hello this is a comment 
and this is also a comment"""

print("Hello world! This is my first Python Program")
# print("prachi")
# print("prachi verma")
# x="Prachi"
# y=x
# print(x+" "+"Patel")
# print(12*2)
# print(type(y))
# name="Ram shyam"
# name1='Ram shyam'
# print(name)
# print(name1)
# com = "1234ij"
# print(type(com))

# import constant
# print(constant.PI)
# a=12
# print(a)
# _12=a
# print(_12)
# a=True
# print(type(a))
# x= 0b1110+11
# print(x)
# y=4.64e2
# print(y)
# c=1+2j
# print(type(c))
# n=set([1,1,2,34,4])
# print(n)
# print(type(n))
# print(type(id(n)))
# print(id(n))
# setx=set([1])
# print(setx)
# s={1,2,3,4,5,6,6}
# print(s)
# big_val=2e204
# print(big_val)
# e={'a','p','p','l','e'}
# print(e)
# colours=set()
# colours.add('Red')
# colours.update(['Yellow','Blue','Green'])
# print(colours)
# colours.pop() #Pop Red
# print(colours)
# colours.pop()  #Pop Blue
# print(colours)

# num={1,2,3,4,5,6,7,8}
# print(num)  # 1,2,3,4,5,6,7,8
# num.pop()   #remove 1
# print(num)
# num.remove(3)   # remove 3
# print(num)
# num.discard(0)  # discard 6 
# print(num)
# num.clear()
# print(num)
# print(len(num))

           # !!!!! Sritng !!!!!!!!!!!#
# name="DGukesh"   
# gname='''DGukesh is a "tamil nadu" player and he is a 'indian Grandmaster' and also a 2025 world chess olympiad winner.
# DGukesh is a tamil nadu player and he is a indian Grandmaster and also a 2025 world chess olympiad winner.'''
# print(name)   
# print(gname)   

# name="Abdul Kalam"
# info="""Ram is a "good boy"."""
# print(len(info))
# print(len(name.strip()))
# print(name)
# print(name[2:-4])
# no="good morning"
# print(no[4:2])
# print(no[-5])

              # !!!!!!! Concatenation !!!!!!!!!!!!!!!!!!


# first_name="Prachi "
# last_name="Verma"
# age=18
# isgood = True
# print("The full name is:"+ first_name +" "+last_name + " age is: "+ str(age)+ str(isgood))
# print(first_name * 3)
# txt= "my name is {0}{1} and my age is {2}."
# print(txt.format(first_name,last_name,age))

# a=123
# b=12.3
# c=a+b
# print(c)
# print(type(c))

# name='65433'
# print(name)
# print(type(name))
# print(int(name))

# a=12.22
# b=23
# print(type(b))
# print(type(int(a)))
# c=a+b
# print(c)
# print(type(c))

# name='Prachi '
# print(name*3)

# a="Ram is a good boy."
# b={1,2,3,4,5,6,7,8}
# print(a[0:20:2])
# name="Prachi"
# lname="Verma"
# number="1234"
# print(type(number))
# print(type(int(number)))
# print(b.pop())
# txt="{1} {0} is a developer."
# fname=print(txt.format(name,lname))
# a="21"
# b=12
# print(type(a))
# print(type(int(a)))
# print(complex(12,12))
# print(float(b))
# a,b,c=12,13,14
# print("This is number a:",a)

        # !!!!!!!!!!!!!!!!!! SUM OF TWO NUMBERS !!!!!!!!!!!!!!!!!!!#

# f_num = int(input("Enter you first number:"))
# s_num = int(input("Enter you second number:"))
# t_sum=f_num+s_num
# print("Sum of two numbers is:",t_sum)

  #!!!!!!!!!!!!!!!!!!!!!! MUTABILITY AND IMMUTABILITY !!!!!!!!!!!!!#
# identity =  memory adderess
# id() = reprsent memory adderess


# a=12
# print(id(a))
# a=15
# b=12
# c=3
# c=b
# print(a)
# print(id(a))
# print(id(b))
# print(type(c))
# a=[1,1,3,4]
# print('This is the id of a:',id(a))
# print('This is the id of a[0]:',id(a[0]))
# print('This is the id of a[1]:',id(a[1]))

# name="Prachi"
# fname = "prachi"
# print("id of name",id(name))
# print("id of fname",id(fname))

# a=[1,2,3,4,5]
# print("This is a[0]",id(a[0]))
# print("This is a[1]",id(a[1]))
# print("This is a :",id(a))
# a[0]=a[0]+20
# print(a[0])
# print("This is a[0]",id(a[0]))
# print("This is a[1]",id(a[1]))
# print("This is a :",id(a))
# c=20
# b=c
# print(id(c))
# print(id(b))
# print(type(c))
# print(type(b))
# a=200
# b=200.0
# c=a
# d=3
# print("this is a:",id(a))
# print("this is b:",id(b))
# print("this is c:",id(c))
# print(b is a)
# print(b is c)
# print(c is d)


#  !!!!!!!!!!!!!!!!!!!! Accepting input from Console    !!!!!!!!!!!!!!!!!!!!!


# name=input("Enter you name:")
# print(type(name))

# expression = input("Enter an expression: ")  # e.g., 2 + 3 * 4
# print(eval(expression))                       # this is dengerous 

# b= list(input('Make you list using input:').split())
# print("The value of b:",b)
# print("The value of b[1]:",b[1])

# c= set(input('Make you set using input:').split(","))
# print("The value of c:",c)
# print("The value of c[0]:",c[0])
# print("The value of c[1]:",c[1])
# d={
#   'name':'prachi',
#   'course':'python',
# }
# print('value of d:',d)

# $$$$$$  Write a program which will accept principle amount, time and rate of intrest. Calculate the simple intrest & total amount. $$$$

# principle= int(input("Enter the principle value:"))
# rate= int(input("Enter the rate value:"))
# time= int(input("Enter the time value:"))
# si= principle*rate*time/100
# print("Simple interest is:",si)
# total=si+principle
# print("Enter the total:",total)


# !!!!!!!!!!!!!!!!!!!!!!! Printing Statement  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# print("hello "*20)
# print('hello this is a \'man\'')
# print("hello this is a \"women\"")
# print(r"heloo this is a \tboy")
# print("heloo this is a \ boy")
# print("heloo this is a \\ boy")
# print(r"C:\new\test")
# name=input("Enter you first name")
# lname=input("Enter you last name")
# print(name,lname,sep="",end="@zoho.com")
# print('hello this is\v prachi')


# !!!!!!!!!!!!!!!!!! 3.12 Simple 'python' programs !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Program 1.py
# $$$$$$$$$$$$$$$$$$$$$$$ Enter your,age and address one by one and display them.$$$$$$$$$$$$$$$$$$$$$$$$4

# name= input("Enter you Name:")
# age= int(input("Enter you Age:"))
# address= input("Enter you Address:")
# print('Name:',name)
# print('Age:',age)
# print('Address:',address)

# Program 2.py
# $$$$$$$$$$$$$$$$$$$$$$$$$$$ Enter 3 numbers, and find their sum, average and display them. $$$$$$$$$$$$$$$$$$$$
 
# num1= int(input("Enter you First number:"))
# num2= int(input("Enter you Second number:"))
# num3= int(input("Enter you Third number:"))

# total_sum= num1+num2+num3
# print("Sum of three numbers:",total_sum)
# average= total_sum/3
# print("Average of three numbers:",average)

# Program 3.py
#$$$$$$$$$$$$$$$$$ Enter the radius of a circle and find the area. $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# r=int(input("Enter you circle radius:"))
# PI= 3.14
# area=PI*r*r
# circumfrence=2*PI*r
# print("Area of your circle:",area)
# print("Circumfrence of your circle:",circumfrence)

#Program 4.py
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Python Program to finnd Area of Circle using Circumference $$$$$$$$$$$$$$$$$$

# cfrence= int(input("Enter the circumfrence of your circle:"))
# Pi= 3.14
# r=cfrence/(2*Pi)
# area=Pi*r*r
# print("Area of your circle:",area)

#Program 5.py
# $$$$$$$$$$$$$$$$$$$$$$ Add two Numbers provided by the user $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#Program 6.py
# $$$$$$$$$$$$$$$$$$$$$$ Enter a number and display its cube value. $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# number= int(input("Enter your number:"))
# cube= number*number*number
# txt=("Cube of {} is:{}")
# print(txt.format(number,cube))  # short version     print("Cube of {} is:{}".format(number,cube))

#Program 7.py
# The standard form of a quadratic equation is: ax<sup>2</sup>+bx+c=0, where a,b and c are real numbers and a=!0 $$$

# import cmath
# a= int(input("Enter the value of a:"))
# b= int(input("Enter the value of b:"))
# c= int(input("Enter the value of c:"))
# d=b**2-4*a*c
# x1=(-b-cmath.sqrt(d))/2*a
# x2=(-b+cmath.sqrt(d))/2*a
# print("The value of x1 is",x1)
# print("The value of x2 is",x2)

#Program 8.py
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Find the square root $$$$$$$$$$$$$$$$$$$$$$$$$

# import cmath
# value=int(input("Enter the value you want square root:"))
# sqrt=int(cmath.sqrt(value))
# print("Square root of {} is:{}".format(value,sqrt))

# &&&&&&&&&&&&&&&&&&&&  output:- but it gives a complex number but we can't convert complex to int numbers

# value=int(input("Enter the value you want square root:"))
# sqrt= value**0.5 # in math sqrt is written in 1/2 or 0.5
# print("Square root of {} is:{}".format(value,sqrt))

# Program 9.py
# $$$$$$$$$$$$$$$$$$$$$$ Swap two variables $$$$$$$$$$$$$$$$$$$$$$$

# x=int(input("Enter the first value:"))
# y=int(input("Enter the second value:"))
# temp=x
# x=y
# y=temp
# print("Now,First value is changed:",x)
# print("Now,First value is changed:",y)


# Program 10.py
# $$$$$$$$$$$$$$$$$$$$$$ Without using temporary variable swapping $$$$$$$$$$$$$$$$$$$$$$$

# x=int(input("Enter the first value:"))
# y=int(input("Enter the second value:"))
# x,y=y,x
# print("Now,First value is changed:",x)
# print("Now,First value is changed:",y)

# Program 11.py
# $$$$$$$$$$$$$$$$$$$$$ Generate a Random Number $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# import random
# print(random.randrange(0,9))    # 9 nahi aaye ga 
# print(random.randint(0,9))      # 0 - 9 koi bhi aa sakta hai 0 aur 9 bhi

# Program 12.py
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Convert Kilometers to Miles $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# kmval= float(input("Enter your value in kilometer:"))
# chmiles= kmval*0.621371
# print("%0.1i kilometers is equal to %0.3f miles" %(kmval,chmiles))

   #Extra:-
      # name=input("Enter your name:")
      # print("You name is %1s"%(name))

# Program 13.py
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Convert Celsius To Fahrenheit $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# C=float(input("Enter your Celsius value:"))
# f=(9*C/5)+32
# print("%0.1fC = %0.1fF"%(C,f))

