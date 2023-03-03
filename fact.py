def fac(n):
    if n<0:
        return "Please enter a positive number"
    elif n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)

print("Please enter the number")
n=int(input(">>>"))
print(fac(n))
