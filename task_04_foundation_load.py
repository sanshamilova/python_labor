day = int(input("Введите номер дня недели: "))

if day == 1:
    print("Понедельник")

elif day == 2:
    print("Вторник")

elif day == 3:
    print("Среда")

elif day == 4:
    print("Четверг")

elif day == 5:
    print("Пятница")

elif day == 6:
    print("Суббота")

elif day == 7:
    print("Воскресенье")

else:
    print("В неделе семь дней")

if 0 <= day <= 5:
    print("8:00 - начало смены.")
    
elif 5 < day <= 7:
    print("Отдых.")

else:
    1 == 1