# Program: Bottles of Beer Program
# Author: Zachariah King
# Date: 01/12/25
# Description: This program asks the user how many bottles of beer there are on the wall and then performs
#              a countdown of the amount while mimicking the famous song. When the user is about to run out
#              of beer, the program reminds the user to buy more beer.

def countdown_bottles(bottles):
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles-1} bottles of beer on the wall.\n")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        bottles -= 1
    
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.\n")

def main():
    try:
        bottles = int(input("How many bottles of beer are on the wall? "))
        if bottles <= 0:
            print("You need at least 1 bottle of beer to start.")
        else:
            countdown_bottles(bottles)
    except ValueError:
        print("Please enter a valid number.")

# Run the program
main()
