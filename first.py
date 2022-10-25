'''.printing every character entered by the user in new line'''
 s=input('Enter the word: ')
 str = s
for i in str:
    print(i)


'''Adding list of items in a set'''
set=set()
list=[]
a=int(input('Enter the number of items to add: '))
for i in range(1,a+1):
    z=input()
    list.append(z)
set.update(list)
print(set)








