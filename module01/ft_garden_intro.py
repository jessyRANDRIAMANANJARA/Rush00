# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_intro.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hrandri2 <hrandri2@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/27 08:46:10 by hrandri2          #+#    #+#              #
#    Updated: 2026/03/27 08:46:10 by hrandri2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_intro():
    name = "Rose"
    height = 25
    age = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print(f"\n=== End of Program ===")

def main():
    ft_garden_intro()

# if __name__ == "__main__":
#     ft_garden_intro()
main()