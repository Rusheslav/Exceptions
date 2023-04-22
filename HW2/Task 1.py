def show_float():
    flag = True
    while flag:
        try:
            user_input = input("Введите дробное число: ")
            print(float(user_input))
            flag = False
        except ValueError:
            continue


show_float()
