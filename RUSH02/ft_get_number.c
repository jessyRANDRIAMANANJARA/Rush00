/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_get_number.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hasratsi <hasratsi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/29 08:34:57 by hasratsi          #+#    #+#             */
/*   Updated: 2025/11/29 10:49:57 by hasratsi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int len(char *str)
{
	int i = 0;
	while (str[i])
		i++;
	return i;
}
int	verify(char c)
{
	if ((c == '-' || c == '+') || (c >= '0' && c <= '9'))
		return (1);
	else if ((c == ' ') || (c >= 9 && c <= 13))
		return (0);
	else
		return (1);
}

int	ft_atoi(char *str)
{
	int	i;
	int	count;
	int	number;

	count = 0;
	number = 0;
	i = -1;
	while (!verify(str[++i]) && str[i])
		;
	while (str[i])
	{
		if (str[i] == '-')
			count++;
		else if (str[i] == '+')
			;
		else
			break ;
		i++;
	}
	while (str[i++] >= '0' && str[i - 1] <= '9')
		number = number * 10 + (str[i - 1] - '0');
	if (count % 2 == 1)
		number = -number;
	return (number);
}

char *get_nth_line(int nb)
{
	char *buffer = malloc(sizeof(char) * 250);
	int i;
	FILE *file = fopen("./numbers.dict", "r");
	if (file == NULL)
	{
		printf("Error opening file!\n");
		return NULL;
	}
	i = 0;
	while (fgets(buffer, 250, file) != NULL)
	{
		// printf("%s", buffer);
		if (i == nb)
			return buffer;
		i++;
	}
}

void to_letter(char *nb)
{

	int c;
	int tmp;
	int *str;

	if (len(nb) <= 2)
	{
		if(ft_atoi(nb) <= 20)
		{
			c = ft_atoi(nb);
			printf("%s",get_nth_line(c));
			return ;
		}
		else
		{
			tmp = nb[0] - '0';
			c = 20 + (tmp - 2);
			printf("%s",get_nth_line(c));
			if((nb[1] - '0') != 0)
				to_letter(nb+1);
			return ;
		}
	}
	else if(len(nb) <= 3)
	{
		printf("%s",get_nth_line(nb[0]-'0'));
		printf("hundred\n");
		to_letter(nb+1);
	}
}


int main()
{
	// char *number = get_nth_line(28); // 545
	// printf("%s\n", number);
	to_letter("901");
}
