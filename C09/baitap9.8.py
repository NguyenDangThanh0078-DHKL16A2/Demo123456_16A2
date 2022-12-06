#hàm kiểm tra số hoàn hảo
n = int(input('Nhập số:'))
def kiem_tra_so_hoan_hao(n):
    s=0
    for i in range(1,n+1):
        if n%i ==0:
            s += 1/i
    if s==2:
        print(n,'là số hoàn hảo!')
    else:
        print(n,'không phải là số hoàn hảo')

kiem_tra_so_hoan_hao(n)