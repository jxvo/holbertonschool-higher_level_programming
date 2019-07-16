#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks whether list is a palindrome or not
 * @head: double pointer to head node
 *
 * Return: 1 if True, 0 if False or failure
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	int arr_vals[9000], idx, len = 0;

	if (!head)
		return (0);
	if (head && !*head)
		return (1);

	node = *head;

	while (node)
	{
		node = node->next;
		len++;
	}
	/*arr_vals = malloc(sizeof(int) * (len));
	if (!arr_vals)
	return (0);*/
	node = *head;
        for (idx = 0; node; idx++)
	{
		arr_vals[idx] = node->n;
		node = node->next;
	}
	for (idx = 0, len--; idx < len; idx++, len--)
	{
		if (arr_vals[idx] != arr_vals[len])
		{
			/*free(arr_vals);*/
			return (0);
		}
	}
	/*free(arr_vals);*/
	return (1);
}
