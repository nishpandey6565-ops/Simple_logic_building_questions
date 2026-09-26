# Count even and odd digits
# Example: 123456 → Even = 3, Odd = 3

num=int(input("Enter number to count even or odd digits:"))
even_count=0
odd_count=0
while num>0:
    digit=num%10
    num=num//10
    if digit%2 == 0:
        even_count+=1
    else:
        odd_count+=1
print("Even numbers:",even_count)
print("Odd numbers:", odd_count)