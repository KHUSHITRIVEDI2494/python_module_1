'''print(food_list[0])
print(food_list)
pnt(food_list[3])
print(food_list[0:3])
print(food_list[3:6])
print(food_list[-1])
print(food_list[2:])
print(food_list[:5])
print(food_list[0::2])
print(len(food_list))

if 'sandwich' in food_list:
    print('yes')

else:
    print('no')

for items in food_list:
    print(items)'''


'''LIST INBUILT FUNCTIONS

food_list.append('idli') to add items in list
food_list.insert(2,'dhosa') to add item in particular index
print(food_list.index('sandwich')) to find the index of any item
food_list.pop() bydefault it will remove last item from list
food_list.pop(3) it will remove at particular index
food_list.remove('pizza')
print(food_list.count('burger')) to count the frequency of items
food_list.sort() to sort the list
food_list.reverse() reverse the list
food_list.clear() clear the list
del food_list delete the list
print(food_list)'''



'''reastaurant_list=['pizza hut', 'octant pizza', 'honest', 'gloria', 'dominoz']
print(reastaurant_list)

print(reastaurant_list + food_list)'''

'''food_list.extend(reastaurant_list) it will combine the list
print(food_list)'''


mylist=[]

n=(input('how many items do you want to put:'))

for items in range(n):
    el=input('enter the elements of list')
    mylist.append(el)

print(mylist)