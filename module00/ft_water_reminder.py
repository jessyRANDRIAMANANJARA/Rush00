# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hrandri2 <hrandri2@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/12 14:38:14 by hrandri2          #+#    #+#              #
#    Updated: 2026/03/12 14:38:14 by hrandri2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    water_r = int(input("Days since last watering: "))
    if water_r > 2:
        print("Water the plant!")
    else :
        print("Plant are fine")