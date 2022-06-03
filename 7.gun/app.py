list1 = [1,2,3,4,5]

list2= ['banana', 'apples', 'mango', 'oranges']

list3 =list2.copy()    #['banana', 'apples', 'mango', 'oranges']

list1.extend(list2)    # [1, 2, 3, 4, 5, 'banana', 'apples', 'mango', 'oranges']

list2.reverse()     #['oranges', 'mango', 'apples', 'banana']

print(list1)   
print(list2)    
print(list3)  

