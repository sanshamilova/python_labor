#Введение исходных адресов
addresses = [ 
"  г. Москва, ул. Ленина, д. 10  ", 
"г.Казань,ул.Баумана,д.15", 
"  г. Санкт-Петербург, ул. Невский, д. 100  " 
]

#Создание нового пустого списка
clear_adresses = []

#Цикл проверки адресов
for address in addresses:
   
    #Удаление лишних пробелов
    address = " ".join(address.split())
    
    #Добавление пробелов после сокращений
    address = address.replace("г.", "г. ")
    address = address.replace("ул.", "ул. ")
    address = address.replace("д.", "д. ")
    
    #Унифицирование запятых
    address = address.replace(" ,", ",")
    address = address.replace(", ", ",")
    address = address.replace(",", ", ")
    
    #Повторное удаление пробелов
    address = " ".join(address.split())

    #Добавление всех элементов после изменений в пустой список
    clear_adresses.append(address)

#Вывод результата
print("=== СРАВНЕНИЕ ===")
print()
print("№1")
print("До изменений:", addresses[0])
print("После изменений:", clear_adresses[0])
print("№2")
print("До изменений:", addresses[1])
print("После изменений:", clear_adresses[1])
print("№3")
print("До изменений:", addresses[2])
print("После изменений:", clear_adresses[2])