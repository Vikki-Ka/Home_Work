n=int (input("Ввидите число "))
a=n
n=n*(-1)

if a>0 :
    if a<10:
        while n<=a:
            print(n)
            n+=1
    else:
        print ("Ввидите число меньше 10")        
else:
    print("Ввидите положительное число")
