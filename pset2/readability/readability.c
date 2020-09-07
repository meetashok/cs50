#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

// function declaration to be defined later
float coleman_liau(float l, float s);

int main(void)
{
    // reading input string
    string s = get_string("Text: ");
    
    // initializations, words is initialized to 1 as the last word is not counted
    int words = 1;
    int characters = 0;
    int sentences = 0;
    
    // for loop to count words, characters and sentences
    for (int i = 0, length = strlen(s); i < length; i++)
    {
        if (s[i] == ' ') 
        {
            words++;
        } 
        else if (s[i] == '.' || s[i] == '?' || s[i] == '!')
        {
            sentences++;
        } 
        else if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z'))
        {
            characters++;
        }
        else 
        {
            continue;   
        }
    }
    
    // calculate readability index
    float L = (float) characters / words * 100;
    float S = (float) sentences / words * 100;
    float index = coleman_liau(L, S);
    
    // printing results
    if (index < 1) 
    {
        printf("Before Grade 1");
    }
    else if (index > 16)
    {
        printf("Grade 16+");
    }
    else 
    {
        printf("Grade %i", (int) round(index));
    }
    printf("\n");
}

float coleman_liau(float L, float S) 
{
    return 0.0588 * L - 0.296 * S - 15.8;
}