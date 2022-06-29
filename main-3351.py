from classes import *
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
            print("Σκορ")
        case '2':
            settings()
        case '3':
            gameOption()
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

main()
