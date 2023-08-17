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
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    string plain = get_string("plaintext: ");
    int key = atoi(argv[1]) % 26;

    printf("ciphertext: ");

    for (int j = 0, nn = strlen(plain); j < nn; j++)
    {
        char c = plain[j];
        char co;

        if (isalpha(c))
        {
            if (islower(c))
            {
                co = 'a' + (c - 'a' + key) % 26;
            }
            else
            {
                co = 'A' + (c - 'A' + key) % 26;
            }
        }
        else
        {
            co = c;
        }

        printf("ciphertext: %c", co);
    }

    printf("\n");
    return 0;
}
