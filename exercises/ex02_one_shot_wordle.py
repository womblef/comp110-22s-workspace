"""ex02 one shot wordle"""

__author__ = "730530580"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secretword: str = "python"
boxes: str = ""
i: int = 0

char_in_secret: bool = False
j: int = 0

guess = input(f"What is your {len(secretword)}-guess? ")

while len(guess) != len(secretword):
    guess = input(f"That was not {len(secretword)} letters! Try again: ")

while(i < len(secretword)):
    if(secretword[i] == guess[i]):
        boxes += GREEN_BOX
    else:
        j = 0
        char_in_secret = False
        while not char_in_secret and j < len(secretword):
            if(guess[i] == secretword[j]):
                char_in_secret = True
            else:
                j += 1
        if(char_in_secret):
            boxes += YELLOW_BOX
        else:
            boxes += WHITE_BOX
    i += 1

print(boxes)

if(secretword == guess):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")