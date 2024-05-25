def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
number = int(input("Nhập vào một số nguyên: "))
if is_prime(number):
    print("Số bạn nhập là số nguyên tố.")
else:
    print("Số bạn nhập không phải là số nguyên tố.")
