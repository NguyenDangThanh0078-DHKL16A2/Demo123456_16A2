L = [1,2,3,4]

thresh = int(input('Nhập thresh:'))
def elementwise_greater_than(L,thresh):
    for i in range(len(L)):
        if L[i] > thresh:
            L[i] = True
        else:
            L[i] = False
    print(L)
elementwise_greater_than(L,thresh)
