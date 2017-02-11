p=int(input("Enter the principle amount"))
t=int(input("Enter the time"))
r=int(input("Enter the interest rate"))
n=int(input("The number of values"))
ci=p+(1+r/n)**n*t
print("The compound interest is",ci)
