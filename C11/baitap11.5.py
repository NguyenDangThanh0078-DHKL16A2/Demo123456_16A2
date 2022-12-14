a = 1
b = []

while a==1:
    if a == 1:
        x = int(input('Nhập giá trị:'))
        b += [x]
    a = int(input('Tiếp tục nhập giá trị? 1: Có, 0: không '))
def xu_ly_list(b):
    b.sort
    d = []
    e = []
    f = []
    print(b)
    def check_SNT(n):
        flag = True
        if n >=0:
            if n<2:
                flag = False
            elif n ==2:
                flag = True
            elif n%2 == 0:
                flag = False
            else:
                for i in range(3,n,2):
                    if n%i ==0:
                        flag = False
        else:
            flag = False
        return flag
    for i in range(len(b)):
        if check_SNT(b[i]):
            d = d + [b[i]]
        if b[i]<0:
            e = e + [b[i]]
        else:
            f = f +[b[i]]


    print('Các số nguyên tố trong list:',d)
    print('Các phần tử âm trong list:',d)
    print('Trung bình cộng các phần tử âm:',sum(e)/len(e))
    print('Các phần tử dương trong list:',f)
    print('Trung bình cộng các phần tử dương:',sum(f)/len(f))
    print('Giá trị max trong list ',max(b))
    print('Giá trị min trong list ',min(b))
    print('List sắp tăng dần:',b)

xu_ly_list(b)