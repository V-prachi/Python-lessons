
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