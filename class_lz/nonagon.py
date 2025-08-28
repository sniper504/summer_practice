import math
import matplotlib.pyplot as plt
import numpy as np

class Nonagon:
    def __init__(self, side_length):
        self.side = side_length
        self.angle = 140  # внутренний угол девятиугольника
        self.k = 1 

    def circumcircle_radius(self):  # Радиус описанной окружности
        return self.side / (2 * math.sin(math.pi / 9))

    def circumcircle_area(self):  # Площадь описанной окружности
        r = self.circumcircle_radius()
        return math.pi * r**2

    def incircle_radius(self):  # Радиус вписанной окружности
        return self.side / (2 * math.tan(math.pi / 9))

    def incircle_area(self):  # Площадь вписанной окружности
        r = self.incircle_radius()
        return math.pi * r**2

    def area(self):  # Площадь девятиугольника
        cot_pi_9 = 1 / math.tan(math.pi / 9)
        return (9.0 / 4.0) * self.side**2 * cot_pi_9

    def perimetr(self):  # Периметр девятиугольника
        return self.side * 9

    def draw(self):
        fig, ax = plt.subplots(figsize=(15, 15))
        ax.set_aspect('equal')

        R_out = self.circumcircle_radius()
        R_in = self.incircle_radius()

        # координаты вершин девятиугольника
        x = [R_out * math.cos(2 * math.pi * i / 9) for i in range(9)]
        y = [R_out * math.sin(2 * math.pi * i / 9) for i in range(9)]

        ax.fill(x, y, color='black', label='Девятиугольник')

        # описанная окружность
        circle_circ = plt.Circle((0, 0), R_out, color="blue", fill=False, label="Описанная окружность")
        ax.add_patch(circle_circ)

        # вписанная окружность
        circle_in = plt.Circle((0, 0), R_in, color="red", fill=False, label="Вписанная окружность")
        ax.add_patch(circle_in)

        plt.legend()
        plt.grid()
        plt.show()



