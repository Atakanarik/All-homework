// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table (using a larger prime for better distribution)
const unsigned int N = 10007;

// Hash table
node *table[N];

// Global word counter
unsigned int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Hash the word to find the bucket index
    unsigned int index = hash(word);

    // Walk the linked list in that bucket
    for (node *tmp = table[index]; tmp != NULL; tmp = tmp->next)
    {
        // Compare using case-insensitive string comparison
        if (strcasecmp(tmp->word, word) == 0)
        {
            return true;
        }
    }

    return false;
}

// Hashes word to a number (djb2 algorithm for better distribution)
unsigned int hash(const char *word)
{
    unsigned long hash_val = 5381;
    for (int i = 0; word[i] != '\0'; i++)
    {
        hash_val = ((hash_val << 5) + hash_val) + tolower(word[i]);
    }
    return hash_val % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open the dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    // Buffer for reading words
    char word[LENGTH + 1];

    // Read words one by one
    while (fscanf(file, "%45s", word) != EOF)
    {
        // Allocate memory for a new node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }

        // Copy word into node
        strcpy(n->word, word);

        // Find bucket index
        unsigned int index = hash(word);

        // Prepend node to the linked list
        n->next = table[index];
        table[index] = n;

        // Increment counter
        word_count++;
    }

    // Close dictionary
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Loop over all buckets
    for (int i = 0; i < N; i++)
    {
        // Walk the linked list and free every node
        node *tmp = table[i];
        while (tmp != NULL)
        {
            node *next = tmp->next; // Save next BEFORE freeing
            free(tmp);
            tmp = next;
        }
    }

    return true;
}
