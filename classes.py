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
        if amount > self.itemCount:
            amount = self.itemCount
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
        self.algorithm = "3"

    def __repr__(self):
        repr(", ".join(letter for letter in self.lettersInHand))

    def printLettersInHand(self):
        stringToReturn = ""
        for letter in self.lettersInHand:
            stringToReturn += letter + "[" + str(letters[letter][1]) + "], "
        return stringToReturn[:-2]


class Human(Player):
    def play(self, sak):
        playedWord = input("ΛΕΞΗ: ")

        while (playedWord == "q" and len(self.lettersInHand) <= sak.itemCount) or (
                playedWord == "p" and len(self.lettersInHand) > sak.itemCount) or self.checkword(
            playedWord) == False:
            print("--------------------")
            if playedWord == "q":
                print("Δεν μπορείτε να σταματήσετε το παιχνίδι όσο μπορείτε να πάτε πάσο.")
            elif playedWord == "p":
                print("Δεν υπάρχουν αρκετά γράμματα στο σακουλάκι για να πάτε πάσο. Μπορείτε όμως να σταματήσετε.")
            else:
                print("ΜΗ ΑΠΟΔΕΚΤΗ ΛΕΞΗ. Προσπάθησε ξανα.")
            print("Γράμματα: " + self.printLettersInHand())
            playedWord = input("ΛΕΞΗ: ")

        return playedWord

    def checkword(self, word):
        if word == "p" or word == "q":
            return True

        testLettersInHand = str("".join(letter for letter in self.lettersInHand))
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

        if word not in dictionary:
            return False

        return True


class Computer(Player):
    def play(self, lettersInHand, lettersInBag):
        word = self.searchword(lettersInHand)
        if word == "nothing":
            if lettersInBag >= len(lettersInHand):
                return "p"
            else:
                return "q"
        else:
            return word

    def searchword(self, lettersInHand):
        # MIN Letters
        if self.algorithm == "1":
            for i in range(2, len(lettersInHand)):
                for y in self.permutations(lettersInHand, i):
                    wordToCheck = "".join(p for p in y)
                    if wordToCheck in dictionary:
                        return wordToCheck
            return "nothing"
        # MAX Letters
        elif self.algorithm == "2":
            for i in range(len(lettersInHand), 2, -1):
                for y in self.permutations(lettersInHand, i):
                    wordToCheck = "".join(p for p in y)
                    if wordToCheck in dictionary:
                        return wordToCheck
            return "nothing"
        # SMART
        else:
            highest = 0
            wordToReturn = "nothing"
            for i in range(2, len(lettersInHand)):
                for y in self.permutations(lettersInHand, i):
                    wordToCheck = "".join(i for i in y)
                    if wordToCheck in dictionary:
                        points = self.countpoints(wordToCheck)
                        if points > highest:
                            wordToReturn = wordToCheck
                            highest = points
            return wordToReturn

    def countpoints(self, word):
        points = 0
        for letter in word:
            for i in letters:
                if letter == i:
                    points += letters[i][1]
                    break
        return points

    def permutations(self, iterable, r):
        # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
        pool = tuple(iterable)
        n = len(pool)
        if r > n:
            return
        indices = list(range(n))
        cycles = list(range(n, n - r, -1))
        yield tuple(pool[i] for i in indices[:r])
        while n:
            for i in reversed(range(r)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i + 1:] + indices[i:i + 1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    yield tuple(pool[i] for i in indices[:r])
                    break
            else:
                return


class Game:
    def __init__(self, player: Human, pc: Computer):
        self.player = player
        self.pc = pc
        self.keepPlaying = True
        self.round = 0
        self.sak = SakClass()

        global dictionary
        if "dictionary" not in globals():
            dictionary = open("greek7.txt", encoding="utf8").read().splitlines()

    def __repr__(self):
        return repr("This is the game")

    def setup(self):
        for letter in self.sak.getletters(7):
            self.player.lettersInHand.append(letter)

        for letter in self.sak.getletters(7):
            self.pc.lettersInHand.append(letter)

    def run(self):
        while self.keepPlaying:
            self.round += 1
            print("--------------------")
            print("Γύρος:         " + str(self.round))
            print("Σκορ:          " + str(self.player.score) + "-" + str(self.pc.score))
            print("Στο σακουλάκι: " + str(self.sak.itemCount) + " γράμματα\n")

            # σειρά του παίκτη
            if self.round % 2 == 1:
                print("Σειρά του " + self.player.name)
                print("Γράμματα: " + self.player.printLettersInHand())
                playedWord = self.player.play(self.sak)

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
                    points = self.countpoints(playedWord)
                    print("AΠΟΔΕΚΤΗ ΛΕΞΗ! Πήρατε " + str(points) + " πόντους.")
                    self.player.score += points
                    for i in range(len(playedWord)):
                        self.player.lettersInHand.remove(playedWord[i])
                    for letter in self.sak.getletters(len(playedWord)):
                        self.player.lettersInHand.append(letter)

                if len(self.pc.lettersInHand) == 0:
                    self.end()

            # σειρά του υπολογιστή
            else:
                print("Σειρά του " + self.pc.name)
                print("Γράμματα: " + self.pc.printLettersInHand())
                lettersInHand = str("".join(letter for letter in self.pc.lettersInHand))
                playedWord = self.pc.play(lettersInHand, self.sak.itemCount)
                print(playedWord)

                if playedWord == "q":
                    print("Ο " + self.pc.name + " δεν μπορεί να συνεχίσει.")
                    self.end()
                elif playedWord == "p":
                    print("Ο " + self.pc.name + " πήγε πάσο. Τα γράμματά του αλλάχθηκαν.")
                    self.sak.putbackletters(self.pc.lettersInHand)
                    self.pc.lettersInHand = []
                    for letter in self.sak.getletters(7):
                        self.pc.lettersInHand.append(letter)
                else:
                    points = self.countpoints(playedWord)
                    print("AΠΟΔΕΚΤΗ ΛΕΞΗ! Πήρατε " + str(points) + " πόντους.")
                    self.pc.score += points
                    for i in range(len(playedWord)):
                        self.pc.lettersInHand.remove(playedWord[i])
                    for letter in self.sak.getletters(len(playedWord)):
                        self.pc.lettersInHand.append(letter)

                if len(self.player.lettersInHand) == 0:
                    self.end()

    def countpoints(self, word):
        points = 0
        for letter in word:
            for i in letters:
                if letter == i:
                    points += letters[i][1]
                    break
        return points

    def end(self):
        self.keepPlaying = False
        print("--------------------")
        print("ΤΕΛΟΣ ΠΑΙΧΝΙΔΙΟΥ!")
        if self.player.score > self.pc.score:
            print("Νικητής ο " + self.player.name + " με σκορ " + str(self.player.score) + "-" + str(self.pc.score))
        elif self.player.score < self.pc.score:
            print("Νικητής ο " + self.pc.name + " με σκορ " + str(self.player.score) + "-" + str(self.pc.score))
        else:
            print("Το παιχνίδι έληξε ισόπαλο " + str(self.player.score) + "-" + str(self.pc.score))
