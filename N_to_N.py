n=int (input("Ввидите положительное число "))
a=n
n=n*(-1)

if a>0 :
    while n<=a:
        print(n)
        n+=1
else:
    print("Ввидите положительное число")
