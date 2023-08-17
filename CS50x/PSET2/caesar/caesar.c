#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    int n = strlen(argv[1]);
    for (int i = 0; i < n; i++)
    {
        // Exit if find alphabet
        if (isalpha(argv[i][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    string plain = get_string("plaintext:  ");
    // atoi : convert string to int
    int key = atoi(argv[1]);

    char co;
    int nn = strlen(plain);
    // char cipher[nn];

    for (int j = 0; j < nn; j++)
    {
        int c = plain[j];
        if (isalpha(c))
        {
            co = c + key % 26;

            if (!(islower(co) || isupper(co)))
            {
                co -= 26;
            }
        }
        else
        {
            co = c;
        }
        printf("%c", co);
    }
    printf("\n");
    return 0;
}