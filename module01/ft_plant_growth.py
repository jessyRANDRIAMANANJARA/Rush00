# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hrandri2 <hrandri2@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/06 21:29:49 by hrandri2          #+#    #+#              #
#    Updated: 2026/04/06 21:29:49 by hrandri2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class plant_blueprint:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def age(init_day:int ,day:int):
    return (init_day + day)


def grow(init_height:int ,height:int):
    return (init_height + height)

plant1 = plant_blueprint("Rose", 25, 30)
plant2 = plant_blueprint("Sunflower", 80, 45)
plant3 = plant_blueprint("Cactus", 15, 120)

def get_info():
    plant = plant1
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
    i = 1
    while i in range (1,6):
        print(f"=== Day {i} ===")
        print(f"{plant.name}: {grow(plant.height, i)}cm, {age(plant.age, i)} days old")
        i += 1
    print(f"Growth this week: +{i - 1}cm")


if __name__ == "__main__":
    get_info()