def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("enter a number:"))
result=factorial(num)
print("f the factorial of{num}is {result}")