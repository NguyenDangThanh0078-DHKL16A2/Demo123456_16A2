print("Bài tập Python dùng hàm tính tổng các SNT từ 0 - 1000")
 
def check_SNT(n):
    flag = True
 
    # Kiểm tra SNT
    if (n < 2):
        flag = False
    elif (n == 2):
        flag = True
    elif (n % 2 == 0):
        flag = False
    else:
        # Lặp qua các số lẻ nên bắt đầu từ 3 với bước nhảy là 2
        for i in range(3, n, 2):
            if (n % i == 0):
                flag = False
 
    return flag
 
# Chương trình chính
tong = 0
 
for i in range(0, 1001):
    if (check_SNT(i)):
        print(i)
        tong += i
 
print("Tính tổng tất cả các SNT là: ", tong)