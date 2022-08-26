def pattern(number):
    if number == 1:
        return 1
    else:
        i=1
        while i<=number:
            return pattern(number-1)+3
j=pattern(4)
# print(j)        

index=1
while index<=5:
    print(pattern(index),",",end="")
    index=index+1    
