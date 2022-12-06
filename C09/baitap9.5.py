#S = (x^2=x+1)^n+(x^2-x+1)^n
x = eval(input('Nhập giá trị của x:'))
n = eval(input('Nhập giá trị cảu n:'))
def tinh_A(x,n):
    A = (x*x+x+1)**n+(x*x-x+1)**n
    return A
print("A=",tinh_A(x,n))