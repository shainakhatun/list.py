# 16.Write a Python program to find the difference between elements
# (n+1th - nth) of a given list of numeric values.

a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i=0
c=[]
while i<len(a):
    b=(a[i]+1-(a[i]))
    c.append(b)
    i=i+1
print(c)


