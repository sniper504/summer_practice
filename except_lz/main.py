from D_P import DataChecker

def main():

    expected_columns = ["Участники гражданского оборота","Тип операции","Сумма операции","Вид расчета","Место оплаты","Терминал оплаты","Дата оплаты","Время оплаты","Результат операции","Cash-back","Сумма cash-back"]

    checker = DataChecker("var1.csv", expected_columns)
    checker.check_and_load()

if __name__ == "__main__":
    main()
