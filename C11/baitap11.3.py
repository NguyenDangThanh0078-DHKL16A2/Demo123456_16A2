list_animals = ['ant','bear','cat','dog','elephant','fish','goat','hippo']
print('List of animals:',list_animals)
print(len(list_animals))
a = input('I want to find:\n')
if a in list_animals:
    print('There is ',a,'in list of animals')
else:
    print('')