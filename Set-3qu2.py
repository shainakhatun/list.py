# count the occurences of characters present in the char_list 
# and we have to save in the nested list,
# then we have to use that nested list to print the output.

list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
n=[]
while i<len(list):
    j=1
    c=0
    while j<len(list):
        if list[i]==list[j]:
            c=c+1
        j=j+1
    if c>0:
        if [list[i],c] not in n:
            
           n.append([list[i],c])
    i=i+1
    print(list[i],"-",c,"times")
    