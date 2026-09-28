# Remove duplicates from a list
# Write a Python program to remove duplicate elements from a list.
# Example:
# lst = [1, 2, 2, 3, 4, 3, 5, 1]
# Expected output:
# [1, 2, 3, 4, 5]
lst = [1, 2, 2, 3, 4, 3, 5, 1]
sorted_lst=[]
for i in lst:
    if i in sorted_lst:
        continue
    else:
        sorted_lst.append(i)
print(sorted_lst)
