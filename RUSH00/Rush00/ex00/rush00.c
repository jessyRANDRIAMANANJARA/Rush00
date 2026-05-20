/*
 * =============<< ********* >>=============
 * Author       : Jessy RANDRIA
 * Email        : randriamananjarajessy@gmail.com
 * Organization : jR
 * Created On   : 2025-12-08
 * Title        :
 * Description  :
 * Copyright (c) 2025 jR.
 * =============<< ********* >>=============
 */

void	ft_putchar(char c);

void	head(int j, int x)
{
	ft_putchar('o');
	while (j <= x)
	{
		if (j > 1 && j < x)
		{
			ft_putchar('-');
		}
		else if (j == x && x != 1)
		{
			ft_putchar('o');
		}
		j++;
	}
	write(1, "\n", 2);
}

void	between(int x, int k)
{
	while (k <= x)
	{
		if (k == 1)
			ft_putchar('|');
		if (k > 1 && k < x)
		{
			ft_putchar(' ');
		}
		else if (k == x && x != 1)
		{
			ft_putchar('|');
		}
		k++;
	}
	write(1, "\n", 2);
	k = 1;
}

void	base(int l, int x)
{
	ft_putchar('o');
	while (l <= x)
	{
		if (l > 1 && l < x)
		{
			ft_putchar('-');
		}
		else if (l == x && x != 1)
		{
			ft_putchar('o');
		}
		l++;
	}
	write(1, "\n", 2);
}

void	rush(int x, int y)
{
	int	i;
	int	j;
	int	k;
	int	l;

	i = 1;
	j = 1;
	k = 1;
	l = 1;
	if (x < 1 || y < 1 || x > 51 || y > 51)
		write(1, "error! Please enter a number between 1 and 50", 45);
	else
	{
		while (i <= y)
		{
			if (i == 1)
				head(j, x);
			else if (i > 1 && i < y)
				between(x, k);
			else if (i == y)
				base(l, x);
			i++;
		}
	}
}