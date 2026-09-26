# Find the largest digit
# Example: 58321 → 8
num=int(input("Enter a number to check which one is largest:"))
large_digit=0
while num>0:
    digit=num%10
    num=num//10
    if large_digit<digit:
        large_digit=digit
print(large_digit)