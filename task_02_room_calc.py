length = 6
width = 3
height = 2.7

paint_price = 125

floor_area = length * width 
walls_area = 2 * height * ( length + width )
room_volume = length * width * height 

painting_cost = paint_price * walls_area

print(f"Площадь пола = {floor_area:.2f}")
print(f"Площадь стен = {walls_area:.2f}")
print(f"Объем комнаты = {room_volume:.2f}")
print(f"Стоимость покраски стен = {painting_cost:.2f}")