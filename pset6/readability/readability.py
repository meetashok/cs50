from cs50 import get_string
from string import ascii_lowercase


def coleman_liau(L, S):
    # formula for coleman liau index
    # 0.0588 * L - 0.296 * S - 15.8
    return 0.0588 * L - 0.296 * S - 15.8


def print_grade(index):
    if index > 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {round(index)}")


s = get_string("Text: ")

words, sents, chars = 0, 0, 0
for c in s:
    if c in [".", "!", "?"]:
        sents += 1
    elif c == " ":
        words += 1
    elif c.lower() in ascii_lowercase:
        chars += 1

# to account for the last word        
words += 1
    
# L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.
L = chars / words * 100
S = sents / words * 100

index = coleman_liau(L, S)
print_grade(index)

