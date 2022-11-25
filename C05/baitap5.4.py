#Bài tập 5.4: Tính diện tích tam giác ABC với a,b,c nhập từ bàn phím
#Theo công thức Heron
import math  #gọi thư viện math chứa các hàm toán học
print("Nhập số đo accs cạnh tam giác: ")
a = eval(input('a='))
b = eval(input('b='))
c = eval(input('c='))
p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))

print("Diện tích tam giác ABC là: ", s)
