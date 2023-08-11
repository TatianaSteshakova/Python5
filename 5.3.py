min = int(input("Введите мин. сумму инвестиций: "))
mike = int(input("Сколько долларов у Майкла: "))
ivan = int(input("Сколько долларов у Ивана: "))

if (mike > min and ivan > min):
    print(2)
else: 
    if (mike > min):
        print("Mike")
    else:
        if(ivan > min):
            print("Ivan")
        else:
            if (mike + ivan >= min):
                print(1)
            else:
                print(0)
    
