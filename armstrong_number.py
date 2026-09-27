# Check whether a number is an Armstrong number
# Example:
# 153 → Armstrong
# Because:
# 1³ + 5³ + 3³ = 153

num = int(input("Enter a number: "))
original = num
temp = num
count = 0

while temp > 0:
    temp = temp // 10
    count += 1
sum = 0
while num > 0:
    digit = num % 10
    sum += digit ** count
    num = num // 10
if sum == original:
    print(f"{original} is an Armstrong number")
else:
    print(f"{original} is not an Armstrong number")
