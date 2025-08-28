import os
import pandas
from datetime import date, datetime

# Декоратор для логирования
def log(func):
    def wrapper(*args, **kwargs):
        # Выполняем исходную функцию
        result = func(*args, **kwargs)

        # Получаем имя пользователя
        username = os.getlogin()

        # Имя функции
        func_name = func.__name__

        # Текущая дата и время
        today = date.today()
        formatted_date = today.strftime("%d-%m-%Y")
        now_time = datetime.now()
        formatted_time = now_time.strftime("%H:%M:%S")

        # Проверка наличия файла логов
        if os.path.exists("logs.csv"):
            file_df = pandas.read_csv("logs.csv")
            new_id = len(file_df)

            # Создаём новую строку с данными
            new_row = pandas.DataFrame({
                'id': [new_id],
                'pc_username': [username],
                'function_name': [func_name],
                'Date in date.month.year': [formatted_date],
                'Time': [formatted_time]
            })

            # Записываем без заголовка
            new_row.to_csv("logs.csv", mode="a", header=False, index=False)
        else:
            # Если файла нет то создаём с первой строкой
            df = pandas.DataFrame({
                'id': [0],
                'pc_username': [username],
                'function_name': [func_name],
                'Date in date.month.year': [formatted_date],
                'Time': [formatted_time]
            })
            df.to_csv("logs.csv", index=False)

        return result
    return wrapper
