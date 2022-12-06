#Tính năm âm lịch

n = int(input('Nhập năm:'))
def tinh_can(n):
    if n%10 == 0:
        return "Canh"
    elif n%10 ==1:
        return "Tân"
    elif n%10 ==2:
        return 'Nhâm'
    elif n%10 ==3:
        return "Quý"
    elif n%10 ==4:
        return 'Giáp'
    elif n%10 ==5:
        return 'Ất'
    elif n%10 ==6:
        return 'Bính'
    elif n%10 ==7:
        return 'Đinh'
    elif n%10 ==8:
        return 'Mậu'
    else:
        return 'Kỷ'

def tinh_chi(n):
    if n%12 ==0:
        return 'Thân'
    elif n%12 ==1:
        return 'Dậu'
    elif n%12 ==2:
        return 'Tuất'
    elif n%12 ==3:
        return 'Hợi'
    elif n%12 ==4:
        return 'Tý'
    elif n%12 ==5:
        return 'Sửu'
    elif n%12 ==6:
        return 'Dần'
    elif n%12 ==7:
        return 'Mão'
    elif n%12 ==8:
        return 'Thìn'
    elif n%12 ==9:
        return 'Tỵ'
    elif n%12 ==10:
        return 'Ngọ'
    else:
        return 'Mùi'
print('Năm',n,'lịch âm là năm',tinh_can(n),tinh_chi(n))