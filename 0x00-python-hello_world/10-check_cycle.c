#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to first node of linked list
 *
 * Return: is there a cycle? 0 if no, 1 if yes
 */
int check_cycle(listint_t *list)
{
	listint_t *skippy;
	listint_t *node;

	if (!list || !list->next)
		return (0);
	node = list;
	skippy = list->next;

	while (skippy && skippy->next && node && node->next)
	{
		if (skippy == node)
			return (1);
		skippy = skippy->next->next;
	        if (!skippy)
			break;
		node = node->next;
	}
	return (0);
}
