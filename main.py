num = int(input("Введите число -> "))
if (num % 2 == 0) :
    print(f"Число четное")
else :
    print(f"Число нечетное")  
if (num % 3 == 0) :
    print(f"Число делится на 3")
else :
    print(f"Число не делится на 3") 
if (num < 0) :
    print(f"Число отрицательное")
elif (num > 0):
    print(f"Число положительное") 
else:
    print(f"Число является нулем") 