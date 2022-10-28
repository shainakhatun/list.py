# 30.Given a list of numbers, write a Python program to count positive and negative numbers in a List.
# Output: pos = 2, neg = 3

# list1 = [2, -7, 5, -64, -14]
# i=0
# a=[]
# b=[]
# while i<len(list1):
#     if list1[i]<0:
#         a.append(list1[i])
#     else:
#         b.append(list1[i])
#     i=i+1
# print("negative",a,":",len(a))
# print("positive",b,":",len(a))




# Output: pos = 3, neg = 1

list2 = [-12, 14, 95, 3]
i=0
a=[]
b=[]
while i<len(list2):
    if list2[i]<0:
        a.append(list2[i])
    else:
        b.append(list2[i])
    i=i+1
print("positive",a,":",len(a))
print("negative",b,":",len(b))

