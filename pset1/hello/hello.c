#include <stdio.h>
#include <cs50.h>

int main(void) 
{
    // taking name from user input
    string name = get_string("What is your name?\n");
    
    //printing name to stdout
    printf("hello, %s\n", name);
}