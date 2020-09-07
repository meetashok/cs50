#include "helpers.h"
#include <math.h>
#include <stdlib.h>

int to_int(float color);
void blur_pixel(int height, int width, RGBTRIPLE image_copy[height][width], RGBTRIPLE image[height][width], int i, int j);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int r = 0; r < height; r++)
    {
        for (int c = 0; c < width; c++)
        {
            float average = ((float)image[r][c].rgbtBlue + (float)image[r][c].rgbtGreen + (float)image[r][c].rgbtRed) / 3;
            image[r][c].rgbtBlue = (int) round(average);
            image[r][c].rgbtGreen = (int) round(average);
            image[r][c].rgbtRed = (int) round(average);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // formula for sepia
    // sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
    // sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
    // sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue
    for (int r = 0; r < height; r++)
    {
        for (int c = 0; c < width; c++)
        {
            float sepiaRed = 0.393 * image[r][c].rgbtRed + 0.769 * image[r][c].rgbtGreen + 0.189 * image[r][c].rgbtBlue;
            float sepiaGreen = 0.349 * image[r][c].rgbtRed + 0.686 * image[r][c].rgbtGreen + 0.168 * image[r][c].rgbtBlue;
            float sepiaBlue = 0.272 * image[r][c].rgbtRed + 0.534 * image[r][c].rgbtGreen + 0.131 * image[r][c].rgbtBlue;
            
            image[r][c].rgbtBlue = to_int(sepiaBlue);
            image[r][c].rgbtGreen = to_int(sepiaGreen);
            image[r][c].rgbtRed = to_int(sepiaRed);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE(*image_copy)[width] = calloc(height, width * sizeof(RGBTRIPLE));
    
    for (int r = 0; r < height; r++)
    {
        for (int c = 0; c < width; c++)
        {
            image_copy[r][c].rgbtBlue = image[r][c].rgbtBlue;
            image_copy[r][c].rgbtGreen = image[r][c].rgbtGreen;
            image_copy[r][c].rgbtRed = image[r][c].rgbtRed;
        }
    }
    
    for (int r = 0; r < height; r++)
    {
        for (int c = 0; c < width; c++)
        {
            image[r][c].rgbtBlue = image_copy[r][width - 1 - c].rgbtBlue;
            image[r][c].rgbtGreen = image_copy[r][width - 1 - c].rgbtGreen;
            image[r][c].rgbtRed = image_copy[r][width - 1 - c].rgbtRed;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE(*image_copy)[width] = calloc(height, width * sizeof(RGBTRIPLE));
    
    for (int r = 0; r < height; r++)
    {
        for (int c = 0; c < width; c++)
        {
            image_copy[r][c].rgbtBlue = image[r][c].rgbtBlue;
            image_copy[r][c].rgbtGreen = image[r][c].rgbtGreen;
            image_copy[r][c].rgbtRed = image[r][c].rgbtRed;
        }
    }
    
    for (int r = 0; r < height; r++)
    {
        for (int c = 0; c < width; c++)
        {
            blur_pixel(height, width, image_copy, image, r, c);
        }
    }
    return;
}

int to_int(float color)
{
    int color_int = (int) round(color);
    if (color_int > 255)
    {
        return 255;
    }
    else 
    {
        return color_int;
    }
}

void blur_pixel(int height, int width, RGBTRIPLE image_copy[height][width], RGBTRIPLE image[height][width], int i, int j)
{
    int sum_blue = 0;
    int sum_green = 0;
    int sum_red = 0;
    int count = 0;
    
    for (int r = -1; r < 2; r++)
    {
        for(int c = -1; c < 2; c++)
        {
            int neigh_i = i + c;
            int neigh_j = j + r;
            
            if (neigh_i >= 0 && neigh_i < height && neigh_j >= 0 && neigh_j < width)
            {
                sum_blue += image_copy[neigh_i][neigh_j].rgbtBlue;
                sum_green += image_copy[neigh_i][neigh_j].rgbtGreen;
                sum_red += image_copy[neigh_i][neigh_j].rgbtRed;
                count++;
            }
        }
    }
    
    image[i][j].rgbtBlue = to_int((float)sum_blue / count);
    image[i][j].rgbtGreen = to_int((float)sum_green / count);
    image[i][j].rgbtRed = to_int((float)sum_red / count);
}