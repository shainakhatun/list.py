# 25.Given a List, extract all elements whose frequency is greater than K.
#K=3-Output: [4, 3] 

a= [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
i=0
k=3
count=0
while i<len(a):
    if a[i]==k:
        count=count+1
    i=i+1
print(count,",",k)


#K=2-Output: [4, 3, 6]

a=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
i=0
b=[]
k=2
while i<len(a):
    j=0
    count=0
    while j<len(a):
        if a[i]==a[j]:
            count=count+1
        j=j+1
    if count>k and a[i] not in b:
        b.append(a[i])
    i=i+1
print(b)
    