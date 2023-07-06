a={1,2,3,4}
#class set
print(type(a))
#empty set
a=set()
print(type(a))
#added value
a.add(4)
a.add(5)
print(a)  
#we can print tauple in set
#but list is not run in set
#a.add([1,2,3])#list
#a.add((1,2,3))#tauple
print(len(a))#check the lengtha.
a.remove(4)#remove method
print(a)