car_price = float(input("\nВведите стоимость автомобиля без наценок "))
car_tax = float(input("\nВведите налог на машину в процентах числом "))
car_price = car_price * car_tax /100 + car_price
reg_fee = float(input("\nВведите регистрационный сбор на машину в процентах "))
car_price = car_price * reg_fee / 100 + car_price
ag_fee = float(input("\nВведите агенский сбор на машину в гривнах "))
car_price += ag_fee
car_delivery = float(input("\nВведите стоимость доставки машины в гривнах "))
car_price += car_delivery
print("\nОкоечательная цена автомобиля ",car_price,"грн.\nНажмите Enter для завершения программы")
input()
