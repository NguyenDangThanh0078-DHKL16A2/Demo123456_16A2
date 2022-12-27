danh_ba = {'Minh': '0989741258','Hạnh':'0903852147','Bình':'0913753951','An':'0933753654'}
keys = danh_ba.keys()
items = danh_ba.items() 
    
def xem_danh_ba():
    print('{:-^100}'.format('XEM DANH BẠ'))
    for key, value in danh_ba.items():
        print(key,':',value)
    a = int(input('''
1.Quay lại
2.Thoát
Entry your chosse:'''))
    if a == 1:
        bookphone()
    if a == 2:
        print('Xin cảm ơn!!')
    

def search_name():
    print('{:-^100}'.format('TÌM DANH BẠ'))
    b = input('Nhập tên cần tìm: ')
    if b in keys:
        print(danh_ba.get(b))
        bookphone()
    else:
        print('Không tìm thấy!!!')
        b1 = int(input('''
1.Quay lại
2.Thoát
Entry your choose: '''))
        if b1 == 1:
            bookphone()
        elif b1 == 2:
            print('Xin cảm ơn!!')

def them_danh_ba():
    print('{:-^100}'.format('THÊM DANH BẠ'))
    c = input('Nhập tên muốn thêm:')
    try:
        c1 = int(input('Nhập số điện thoại muốn thêm:'))
    except:
        print('Hãy nhập lại')
        them_danh_ba()
    danh_ba[c] = str(c1)
    xem_danh_ba()
    
def xoa_lien_lac():
    print('{:-^100}'.format('XÓA LIÊN LẠC'))
    if len(danh_ba) == 0:
        print('danh bạ trống')
        bookphone()
    for i in items:
        print(i)
    d = input('''
Nhập tên bạn muốn xóa:
1.Quay lại
2.Thoát 
Entry your choose:''')
    try:
        if d in keys:
            print('{:^70}'.format('Bạn có chắc chắn muốn xóa??'))
            print('{:^70}'.format('1.Có     2.Không'))
            d1 = int(input('Entry your number:'))
            if d1 == 1:
                    danh_ba.pop(d)
                    print('Đã xóa')
                    xoa_lien_lac()
            elif d1 == 2:
                xoa_lien_lac()
        elif int(d) == 1:
            bookphone()
        elif int(d) == 2:
            print('Xin cảm ơn!')
    except:
        print(d,'không tồn tại!!\nHãy nhập lại:')
        xoa_lien_lac()

def welcome():
    row = '{:_^100}'.format('{:-^62}'.format('{:*^31}'.format('DANH BẠ')))
    print(row)
    try:
        entry = int(input('''
1. Xem danh bạ
2. Tìm danh bạ
3. Thêm danh bạ
4. Xóa liên lạc
5. Thoát 
Entry your number:'''))
    except:
        print('Hãy nhập lại!!!')
        bookphone()
    return entry

def bookphone():
    entry = welcome()
    if entry == 1:
        xem_danh_ba()
    elif entry == 2:
        search_name()
    elif entry == 3:
        them_danh_ba()
    elif entry == 4:
        xoa_lien_lac()
    elif entry == 5:
        print('Xin cảm ơn!!')
    else:
       print('Hãy nhập lại!!!')
       bookphone()
bookphone()