
#     ~~~~~~~~~~~~~~~~~~~~~~~~~ Operators, Experssion and Python Statements  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("Welcome python chapter-4")

# 4.1 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Assignment Statement $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# val= 20
# a=b=c=20
# name,age,achivement="DGukesh",18,"Youngest World Chess Champian"
# print("name:",name)
# print("Age:",age)
# print("Achivement:",achivement)

# print("val+=10 =",val+10)
# print("val-=10 =",val-10)
# print("val*=10 =",val*10)
# print("val/=10 =",val/10)     # This is store float value
# print("val//=10 =",val//10)   # This is store only integer value
# print("val%=10 =",val%10)  
# print("val**=3 =",val**3)  
# print("val^=3 =",val^10)  #  
# print("val&=3 =",val&10)  #
# print("val|=3 =",val|10)  #


# 4.3 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Arithmetic $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# print("Hello"+"3")  
# print("Hello"+3)    # python cannot concatenate a strig with integer
# print(3+30)           # addition hoga kunki dono integer hai lekin agar dono string hota to concatenate ho jata 

# a= int(input("Enter the first value:"))
# b= int(input("Enter the second value:"))
# print("1. Addition of two numbers {} and {}: {}".format(a,b,a+b))
# print("2. Subtracting numbers {} from {}: {}".format(a,b,a-b))
# print("3. Multiplication of two numbers {} and {}: {}".format(a,b,a*b))
# print("4. Divison of two numbers {} and {}: {} in float".format(a,b,a/b))
# print("5. Divison of two numbers {} and {}: {} in int".format(a,b,a//b))
# print("6. Exponent of two numbers {} and {}: {} ".format(a,b,a**b))
# print("6. Modulus of two numbers {} and {}: {} ".format(a,b,a%b))


# print("Hello"*"3")  
# print("Hello"*3)    # python can repeat a strig with integer
# print(3*30)           # multipy hoga kunki dono integer hai lekin agar dono string hoga to error dega

# 4.4 $$$$$$$$$$$$$$$$$$$$$$$$$$$$  Relational operator or Camparision Operator  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# a=200
# b=79
# print("a<b=",a<b)
# print("a>b=",a>b)
# print("a<=b=",a<=b)
# print("a>=b=",a>=b)
# print("a==b=",a==b)
# print("a!=b=",a!=b)

# print(ord("a"))     #ord() => change character into ASCII value
# print(chr(190))    # chr() => change ASCII value into character

# a=20
# print(a>True)   # Here, True => 1 , False => 0 , so 10>1=True
# print(a<True)
# print(40<=a<=60)

# a=[1,2,3]
# b=[1,2,3]
# print(id(a))
# print(id(b))
# print("a==b:",a==b)
# print("a is b:",a is b)     # because '==' is compare values but 'is' operator compare memory address

# 4.5 $$$$$$$$$$$$$$$$$$$$$$$$$$$$  Logical Operator  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 4.6 $$$$$$$$$$$$$$$$$$$$$$$$$$$$  Bitwise operators and their precedence  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 
# a=12
# b=10
# print(bin(6))
# print(bin(b))
# print("a&b:",a&b)     # agar dono bit 1 hai to 1 prit hoga varna 0 print hoga
# print("a|b",a|b)      # agar dono mi se kisi ke pass 1 to 1 print kar do varna 0 print kar do (jab dono 0 ho to 0 print hoga)
# print("a^b",a^b)      # agar dono same hai to 0 print hoga lakin jab dono differet hoga to 1 print hoga (same same =0 but different= 1)
# print("5 << 2:",5 << 1)     # 5 binary: 00000101 "<<" matlab left  side me 0 add karna hota hai so, 00010100
# print("6 >> 2:",6 >> 2)     # 6 binary: 00000110 "<<" matlab right side me 0 aur 1 sub karna hota hai so, 00000001
 
# print("5-3+3:",5-3+3)   # same presedece hai isle left to right evaluate hoga
# print(2**3**2)  # note:- exponent is the only opertor in the same presedence jo right to left evaluate  karta hai 


# 4.7 $$$$$$$$$$$$$$$$$$$$$$$$$$$$  Conditional Statements  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# # ________ Example 1 _____________
# x=int(input(("Enter the x value")))

# if x<4:
#   print("x is less than 4")
# else:
#   print("x is greater than 4")

# # ________ Example 3 _____________
# x=int(input(("Enter the x value")))
# if x>0:
#   print("This is first line")
#   print("This is second line")
#   print(".........")
#   print("End")
# print("After if block")

# # ________ Example 4 _____________
# x=int(input(("Enter the x value")))
# if x>0:
#   print(" +Ve Value")
#   print("This is first block")
# if x<0:
#   print(" -Ve Value")
#   print("This is second block")

# # ________ Example 5 _____________
# x=input(("Enter the name"))
# if x=="VPrachi":
#   print("heloo",x)
#   print("Welcome")
# print("How are you .........",x)

# 4.7.2 # ________ Example 1 _____________
# x=int(input(("Enter the number")))
# if x>0:
#   print("This is positive number +Ve")
# else:
#   print("This is Negative number -Ve")

# ----Example 2----&&&&&&&&& Find the Biggest value of given 2 numbers from the command line.
# x=int(input(("Enter the first number")))
# y=int(input(("Enter the second number")))
# if x>y:
#   print("This is the bigget value between {0} and {1}={0}".format(x,y))
# else:
#   print("This is the bigget value between {0} and {1}={1}".format(x,y))


# 4.7.2 # ________ Example 3 _____________
# x=int(input(("Enter the first number")))
# y=int(input(("Enter the second number")))
# print("This is the bigget value ={0}".format(x,y)) if x>y else print("This is the bigget {1}".format(x,y))

# ----Example 4----&&&&&&&&& Find the given number is even or odd.
# x=int(input(("Enter the number")))
# if x%2==0:
#   print("This is even number")
# else:
#   print("This is odd number")
# This is short hand rule:-
# print("This is even number") if x%2==0 else print("This is odd number")

# 4.7.3 #----Example 1---- &&&& Find Biggest value of given 3 numbers from the command line.
# a=int(input("Enter the first numbers"))
# b=int(input("Enter the second numbers"))
# c=int(input("Enter the third numbers"))
# if((a<b)&(b>c)):
#   print("{1} is greater than {0} and {2}".format(a,b,c))
# elif(c<a):
#   print("{0} is greater than {1} and {2}".format(a,b,c))
# else:
#   print("{2} is greater than {0} and {1}".format(a,b,c))

# 4.7.3 #----Example 2---- &&&& Program to find given value is Positive or negative or equal to zero.

# a=int(input("Enter your numbers:"))
# if(a>0):
#   print("Number is Positive.")
# elif a<0:
#   print("Number is Negative")
# else:
#   print("Numerb is zero")


#4.7.3 #----Example 3---- &&&& Program to find given value is Positive or negative or equal to zero.

# a=int(input("Enter your grade:"))
# if(a>=90):
#   print("Your grade is A+")
# elif(90>a>=80):
#   print("Your grade is A")
# elif(80>a>=70):
#   print("Your grade is B")
# elif(70>a>=60):
#   print("Your grade is C")
# else:
#   print("Fail")

#4.7.3 #----Example 4---- &&&& Program to find your grade according to following condition.

# a=int(input("Enter Your Grade:"))
# if(a>=90):
#   print("Your grade is A+")
# else:
#   if(a>=80):
#     print("Your grade is A")
#   else:
#     if(a>=70):
#       print("Your grade is B")
#     else:
#       if(a>=60):
#         print("Your grade is C")
#       else:
#         print("FAIL")

#4.7.3 #----Example 5---- &&&& Program to find given year is leap year or not.

# a=int(input("Enter your Year"))
# if(a%4==0):
#   if(a%100==0):
#     if(a%400==0):
#         print("Year {} is a leap year".format(a))
#   else:
#     print("Year {} is not a leap year".format(a))
# else:
#   print("Year {} is not a leap year".format(a))

#4.8 #----Example 1---- &&&& Program to print 1 to 5 natural numbers.

# count=0
# while count<=5:
#   print(count)
#   count=count+1

#4.8 #----Example 2---- &&&& Program to print sum of n natural numbers (sum=1+2+3+...+n)

# num=int(input("Enter the number"))
# count=0
# sum=0
# while count<=num:
#   sum=count+sum
#   count=count+1
# print("The sum of {} natural number is {}".format(num,sum))

#4.8 #----Example 3---- &&&& Program to find sum of all even and odd numbers up to specified number.

# num=int(input("Enter the number"))
# even=0
# odd=0
# sum=0
# while (sum<=num):
#   if (sum%2==0):
#     even=even+sum
#   if (sum%2!=0):
#     odd=odd+sum
#   sum=sum+1
# print("The sum of even natural numbers is:",even)
# print("The sum of odd natural numbers is:",odd)

#4.8 #----Example 4---- &&&& Program to find factorial of any input number.

# num=int(input("Enter the number"))
# count=1
# fac=1
# while count<=num:
#   fac=count*fac
#   count=count+1
# print("The factorial of {} natural number is {}".format(num,fac))

#4.8 #----Example 5---- &&&& Program to input any number from the keyboard and check it number is palindrome or not

# num=int(input("Enter you palidrome number:"))
# n=num
# rev=0
# while num:
#   pro=num%10
#   rev=rev*10+pro
#   num=num//10
# if(n==rev):
#   print("This number is palindrome")
# else:
#   print("This number is not a palindrome")

#4.8.1 --Example 6- This will print the woed 'hello' indefinitely because the condition will always be true.
# while True:
#   print("hello prachi")
# for exit short cut is Ctrl+C

#4.8.1 --Example 7- This will print the word 1 indefinitely becaues the codition will always be true.
# num=1
# while num<2:
#   print(num)

#4.8.1 --Example 8- Program will print the pattern as shown in the output.

# i=0
# while i<=3:
#   j=0
#   while j<=4:
#     print(j*i,end=" ")
#     j+=1
#   print()
#   i+=1
  
#4.8.2 --Example 9-Program to use While loop with statement in one line.
# i=0
# while i<=6:i+=1; print("🙏 Namaste Bharat!")    # while condition:incre/decre;statement

#4.8.3 --Example 10- print 1 to 5 Number by using While with else claues.
# i=0
# while i<=5:
#   print(i)
#   i+=1
# else:
#   print("This loop is finished")

#4.8.3 --Example 11- print 10 to 6 Number by using Wjhile with else clause.
# x=10
# while x>5:
#   print("value of x is:",x)
#   x-=1 
# else:
#   print("value of x is less than 5 so this loop is finished.")

# -------------------- 4.9 --------- For loop ----------------------------------------------------
#4.9 --Example 1- Program to print characters present in the given string.
# str='VPrachi'
# for i in str:
#   print(i)

#4.9 --Example 2- Program to display the use of 'for' Loop with string,List and Tuple Dictionary Iteration.
# ----------------- For loop using strings ----------------------
# print("*"*70)
# print("\t \t For loop using strings")
# str='DGukesh'
# for i in str:
#   print(i)
# # ----------------- For loop using List ----------------------
# print("*"*70)
# print("\t \t For loop using List")
# lst=['VAnand','DGukesh','VPrachi','RPraggnanandhaa']
# for i in lst:
#   print(i)

# # ----------------- For loop using Tuple ----------------------
# print("*"*70)
# print("\t \t For loop using List")
# tup=("Indore","Surat","Navi Mumbai","Ahmedabad","Bhopal")
# for i in tup:
#   print(i)

#4.9 --Example 3- Program to print characters present in string index wise.
# strn="VPrachi"
# n=0
# for i in strn:
#   print("{} is a index of {}".format(n,i))
#   n+=1

#4.9 --Example 4- Using only one argument in range().
# for i in range(6):
#   print(i,end=" ")

#4.9 --Example 5- Using two arguments in range().
# for i in range(5,16):
#   print(i,end=" ")

#4.9 --Example 6- Using three arguments in range() function. Printing all odd numbers between 1 to 100 using range()
# for i in range(1,100,2):
#   print(i, end=" ")

#4.9 --Example 7- Program to print sum of even number series up to 10
# sum=0
# for i in range(0,11,2):
#   sum=sum+i
# print("Total of 10 even numbers:",sum)

#4.9 --Example 8- Program to display the use of Nested for loop
# for i in range(6):
#   for j in range(1,2):
#     print("This is j",j)
#   print("This is i",i)
#   print("*"*4)
#4.9 --Example 9- program to display the pattern as shown in the below figure



