# Find the smallest number in a list
lst=[22,34,12,32,68,90]
temp=lst[0]
for i in lst:
    if i<=temp:
        temp=i
print(temp)
