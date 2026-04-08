# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hrandri2 <hrandri2@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/27 08:54:05 by hrandri2          #+#    #+#              #
#    Updated: 2026/03/27 08:54:05 by hrandri2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class plant_blueprint:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def __str__(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"

plant1 = plant_blueprint("Rose", 25, 30)
plant2 = plant_blueprint("Sunflower", 80, 45)
plant3 = plant_blueprint("Cactus", 15, 120)
    
def ft_garden_data():
    print("=== Garden Plant Registry ===")
    print(plant1)
    print(plant2)
    print(plant3)

if __name__ == "__main__":
    ft_garden_data()