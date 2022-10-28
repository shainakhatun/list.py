#14.Write a Python program to find the list with maximum and minimum length.

a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
c=0
max=0
min=0
while i<len(a):
    b=len(a[i])
    if max<b:
        c=a[i]
        max=max+1
    i=i+1
    print(max,":",c)
