from enum import Enum
import logging

class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    def __str__(self) -> str:
        match self.value:
            case 10:
                return "T"
            case 11:
                return "J"
            case 12:
                return "Q"
            case 13:
                return "K"
            case 1:
                return "A"
            case _:
                return str(self.value)


class Suit(Enum):
    CLUB = 1
    DIAMOND = 2
    HEART = 3
    SPADE = 4

    def __str__(self) -> str:
        match self.name:
            case "CLUB":
                return "\U00002663"
            case "DIAMOND":
                return "\U00002666"
            case "HEART":
                return "\U00002665"
            case "SPADE":
                return "\U00002660"


class Card():
    def __init__(self, rank: Rank, suit: Suit) -> None:
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"


def main():
    ranks_test = [
        Rank.ACE,
        Rank.TWO,
        Rank.TEN,
        Rank.JACK,
        Rank.QUEEN,
        Rank.KING
    ]
    suits_test = [
        Suit.CLUB,
        Suit.DIAMOND,
        Suit.HEART,
        Suit.SPADE
    ]

    for rank_test in ranks_test:
        for suit_test in suits_test:
            card = Card(rank_test, suit_test)
            print(card)


if __name__ == "__main__":
    main()