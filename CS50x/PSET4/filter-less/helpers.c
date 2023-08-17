#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int redmain,greenmain , bluemain;
    float grayout;

    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            redmain = image [i][j].rgbtRed;
            greenmain = image [i][j].rgbtGreen;
            bluemain = image [i][j].rgbtBlue;

            grayout = round((redmain + greenmain + bluemain) / 3.0);

            image [i][j].rgbtRed = grayout;
            image [i][j].rgbtGreen = grayout;
            image [i][j].rgbtBlue = grayout;


        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
        int redmain,greenmain , bluemain;
        int redsep,greensep , bluesep;
        for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            redmain = image [i][j].rgbtRed;
            greenmain = image [i][j].rgbtGreen;
            bluemain = image [i][j].rgbtBlue;

            grayout = round((redmain + greenmain + bluemain) / 3.0);

            image [i][j].rgbtRed = grayout;
            image [i][j].rgbtGreen = grayout;
            image [i][j].rgbtBlue = grayout;
        }
    }

}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
