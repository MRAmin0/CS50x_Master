#include <cs50.h>
#include <stdio.h>

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
        // m
        if (isalpha(argv[i][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
}