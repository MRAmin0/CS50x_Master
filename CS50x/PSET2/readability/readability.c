#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    string text = get_string("Text: ");

    int l = 0;
    int n = strlen(text);
    for (int i = 0; i <n; i++)
    {
        if (isalpha(text[i] == 1 ) || isalpha(text[i]) == 2)
        {
            l++;
        }
    }
    printf("l= %i\n",l);

}