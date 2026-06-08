#Введение исходных данных
price = float(input("Впишите цену за единицу товара: "))
quantity = int(input("Впишите количество товара: "))

#Расчёт стоимости без скидки
all_cost = price * quantity

#Система скидок
if all_cost < 1000:
    sale_coef = 1

elif 1000 <= all_cost <= 5000:
    sale_coef = 0.95
    
else:
    sale_coef = 0.9

#Расчёт стоимости с учётом скидки
end_cost = all_cost * sale_coef

print ("Производим расчёт итоговой стоимости: ")
print (f"Стоимость товара без скидки = {price} * {quantity} = {all_cost:.2f}")
print (f"Стоимость товара с учётом скидки = {all_cost:.2f} * {sale_coef} = {end_cost:.2f} ")
print (f"Итоговая стоимость = {end_cost}") 