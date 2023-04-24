class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        circumference = self.diameter * Circle.__pi
        return circumference

    def calculate_area(self):
        area = self.diameter**2 * Circle.__pi * 0.25
        return area

    def calculate_area_of_sector(self, angle):
        area_of_sector = (angle / 360) * Circle.__pi * self.diameter / 2 * self.diameter / 2
        return area_of_sector
