#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void) 
{
    float change;
    do 
    {
        change = get_float("Change owed: ");
    } 
    while (change < 0);
    
    // convert change to int by multiplying by 100
    int c = round(change * 100);
    
    // initialize n to 0, remaining to c
    int n = 0;
    int remaining = c;
    
    // check how many 25c coins are needed
    n += remaining / 25;
    remaining -= (remaining / 25) * 25;
    
    // add how many 10c coins are needed
    n += remaining / 10;
    remaining -= (remaining / 10) * 10;
    
    // add how many 5c coins are needed
    n += remaining / 5;
    remaining -= (remaining / 5) * 5;
    
    // add how many 1c coins are needed
    n += remaining;
    
    printf("%i\n", n);
}