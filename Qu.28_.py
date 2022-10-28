#28.The task is to perform the operation of removing all the occurrences 
# of a given item/element present in a list.
# Output :2 3 4 5 2

# a=[1, 1, 2, 3, 4, 5, 1, 2]
# i=0
# while i<len(a):
#     if a[i]!=1:
#         print(a[i],end=" ")
#     i=i+1

# By useing for loop....

# a=[1, 1, 2, 3, 4, 5, 1, 2] 
# b=[]
# for i in a:
#     if i!=1:
#         b.append(i)    
# print(b)


# Output :5 6 8 9 10

# a=[5,6,7,8,9,10,7]
# i=0
# while i<len(a):
#     if a[i]!=7:
#         print(a[i],end=" ")
#     i=i+1

#29.Remove empty List from List....
#Output: [5, 6, 3, 9]		

# a=[5, 6, [], 3, [], [], 9]
# i=0
# b=[]
# while i<len(a):
#     if a[i]!=[]:
#         b.append(a)
#         print(a[i],end=" ")
#     i=i+1
