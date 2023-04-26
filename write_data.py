def write_data(file_name, data):
    """Запись данных в файл"""
    try:
        # Для записи в файл используется менеджер контекста, 
        # который закроет файл автоматически вне зависимости 
        # от возникновения возможных исключений.
        with open(f"{file_name}.txt", 'a+', encoding='utf-8') as f:
            f.write(data + "\n")
    except Exception as e:
        print(e)