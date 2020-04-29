#include "lists.h"
/**
 * insert_node - adds a new int node in numeric order
 * @head: pointer to sorted list
 * @number: int to add
 * Return: pointer to list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cpy;
	listint_t *ptr;

	ptr = malloc(sizeof(listint_t));
	if (ptr != NULL)
		return (NULL);
	cpy = *head;
	ptr->n = number;
	if (!*head || cpy->n > number)
	{
		ptr->next = *head;
		*head = ptr;
		return (ptr);
	}
	while (cpy->next)
	{
		if (cpy->next->n >= number)
		{
			ptr->next = cpy->next;
			cpy->next = ptr;
			return (ptr);
		}
		cpy = cpy->next;
	}
	ptr->next = NULL;
	cpy->next = ptr;
	return (ptr);
}
