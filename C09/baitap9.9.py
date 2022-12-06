import math
r = eval(input('Nhập bán kính:'))
a = eval(input('Nhập chiều dài'))
b = eval(input('Nhập chiều rộng'))
S_tron = lambda r: r*r*math.pi
P_tron = lambda r: 2*r*math.pi
S_hcn = lambda a,b: a*b
P_hcn = lambda a,b: 2*(a+b)

print('S,P hình tròn:',S_tron(r),',',P_tron(r))
print('S,P hình chữ nhật',S_hcn(a,b),',',P_hcn(a,b))
