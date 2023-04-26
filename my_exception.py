
class Exception_not_all_data_is_entered(Exception):
    """Класс исключения когда введены не все данные"""
    def __str__(self) -> str:
        return "\033[1m\033[31m{}\033[0m".format("Ошибка: Введены не все необходимые данные!!!")


class Exception_unnecessary_data_is_entered(Exception):
    """Класс исключения когда введены лишние данные"""
    def __str__(self) -> str:
        return "\033[1m\033[31m{}\033[0m".format("Ошибка: Введены лишние данные!!!")


class Exception_first_symbol_not_letter(Exception):
    """Класс исключения когда в Фамилии Имени или Отчестве первый символ не буква"""
    def __str__(self) -> str:
        return "\033[1m\033[31m{}\033[0m".format("Ошибка: В Фамилии Имени или Отчестве первый символ не буква!!!")
    

class Exception_first_symbol_not_capital_letter(Exception):
    """Класс исключения когда в Фамилии Имени или Отчестве первая буква не заглавная"""
    def __str__(self) -> str:
        return "\033[1m\033[31m{}\033[0m".format("Ошибка: Первая буква Фамилии Имени или Отчества не может быть не заглавной!!!")


class Exception_contain_symbol_not_being_letters(Exception):
    """Класс исключения когда в Фамилии Имени или Отчестве присутствуют символы не являющиеся буквами"""
    def __str__(self) -> str:
        return "\033[1m\033[31m{}\033[0m".format("Ошибка: В Фамилии Имени или Отчестве не могут присутствовать символы не являющиеся буквами!!!")


class Exception_symbols_not_for_date(Exception):
    """Класс исключения когда символы не соответствуют формату даты"""
    def __str__(self) -> str:
        return "\033[1m\033[31m{}\033[0m".format("Ошибка: Символы не соответствуют формату даты!!!")


class Exception_bad_format_date(Exception):
    """Класс исключения при не правильном формате даты"""
    def __str__(self) -> str:
        return "\033[1m\033[31m{}\033[0m".format('Ошибка: Неправильный формат даты - должны быть "день.месяц.год" !!!')


class Exception_bad_day(Exception):
    """Класс исключения когда день месяца вне диапазона чисел или равен 0"""
    def __str__(self) -> str:
        return "\033[1m\033[31m{}\033[0m".format("Ошибка: Количество дней месяца не может быть больше 31 или равен 0!!!")


class Exception_bad_month(Exception):
    """Класс исключения когда месяц вне диапазона чисел или равен 0"""
    def __str__(self) -> str:
        return "\033[1m\033[31m{}\033[0m".format("Ошибка: Номер месяца не может быть больше 12 или равно 0!!!")


class Exception_bad_year(Exception):
    """Класс исключения когда год вне диапазона чисел"""
    def __str__(self) -> str:
        return "\033[1m\033[31m{}\033[0m".format("Ошибка: Год не могжет быть меньше 1900 или больше 2023!!!")
    

class Exception_bad_gender(Exception):
    """Класс исключения для не правильно введенного пола"""
    def __str__(self) -> str:
        return "\033[1m\033[31m{}\033[0m".format('Ошибка: Не правильно введен пол - только "f" или "m" латиницей!!!')


