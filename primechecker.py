def isPrime(no):
    isit = False
    if no>0 and no != 2:
        for i in range(2,no):#2,3
            if no%i==0:
                isit = False
                break
        else:
            isit=True
    elif no==2:
        isit = True
    else:
        isit = False
    return isit

no = 2
times = 0
till = int(input("Enter the no. till where you want Primes:  "))


while no<till:
    if isPrime(no)==True:
        times += 1
        print(no)
        no += 1
    else:
        no += 1
        continue
print("Total No.s of Primes till "+ str(till)+ " are "+str(times))
        
            
        
        
