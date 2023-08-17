#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("Text: ");

    int l = 0;
    int w = 0;
    int n = strlen(text);
    for (int i = 0; i < n; i++)
    {
        if (isalpha(text[i]) != 0)
        {
            l++;
        }
        // if (text[i] >= '97' && text[i] <= '122' || text[i] >= '65' && text[i] <= '90' )


        if (text[i] == 32)
        {
            w++;
        }

    }
    printf("l = %i    w = %i\n",l,w);
}