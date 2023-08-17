#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("Text: ");

    float letter = 0;
    float word = 1;
    float sentence = 0;
    int n = strlen(text);
    for (int i = 0; i < n; i++)
    {
        if (isalpha(text[i]) != 0)
        {
            letter++;
        }
        // if (text[i] >= '97' && text[i] <= '122' || text[i] >= '65' && text[i] <= '90' )

        if (text[i] == 32)
        {
            word++;
        }
        if (text[i] == 46 || text[i] == 33 || text[i] == 63)
        {
        }
    }




   
}