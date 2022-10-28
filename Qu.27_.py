# 27.Given 3 digits a, b, and c. The task is to find all the possible 
# combinations from these digits.
# Output:1 2 3,1 3 2,2 1 3,2 3 1,3 1 2,3 2 1

# By For loop....

# a=[1, 2, 3]
# for i in a:
#     for j in a:
#         for k in a:
#             if i!=k and i!=j and k!=j:
#                 print(i,j,k)

# By While loop....

# a=[1, 2, 3]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
#             if a[i]!=a[j] and a[j]!=a[k] and a[k]!=a[i]:
#                 print(a[i],a[j],a[k])
#             k=k+1
#         j=j+1
#     i=i+1

# Output:0 9 5,0 5 9,9 0 5,9 5 0,5 0 9,5 9 0
# a=[0, 9, 5]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
#             if a[i]!=a[j] and a[j]!=a[k] and a[k]!=a[i]:
#                 print(a[i],a[j],a[k],end="")
#             k=k+1
#         j=j+1
#     i=i+1
