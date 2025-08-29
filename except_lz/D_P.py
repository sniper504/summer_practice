import os
import pandas

class DataChecker:
    def __init__(self, file_path, expected_columns):
        self.file_path = file_path
        self.expected_columns = expected_columns
        self.df = None

    def check_and_load(self):
        try:
            #  Проверка наличия файла
            if not os.path.exists(self.file_path):
                raise FileNotFoundError("Файл не найден в директории")

            #  Попытка открыть CSV
            self.df = pandas.read_csv(self.file_path)

            #  Проверка структуры 
            for col in self.expected_columns:
                if col not in self.df.columns:
                    raise ValueError("Отсутствует столбец: " + col)

            # Если всё ok
            print("Файл успешно найден, открыт и проверен. Структура корректна.")

        except FileNotFoundError as e:
            print("Ошибка:", e)
        except pandas.errors.EmptyDataError:
            print("Ошибка: файл пустой")
        except pandas.errors.ParserError:
            print("Ошибка: неверный CSV-формат или повреждённый файл")
        except ValueError as e:
            print("Ошибка структуры:", e)
        except Exception as e:
            print("Непредвиденная ошибка:", e)



