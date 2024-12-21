
def prime(start, end):
    flag = 0 
    print(f"The Prime Number from {start} to {end} are: ")
    for i in range(start, end):
        for j in range(2, i):
            if(i % j == 0):  
                flag = 1  
                break
            else:
                flag = 0
        if(flag == 0): 
           print(i) 
  
start = 2
end = 10
primeNumber = prime(start, end)