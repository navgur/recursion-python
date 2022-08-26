def pattern(number):
    if number == 1:
        return 1
    elif number % 2 == 0:
        return pattern(number - 1) + 1
    else:
        return pattern(number - 1) * 10
n=pattern(6)
print(n)
i=1
while i<=5:
    print(pattern(i))  
    i=i+1      