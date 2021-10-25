revenue = float(input("Выручка: "))
costs = float(input("Издержки: "))
result = revenue - costs
if result > 0:
    print(f" Прибыль :{result}")
    print(f'Рентабельность: {100* result/revenue:.1f}%')
    employee = int(input("Количество сотрудников: "))
    print(f"Выручка на кадого: {result / employee:.3f}")
elif result < 0:
    print("убыток")
else:
    print ("0")
