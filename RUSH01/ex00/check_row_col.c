/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_row_col.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hrandri2 <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/23 21:39:41 by hrandri2          #+#    #+#             */
/*   Updated: 2025/11/23 21:39:43 by hrandri2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	check_col_up(int tab[4][4], int pos, int entry[16])
{
	int	i;
	int	max_size;
	int	visible_boxes;

	i = -1;
	max_size = 0;
	visible_boxes = 0;
	if (pos / 4 == 3)
	{
		while (++i < 4)
		{
			if (tab[i][pos % 4] > max_size)
			{
				max_size = tab[i][pos % 4];
				visible_boxes++;
			}
		}
		if (entry[pos % 4] != visible_boxes)
			return (1);
	}
	return (0);
}

int	check_row_right(int tab[4][4], int pos, int entry[16])
{
	int	i;
	int	max_size;
	int	visible_boxes;

	i = 4;
	max_size = 0;
	visible_boxes = 0;
	if (pos % 4 == 3)
	{
		while (--i >= 0)
		{
			if (tab[pos / 4][i] > max_size)
			{
				max_size = tab[pos / 4][i];
				visible_boxes++;
			}
		}
		if (entry[12 + pos / 4] != visible_boxes)
			return (1);
	}
	return (0);
}

int	check_col_down(int tab[4][4], int pos, int entry[16])
{
	int	i;
	int	max_size;
	int	visible_boxes;

	i = 4;
	max_size = 0;
	visible_boxes = 0;
	if (pos / 4 == 3)
	{
		while (--i >= 0)
		{
			if (tab[i][pos % 4] > max_size)
			{
				max_size = tab[i][pos % 4];
				visible_boxes++;
			}
		}
		if (entry[4 + pos % 4] != visible_boxes)
			return (1);
	}
	return (0);
}

int	check_row_left(int tab[4][4], int pos, int entry[16])
{
	int	i;
	int	max_size;
	int	visible_boxes;

	i = -1;
	max_size = 0;
	visible_boxes = 0;
	if (pos % 4 == 3)
	{
		while (++i < 4)
		{
			if (tab[pos / 4][i] > max_size)
			{
				max_size = tab[pos / 4][i];
				visible_boxes++;
			}
		}
		if (entry[8 + pos / 4] != visible_boxes)
			return (1);
	}
	return (0);
}
