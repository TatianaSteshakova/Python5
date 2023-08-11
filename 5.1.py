num = int(input("Введите число: "))

txt = ""

if (num == 0):
    print("Нулевое")
else:
    if (num > 0):
        txt = txt + "Положительное"
    else:
        txt = txt + "Отрицательное"
    
    if (num % 2 == 0):
        txt = txt + " четное"
    else:
        txt = txt + " нечетное"


txt = txt + " число"

print(txt)