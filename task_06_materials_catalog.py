materials = ["Бетон", "Дерево", "Металл", "Стекло", "Цемент"]

print("Первый, средний и последний материалы из списка: ")
print(materials[0])
print(materials[2])
print(materials[-1])
print()

materials.append("Песок")
materials.append("Пластик")

materials.remove("Пластик")

print("Итоговый список материалов: ")
print(materials)
print()
length = len(materials)
print("Длина списка:", length)