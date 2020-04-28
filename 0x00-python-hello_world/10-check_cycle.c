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
	
	if (!turtle || !turtle->next)
		break;	
	while (rabbit)
	{
		rabbit = rabbit->next->next;
		if (rabbit == turtle)
			return (1);
		else
			turtle = turtle->next;
	}
	return (0);
}
