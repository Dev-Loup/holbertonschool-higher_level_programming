#include "lists.h"

/**
 * is_palindrome - check if a linked lists is palindrome
 * @head: head pointer to linked list
 * Return: 0 on Success, 1 if palindrome is approved.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tail = *head;
	listint_t *nose = *head;
	int idxtail;
	int mvtail;
	int idxhead;

	if (*head == NULL)
		return (1);
	for (idxtail = 0; tail; idxtail++)
	{
		if (tail->next)
		{
			tail = tail->next->next;
			idxtail++;
		}
		else
			tail = tail->next;
	}
	idxtail--;
	for (idxhead = 0; idxhead < idxtail; idxhead++, idxtail--)
	{
		tail = *head;
		for (mvtail = 0; mvtail < idxtail; mvtail++)
		{
			tail = tail->next;
		}
		if (nose->n != tail->n)
			return (0);
		nose = nose->next;
	}
	return (1);
}
