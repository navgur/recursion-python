def prime(n,i):
    if i==1:
        return 1
    if (n%i)==0:
        return 0
    return prime (n,i-1)
n=int(input("enter the number"))  
z=prime(n,int(n/2))
print(z) 
if z==1:
    print(n,"is a prime number") 
else:
    print(n, "is a composite number")    


# prime=if number of factor =2
# that number is prime  number




              
       


