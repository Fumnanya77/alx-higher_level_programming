#include "hash_tables.h"

/**
 * hash_table_create - Create a hash table
 *
 * @size: the size of the hash yable
 *
 * Return: A pointer to the newly created table
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *new;
	unsigned long int i;

	new = malloc(sizeof(hash_table_t));
	if (new == NULL)
	{
		return (NULL);
	}

	new->size = size;
	new->array = calloc(new->size, sizeof(hash_node_t *));

	for (i = 0; i < new->size; i++)
		new->array[i] = NULL;

	return (new);
}
