#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * add_nodeint - adds a new node at the beginning
 * of listint_t list
 * @head: head of listint_t
 * @n: int to add in listint_t
 * Return: address of new element
 * or NULL if it fails
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *top;

	new = malloc(sizeof(listint_t));
	if (top == NULL)
		return (NULL);
	top->n = n;
	top->next = *head;
	*head = top;
	return (top);
}
/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: head of listint_t
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *head2 = head;
	listint_t *aux = NULL, aux2 = NULL;

	if (*head == NULL || head2->next == NULL)
		return (1);

	while (head2 != NULL)
	{
		add_nodeint(&aux, head2->n);
		head2 = head2->next;
	}
	aux2 = aux;

	while (head != NULL)
	{
		if ((*head)->n != aux2->n)
		{
			free_listint(aux);
			return (0);
		}
		*head = (*head)->next;
		aux2 = aux2->next;
	}
	free_listint(aux);
	return (1);

}
