# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hrandri2 <hrandri2@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/13 16:04:56 by hrandri2          #+#    #+#              #
#    Updated: 2026/03/13 16:04:56 by hrandri2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))
    
    def countdown(d):
        if(d >= 1):
            countdown(d - 1)
            print(f"day {d}")
    countdown(day)
    print("Harvest time!")
