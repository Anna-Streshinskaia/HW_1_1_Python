number = int(input("введите целое число: "))
big_num = 0
num = number
while num > 0:
    digit = num % 10
    if digit > big_num:
        big_num = digit
        if big_num == 9:
            break
        num = num // 10
print(f"наибольшая цифра в числе {number} равна {big_num}")



