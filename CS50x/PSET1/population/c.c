#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size

    int start;

    {

        printf("hello  ");
        start = get_int("start size:");
    }
    while (start < 9);


    // TODO: Prompt for start size
    //هرشروعی پایانی دارد
    int end;
    do
    {
        end = get_int("end size:");
    }
    while (end < start);
    // TODO: Calculate number of Years until we reach threshold
    int Years = 0;
    while (start <= end)
    {
        start = start + (start / 3) - (start / 4);
        Years++;
    }
    // TODO: Print number of Years

    printf("Years: %i\n", Years);
}
