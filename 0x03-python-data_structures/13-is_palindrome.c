#include "lists.h"

/**
 * is_palindrome - check if singly linked list is a palindrome
 * @head: pointer to head of singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *currentNode;
	char buffer[8000];
	int i, length = 0;	

	if (!*head || !head)
		return (1);

	currentNode = *head;
	if (!currentNode->next)
		return (1);

	while (currentNode)
	{
		buffer[length] = currentNode->n;
		currentNode = currentNode->next;
		length++;
	}
	length = length - 1;
	for (; length >= 0 && i <= length; length--, i++)
	{
		if (buffer[length] != buffer[i])
			return (0);
	}
	return (1);
}
