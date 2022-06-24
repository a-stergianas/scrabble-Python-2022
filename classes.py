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

    def __repr__(self):
        return repr('Hello ' + self.name)


class Human(Player):
    def play(self):
        return


class Computer(Player):
    def play(self):
        return


class Game:
    def __init__(self):
        self.round = 0

    def __repr__(self):
        return repr("This is the game")

    def setup(self):
        sak = SakClass()
        return

    def run(self):
        return

    def end(self):
        return
