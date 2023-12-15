car_01 = {'make' : 'Volvo', 'drive' : 'petrol', 'price' : 649000}
car_02 = {'make' : 'Ford', 'drive' : 'petrol', 'price' : 349800}
car_03 = {'make' : 'Tesla', 'drive' : 'electric', 'price' : 989000}
car_04 = {'make' : 'Ferrari', 'drive' : 'petrol', 'price' : 1649200}
car_05 = {'make' : 'Audi', 'drive' : 'petrol', 'price' : 897000}
car_06 = {'make' : 'VW', 'drive' : 'electric', 'price' : 279800}
car_07 = {'make' : 'Honda', 'drive' : 'electric', 'price' : 466000}
car_08 = {'make' : 'Fiat', 'drive' : 'electric', 'price' : 158600}
car_09 = {'make' : 'porche', 'drive' : 'petrol', 'price' : 971000}
car_10 = {'make' : 'Toyota', 'drive' : 'petrol', 'price' : 345800}

moreCars = []

for i in range(10):
    x = i+1
    if x < 10:
        car = f"car_0{x}"
    else:
        car = f"car_{x}"

    moreCars.append(locals()[car])

print(moreCars)
