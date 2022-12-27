set1 = set()
set2 = set()
while True:
    a = int(input('Nhập 1 để tiếp tục nhập phần tử cho set1\n:'))
    if a == 1:
        set1.add(int(input('Nhập giá trị:')))
    else:
        break
print('\n'*3)
while True:
    b = int(input('Nhập 1 để tiếp tục nhập phần tử cho set2\n:'))
    if b == 1:
        set2.add(int(input('Nhập giá trị:')))
    else:
        break
print(set1)    
print(set2)
print('set1 có',len(set1),'phần tử')
print('set2 có',len(set2),'phần tử')
print('Max set1 là:',max(set1))
print('Max set2 là:',max(set2))
set3=set1.copy()
print('Lấy một phần tử bất kì từ set1:',set3.pop())
print('set1 sau khi pop:,',set3)
print('Set Union:',set1|set2)
print('Set Intersection:',set1&set2)
print('set difference;',set1-set2)
print('set symmetric difference:',set1^set2)
print(sorted(set1))
print(sorted(set2,reverse=True))



    