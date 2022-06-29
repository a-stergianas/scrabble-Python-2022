from classes import *
import json

pc = Computer("Η/Υ")

def main():
    print("***** SCRABBLE *****")
    print("--------------------")
    print("1: Σκορ")
    print("2: Ρυθμίσεις")
    print("3: Παιχνίδι")
    print("q: Έξοδος")
    print("--------------------")
    x = input("Επιλογή: ")

    while x != '1' and x != '2' and x != '3' and x != 'q':
        print("\n\n\n\n\n")
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
            showScores()
        case '2':
            settings()
        case '3':
            gameOption()
        case 'q':
            print("\nΕυχαριστούμε που έπαιξες!")
            quit()


def write_score(name):
    if name not in scores:
        scores[name] = 1
    else:
        scores[name] += 1
    with open("scores.txt", 'w') as f:
        json.dump(scores, f)


def read_scores():
    try:
        with open("scores.txt", 'r') as f:
            scores = json.load(f)
        return scores
    except IOError:
        # if file does not exist - we have no scores
        return {}

def showScores():
    print("--------------------")
    print("******* ΣΚΟΡ *******")
    scoresToPrint = read_scores()
    for name, score in scoresToPrint.items():
        print(name + ": " + str(score) + " νίκες")
    print("--------------------")
    print("1: Επιστροφή στο αρχικό μενού")
    print("q: Έξοδος")
    x = input("Επιλογή: ")

    while x != '1' and x != 'q':
        print("--------------------")
        print("1: Επιστροφή στο αρχικό μενού")
        print("q: Έξοδος")
        x = input("ΛΑΘΟΣ! Επέλεξε ξανά: ")

    match x:
        case '1':
            print("\n\n\n\n\n")
            main()
        case 'q':
            print("\nΕυχαριστούμε που έπαιξες!")
            quit()


def settings():
    print("--------------------")
    print("1: MIN Letters")
    print("2: MAX Letters")
    print("3: SMART")
    algorithm = input("Διάλεξε αλγόριθμο για τον υπολογιστή: ")

    while algorithm != '1' and algorithm != '2' and algorithm != '3':
        print("--------------------")
        print("1: MIN Letters")
        print("2: MAX Letters")
        print("3: SMART")
        algorithm = input("ΛΑΘΟΣ! Επέλεξε ξανά: ")

    pc.algorithm = algorithm
    print("\n\n\n\n\n")
    main()


def gameOption():
    print("--------------------")
    name = input("Γράψε το όνομά σου: ")
    player = Human(name)

    game = Game(player, pc)
    game.setup()
    game.run()
    if game.winner == game.player.name:
        write_score(game.winner)

    print("--------------------")
    print("1: Επιστροφή στο αρχικό μενού")
    print("q: Έξοδος")
    x = input("Επιλογή: ")

    while x != '1' and x != 'q':
        print("--------------------")
        print("1: Επιστροφή στο αρχικό μενού")
        print("q: Έξοδος")
        x = input("ΛΑΘΟΣ! Επέλεξε ξανά: ")

    match x:
        case '1':
            print("\n\n\n\n\n")
            main()
        case 'q':
            print("\nΕυχαριστούμε που έπαιξες!")
            quit()


scores = read_scores()
main()
