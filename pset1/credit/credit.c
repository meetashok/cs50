#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    long cc = get_long("Number: ");
    
    long n = cc;
    int digits = 0;
    
    while (n != 0) 
    {
        digits++;
        n /= 10;
    }
    
    if (digits < 13) 
    {
        printf("INVALID");
    }
    else 
    {
        
    }
}