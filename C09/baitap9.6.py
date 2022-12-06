#Kiểm tra số nguyên tố
n = int(input('nhập số nguyên:'))
if n>=0:
    def kiem_tra_so_nguyen_to(n):
        flag = True
        if n<2:
            flag = False
        elif n==2:
            flag = True
        elif n%2==0:
            flag = False
        else:
            for i in range(3,n,2):
                if n%i==0:
                    flag = False
        return flag
    print(kiem_tra_so_nguyen_to(n))
else:
    print('đây là số âm, ngu lắm')

    