#Введение размеров
length = 6
width = 3
height = 2.7

#Введение стоимости покраски 1 м2
paint_price = 125

#Расчет геометрических параметров помещения
floor_area = length * width #Площадь пола
walls_area = 2 * height * ( length + width ) #Площадь стен
room_volume = length * width * height #Объём

#Расчет стоимости покраски стен
painting_cost = paint_price * walls_area

#Вывод результатов расчёта
print(f"Площадь пола = {floor_area:.2f}")
print(f"Площадь стен = {walls_area:.2f}")
print(f"Объем комнаты = {room_volume:.2f}")
print(f"Стоимость покраски стен = {painting_cost:.2f}")