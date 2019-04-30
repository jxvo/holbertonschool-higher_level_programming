#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to first node of linked list
 *
 * Return: is there a cycle? 0 if no, 1 if yes
 */
int check_cycle(listint_t *list)
{
	listint_t *begin;
	listint_t *node;

	if (list == NULL)
		return (NULL);
	begin = list;
	node = list->next;
	while (node)
	{
		if (node == begin)
			return (1);
		else if (node == NULL)
		node = node->next;
	}
}
