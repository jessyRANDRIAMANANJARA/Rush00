SRC = ./main.c \
      ./rush02.c \
      ./ft_putchar.c

OBJ = $(SRC:.c=.o)

CFLAGS += -Wall -Werror -Wextra

NAME = rush02

all:$(NAME)

$(NAME):$(OBJ)
    cc -o $(NAME) $(OBJ)

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean $(NAME)

.PHONY: all clean fclean re

