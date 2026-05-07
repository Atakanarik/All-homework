#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float avg = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0;
            int rounded = (int) round(avg);
            image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue = rounded;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
        for (int j = 0; j < width; j++)
            copy[i][j] = image[i][j];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float tR = 0, tG = 0, tB = 0, count = 0;
            for (int r = -1; r <= 1; r++)
            {
                for (int c = -1; c <= 1; c++)
                {
                    if (i + r >= 0 && i + r < height && j + c >= 0 && j + c < width)
                    {
                        tR += copy[i + r][j + c].rgbtRed;
                        tG += copy[i + r][j + c].rgbtGreen;
                        tB += copy[i + r][j + c].rgbtBlue;
                        count++;
                    }
                }
            }
            image[i][j].rgbtRed = (int) round(tR / count);
            image[i][j].rgbtGreen = (int) round(tG / count);
            image[i][j].rgbtBlue = (int) round(tB / count);
        }
    }
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
        for (int j = 0; j < width; j++)
            copy[i][j] = image[i][j];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float gxR = 0, gxG = 0, gxB = 0;
            float gyR = 0, gyG = 0, gyB = 0;

            for (int r = -1; r <= 1; r++)
            {
                for (int c = -1; c <= 1; c++)
                {
                    if (i + r >= 0 && i + r < height && j + c >= 0 && j + c < width)
                    {
                        gxR += Gx[r + 1][c + 1] * copy[i + r][j + c].rgbtRed;
                        gxG += Gx[r + 1][c + 1] * copy[i + r][j + c].rgbtGreen;
                        gxB += Gx[r + 1][c + 1] * copy[i + r][j + c].rgbtBlue;

                        gyR += Gy[r + 1][c + 1] * copy[i + r][j + c].rgbtRed;
                        gyG += Gy[r + 1][c + 1] * copy[i + r][j + c].rgbtGreen;
                        gyB += Gy[r + 1][c + 1] * copy[i + r][j + c].rgbtBlue;
                    }
                }
            }

            int red = round(sqrt(gxR * gxR + gyR * gyR));
            int green = round(sqrt(gxG * gxG + gyG * gyG));
            int blue = round(sqrt(gxB * gxB + gyB * gyB));

            image[i][j].rgbtRed = (red > 255) ? 255 : red;
            image[i][j].rgbtGreen = (green > 255) ? 255 : green;
            image[i][j].rgbtBlue = (blue > 255) ? 255 : blue;
        }
    }
}
