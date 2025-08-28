from nonagon import Nonagon

nonagon = Nonagon(10)

print("Радиус описанной окружности:", nonagon.circumcircle_radius())
print("Площадь описанной окружности:", nonagon.circumcircle_area())
print("Радиус вписанной окружности:", nonagon.incircle_radius())
print("Площадь вписанной окружности:", nonagon.incircle_area())
print("Площадь нонагона:", nonagon.area())
print("Периметр нонагона:", nonagon.perimetr())

nonagon.draw()
