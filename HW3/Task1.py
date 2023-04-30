import re


class FewDataException(Exception):
    def __init__(self, data_list):
        self.data_list = data_list

    def __str__(self):
        return f"Вы ввели слишком мало данных: {len(self.data_list)} вместо 6"


class MuchDataException(Exception):
    def __init__(self, data_list):
        self.data_list = data_list

    def __str__(self):
        return f"Вы ввели слишком много данных: {len(self.data_list)} вместо 6"


class SexException(Exception):
    def __str__(self):
        return 'Вы не ввели пол в нужном формате: "m" или "f"'


class BirthDateException(Exception):
    def __str__(self):
        return 'Вы не ввели дату рождения в нужном формате: "dd.mm.yyyy"'


class PhoneNumberException(Exception):
    def __str__(self):
        return 'Вы не ввели номер телефона в нужном формате (только цифры)'


data = input("Введите данные: ")
data_list = data.split()

try:
    if len(data_list) < 6:
        raise FewDataException(data_list)
    elif len(data_list) > 6:
        raise MuchDataException(data_list)

    surname = data_list.pop(0)

    if "m" in data_list:
        sex = "m"
        data_list.remove("m")
    elif "f" in data_list:
        sex = "f"
        data_list.remove("f")
    else:
        raise SexException

    date_of_birth = None
    phone_number = None
    patronim = None
    for s in data_list:
        if re.match(r'^\d\d\.\d\d\.\d\d\d\d$', s):
            date_of_birth = s
        elif re.match(r'^\d*$', s):
            phone_number = s
        elif re.match(r'^.*[ь,в]ич$', s) or re.match(r'^.*[в,ч]на$', s):
            patronim = s
    if date_of_birth is None:
        raise BirthDateException
    if phone_number is None:
        raise PhoneNumberException
    data_list.remove(date_of_birth)
    data_list.remove(phone_number)

    if patronim:
        data_list.remove(patronim)
    else:
        patronim = data_list[1]
    name = data_list[0]

    print(f'{surname} {name} {patronim} {date_of_birth} {phone_number} {sex}')
    with open(f'{surname}.txt', 'a') as file:
        file.write(f'{surname} {name} {patronim} {date_of_birth} {phone_number} {sex}\n')

except FewDataException as exc:
    print(exc)
except MuchDataException as exc:
    print(exc)
except SexException as exc:
    print(exc)
except BirthDateException as exc:
    print(exc)
except PhoneNumberException as exc:
    print(exc)
