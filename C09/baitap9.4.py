#S = (x^2+1)^n
x = eval(input('Nhập giá trị của x:'))
n = eval(input('Nhập giá trị của n '))
def tinh_S(x,n):
    S= (x*x+1)**n
    return S
print('S=',tinh_S(x,n))