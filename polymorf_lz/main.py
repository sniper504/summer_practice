from divider import Divider

def main():
    file_path = "var1.csv"

    processor = Divider(file_path)
    ~processor  # удаляем дубликаты
    processor.split_dataset()
    processor.print_result()

if __name__ == "__main__":
    main()
