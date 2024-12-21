
a, b =0, 1
count=0

terms = int(input("Enter the number of terms: "))

if terms<= 0:
    print("Enter positive Number...")

else:
    while count< terms:
        print(a)
        c= a+b
        a= b
        b=c
        count+=1


