# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hrandri2 <hrandri2@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/13 16:05:48 by hrandri2          #+#    #+#              #
#    Updated: 2026/03/13 16:05:48 by hrandri2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    day = int(input("Days until harvest: "))
    i = 1
    while i in range(day + 1):
        print(f"Day {i}")
        i += 1
    print("Harvest time!")