#tìm UCLN
a = int(input("Nhập a:"))
b = int(input("Nhập b:"))
y = max(a,b)
x = min(a,b) 
k = 1
while k!=0:
    if y%x == 0:
        print("UCLN:",x)
        k = 0
    else:
        x = y%x
        y = x




