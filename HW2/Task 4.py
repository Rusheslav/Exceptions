def check_input():
    user_input = input("Введите что-нибудь: ")
    if not user_input:
        raise Exception("Нельзя вводить пустую строку!")


check_input()
