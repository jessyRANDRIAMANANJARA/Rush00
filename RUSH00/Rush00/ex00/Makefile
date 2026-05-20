CC:cc
SRC:main.c ft_putchar.c rush00.c
OBJS:${SRC:.c=.o}
NAME:rush00
CFLAGS:-Wall -Werror -Wextra

all:${OBJS}
	CC ${SRC} ${CFLAGS} ${OBJS} ${NAME}
clear:
	rm -rf ${NAME}
fclean:clean
	rm -rf ${OBJS}
re:fclean all
.PHONY: all re