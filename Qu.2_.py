# 2.Convert Character Matrix to single String;
# The String after join: gfgisbest
	
list=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
i=0
sum=""
while i<len(list):
    a=0
    while a<len(list[i]):
        sum=sum+(list[i][a])
        a=a+1
    i=i+1
print(sum)