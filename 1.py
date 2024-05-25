def is_int(number):
    if isinstance(number, float):
        return number.is_integer()
    return isinstance(number, int)
number = float(input("Nhập vào một số thực: "))
if is_int(number):
    print("Số bạn nhập là một số nguyên.")
else:
    print("Số bạn nhập không phải là số nguyên.")