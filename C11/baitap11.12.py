a = (3,1,2,4)
b = (5,7,6,8)
c = a+b
d = list(c)
d.sort()


print('Tuple a:',a)
print('Tuple b:',b)
print('Tuple c:',c)
print('Tuple d:',tuple(d))
print('Tuple[3]=',d[3])
print('3 phần tử cuối cùng của tuple d',tuple(d[-3:]))
