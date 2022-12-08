
d = int(input('Nhập ngày: '))
m = int(input('Nhập tháng: '))
y = int(input('Nhập năm: '))

def time(d,m,y):
    from datetime import datetime
    import calendar
    ngay_thang_nam = datetime(y,m,d)

    a = ngay_thang_nam.strftime('%d-%m-%Y')
    print('Ngày tháng năm vừa nhập:',a)

    b = calendar.weekday(y,m,d)
    if b == 0:
        print(a,'là Thứ Hai')
    elif b == 1:
        print(a,'là Thứ Ba')
    elif b == 2 :
        print(a,'là Thứ Tư')
    elif b == 3 :
        print(a,'là Thứ Năm')
    elif b == 4:
        print(a,'là Thứ Sáu')
    elif b == 5:
        print(a,'là Thứ Bảy')
    else:
        print(a,'là Chủ Nhật')

    if calendar.isleap(y):
        print('Năm',y,'là năm nhuận')
    else:
        print('Năm',y,'không là năm nhuận')

    c = calendar.monthrange(y,m)

    print('Số ngày trong tháng',m,'là:',c[1])

time(d,m,y)

