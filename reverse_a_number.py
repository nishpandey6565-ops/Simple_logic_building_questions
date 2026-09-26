# Reverse a number
# Example: 12345 → 54321

num=int(input("Enter a number to reverse it:"))
reverse=0
while num>0:
    digit=num%10
    num=num//10
    reverse=reverse*10+digit
print(reverse)