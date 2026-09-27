# Find the largest number in a list
# Don't use max().

lst=[10,20,33,44,56]
temp=lst[0]
for i in lst:
    if i>temp:
        temp=i   
print(temp)