import pandas
import matplotlib.pyplot as plt
from logs import log

class PlayerStats:
    @log
    def __init__(self, file_path):
        # Читаем CSV в DataFrame
        self.file_path = file_path
        self.df = pandas.read_csv(file_path)

    def plot_country_distribution(self):
        # Группируем данные по странам
        country_counts = self.df['country'].value_counts()

     # Строим круговую диаграмму
        plt.figure(figsize=(8, 8))
        plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
        plt.title('количество игроков PS')
        plt.axis('equal')  
        plt.show()  