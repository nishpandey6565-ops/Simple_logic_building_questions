# Sum of digits
# Example: 583 → 5 + 8 + 3 = 16
num=int(input("Enter a number to add its digit:"))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)