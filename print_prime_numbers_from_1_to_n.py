# Print all prime numbers from 1 to N
# Example: N = 10
# Output: 2 3 5 7

num=int(input("Enter a number to print prime numbers:"))
for i in range(2,num+1):
    is_prime=True
    for j in range(2,i):
        if i%j == 0:
            is_prime=False
    if is_prime==True:
        print(i)