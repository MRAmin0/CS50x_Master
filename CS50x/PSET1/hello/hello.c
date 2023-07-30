#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get user name
    string name = get_string("What's your name? ");
    //say hello to user's name
    printf("hello, %s\n", name);
}