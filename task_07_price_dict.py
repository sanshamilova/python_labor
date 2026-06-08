#Создание словаря материалов с ценами
material_prices = {
    "Бетон": 123,
    "Дерево": 456,
    "Металл": 789,
    "Стекло": 987,
    "Цемент": 654
}
#Выведение списка материалов
print("Список материалов с ценами: ")
print(material_prices)
print()

#Добавление 2 новых материалов
material_prices["Песок"] = 321
material_prices["Пластик"] = 123
#Изменение цены одного материала
material_prices["Бетон"] = 369
#Удаление одного материала
del material_prices["Стекло"]
#Выведение списка материалов
print("Список материалов после изменений: ")
print(material_prices)
print()

#Расчёт средней стоимости материалов
total_cost = sum(material_prices.values())
length = len(material_prices)

average_cost = total_cost / length

#Вывод средней стоимости материалов
print(f"Средняя стоимость материалов: {average_cost:.2f}")
