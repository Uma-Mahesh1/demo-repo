def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def abs_diff(a,b):
    return abs(sub(a,b))
def mul(a,b):
    return a*b
def div(a,b):
    try:
        return round(a/b,3)
    except:
        return ("The denominator should not be a zero")

f={1:add,2:sub,3:mul,4:div,5:abs_diff}
d={1:"add",2:"sub",3:"mul",4:"div",5:"abs_diff"}
print("what do you want to do ?")
print(d)
n=int(input(">>>"))
l=list(map(int,input("Please enter the numbers seperated by spaces").split()))
print(f[n](*l))