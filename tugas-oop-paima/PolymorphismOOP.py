class Rectangle:
    def __init__(self, height:int, base:int):
        self.height = height
        self.base = base

    def calculated_area(self):
        area = self.height * self.base / 2
        return area


class Circle:
    def __init__(self, radius:int):
        self.radius = radius
    
    def calculated_area(self):
        area = self.radius * 3.14
        return area
    
if __name__ == "__main__":
    segitiga = Rectangle(10,5)
    lingkaran = Circle(14)

    print(segitiga.calculated_area())
    print(lingkaran.calculated_area())

