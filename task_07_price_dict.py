material_prices = {
    "Бетон": 123,
    "Дерево": 456,
    "Металл": 789,
    "Стекло": 987,
    "Цемент": 654
}
print("Список материалов: ")
print(material_prices)
print()

material_prices["Песок"] = 321
material_prices["Пластик"] = 123
material_prices["Бетон"] = 369
del material_prices["Стекло"]
print("Список материалов после изменений: ")
print(material_prices)
print()

total_cost = sum(material_prices.values())
length = len(material_prices)

average_cost = total_cost / length

print(f"Средняя стоимость материалов: {average_cost:.2f}")
