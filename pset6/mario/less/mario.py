from cs50 import get_int 

while True:
    # get user input
    n = get_int("Height: ")
    
    # keep prompting until n is in [1, 8]
    if (n >= 1) and (n <=8):
        break

# printing information 
for i in range(n):
    for j in range(n):
        # print # if jth index is greater than n - 1 - i
        if j >= n - i - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()