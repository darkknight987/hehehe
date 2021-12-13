def gcdExtended(a, b):
    if a == 0 :
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y

a = int(input("ENTER VALUE OF A:"))
b = int(input("ENTER VALUE OF B:"))
gcd,x,y= gcdExtended(a, b)
print("GCD(",a,",",b,")=",gcd)
print("X and Y values are:",x,y)