tu_dien = {'dog':'con chó','cat':'con mèo'}
keys = tu_dien.keys()
values = tu_dien.values()
print(keys,values)
def back():
    print('{:?^70}'.format(' 1.Quay lại        2.Thoát '))
    try:
        l = int(input('Entry your choose:'))
        if l == 1:
            control()
        if l == 2:
            print('Xin cảm ơn')
    except:
        print('Hãy nhập lại!')
        back()
def xem():
    print('{:-^100}'.format('TỪ ĐIỂN'))
    for i in keys:
        print(i,'       ',tu_dien.get(i))
    back()

def tra():
    print('{:-^100}'.format('TRA TỪ'))
    a = input('Nhập từ Anh:')
    if a in keys:
        print('Nghĩa Việt là:',tu_dien.get(a))
        back()
    else:
        print(a,'Không tồn tại!!')
        back()
        
def them():
    print('{:-^100}'.format('THÊM TỪ'))
    b = input('Nhập từ Anh:')
    b1 = input('Nhập nghĩa Việt:')
    tu_dien[b] = b1
    print('Đã thêm từ điển')
    xem()

def xoa():
    print('{:-^100}'.format('XÓA'))
    for i in keys:
        print(i, tu_dien.get(i))
    c = input('Nhập từ cần xóa:')
    if c in keys:
        print('{:?^70}'.format(' Bạn có chắc chắn muốn xóa '))
        print('{:^70}'.format("1.Xóa      2.Quay lại      3.Thoát"))
        try:
            c1 = input('Entry your choose:')
            if int(c1) == 1:
                tu_dien.pop(c)
                print('Đã xóa',c,'khỏi từ điển')
                xoa()
            elif int(c1) == 2:
                control()
            elif int(c1) == 3:
                print('Xin cảm ơn!')
        except:
            print('Hãy nhập lại!')
            xoa()
       
    else:
        print(c,'không có trong từ điển!')
        xoa()
    pass

def welcome():
    try:
        entry = int(input('''
Bạn muốn làm gì??
1.Xem từ điển
2.Tra từ
3.Thêm từ
4.Xóa từ
Entry your choose:'''))
    except:
        print('Hãy nhập lại!')
        control()

    return entry
def control():
    entry = welcome()
    if entry == 1:
        xem()
    elif entry == 2:
        tra()
    elif entry == 3:
        them()
    elif entry == 4:
        xoa()
    else:
        print('Hãy nhập lại!')
        control()
control()


