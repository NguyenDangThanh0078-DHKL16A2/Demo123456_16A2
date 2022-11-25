import math
a = eval(input("Nhập cạnh a:"))
b = eval(input("Nhập cạnh b:"))
c = eval(input("Nhập cạnh c:"))
if (a+b)<c or (a+c)<b or (a+c)<b:
    print("Đây không phải là tam giác")
p = (a+b+c)/2
print("Diện tích tam giác là S=",math.sqrt(p*(p-a)*(p-b)*(p-c)))