def test(i,j):
    if(i==0):
        return j
    else:
        return test(i-1,i+j)
print test(4,7)

def fun(n):
    if (n > 100):
        return n - 5
    return fun(fun(n+11));
 
print fun(45)

def a(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return a(n-1)+a(n-2)
for i in range(0,4):
    print a(i)
