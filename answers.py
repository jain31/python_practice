#1.

# a = int(input("Enter first number -> "))
# b = int(input("Enter second number -> "))
# print("choose following for the calculation\n")
# print("1 for sum\n2 for sub\n3 for product\n4 for divide")
# x = int(input("Enter any above options -> "))
# if x == 1:
#     print (a+b)
# elif x==2:
#     print(a-b)
# elif x==3:
#     print(a*b)
# elif x==4:
#     print(a/b)
# else:
#     print("invalid option")

# print("calculation done")

#2. 

# a = int(input("Enter first number -> "))
# b = int(input("Enter second number -> "))
# print ("--before swapping--")
# print(f"a =",a,"b =",b)
# c = a
# a = b
# b = c
# print("--after swapping--")
# print(f"a =",a,"b =",b)

#3.

# a = int(input("Enter first number -> "))
# b = int(input("Enter second number -> "))
# print ("--before swapping--")
# print(f"a =",a,"b =",b)
# a,b = b, a
# print("--after swapping--")
# print(f"a =",a,"b =",b)

#4.

# a = int(input("Enter a number -> "))
# if a%2 ==0:
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")

#5.

# a = int(input("Enter first number -> "))
# b = int(input("Enter second number -> "))
# c = int(input("Enter third number -> "))
# if a<b:
#     if c<b:
#         print(f"{b} is greatest number")
#     elif b<c:
#         print(f"{c} is greatest number")
# elif b<a:
#         if c<a:
#             print(f"{a} is greatest number")
#         elif b<c:
#             print(f"{c} is greatest number")
# else:
#      print(f"number")

# 6.
# x = int(input("Enter any percentage -> "))
# if x>= 90:
#     print("A grade")
# elif x>80 & x<=90:
#     print("B grade")
# elif x>=60 & x<=80:
#     print("C grade")
# else:
#     print("D grade")

# 7.
# x = int(input("Enter any cp -> "))
# if x>100000:
#     print("tax = 15%")
# elif x>50000:
#     print("tax = 10%")
# else:
#     print("tax = 5%")

#8.
# x = int(input("Enter the working day of the man = "))
# y = int(input("Enter the per day income = "))
# sal = x*y
# print(f"salary of the man = {sal}")

# #9.
# t = int(input("Enter your time period"))
# sal = int(input("Enter your salary"))
# bonus = 0
# if t>10:
#     bonus = 10*sal/100
# elif t>=6 and t<=10:
#     bonus = 8*sal/100
# else:
#     bonus = 5*sal/100
# print(f"bonus = {bonus}")

#10 

# while True:
#     a = int(input("Enter the first number"))
#     b = int(input("Enter the second number")) 
#     op = input("Enter the operator = +,-,/,* = ")
#     if op == "+":
#         answer = a+b
#     elif op == "-":
#         answer = a-b
#     elif op == "/":
#         answer = a/b
#     elif op == "*":
#         answer = a*b
#     else:
#         print("invalid option")

#     print(f"final output = {answer}")
#     x = input("Enter 0 to end the program -> ")
#     if x == 0:
#         break
#     else:
#         continue
# 11
# for i in range(1,11):
#     print(i)
# 12
# for i in range(1,11):
#     if i%2 == 0:
#         print(i)
#13
# for i in range(1,11):
#     if i%2 != 0:
#         print(i)
#14 -- 30/09/2026
sum = 0
# for i in range(1,11):
#     sum += i
# print(sum)
#15
# sum = 0
# for i in range(1,11):
#     if i%2 == 0:
#         sum+=i
# print(sum)
#16
# sum = 0
# for i in range(1,11):
#     if i%2 != 0:
#         sum+=i
# print(sum)
#17
# e_sum = 0
# o_sum = 0
# for i in range(1,11):
#     if i%2 == 0:
#         e_sum+=i
#     else:
#         o_sum+=i
# print(f"sum of even = {e_sum}, odd sum = {o_sum}")
#18
# num = int(input("Enter a number -> "))
# sum = 0
# while num >0 :
#     digit = num%10
#     num = num//10
#     sum += digit
# print(sum)
#19
# num = int(input("Enter a number -> "))
# # while num >0:
# digit = num % 10
# print(digit)
#20
# year = int(input("Enter a year -> "))
# if year % 400 == 0 or (year % 4 == 0 and year % 100!= 0):
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")
#21
# num = int(input("Enter a number -> "))
# if num < 2:
#     print("Not prime")
# for i in range (2,num):
#     if num % i == 0:
#         print("Not Prime")
#         break
#     else:
#         print("prime")
#         break
#22
# char = input("Enter a charcter -> ")
# if char in "aeiou":
#     print("vowel")
# else:
#     print("not")
#23

# units = int(input("Enter number of units -> "))
# amt = 0

# if units<=100:
#     amt = 0
# elif units> 100 and units<=300:
#     amt = (units - 100)*2
# elif units>300:
#     amt = 0+(200*2)+((units-300)*5)
# else:
#     print("confused")
# print(amt)
#26
# num = int(input("Enter a number"))
# sum = 0
# while num > 0:
#     digit = num % 10
#     sq = digit**2
#     sum+= sq
#     num=num//10
# print(sum)
# 27
# num = int(input("Enter a number"))
# sum = 0
# while num>0:
#     digit = num%10
#     cu = digit**3
#     sum+=cu
#     num=num//10
# print(sum)
# 28
# num = int(input("Enter a number"))
# prod = 1
# while num>0:
#     digit = num%10
#     prod*=digit
#     num = num//10
# print(prod)
# 29
# num = int(input("Enter a number"))
# rev = 0
# while num>0:
#     digit = num%10
#     rev = rev*10 + digit
#     num = num//10
# print(rev)
# 30 palindrome
# num = int(input("Enter a number -> "))
# n = num
# rev = 0
# while num >0:
#     digit = num%10
#     rev = rev*10+digit
#     num=num//10
# print(rev)
# if n == rev:
#     print(f"{n} is palindrome ")
# else:
#     print("Not")
#31 armstrong
# num = int(input("Enter a number -> "))
# n = num
# cu = 1
# while num>0:
#     digit = num%10
#     cu = digit**3
#     sum += cu
#     num = num//10
# if sum==n:
#     print("Armstrong")
# else:
#     print("not")
 #32
# i = 1
# while i<=10:
#     print(i)
#     i+=1
#33
# i = 1
# while i <=10:
#     if i%2==0:
#         print(i)
#     i+=1
#34
# i = 1
# while i<=10:
#     if i %2!=0:
#         print(i)
#     i+=1
#35
# sum = 0
# i=1
# while i<=10:
#     sum+=i
#     i+=1
# print(sum)
#36
# sum=0
# i=1
# while i<=10:
#     if i%2==0:
#         sum+=i
#     i+=1
# print(sum)
#37
# sum=0
# i =1
# while i<=10:
#     if i%2!=0:
#         sum+=i
#     i+=1
# print(sum)
#38
# i = 1
# esum =0
# osum=0
# while i<=10:
#     if i%2==0:
#         esum+=i
#     else:
#         osum+=i
#     i+=1
# print(esum,osum)
#39 factorial
fact = 1
n = int(input("Enter a number -> "))
for i in range(1,n+1):
    fact*=i
print(fact)
