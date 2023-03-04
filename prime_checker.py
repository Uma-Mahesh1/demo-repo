from primePy import primes
print("please enter a number")
n=int(input(">>>"))
if primes.check(n):
    print("The number is a Prime Number")
else:
    print("The number is not a prime number")