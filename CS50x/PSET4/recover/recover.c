#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc < 2 )
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
    //OPEN FILE WITH MODE WRITE
    FILE *file = fopen(argv[1], "r");

    unsigned char *temp = malloc(512);

    char *filename = malloc (3 * sizeof(int));
    if (filename == NULL )
    {
        return 1;
    }
    int image = 0;
    if (temp == NULL )
    {
        return 1;
    }
    while (fread (temp,sizeof(unsigned char), 512 , file))
    {
        if (temp[0] ==0xff)
    {
        return 1;
    }
    }


}