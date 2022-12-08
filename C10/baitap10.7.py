


s= input('Nhập chuỗi s: ')
s_sub = input('Nhập chuỗi con s_sub: ')
s_find = input('Nhập chuỗi cần tìm s_find: ')
s_replace = input('Nhập chuỗi thay thế s_replace: ')
def xu_ly_chuoi(s,s_sub,s_find,s_replace):
    print('Chuỗi sau khi loại bỏ khoảng trắng ở đầu và cuối chuỗi:',s.strip())
    print('số lần s_sub xuất hiện trong s:',s.count(str(s_sub)))
    print(s.find(s_find))
    s = s.capitalize()
    s = s.replace('duck','dog')
    print('Chuỗi s sau khi tìm kiếm và thay thế: ',s)

xu_ly_chuoi(s,s_sub,s_find,s_replace)