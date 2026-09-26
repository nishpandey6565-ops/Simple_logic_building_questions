# Input a number and count how many digits it has.
# Example: 58321 → 5
num=int(input("Enter a number to check how many digits it has:"))
count=0
while num>0:
    num=num//10
    count+=1
print(count)
