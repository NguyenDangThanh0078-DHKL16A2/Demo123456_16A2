a = 1
b = []

while a==1:
    if a == 1:
        x = int(input('Nhập giá trị:'))
        b += [x]
    a = int(input('Tiếp tục nhập giá trị? 1: Có, 0: không '))


def xu_ly_list(b):
    d = []
    c = int(input('Nhập giá trị cần tìm: '))
    print(b)
    print('Tổng các giá trị trong list:',sum(b))
    if c in b:
        print(c,'xuất hiện',b.count(c),'lần trong list')
        if max(b) ==c:
            print(c,'lớn hơn tất cả các phần tử trong list')
        else:
            print(c,'không lớn hơn tất cả các phần tử trong list')
            for i in range(len(b)):
                if b[i] > c:
                    d = d +[b[i]]
            
    
            print('Các số lớn hơn',c,'trong list',d)
    else:
        print(c,'không xuất hiện trong list')
xu_ly_list(b)


