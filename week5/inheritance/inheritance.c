#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Each person has two parents and two alleles
#define GENERATIONS 3
#define INDENT_LENGTH 4

typedef struct person
{
    struct person *parents[2];   // NULL if no parents
    char alleles[2];             // 'A', 'B', or 'O'
} person;

// Function prototypes
person *create_family(int generations);
void free_family(person *p);
void print_family(person *p, int generation);
char random_allele(void);

int main(void)
{
    // Seed random number generator
    srand(time(0));

    // Create a new family with three generations
    person *p = create_family(GENERATIONS);

    // Print family tree of blood types
    print_family(p, 0);

    // Free memory
    free_family(p);

    return 0;
}

// Create a new individual with `generations`
person *create_family(int generations)
{
    // Allocate memory for a new person
    person *p = malloc(sizeof(person));
    if (p == NULL)
    {
        return NULL;
    }

    // If there are still generations left to create
    if (generations > 1)
    {
        // Create two new parents recursively
        p->parents[0] = create_family(generations - 1);
        p->parents[1] = create_family(generations - 1);

        // Set child's alleles based on parents
        p->alleles[0] = p->parents[0]->alleles[rand() % 2];
        p->alleles[1] = p->parents[1]->alleles[rand() % 2];
    }

    // If there are no generations left to create
    else
    {
        // Set parent pointers to NULL
        p->parents[0] = NULL;
        p->parents[1] = NULL;

        // Randomly assign alleles
        p->alleles[0] = random_allele();
        p->alleles[1] = random_allele();
    }

    // Return newly created person
    return p;
}

// Free `p` and all ancestors of `p`
void free_family(person *p)
{
    // Base case: handle NULL pointer
    if (p == NULL)
    {
        return;
    }

    // Recursively free parents first
    free_family(p->parents[0]);
    free_family(p->parents[1]);

    // Free the person structure itself
    free(p);
}

// Print each family member and their blood type
void print_family(person *p, int generation)
{
