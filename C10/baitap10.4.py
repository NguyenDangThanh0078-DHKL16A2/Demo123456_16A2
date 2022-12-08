#S = (x^2+x+1)^n+(x^2-x+1)^n
import math
x = float(input('Nhập x:'))
n = float(input('Nhập n:'))
S = math.pow(math.pow(x,2)+x+1,n) + math.pow(math.pow(x,2)-x+1,n)
print(S)