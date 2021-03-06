"""
The Subtraction Game (Thai 21 version)

CMS 195, Spring 2020
"""

stones = 21
player = 1

playing = True

while playing:

    # Print the current player
    print("It's player %d's turn." % player)
    print(stones)

    # Prompt the player to remove 1, 2, or 3 stones and read the input value
    remove = int(input('Choose 1, 2, or 3 stones to remove: '))
    
    # If the player enters 1, 2, or 3, update the number of stones
    if remove == 1 or remove == 2 or remove == 3:
        stones = stones - remove
    
    # Else, print "You can't do that."
    else:
        print("You can't do that.")
    
    # If there are 0 stones remaining, set playing = False
    if stones == 0:
        print("You win!")
        playing = False
    
    # Else, switch to the other player
    else:
        if player == 1:
            player = 2
            
        elif player == 2:
            player = 1
    
