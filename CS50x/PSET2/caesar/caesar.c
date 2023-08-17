#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if(argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    int n = trlen(argv[1]);
    for (int i = 0;i < n; i++)
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
    int key = atio(argv[1]);

    printf("ciphertext: ");
    char ci;
    int nn = strlen(plain);
    char cipher[nn];


    for (int j =0; j < nn ; j++)
    {
        int c = plain[j];
        if(isalpha(c))
        {
            ci = c+ key % 26;

            if(!(islower(ci)|| isupper(ci)))
            {
                ci -=26;
            }
        }
        else
        {
            c
        }
    }

}