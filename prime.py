# given number is prime or not

n=19
for i in range(2,n):
    if n%i==0:
        print (n,"equals", i,"*",n//i)
        print (n,"is not a prime number");
        break;
else:
    print(n,"is a prime number")
    
# list of prime numbers till 100

for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            print(i,"equals",j,"*",i//j)
            print("Hence",i,"is not a prime number");
            break;
    else:
        print (i,"is a prime number")
