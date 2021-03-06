#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node at a given index
 * @head: double pointer to head node
 * @number: value of new node
 *
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *node, *prev;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	prev = NULL;
	node = *head;
	while (node && node->n < number)
	{
		prev = node;
		node = node->next;
	}
	new->next = node;
	if (prev)
		prev->next = new;
	else
		*head = new;
	return (new);
}
