# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hrandri2 <hrandri2@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/12 14:28:06 by hrandri2          #+#    #+#              #
#    Updated: 2026/03/12 14:28:06 by hrandri2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    a = int(input("Day 1 harvest: "))
    b = int(input("Day 2 harvest: "))
    c = int(input("Day 3 harvest: "))
    total = a + b + c
    print(f"Total harvest: {total}")