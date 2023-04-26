from my_exception import *


def check_number_data_entered(list):
    """Проверка количества введенных данных"""
    try:
        if len(list) < 6:
            raise Exception_not_all_data_is_entered
        if len(list) > 6:
            raise Exception_unnecessary_data_is_entered
        return True
    except (Exception_not_all_data_is_entered, 
            Exception_unnecessary_data_is_entered) as e:
        print(e)
        return False


def check_surname_name_patronymic(string):
    """Проверка правильности введения ФИО"""
    try:
        # Коды с 1040 по 1071 и 1025 - заглавные буквы кириллицы в HTML-коде
        # Коды с 1072 по 1103 и 1105 - прописные буквы кириллицы в HTML-коде
        if not (1040 <= ord(string[0]) <= 1071 or ord(string[0]) == 1025 
                or 1072 <= ord(string[0]) <= 1103 or ord(string[0]) == 1105):
            raise Exception_first_symbol_not_letter

        if not (1040 <= ord(string[0]) <= 1071 or ord(string[0]) == 1025):
            raise Exception_first_symbol_not_capital_letter

        for i in string[1:]:
            if not (1072 <= ord(i) <= 1103 or ord(i) == 1105):
                raise Exception_contain_symbol_not_being_letters
        
        return True

    except (Exception_first_symbol_not_letter, Exception_first_symbol_not_capital_letter, 
            Exception_contain_symbol_not_being_letters) as e:
        print(e)
        return False
    

def check_date_birth(date):
    """Проверка правильности введения даты рождения"""
    try:
        # Коды с 48 по 57 арабские цифры, а 46 - точка в HTML-коде
        for i in date:
            if not (48 <= ord(i) <= 57 or ord(i) == 46):
                raise Exception_symbols_not_for_date
        list = date.split(".")
        if (len(list) < 3 or list[1] == "" or list[2] == ""):
            raise Exception_bad_format_date
        day = int(list[0])
        if not (1 <= day <= 31):
            raise Exception_bad_day
        month = int(list[1])
        if not (1 <= month <= 12):
            raise Exception_bad_month
        year = int(list[2])
        if not (1900 <= year <= 2023):
            raise Exception_bad_year
        return True
    except (Exception_symbols_not_for_date, Exception_bad_format_date, 
            Exception_bad_day, Exception_bad_month, Exception_bad_year) as e:
        print(e)
        return False
    
    
def check_telephon_number(value):
    """Проверка правильности ввода телефонного номера"""
    try:
        int(value)
        return True
    except ValueError:
        print("\033[1m\033[31m{}\033[0m".format("Ошибка: телефон должен состоять из цифр без форматирования!!!"))
        return False
    

def check_input_gender(value):
    """Проверка правильности ввода пола"""
    try:
        if len(value) > 1:
            raise Exception_bad_gender
        # Коды 102 - латиницей "f" в HTML-коде
        # Коды 109 - латиницей "m" в HTML-коде
        if not (ord(value) == 102 or ord(value) == 109):
            raise Exception_bad_gender
        return True
    except Exception_bad_gender as e:
        print(e)
        return False



