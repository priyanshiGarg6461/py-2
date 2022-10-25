''ASSIGNMENT 4'''

'''1.printing initial names letter and surname full'''
 #Method 1
user = input('Please Enter your name: ')
 names = user.split()
 for i in range(0, len(names)):
     if i < len(names) - 1:
        print(names[i][0], end=" ") 
   else:
        print(names[i])

# #Method 2
name = input("Please enter a name: ")
name = name.split()
initials = [x[0] for x in name[:-1]]
print(*initials, name[-1])


'''2.Program to find word'''
# s='This is umbrella'
# print(s.count('e'))


'''3.removing items which is not common in both set'''
# set1 = {1,2,3,4,5,6,7}
# set2 = {1,2,3,4}
# set=set1.intersection(set2)
# print(set)


'''4.checking the presence of the word in a string'''
# s = 'This is orange juice'
# i = input('Enter a word: ')
# if i in s:
#     print('Yes')
# else:
#     print('No')


'''5.length of the string'''
# str = 'refrigerator'
# a=0
# for i in str:
#     a=a+1
# print(a)


'''6.printing every character entered by the user in new line'''
# s=input('Enter the word: ')
# str = s
# for i in str:
#     print(i)


'''7.Adding list of items in a set'''
# set=set()
# list=[]
# a=int(input('Enter the number of items to add: '))
# for i in range(1,a+1):
#     z=input()
#     list.append(z)
# set.update(list)
# print(set)


'''8.returning identical set from 2 diff set'''
# set1={1,2,3}
# set2={3,4,5}
# set=set1.intersection(set2)
# print(set)


'''9.printing a new set of union 2 set without same items'''
# set1={1,2,3,4,5}
# set2={3,4,5,6,7,8}
# set=set1.union(set2)
# print(set)


'''10.updating 1st set from the two defined sets'''
# set1={1,2,3,4,5}
# set2={3,4,5,6,7,8}
# set1=set1-set2
# print(set1)


'''11.removing following elements from the set'''
# set = {10,20,30,40,50}
# x = list(map(int, input("Enter the item to remove: ").split()))
# set=set.difference(x)
# print(set)


'''12.filling a set'''
# set={1,2,3}
# a={4,5}
# b={6,7}
# n=int(input('''In which set you want to add set(s): 
# press 1 for set a
# press 2 for set b
# :-'''))
# if n==1:
#     print(a.union(set))
# elif n==2:
#     print(b.union(set))


'''13.printing same elements of 2 sets'''
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# if set1.isdisjoint(set2):
#       print("No common items present!")
# else:
#   print("Yes,common items present.")
#   print(set1.intersection(set2))


'''14.updating set1 by adding set2 items'''
# set1={1,2}
# set2={2,3,4}
# set2.difference_update(set1)
# set1.update(set2)
# print(set1)


'''15.list to dictionary coversion'''
# keys = ["Ten","Twenty","Thirty"]
# values = [10,20,30]
# dict = {keys[i]:values[i] for i in range (len(keys))}
# print(dict)


'''16.merging 2 dictionaries'''
# dict1 = {'Ten':10 , 'Twenty':20 , 'Thirty':30}
# dict2 = {'Thirty':30 , 'Fourty':40 , 'Fifty':50}
# print(dict1|dict2)


'''17.initialising dictionary with default values'''
# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}
# d = {}
# for i in employees:
#     key=[i]
#     d = d.fromkeys(key,defaults)
#     print(d)