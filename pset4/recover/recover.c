#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc == 1)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    
    FILE *file = fopen(argv[1], "r");
 
    if (!file)
    {
        printf("Count not open the file\n");
        return 1;
    }
    
    int filenumber = -1;
    char *filename = malloc(7);
    bool writing = false;
    
    FILE *image;

    BYTE *block = malloc(512);
    
    while (fread(block, 512, 1, file))
    {
        
        if (block[0] == 0xff && block[1] == 0xd8 && block[2] == 0xff && (block[3] == 0xe0 || block[3] == 0xe1 || block[3] == 0xe2 || block[3] == 0xe3 || block[3] == 0xe4 || block[3] == 0xe5 || block[3] == 0xe6 || block[3] == 0xe7 || block[3] == 0xe8 || block[3] == 0xe9 || block[3] == 0xea || block[3] == 0xeb || block[3] == 0xec || block[3] == 0xed || block[3] == 0xee))    
        {
            filenumber++;
            sprintf(filename, "%03d.jpg", filenumber);
            image = fopen(filename, "w");
            writing = true;
            
            printf("%i, %s\n", filenumber, filename);
        }
        
        if (writing)
        {
            fwrite(block, 512, 1, image);    
        }
        
    }
    
    fclose(file);
    free(block);
    free(filename);
    fclose(image);
    
}
