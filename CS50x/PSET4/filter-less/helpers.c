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

            image[i][j].rgbtRed = (int) round(sepiaRed);
            image[i][j].rgbtGreen = (int) round(sepiaGreen);
            image[i][j].rgbtBlue = (int) round(sepiaBlue);
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE rowplace[width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            rowplace[j] = image[i][j];
        }
        for (int j = 0; j < height; j++)
        {
            image[i][j].rgbtRed = rowplace[width - j - 1].rgbtRed;
            image[i][j].rgbtGreen = rowplace[width - j - 1].rgbtGreen;
            image[i][j].rgbtBlue = rowplace[width - j - 1].rgbtBlue;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < height; w++)
        {
            copy[h][w] = image[h][w];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < height; j++)
        {
            int counter = 0;
            float redsum = 0;
            float greensum = 0;
            float bluesum = 0;

            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    if (!(i + k < 0 || i + k >= height || j + l < 0 || j + l >= width))
                    {
                        redsum += copy[i + k][j + l].rgbtRed;
                        greensum += copy[i + k][j + l].rgbtGreen;
                        bluesum += copy[i + k][j + l].rgbtBlue;
                        counter++;
                    }
                    else
                    {
                        continue;
                    }
                }
            }
            image[i][j].rgbtRed = (int) round(redsum / counter);
            image[i][j].rgbtGreen = (int) round(greensum / counter);
            image[i][j].rgbtBlue = (int) round(bluesum / counter);
        }
    }
}
