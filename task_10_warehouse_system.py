warehouse = { 
"Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000}, 
"Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50}, 
"Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10}, 
"Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20}, 
"Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15} 
}

total_cost = 0
most_expensive_material = []
most_expensive_material_cost = 0
materials_in_danger = 0

print("=" * 75)
print("Cистема учета склада")
print("=" * 75)
print("Материал   | Кол-во | Цена       | Мин.  | Стоимость")
print("-" * 75)
for material, info in warehouse.items():
    total_value = info["quantity"] * info["price"]
    total_cost = total_cost + total_value
    if total_value > most_expensive_material_cost:
        most_expensive_material_cost = total_value
    else:
        most_expensive_material_cost = most_expensive_material_cost

    if info["quantity"] < info["min_quantity"]:
        print(f"{material:10} | {info['quantity']:>6} | "
          f"{info['price']:>10.2f} | {info['min_quantity']:>5} | {total_value:>10.2f} !!!Внимание!!!")
    else:
        print(f"{material:10} | {info['quantity']:>6} | "
          f"{info['price']:>10.2f} | {info['min_quantity']:>5} | {total_value:>10.2f}")
  
for material, info in warehouse.items():
    if most_expensive_material_cost / info["price"] == info["quantity"]:
        most_expensive_material = material
    else:
        most_expensive_material = most_expensive_material

print("=" * 75)
print("Общая стоимость материалов на складе: ", total_cost)
print("=" * 75)
print("Самый дорогой материал на складе:", most_expensive_material, {most_expensive_material_cost})
print("=" * 75)
print("Критические остатки материала: ")
for material, info in warehouse.items():
    if info["quantity"] < info["min_quantity"]:
        materials_in_danger += 1
        print("-", material,":", info["quantity"], "<", info["min_quantity"])
    else:
        materials_in_danger = materials_in_danger
print("Критических остатков всего: ", materials_in_danger)
print("=" * 75)