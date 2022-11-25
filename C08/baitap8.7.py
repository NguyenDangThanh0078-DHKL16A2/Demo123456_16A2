n = eval(input("Nhập số Kwh:"))
b = 0
for i in range(0,n):
    if i <= 50:
        b += 1.678
    if 100 >= i > 50:
        b += 1.734
    if 200 >= i > 100:
        b += 2.014
    if 300 >= i > 200:
        b += 2.536
    if 400 >= i > 300:
        b += 2.834
    if i > 400:
        b +=2.927
print("Số tiền điện phải trả là:",b)
