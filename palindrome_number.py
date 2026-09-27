# Check whether a number is a palindrome

number=int(input("Enter a number:"))
num=number
reverse=0
while num>0:
    digit=num%10
    num=num//10
    reverse=reverse*10+digit
print(reverse)
if reverse == number:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")