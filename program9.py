subject1=float(input("Enter the marks of subject1"))
subject2=float(input("Enter the marks of subject2"))
subject3=float(input("Enter the marks of subject3"))
subject4=float(input("Enter the marks of subject4"))
subject5=float(input("Enter the marks of subject5"))
sum=subject1+subject2+subject3+subject4+subject5
mean=sum/5
p=sum/500*100
print("The mean is",mean)
print("The percentage is ",p)
if p<35:
    print("fail")
else:
    print("pass")
