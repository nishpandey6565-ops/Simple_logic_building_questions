# Check whether a number is prime
num=int(input("Enter a number:"))
factors=[]
for i in range(1,num+1):
    if num%i == 0:
        factors.append(i)
if len(factors) == 2:
    print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")