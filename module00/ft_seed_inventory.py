# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hrandri2 <hrandri2@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/13 16:15:15 by hrandri2          #+#    #+#              #
#    Updated: 2026/03/13 16:15:15 by hrandri2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if unit == "packets":
        print (f"{seed_type} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print (f"{seed_type} seeds: {quantity} {unit} total")
    elif unit == "area":
        print (f"{seed_type} seeds: cover {quantity} square meters")
    else :
        print (f"Unknown unit type")