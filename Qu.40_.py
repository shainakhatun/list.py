#40.Write a Python program to sum two or more lists, the lengths of the lists may 
# be different. 

# Output:[4, 8, 8]

a=[[1, 2, 4], [2, 4, 4], [1, 2]]
i=0
b=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a):
        k=0
        while k<len(a[j]):
            if i==k:
                sum+=a[j][k]
            k=k+1
        j=j+1
    b.append(sum)
    i=i+1
print(b)



#Output: [8, 6, 4]

# a=[[1, 2, 4], [2, 4, 4], [1, 2]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a):
#         k=0
#         while k<len(a[j]):
#             if i==k:
#                 sum+=a[j][k]
#             k=k+1
#         j=j+1
#     b.append(sum)
#     i=i+1
# print(b)

