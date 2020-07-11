# License Plate Generator
# Ervin Centeno
# September 25, 2018
# Lab3

import string
import random

replay = 'Yes'  # Creates a loop based on a while statement.

while replay == 'Yes':
    print('Enter state appreviation.')
    state = input()

    def plate(charSet = string.ascii_uppercase + string.digits):    # Function used for plate number generator.
        print('Enter the length of the plate.')
        size = input()

        print(str(state) + '-' + str(''.join(random.choice(charSet) for _ in range(int(size)))))
        # The string above compiles both the state and plate numbers in the same string.
    plate()

    print('Would you like to create another plate? (Yes or No.)')
    replay = input()
    if replay != 'Yes':     # Ends the loop.
        print("Session Closed!")



