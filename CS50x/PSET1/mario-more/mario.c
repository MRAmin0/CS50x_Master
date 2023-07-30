#include <cs50.h>
#include <stdio.h>

int main(void)
{

    int h;
    do
    {
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);
    for (int i = 0; i < h; i++)
    {
        // insert space before mario stair
        for (int s = 0; s < h - (i + 1); s++)
        {
            printf(" ");
        }
        // insert '#' for make stair
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        // insert 2 space between blocks
        printf("  ");
        // insert '#' for next block
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}