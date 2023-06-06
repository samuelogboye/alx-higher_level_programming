#include "lists.h"

/**
 * check_cycle - a function that checks if a linked list has cycle
 * @list: A list
 * Return: 0 if no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
		{
			return (1);
		}
	}

	return (0);
}
