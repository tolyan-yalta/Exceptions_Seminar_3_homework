from view import *
from check import *
import write_data


def start():
    while True:
        # Ввод данных из консоли
        str, list = input_data()
        # Проверка количества введенных данных 
        if not check_number_data_entered(list):
            continue
        # Проверка правильности введения фамилии
        if not check_surname_name_patronymic(list[0]):
            continue
        # Проверка правильности введения имени
        if not check_surname_name_patronymic(list[1]):
            continue
        # Проверка правильности введения отчества
        if not check_surname_name_patronymic(list[2]):
            continue
        # Проверка правильности введения даты
        if not check_date_birth(list[3]):
            continue
        # Проверка правильности введения телефонного номера
        if not check_telephon_number(list[4]):
            continue
        # Проверка правильности введения пола
        if not check_input_gender(list[5]):
            continue
        # Если все правильно, то выход из цикла
        break
        
    # Запись данных в файл
    write_data.write_data(list[0], str)
    # Вывод сообщения об окончании программы
    output_end()
        

# Иванов Иван Иванович 22.03.1995 88001234569 m
# Пушкин Александр Сергеевич 26.05.1999 88009874563 m
# Иванов Сергей Петрович 13.11.2011 88003214587 m
