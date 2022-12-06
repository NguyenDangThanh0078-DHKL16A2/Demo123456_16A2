def sign(x):
	if x<0:
		return -1
	if x>0:
		return 1
	if x==0:
		return 0
a = int(input('Nhập số nguyên:'))
print(sign(a))
