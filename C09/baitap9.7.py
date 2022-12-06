#hàm trả phần nguyên của phép chia 2 số nguyên
x = int(input('Nhập số nguyên x:'))
y = int(input("Nhập số nguyên y:"))


def phep_chia_hai_so_nguyen(x,y):
    n = x//y
    return n

print('Phần nguyên của x/y:',phep_chia_hai_so_nguyen(x,y))
