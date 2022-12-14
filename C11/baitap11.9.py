arrivals = ['Adela','Fleda','Owen','May','Mona','Gilbert','Ford']
def party_late(arrivals,name):
    flag = True
    if arrivals.index(name) < len(arrivals)/2 or arrivals.index(name) +1 ==len(arrivals):
        flag = False
    return flag
print(party_late(arrivals,name='Gilbert'))
print(party_late(arrivals,name='Ford'))
print(party_late(arrivals,name='Mona'))
