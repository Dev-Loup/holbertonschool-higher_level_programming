#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: pointer to head of the string
 * Return: 0 if there is no cycles, 1 if a cycle is found
 **/
int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *rabbit = list;
	int i = 0;

	while (rabbit)
	{
		for (i = 0; i <= 1; i++)
		{
			rabbit = rabbit->next;
		}
		if (rabbit == turtle)
			return (1);
		else
			turtle = turtle->next;
	}
	return (0);
}
