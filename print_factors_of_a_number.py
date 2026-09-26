# Print all factors of a number
# Example: 12 → 1 2 3 4 6 12

num=int(input("Enter a number to print its factors:"))
for i in range(1,num+1):
    if num%i == 0:
        print(i)