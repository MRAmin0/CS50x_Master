// #include <stdio.h>
// #include <stdlib.h>

// int main(int argc, char *argv[])
// {
//     if (argc != 2)
//     {
//         printf("Usage: ./recover IMAGE\n");
//         return 1;
//     }
//     // OPEN FILE WITH MODE WRITE
//     FILE *file = fopen(argv[1], "r");

//     unsigned char *temp = malloc(512);

//     char *filename = malloc(3 * sizeof(int));
//     if (filename == NULL)
//     {
//         return 1;
//     }
//     int image = 0;
//     if (temp == NULL)
//     {
//         return 1;
//     }
//     while (fread(temp, sizeof(unsigned char), 512, file))
//     {
//         if (temp[0] == 0xff && temp[1] == 0xd8 && temp[2] == 0xff && (temp[3] & 0xf0) == 0xe0)
//         {
//             sprintf(filename, "%03i.jpg", image);
//             FILE *imgf = fopen(filename, "w");
//             fwrite(temp, 1, 512, imgf);
//             fclose(imgf);
//             image++;
//         }
//         else if (image != 0)
//         {
//             FILE *imgf = fopen(filename, "a");
//             fwrite(temp, 1, 512, imgf);
//             fclose(imgf);
//         }
//         free(temp);
//         free(filename);
//         fclose(file);
//         return 0;
//     }
// }
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }

    FILE *File = fopen(argv[1], "r");

    unsigned char *Temp = malloc(512);

    char *Filename = malloc(8 * sizeof(int));
    int file = 0;

    if (Temp == NULL)
    {
        return 1;
    }
    if (Filename == NULL)
    {
       return 1;
    }

    while (fread(Temp, sizeof(unsigned char), 512, File))
    {
        if (Temp[0] == 0xff && Temp[1] == 0xd8 && Temp[2] == 0xff && (Temp[3] & 0xf0) == 0xe0)
        {
            sprintf(Filename, "%03i.jpg", file);
            FILE *images = fopen(Filename, "w");
            fwrite(Temp, 1, 512, images);
            fclose(images);
            file = file + 1;
        }

        else if (file != 0)
        {
            FILE *images = fopen(Filename, "a");
            fwrite(Temp, 1, 512, images);
            fclose(images);
            free(Filename);
            fclose(File);
        }

    }
    free(Temp);


}