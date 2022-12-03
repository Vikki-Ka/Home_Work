a = int(input("Ввидите число "))
n = a * (-1)

if a > 0 and a < 10:
    while n <= a:
        print(n)
        n += 1
else:
    print("Ввидите число больше 0 и меньше 10")