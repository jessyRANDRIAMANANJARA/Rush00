
class plant_blueprint:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

plant1 = plant_blueprint("Rose", 25, 30)
plant2 = plant_blueprint("Oak", 200, 365)
plant3 = plant_blueprint("Cactus", 15, 120)
plant4 = plant_blueprint("Sunflower", 80, 45)
plant5 = plant_blueprint("Fern", 15, 120)

def ft_plant_factory():
    print("=== Plant Factory Output ===")
    