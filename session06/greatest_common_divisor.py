def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(2,12),
gcd(6,12),
gcd(9,12),
gcd(17,12))