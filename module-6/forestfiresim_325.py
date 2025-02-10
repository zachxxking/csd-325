# Jess Monnier, Ryan Monnier, Zachariah King
# CSD 325
# Assignment 6
# 9-Feb-2025


"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""
# Script further modified by Jess Monnier, Ryan Monnier, and Zachariah King for CSD 325


import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22
# Added constraints for lake
LAKE_BOUNDARY = {'left': 25,
                 'right': 55,
                 'top': 16,
                 'bottom': 7}

TREE = 'A'
FIRE = '@'
WATER = '≈' # Added water symbol to populate the lake with
EMPTY = ' '

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here:
                    continue

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Fire spreads to neighboring trees:
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    lake = [] # List to hold all lake coordinates
    # Generates random variations within the defined lake boundaries
    left = LAKE_BOUNDARY['left'] + random.randint(0,5)
    right = LAKE_BOUNDARY['right'] - random.randint(0,5)
    top = LAKE_BOUNDARY['top'] - random.randint(0,5)
    bottom = LAKE_BOUNDARY['bottom'] + random.randint(0,5)
    for x in range(LAKE_BOUNDARY['left'], LAKE_BOUNDARY['right']):
        for y in range(LAKE_BOUNDARY['bottom'], LAKE_BOUNDARY['top']):
            if left <= x <= right and bottom <= y <= top:
                lake.append((x, y))
        # Creates some variance in the shape of the lake, so its not always a rectangle 
        # We tried a larger range of variance but -1,1 seemed to do the best job of 
        # keeping the lake together, and not breaking off into multiple lakes
        top += random.randint(-1,1)
        left += random.randint(-1,1)
        bottom += random.randint(-1,1)
        right += random.randint(-1,1)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (x,y) in lake:
                forest[(x, y)] = WATER # Start as part of the lake.
            elif (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == WATER:
                bext.fg('blue') # Water is displayed in blue
                print(WATER, end='')
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
