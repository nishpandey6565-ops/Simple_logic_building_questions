# Find the smallest digit
# Example: 58321 → 1
num=int(input("Enter a number to find the smallest digit:"))
smallest=9
while num>0:
    digit=num%10
    num=num//10
    if smallest>digit:
        smallest=digit
print(smallest)