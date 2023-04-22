def divide_by_zero():
    user_input = input("Введите произвольный текст: ")
    return len(user_input) / 0


def raise_type_error():
    user_input = input("Введите произвольный текст: ")
    return user_input + 10


def raise_index_error():
    arr = [1, 2, 3]
    return arr[len(arr)]

# divide_by_zero()
# another_exception()
# raise_index_error()