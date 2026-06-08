#Введение списка материалов
materials = ["Бетон", "Дерево", "Металл", "Стекло", "Цемент"]

#Выведение первого, среднего и последнего элементов списка
print("Первый, средний и последний материалы из списка: ")
print(materials[0])
print(materials[2])
print(materials[-1])
print()

#Добавление новых материалов
materials.append("Песок")
materials.append("Пластик")

#Удаление материала
materials.remove(materials[1])

#Выведение итогого списка и длины
print("Итоговый список материалов: ")
print(materials)
print()
length = len(materials)
print("Длина списка:", length)