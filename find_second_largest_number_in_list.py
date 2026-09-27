# Find the second-largest number in a list
lst=[1,23,43,0,76,233,565]
temp=lst[0]
old_temp=lst[0]
for i in lst:
    if i>temp:
        old_temp=temp
        temp=i
    elif i>old_temp and i != temp:
        old_temp=i
print(old_temp)