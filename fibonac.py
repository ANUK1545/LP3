# non recursive
def fibo(n):
    n1,n2=0,1
    print(n1,n2,end=" ")
    for i in range(2,n):
        n3=n1+n2
        print(n3,end=" ")
        n1,n2=n2,n3
    print()
fibo(7)


# ṛecursive
def fibo(i):
    if(i<=1):
        return i
    else:
        return fibo(i-1)+fibo(i-2)
n=int(input("enter a number "))
for a in range(n):
    print(fibo(a),end=" ")
