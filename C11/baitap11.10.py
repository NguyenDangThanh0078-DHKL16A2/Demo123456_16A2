meals_1 = ['Redneck Ribs','Prawn Star','San Quentin Squid','Fist Full of Pizza','Honky Tonk Chicken']
meals_2 = ['Redneck Ribs','Prawn Star','Runing Bear Salmon','Runing Bear Salmon','Honky Tonk Chicken']
def menu_is_boring(n):
    flag = False
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            flag = True
    return flag
print(menu_is_boring(meals_1))
print(menu_is_boring(meals_2))

