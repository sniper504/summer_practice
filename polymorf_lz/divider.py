import pandas

class Divider:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pandas.read_csv(file_path)
        self.duplicates_removed = 0

    def split_dataset(self):
        # Разделяем на два CSV по признаку участники гражданского оборота
        self.individ_p = self.df[self.df['Участники гражданского оборота'] == 'физ. лицо']
        self.legal_p = self.df[self.df['Участники гражданского оборота'] == 'юр. лицо']

        self.individ_p.to_csv('individ_p.csv', index=False)
        self.legal_p.to_csv('legal_p.csv', index=False)

    def __invert__(self):
        # Удаляем дубликаты 
        before = len(self.df)
        self.df.drop_duplicates(inplace=True)
        after = len(self.df)
        self.duplicates_removed = before - after

        # Сохраняем изменённый df
        self.df.to_csv("var1_modified.csv", index=False)

        return self

    def print_result(self):
        print("Количество удалённых дубликатов:", self.duplicates_removed)
