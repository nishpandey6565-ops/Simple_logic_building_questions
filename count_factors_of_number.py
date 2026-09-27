# Count the factors of a number
# Example: 12 → 6 factors
num=int(input("Enter a number to find its factors:"))
count=0
for i in range(1,num+1):
    if num%i == 0:
        count+=1
print(f"{num} has {count} factors")