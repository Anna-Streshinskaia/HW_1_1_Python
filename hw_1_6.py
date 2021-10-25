while True:
    days = 1
    start_km = float(input("старт: "))
    last_km = float(input("финал: "))
    if start_km <= 0 or last_km < 0:
        print("введиде число больше 0")
    else:
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1
        print(f" до резульата {days}")
        break

