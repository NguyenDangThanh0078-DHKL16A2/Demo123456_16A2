n = int(input("Nhập số: "))
S = 0
for i in range(2,n+1):
    if n%i ==0:
        S+=n/i
if S == n:
    print(n,"là số hoàn hảo!")
else:
    print(n,"không là số hoàn hảo.")
