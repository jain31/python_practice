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
# fact = 1
# n = int(input("Enter a number -> "))
# for i in range(1,n+1):
#     fact*=i
# print(fact)
#40 -- 1/10/2026
# n = input("Enter the string finding length")
# length = 0
# for i in n:
#     length+=1
# print(length)
#41
# a = input("ENter string first -> ")
# b = input("Enter string second -> ")
# if len(a) == len(b):
#     print("Same length")
# else:
#     print("Not")
#42
# n = input("enter a string -> ")
# v_count = 0
# c_count = 0
# for i in n:
#     if i in "aeiou":
#         v_count+=1
#     else:
#         c_count+=1
# print(v_count,c_count)
#43
# n = input("Enter a string -> ")
# r = ""
# for i in n:
#     r = i+r
# print(r)
#44
# for i in range(10,0,-1):
#     print(i)
#45
# x = input("Enter a string -> ")
# c = input("Enter the charcter which you want to count in the given string -> ")
# count = 0
# for i in x:
#     if i == c:
#         count+=1
#     else:
#         pass
# print(count)
#46
# n = input("Enter a string -> ")
# for i in range (0,len(n)):
#     print(f"{n[i]}->{i}")
#47
# a = int(input("Enter first number -> "))
# b = int(input("Enter second number -> "))

# def isprime(n):
#     if n<2:
#         return False
    
#     for i in range (2,n):
#         if n % i == 0:
#             return False
#     return True

# for x in range (a,b+1):
#     if isprime(x):
#         print(x)
#48
# a = int(input("Enter first number -> "))
# b = int(input("Enter second number -> "))
# e_sum = 0
# o_sum = 0
# for i in range(a,b+1):
#     if i % 2 == 0:
#         e_sum+=i
#     else:
#         o_sum+=i
# print(e_sum,o_sum)
#49
# for i in range(100,501):
#     if i % 11 ==0 and i%2 !=0:
#         print(i)
#50
# n =1
# while n <=10:
#     sq = n**2
#     print(f"{n}-->{sq}")
#     n+=1
#51
# n = 10
# while n<=300:
#     print(f"{n} ",end ="")
#     n+=10
#52
# n = 105
# while n >=7:
#     print(f"{n} ",end ="")
#     n-=7
#53
# n = 10
# while n>0:
#     print(n,end=" ")
#     n-=1
#54
# for i in range(2,11):
#     for j in range(2,11):
#         print(f"{i}*{j} = {i*j}")
#     print()
# 55
# i = 1
# n = int(input("enter a number which table you want -> "))
# while(i<=10):
#     print(f"{n}x{i}={n*i}")
#     i+=1
#56
# a = int(input("eneter first number -> "))
# b = int(input("Enter second number -> "))
# i = a
# while i<b:
#     if i % 2==0:
#         print(i)
#     i+=1
# print()
#57
# n = int(input("Enter a number -> "))
# i = 2
# if n<2:
#     print("Not prime")
# while i<=n:
#     if n % i ==0:
#         print("Not prime")
#         break
#     else:
#         print("Prime")
#         break
#58 fibonacci series
# n = int(input("Enter number of terms: "))
# a = 0
# b = 1
# i = 0
# while i < n:
#     print(a, end=" ")
    
#     c = a + b
#     a = b
#     b = c    
#     i = i + 1
#59
# n = int(input("Enter a number -> "))
# fact = 1
# i = 1
# while i<=n:
#     fact = fact * i
#     i+=1
# print(fact)
#60
# num = int(input("Enter a number: "))

# original = num
# sum = 0

# while num > 0:
#     digit = num % 10
#     sum = sum + digit ** 3
#     num = num // 10

# if sum == original:
#     print("Armstrong")
# else:
#     print("Not Armstrong")
#88
# n = input("Enter a string -> ")
# dict ={}
# for i in n:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)
#89
# n = int(input("Enter the number of elements -> "))
# l = []
# for i in range(1,n+1):
#     e = int(input(f"Enter elements {i} -> "))
#     l.append(e)
# print(l)
#90
# n = int(input("Enter the number of elements -> "))
# l =[]
# for j in range(n):
#     e = int(input("Enter elements -> "))
#     l.append(e)
# print(f"all elements of list -> {l}")
# el = []
# for i in l:
#     if i % 2 == 0:
#         el.append(i)
# print(f"only even elements are shown -> {el}")
#91
# n = int(input("Enter size of list -> "))
# l = []
# i = 1
# for i in range (n):
#     e = int(input(f"Enter the elements of the list {i} -> "))
#     l.append(e)
# print(l)
# ol = []
# for i in l:
#     if i % 2 !=0:
#         ol.append(i)
# print(ol)
#92
# n = int(input("Enter the size of the list -> "))
# l = []
# for i in range(1,n+1):
#     e = int(input(f"enter the element {i}-> "))
#     l.append(e)
# print(f"list -> {l}" )
# el = []
# el_sum = 0
# for i in l:
#     if i % 2 == 0:
#         el.append(i)
# print(f"even list -> {el}")
# for i in el:
#     el_sum+=i
# print(f"sum of even numbers - > {el_sum}")
# ol=[]
# ol_sum=0
# for i in l:
#     if i%2 !=0:
#         ol.append(i)
# print(f"odd number list ->{ol}")
# for i in ol:
#     ol_sum+=i
# print(f"odd sum -> {ol_sum}")
#93
# l =[]
# n =int(input("Enter the size of list -> "))
# for i in range(1,n+1):
#     e = input(f"Enter the {i} items of list -> ")
#     l.append(e)
# print(f"list of all the items -> {l}")
# d = {}
# for i in l:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(f"frequency of the items of the list -> {d}")
#94
# l = []
# n = int(input("Enter the size of list -> "))
# for i in range(n):
#     e = int(input("Enter element -> "))
#     l.append(e)
# print(f"list -> {l}")

# max_val =l[0]

# for i in l:
#     if i>max_val:
#         max_val = i
# print(max_val)
#95
# min_val=l[0]
# for i in l:
#     if i<min_val:
#         min_val = i
# print(min_val)
#96
#97
#98 --- for-else concept
# l = [3,2,5,12]
# pl =[]
# for i in l:
#     if i > 1:
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else:
#             pl.append(i)
# print(pl)
#99
# n = int(input("Enter the size of the list -> "))
# l=[]
# for i in range(1,n+1):
#     e = int(input("Enter elements -> "))
#     l.append(e)
# print(f"list - > {l}")
# ecount=0
# ocount=0
# for i in l:
#     if i %2 ==0:
#         ecount+=1
#     else:
#         ocount+=1
# print(ecount,ocount)
#100
# s = input("Enter a string -> ")
# r = s[::-1]
# print(r)
#101
# s = input("Enter a string -> ")
# d = {}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
#102
# def sum(a,b,c):
#     return a+b+c
# print(sum(2,3,4))
#103
# n = int(input("Enter any number -> "))
# def even(n):
#     if n % 2 ==0:
#         return "even"
#     else:
#         return "odd"
# print(even(n))
#104
# def sum(s):
#     for i in range(1,11):
#         s+=i
#     return s
# print(sum(0))
#105
# def eocount(ecount,ocount):
#     for i in range(1,12):
#         if i % 2==0:
#             ecount+=1
#         else:
#             ocount+=1
#     return ecount,ocount
# print(eocount(ecount=0,ocount=0))
#106
# def sum(esum,osum):
#     for i in range(1,11):
#         if i % 2==0:
#             esum+=i
#         else:
#             osum+=i
#     return esum,osum
# print(sum(esum =0,osum=0))
#107--3/10/2026
# def table(n):
#     for i in range(1,11):
#        print (f"{i} * {n} = {i*n}")
# table(2)
#108
# n = int(input("Enter any integer number -> "))
# def factorial(n):
#     fact = 1
#     i = 1
#     for i in range(1,n+1):
#         fact = fact* i
#     return fact
# print(factorial(n))
#bonus --- while else
# attempts = 0

# while attempts < 3:
#     password = input("Enter password: ")
#     if password == "secret":
#         print("Access granted!")
#         break  # Skips the else block
#     attempts += 1
# else:
#     print("Account locked. Too many failed attempts.")  # Runs if loop completes without break
#109
# def isprime(n):
#     if n>1:
#         for i in range(2,n+1):
#             if  n % i != 0:
#                 return " prime"
#             else:
#                 return "not prime"
# print(isprime(7))
#110
# n = int(input("Enter the size of the list -> "))
# l = []
# for i in range (1,n+1):
#     e = int(input("Enter element -> "))
#     l.append(e)
# print(l)
# for i in range (len(l)):
#     temp = l[0]
#     l[0]=l[-1]
#     l[-1]=temp
# print(l)
#111
# l = [2,3,4,5,6,7,8,9,0]
# def swap(l,n1,n2):
#     for i in range (len(l)):
#         temp = l[n1]
#         l[n1] = l[n2]
#         l[n2] = temp
#     return l
# print(swap(l,2,0))
#112
#113#114
'''already done'''
#115
# n = int(input("Enter the size of the list -> "))
# l = []
# for i in range(1,n+1):
#     e = int(input(f"enter {i} element -> "))
#     l.append(e)
# print(l)
# item = int(input("Enter the element which you want to find -> "))
# for i in range(len(l)):
#     if item == i:
#         print(f"found {i} at index {l[i]}")
#         break
#     else:
#         continue
#116
# l = [0,1,2,3,2,21,11,22,5]
# print(l)
# l.clear()
# print(l)
#117
# l.reverse()
# print(l)
#118
# l1 = l.copy()
# print(l1)        
#119
# n = int(input("Enter the size of list = "))
# l = []
# for i in range(n):
#     e = input(f"Enter {i} element -> ")
#     l.append(e)
# print(l)
# d ={}
# for i in l:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
#120
# n = int(input("Enter the size of list = "))
# l = []
# for i in range(n):
#     e = int(input(f"Enter {i} element -> "))
#     l.append(e)
# print(l)
# sum = 0
# for i in l:
#     sum+=i
# print(f"Sum of the elements of the list = {sum}")
# avg = sum/len(l)
# print(f"average of the list = {avg}"))
#121#122
'''done'''
#123 --min
# l = [23,4,2,22,1,9] 
# min_num = l[0]
# for i in range(len(l)):
#     if l[i]<min_num:
#         min_num=l[i]
# print(f"{min_num} is smallest number")
#124
# l = [23,4,2,22,1,9] 
# max_num = l[0]
# for i in range(len(l)):
#     if l[i]>max_num:
#         max_num=l[i]
# print(f"{max_num} is largest number")
#125 to #132 -- 
'''done'''
#133
# l=[0,1,22,33,22,1]
# l.remove(33)
# print(l)

#dictionary

# data = {"a": 100, "b": 200, "c": 300}

# # 1. Loop over keys (default)
# for key in data:
#     print(key, "->", data[key])

# # 2. Loop over values directly
# for val in data.values():
#     print(val)

# # 3. Loop over both keys and values using .items()
# for key, val in data.items():
#     print(f"Key: {key}, Value: {val}")

#134
# n = int(input("Enter the size of the dictionary -> "))
# d ={}
# for i in range(n):
#     val = int(input(f"Enter valuse {i} of the dict -> "))
#     d[i]= val
# print(d)
# x = sorted(d.values())
# print(x)
#135
# x = {"name": "Kashish","gender":"female"}
# print(x)
# x.update({"age":"21"})
# print(x)
#136 (a)
# d = {'name': 'Kashish', 'gender': 'female', 'age': '21'}
# n = input("keys find -> ")
# if n in d.keys():
#     print("exist")
# else:
#     print("not")
#(b)
# item = input("Enter item -> ")
# for i in d.values():
#     if i == item:
#         print("exists")
#         break
# else:
#     print("not")
#137
# d = {}
# n = int(input("Enter the size of dictinary -> "))
# for i in range(1, n+1):
#     d[i]=i**2
# print(d)
#138
# cube_dict={}
# while True:
#     n = int(input("Enter an integer and 0 for exit = "))
#     if n == 0:
#         break

#     cube_dict[n] = n **3
# print(cube_dict)
#139
# n = input("Enter the string ->  ")
# d = {}
# for i in n:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
#tuple
#140
# t =(1,2,3,7,5,6,8,9,10,4)
# sum = 0
# for i in t:
#     sum+=i
# print(sum)
#141 ------------------------dry run ------------
# t = (2,3,4,5,6)
# max_t = t[0]
# second_max_t = t[0]
# for i in range(len(t)):
#     if t[i]>max_t:
#         second_max_t = max_t
#         max_t = t[i]
#     elif t[i]>second_max_t and t[i]!= max_t:
#         second_max_t=t[i]
# print(max_t,second_max_t)
#142---------5/10/2026--------
# t = (5,6,7,8,9,0)
# print(t)
# l = list(t)
# print(l)
#143
# l=[0,9,87,686,99]
# print(l)
# t = tuple(l)
# print(t)
#---------recursion----------
#144
# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(n=5))

#145
# def fib(n):
#     if n<=1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# n = 5
# for i in range(n+1):
#     print(fib(i),end=" ")
#146
# l1 = [2,3,4,5,6,7]
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]+l1[j]==9:
#             print(l1[i],l1[j])
#147
# s = "myselfkashishjain"
# if (len(s)<11):
#     print(s)
# else:
#     print(s[0:10],"....")

#148
# l1 = [1,2,3,4,5,6,7,8,9,0]
# l2 = [1,2,3,4,5,6,7,8,9,0]
# sum = []
# for i in range(len(l1)):
#     sum.append(l1[i]+l2[i])
# print(sum)

 #149
# r = int(input("Enter the number of row -> "))
# c = int(input("Enter the number of column -> "))
# l =[]
# for i in range(r):
#     k =[]
#     for j in range(c):
#         e = int(input("Enter the element -> "))
#         k.append(e)
#     l.append(k)
# print(l)

# for i in range(len(l)):
#     for j in range(len(l[i])):
#         print(l[i][j],end=" ")
#     print()
#150
# r = int(input("Enter the number of row -> "))
# c = int(input("Enter the number of columns -> "))
# l = []
# for i in range(r):
#     k =[]
#     for j in range(c):
#         e = int(input("Enter the elements -> "))
#         k.append(e)
#     l.append(k)
# print(l)
# sum = 0
# for i in range(len(l)):
#     for j in range(len(l)):
#         sum+=l[i][j]
# print(f"sum of all elements of the given list = {sum}")
#151
# r = int(input("Enter the row -> "))
# c = int(input("Enter the column -> "))
# l =[]
# for i in range(r):
#     k =[]
#     for j in range(c):
#         e = int(input("Enter the elements -> "))
#         k.append(e)
#     l.append(k)
# print(l)

# prod = 1
# for i in range(len(l)):
#     for j in range(len(l)):
#         prod*=l[i][j]
# print(prod)
#152 -------binary search ----------
# l = []
# n = int(input("Enter the size of the list -> "))
# for i in range(1,n+1):
#     e = int(input(f"Enter the {i} element -> "))
#     l.append(e)
# print(l)
# l.sort()
# print(f"after sorting the elements -> {l}")

# item = int(input("enter the element which you want to search -> "))
# low = 0
# high = len(l)-1
# while(low<=high):
#     mid = (high+low)//2
#     if item == l[mid]:
#         print(f"{item} found at index {mid}")
#         break
#     elif item > l[mid]:
#         low = mid+1
#     elif item<l[mid]:
#         high = mid -1














    


