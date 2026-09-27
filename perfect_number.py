# Check whether a number is a perfect number
# Example: 6 → 1 + 2 + 3 = 6
num=int(input("Enter a number:"))
fact=0
for i in range(1,num):
    if num%i == 0:
        fact+=i
        print(fact)
if fact == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")