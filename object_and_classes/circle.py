class Circle:
    def __init__(self, diameter):
        self.diameter = diameter
        self.pi = 3.14

    def calculate_circumference(self):
        self.radius = self.diameter / 2
        self.circumferance = 2 * self.pi * self.radius
        return self.circumferance


    def calculate_area(self):
        self.radius = self.diameter / 2
        self.area = self.pi * self.radius**2
        return self.area

    def calculate_area_of_sector(self, angle):
        self.angle = angle
        self.radius = self.diameter / 2
        self.sector_area = (self.angle/360) * (self.pi * self.radius**2)
        return self.sector_area


circle = Circle(10)
angle = 5
# circumference = circle.calculate_circumference()
# print(circumference)
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
