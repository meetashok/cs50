#include <stdio.h>
#include <cs50.h>

int main(void) 
{
    int n;
    do 
    {
        n = get_int("Input the height: ");
    } 
    // asks for input again if input is not in [1, 8]
    while (n <= 0 || n > 8);
    
    for (int i = 0; i < n; i ++) 
    {
        for (int j = 0; j < n; j++) 
        {
            // prints # if j > (n - i)
            // example, if i = 2, n = 8, then # should be printed for 
            // j = 5, 6, 7
            if (j >= (n - i - 1)) 
            {
                printf("#");
            } 
            else 
            {
                printf(" ");
            }
        }
        printf("\n");
    }
}