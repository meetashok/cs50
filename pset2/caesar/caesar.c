#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

// prototype for checking if all characters of a string are digits
int is_digit(string s);

int main(int argc, string argv[])
{
    int key;
    
    // input validation
    if (argc != 2) 
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if (!is_digit(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else 
    {
        key = atoi(argv[1]);
    }
    
    // user input
    string s = get_string("plaintext: ");
    
    // converting to cipher
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (isupper(s[i])) 
        {
            int x = (int)(s[i] + key % 26);
            if (x > 90)
            {
                x = x % 90 + 64;
            }
            s[i] = (char) x;
        }
        else if (islower(s[i]))
        {
            int x = (int)(s[i] + key % 26);
            if (x > 122)
            {
                x = x % 122 + 96;
            }
            s[i] = (char) x;
        }
        else
        {
            continue;
        }
    }
    printf("ciphertext: %s\n", s);
}

// function definition
int is_digit(string s)
{
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}