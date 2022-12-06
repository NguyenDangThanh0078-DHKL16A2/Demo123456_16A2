weight = float(input('Nhập cân nặng(kg):'))
hight = float(input('Nhập chiều cao(m):'))
def tinh_BMI(weight,hight):
    return weight/(hight**2)
def danh_gia(n):
    if n<18.5:
        return 'mày bị gầy!'
    elif 18.5<=n<=24.99:
        return 'mày bình thường, giỏi lắm con trai của ta'
    else:
        return 'mày bị thừa cân!!!'
print('Chỉ số BMI:',tinh_BMI(weight,hight))
print(danh_gia(tinh_BMI(weight,hight)))