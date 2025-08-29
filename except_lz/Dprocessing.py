# Необходимо написать класс, который будет обрабатывать полученный датасет: проверять его наличие в дириктории, пытаться открыть,
# свериться с ожидаемой структурой и выдать сообщение, если все успешно выполнилось. В противном случа - обработать с помощью
# исключений все возникшие ошибки, сопроводить каждую из них понятным сообщением об ошибке.


#--------------------------------------------------------------------------------------------------------------------------------

import os 
import pandas as pd  

class Data_Proc:
    def __init__(self, filename):
        self.filename = filename
        # Прописываю ожидаемые названия столбцов.
        self.expected_columns = [ "Участники гражданского оборота", "Тип операции", "Сумма операции", "Вид расчета",
            "Место оплаты", "Терминал оплаты", "Дата оплаты", "Время оплаты", "Результат операции", "Cash-back", "Сумма cash-back"]        
         
        # Прописываю ожидаемые тип данных каждого столбца.
        self.expected_dtypes = {"Участники гражданского оборота": object, "Тип операции": object, "Сумма операции": float, "Вид расчета": object,
            "Место оплаты": object, "Терминал оплаты": object, "Дата оплаты": object, "Время оплаты": object, "Результат операции": object,
            "Cash-back": object,"Сумма cash-back": float }
        
    # Создаю метод для проверки файла.
    def validate_file(self):
        try:
            if not os.path.exists(self.filename):                                                       # Проверяем существует ли файл.
                raise FileNotFoundError(f"[Errno 2] No such file or directory: '{self.filename}'")      # Если файл не найден вызываем исключение FileNotFoundError.

            df = pd.read_csv(self.filename) 

            if df.empty:                                                                                # Проверяем пустой ли датафрейм.
                raise ValueError("Возникла следующая ошибка: Датафрейм пуст")                           # Если нет данных в таблице вызываем исключение ValueError.

            if list(df.columns) != self.expected_columns:                                               # Проверяем названия столбцов. 
                print("Названия столбцов не совпадают.")
                print("Ожидаемые:", self.expected_columns)
                print("Фактические:", list(df.columns))
                return
            
            for column, expected_type in self.expected_dtypes.items():                                  # Проверяем типы данных.
                actual_type = df[column].dtype                                                          # Получаем фактический тип данных для текущего столбца
                if actual_type != expected_type:                                                        # Сравниваем типы.
                    print(f"В столбце '{column}' тип данных не соответствует ожидаемому.")
                    print(f"Ожидается: {expected_type.__name__}, Фактически: {actual_type}")
                    return

            print("Чтение датафрейма завершено успешно.")

        except FileNotFoundError as e:
            print(f"Возникла следующая ошибка: {e}")
        except ValueError as e:
            print(e)
     