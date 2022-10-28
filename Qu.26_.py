#26.Our task is to print the element which occurs 3 consecutive times 
# in a Python list.
# Output: 5

a=[4, 5, 5, 5, 3, 8]
i=0
b=[]
while i<len(a):
    j=0
    c=0
    while j<len(a):
        if a[i]==a[j]:
            c=c+1
        j=j+1
    if c>=3:
        k=a[i]
    i=i+1
print(k)


# Output: 1, 22

b=[1, 1, 1, 64, 23, 64, 22, 22, 22]
i=0
k=[]
while i<len(b):
    j=0
    c=0
    while j<len(b):
        if b[i]==b[j]:
            c=c+1
        j=j+1
    if c>=3:
        k=b[i]
    i=i+1
print(k)

