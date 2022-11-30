#BCNN
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
x = min(a,b)
y = max(a,b)
k = 1
i = 1
while k!=0:
    if (x*i)%y ==0:
        k = 0
        print("BCNN=",x*i)
    else:
        i+=1