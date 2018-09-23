import math

def mysqrt(a):
    epsilon = 0.0000000000000000000000000000001
    x = 1
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return y

print(mysqrt(5))

def test_square_root():
    print('a    mysqrt(a)      math.sqrt(a)   diff')
    print('-    ---------      ------------   ----')
    for i in range(9):
        a = i+1
        b = mysqrt(a)
        c = math.sqrt(a)
        d = abs(b-c)
        print('{:.1f}  {:.11f}  {:.11f}  {}'.format(a, b, c, d))

test_square_root()