from classes import *
import os

global dictionary
dictionary = open("greek7.txt", encoding="utf8").read().splitlines()

print("***** SCRABBLE *****")
print("--------------------")
print("1: Σκορ")
print("2: Ρυθμίσεις")
print("3: Παιχνίδι")
print("q: Έξοδος")
print("--------------------")
x = input("Επιλογή: ")

while x != '1' and x != '2' and x != '3' and x != 'q':
    print("\n\n\n\n\n")  # os.system('cls') δεν δουλεύει για κάποιον λόγο
    print("***** SCRABBLE *****")
    print("--------------------")
    print("1: Σκορ")
    print("2: Ρυθμίσεις")
    print("3: Παιχνίδι")
    print("q: Έξοδος")
    print("--------------------")
    x = input("ΛΑΘΟΣ! Επέλεξε ξανά: ")

match x:
    case '1':
        print("Σκορ")
    case '2':
        print("Ρυθμίσεις")
    case '3':
        print("Παιχνίδι")
    case 'q':
        quit()

newGame = Game()
newPlayer = Human("Achill")
print(newPlayer.__repr__())

def binary_search(low, high, word):
    if high >= low:
        mid = (high + low) // 2
        if dictionary[mid] == word:
            return mid
        elif dictionary[mid] > word:
            return binary_search( mid - 1, low, word)
        else:
            return binary_search( high, mid + 1, word)
    else:
        return -1
