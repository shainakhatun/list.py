#37.Write a Python program to pair up the consecutive elements of a given list.

# Output:[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

# a=[1, 2, 3, 4, 5, 6]
# i=0
# l=[]
# k=[]
# c=0
# while i<len(a):
#     if c==2:
#         l.append(k)
#         k=[]
#         c=1
#     else:
#         c+=1
#     k.append(a[i])
#     i+=1
# l.append(k)
# print(l)