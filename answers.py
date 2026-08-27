#1.wap to add,sub,multi,divide in a single program 
a = int(input("Enter first number -> "))
b = int(input("Enter second number -> "))
print("choose following for the calculation\n")
print("1 for sum\n2 for sub\n3 for product\n4 for divide")
x = int(input("Enter any above options -> "))
if x == 1:
    print (a+b)
elif x==2:
    print(a-b)
elif x==3:
    print(a*b)
elif x==4:
    print(a/b)
else:
    print("invalid option")

print("calculation done")