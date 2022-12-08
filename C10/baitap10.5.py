#kiểm tra mã zip
def kiem_tra_ma_zip(n):
    flag = True
    if str(n).isdigit() == False:
            flag = False 
    if len(str(n)) != 6:
        flag = False
    print(flag)
    


n = input('Nhập vào mã zip:')
kiem_tra_ma_zip(n)
