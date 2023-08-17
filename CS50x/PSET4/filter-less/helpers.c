#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int redmain, greenmain, bluemain;
    float grayout;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            redmain = image[i][j].rgbtRed;
            greenmain = image[i][j].rgbtGreen;
            bluemain = image[i][j].rgbtBlue;

            grayout = round((redmain + greenmain + bluemain) / 3.0);

            image[i][j].rgbtRed = grayout;
            image[i][j].rgbtGreen = grayout;
            image[i][j].rgbtBlue = grayout;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int originalRed, originalGreen, originalBlue;
    int sepiaRed, sepiaGreen, sepiaBlue;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            originalRed = image[i][j].rgbtRed;
            originalGreen = image[i][j].rgbtGreen;
            originalBlue = image[i][j].rgbtBlue;
            
            sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue;
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue;
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue;
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
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
