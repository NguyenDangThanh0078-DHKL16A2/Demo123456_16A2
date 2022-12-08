#giải phương trình ax^2+bx+c=0
def giai_pt_bac_2(a,b,c):
	import math
	if a == 0 and b == 0:
		if c !=0 :
			print('phương trình vô nghiệm')
		else:
			print('phương trình vô số nghiệm')
	elif a == 0:
		print('phương trình có nghiệm',-c/b)
	else:
		d = b*b -4*a*c
		if d < 0 :
			print('pt vô nghiệm')
		elif d == 0:
			print('pt có nghiệm duy nhất x:',-b/2*a)
		else:
			x1 = (-b+math.sqrt(d))/2
			x2 = (-b-math.sqrt(d))/2
			print('phương trình có nghiệm x1:',x1,'x2:',x2)

a = float(input('Nhập a:'))
b = eval(input('Nhập b:'))
c = eval(input('Nhập c:'))

giai_pt_bac_2(a,b,c)
