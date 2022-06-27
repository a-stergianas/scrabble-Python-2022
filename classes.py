from random import shuffle

letters = { 'Α': [12, 1], 'Β': [1, 8], 'Γ': [2, 4],  'Δ': [2, 4],  'Ε': [8, 1],
            'Ζ': [1, 10], 'Η': [7, 1], 'Θ': [1, 10], 'Ι': [8, 1],  'Κ': [4, 2],
            'Λ': [3, 3],  'Μ': [3, 3], 'Ν': [6, 1],  'Ξ': [1, 10], 'Ο': [9, 1],
            'Π': [4, 2],  'Ρ': [5, 2], 'Σ': [7, 1],  'Τ': [8, 1],  'Υ': [4, 2],
            'Φ': [1, 8],  'Χ': [1, 8], 'Ψ': [1, 10], 'Ω': [3, 3]
           }


class SakClass:
    def __init__(self):
        self.lettersInside = []
        self.itemCount = 0
        for letter in letters:
            for i in range(letters[letter][0]):
                self.lettersInside.append(letter)
                self.itemCount += 1
        self.randomize_sak()

    def xara(self):
        print(self.lettersInside)
        print(self.itemCount)

    def getletters(self, amount):
        letterstoreturn = []
        for i in range(amount):
            letterstoreturn.append(self.lettersInside.pop(0))
        self.itemCount -= amount
        return letterstoreturn

    def putbackletters(self, returnedletters):
        for i in returnedletters:
            self.lettersInside.append(i)
        self.randomize_sak()
        self.itemCount += len(returnedletters)

    def randomize_sak(self):
        shuffle(self.lettersInside)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.lettersInHand = []

    def __repr__(self):
        repr(", ".join(letter for letter in self.lettersInHand))

    def printLettersInHand(self):
        stringToReturn = ""

        for letter in self.lettersInHand:
            stringToReturn += letter + "[" + str(letters[letter][1]) + "], "
        return stringToReturn[:-2]

class Human(Player):
    def play(self):
        return input("ΛΕΞΗ: ")

class Computer(Player):
    def play(self):
        print("Edo tha paizei to pc")


class Game:
    def __init__(self, player: Human, pc: Computer):
        self.player = player
        self.pc = pc
        self.keepPlaying = True
        self.dictionary = open("greek7.txt", encoding="utf8").read().splitlines()

        self.setup()

    def __repr__(self):
        return repr("This is the game")

    def setup(self):
        self.round = 0
        self.playerPoints = 0
        self.pcPoints = 0

        self.sak = SakClass()

        for letter in self.sak.getletters(7):
            self.player.lettersInHand.append(letter)

        for letter in self.sak.getletters(7):
            self.pc.lettersInHand.append(letter)

        self.run()

    def run(self):
        while True:
            self.round += 1
            print("--------------------")
            print("Γύρος:         " + str(self.round))
            print("Σκορ:          " + str(self.playerPoints) + "-" + str(self.pcPoints))
            print("Στο σακουλάκι: " + str(self.sak.itemCount) + " γράμματα\n")

            if self.round % 2 == 1:
                print("Σειρά του " + self.player.name)
                print("Γράμματα: " + self.player.printLettersInHand())
                playedWord = self.player.play()

                while (playedWord == "q" and len(self.player.lettersInHand) <= self.sak.itemCount) or (
                        playedWord == "p" and len(self.player.lettersInHand) > self.sak.itemCount) or self.checkWord(
                        playedWord) == False:
                    print("--------------------")
                    if playedWord == "q":
                        print("Δεν μπορείτε να σταματήσετε το παιχνίδι όσο μπορείτε να πάτε πάσο.")
                    elif playedWord == "p":
                        print("Δεν υπάρχουν αρκετά γράμματα στο σακουλάκι για να πάτε πάσο. Μπορείτε όμως να σταματήσετε.")
                    else:
                        print("ΜΗ ΑΠΟΔΕΚΤΗ ΛΕΞΗ. Προσπάθησε ξανα.")
                    print("Γράμματα: " + self.player.printLettersInHand())
                    playedWord = self.player.play()

                if playedWord == "q":
                    print("Ο " + self.player.name + " δεν μπορεί να συνεχίσει.")
                    self.end()
                elif playedWord == "p":
                    print("Ο " + self.player.name + " πήγε πάσο. Τα γράμματά του αλλάχθηκαν.")
                    self.sak.putbackletters(self.player.lettersInHand)
                    self.player.lettersInHand = []
                    for letter in self.sak.getletters(7):
                        self.player.lettersInHand.append(letter)
                else:
                    points = self.countPoints(playedWord)
                    print("AΠΟΔΕΚΤΗ ΛΕΞΗ! Πήρατε " + str(points) + " πόντους.")
                    self.playerPoints += points
                    self.removeLetters(playedWord)
                    for letter in self.sak.getletters(len(playedWord)):
                        self.player.lettersInHand.append(letter)

            else:
                print("Σειρά του " + self.pc.name)
                print("Γράμματα: " + self.pc.printLettersInHand())
                self.pc.play()

    def checkWord(self, word):
        if word == "p" or word == "q":
            return True

        testLettersInHand = str("".join(letter for letter in self.player.lettersInHand))
        count = 0
        for i in range(len(word)):
            flag = True
            for y in range(len(testLettersInHand)):
                if word[i] == testLettersInHand[y] and flag == True:
                    flag = False
                    testLettersInHand = testLettersInHand[:y] + "-" + testLettersInHand[(y+1):]
                    count += 1

        if count != len(word):
            return False

        if word not in self.dictionary:
            return False

        return True

    def countPoints(self, word):
        points = 0
        for letter in word:
            for i in letters:
                if letter == i:
                    points += letters[i][1]
                    break
        return points

    def removeLetters(self, word):
        for i in word:
            for y in self.player.lettersInHand:
                if i == y:
                    self.player.lettersInHand.remove(y)


    def end(self):
        print("telos paixnidioy")
