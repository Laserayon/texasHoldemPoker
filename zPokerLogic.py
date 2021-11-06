from random import randint

nbPlayers = 4
nbCards = 2*nbPlayers+5

deck = []

hands = [[] for i in range(nbPlayers)]

points = []

combinations = [
    "High Card",
    "Pair",
    "Two Pairs",
    "Three of a Kind",
    "Straight",
    "Flush",
    "Full House",
    "Four of a Kind",
    "Straight Flush",
    "Royal Flush"
    ]

ranks = [
    "Ace",
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    "Jack",
    "Queen",
    "King"
    ]

suits = [
    "Clubs",    # : "\U00002663"
    "Diamonds", # : "\U00002666"
    "Hearts",   # : "\U00002665"
    "Spades"    # : "\U00002660"
    ]

class Card:
    def __init__(self, rank, suit):
        global ranks, suits
        
        # defini le rang et la suite de la carte
        # pour l'afficher plus tard
        self.rank = rank if rank in ranks else ranks[rank]
        self.suit = suit if suit in suits else suits[suit]
        
        # defini la "puissance" d'une carte
        if self.rank == "Ace": self.value = 1
        elif self.rank == "Jack": self.value = 11
        elif self.rank == "Queen": self.value = 12
        elif self.rank == "King": self.value = 13
        else: self.value = self.rank

    # au cas ou on veut l'afficher
    def __repr__(self):
        s = ""
        
        if self.rank == "Ace":
            s += "A"
        elif self.rank == 10:
            s += "T"
        elif self.rank == "Jack":
            s += "J"
        elif self.rank == "Queen":
            s += "Q"
        elif self.rank == "King":
            s += "K"
        else:
            s+=str(self.rank)
        
        if self.suit == "Clubs":
            s += "\U00002663"
        elif self.suit == "Diamonds":
            s += "\U00002666"
        elif self.suit == "Hearts":
            s += "\U00002665"
        elif self.suit == "Spades":
            s += "\U00002660"
        
        return s
    
def reset():
    global deck, points, hands
    deck = []
    points = []
    hands = [[] for i in range(nbPlayers)]

    for s in suits:
        for r in ranks:
            deck.append(Card(r,s))

def deal():
    global deck, hands, points
    reset()

    cards = []
    for i in range(nbCards):
        cards.append(deck.pop(randint(0,51-i)))
    for i in range(nbPlayers):
        hands[i] = cards[0:5]+cards[5+2*i:7+2*i]
        points.append(combi(i))

def show():
    global hands
    print("House :")
    for c in hands[0][0:5]:
        print(c, end=" ")
    print()
    for i in range(nbPlayers):
        print("player "+str(i), end=": ")
        print(points[i])
        for c in hands[i][5:7]:
            print(c, end=" ")
        print()

# p is the player
def combi(p):
    cards = hands[p]
    sorting(cards)
    combi = ""

    if testStraight(cards): combi = combinations[4]
    
    if testFlush(cards):
        if combi == combinations[4]: combi = combinations[8]
        else: combi = combinations[5]

    if (
            (combi == combinations[8]) and
            ("Ace" in list(set(card.rank for card in cards)) ) and
            ("10" in list(set(card.rank for card in cards)) )
        ):
        combi = combinations[9]

    if combi == "":
        combi = testOther(cards)

    return combi

def testOther(cards):
    noDouble = list(set(card.value for card in cards))
    values = list( map(lambda c: c.value, cards) )
    counts = sorted([values.count(i) for i in noDouble], reverse=True)

    if counts[0] == 4: return combinations[7]
    if counts[0] == 3:
        if counts[1] >= 2: return combinations[6]
        else: return combinations[3]
    if counts[0] == 2:
        if counts[1] == 2: return combinations[2]
        else: return combinations[1]
    return combinations[0]

def testFlush(cards):
    for s in suits:
        if list( map(lambda c: c.suit, cards) ).count(s) == 5:
            return True
    return False

def testStraight(cards):
    noDouble = list(set(card.value for card in cards))
    lenNoD = len(noDouble)

    incr = 1
    if lenNoD >=5:
        for i in range(lenNoD-1):
            if noDouble[i+1]-noDouble[i] == 1:
                incr += 1
            elif (incr == 4) and (noDouble[0] == 1):
                incr += 1
            else:
                incr = 1

    return True if incr == 5 else False

def sorting(cards):
    cards.sort(key=lambda card: card.value, reverse=True)

def whoWon():
    p = list(map(lambda p: combinations.index(p), points))
    m = max(p)
    winners = [idx for idx, pt in enumerate(p) if pt==m]

    if len(winners) == 1: return winners[0]
    winners.sort(key=lambda w: hands[w][0].value, reverse=True)
    return winners[0]

def play():
    deal()
    show()
    winner = whoWon()
    print(winner)
    print()
    return winner
