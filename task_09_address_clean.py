addresses = [ 
"  г. Москва, ул. Ленина, д. 10  ", 
"г.Казань,ул.Баумана,д.15", 
"  г. Санкт-Петербург, ул. Невский, д. 100  " 
]

clear_adresses = []

for address in addresses:

    address = " ".join(address.split())
    
    address = address.replace("г.", "г. ")
    address = address.replace("ул.", "ул. ")
    address = address.replace("д.", "д. ")
    
    address = address.replace(" ,", ",")
    address = address.replace(", ", ",")
    address = address.replace(",", ", ")
    
    address = " ".join(address.split())

    clear_adresses.append(address)

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