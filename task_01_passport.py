student_name = "Шамилова Саният Алиевна"
group_number = "3140801/52501"
project_name = "Эрмитаж"
floors = "3"
height = "22"
is_residential = False
construction_year = "1764"

print("=== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ===")
print(f"Составитель: {student_name}")
print(f"Группа: {group_number}")
print(f"Объект: {project_name}")
print(f"Этажность: {floors}")
print(f"Высота: {height}")
if is_residential:
  print("Тип: Жилой")
else: 
  print("Тип: Нежилой")
print(f"Год постройки: {construction_year}")
