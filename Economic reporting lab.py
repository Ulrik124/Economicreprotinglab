import random

class Card:
    SUITS = ["♣️", "♦️", "♥️", "♠️"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise Exception(f"Invalid rank, must be one of {self.RANKS}")
        if suit not in self.SUITS:
            raise Exception(f"Invalid suit, must be one of {self.SUITS}")
        self._rank = rank
        self._suit = suit

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        self._cards = [Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS]

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    def shuffle(self):
        random.shuffle(self._cards)

class Hand:
    def __init__(self, deck):
        self._cards = [deck.cards[i] for i in range(5)]

    def __str__(self):
        return str(self._cards)

    @property
    def is_flush(self):
        suit = self._cards[0].suit
        for card in self._cards[1:]:
            if card.suit != suit:
                return False
        return True

tries = 10
i = 0
while tries > 0:
    i += 1
    d = Deck()
    d.shuffle()
    hand = Hand(d)
    if hand.is_flush:
        tries -= 1

probability = (10 / i) * 100
print(f"The odds of getting a flush are {probability}%")

#to see the probability of a flush/straight

import random

class Card:
    SUITS = ["♣️", "♦️", "♥️", "♠️"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    RANK_VALUES = {rank: i for i, rank in enumerate(RANKS, 2)}  # Maps ranks to values

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise Exception(f"Invalid rank, must be one of {self.RANKS}")
        if suit not in self.SUITS:
            raise Exception(f"Invalid suit, must be one of {self.SUITS}")
        self._rank = rank
        self._suit = suit

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def value(self):
        return self.RANK_VALUES[self._rank]

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()

class Deck:
    def __init__(self):
        self._cards = [Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS]

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

class Hand:
    def __init__(self, deck):
        self._cards = [deck.cards[i] for i in range(5)]

    def __str__(self):
        return str(self._cards)

    @property
    def is_flush(self):
        suit = self._cards[0].suit
        for card in self._cards[1:]:
            if card.suit != suit:
                return False
        return True

    @property
    def is_straight(self):
        sorted_values = sorted(card.value() for card in self._cards)
        return all(b - a == 1 for a, b in zip(sorted_values, sorted_values[1:]))

tries = 10000
flush_count = 0
straight_count = 0
for _ in range(tries):
    d = Deck()
    d.shuffle()
    hand = Hand(d)
    if hand.is_flush:
        flush_count += 1
    if hand.is_straight:
        straight_count += 1

flush_probability = (flush_count / tries) * 100
straight_probability = (straight_count / tries) * 100
print(f"The odds of getting a flush are {flush_probability}%")
print(f"The odds of getting a straight are {straight_probability}%")

# to geta 4 of a kind

import random

class Card:
    SUITS = ["♣️", "♦️", "♥️", "♠️"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise Exception(f"Invalid rank, must be one of {self.RANKS}")
        if suit not in self.SUITS:
            raise Exception(f"Invalid suit, must be one of {self.SUITS}")
        self._rank = rank
        self._suit = suit

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()

class Deck:
    def __init__(self):
        self._cards = [Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS]

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

class Hand:
    def __init__(self, deck):
        self._cards = [deck.cards[i] for i in range(5)]

    def __str__(self):
        return str(self._cards)

    @property
    def is_four_of_a_kind(self):
        rank_counts = [card.rank for card in self._cards]
        return max(rank_counts.count(rank) for rank in rank_counts) == 4

tries = 100000
four_of_a_kind_count = 0

for _ in range(tries):
    d = Deck()
    d.shuffle()
    hand = Hand(d)
    if hand.is_four_of_a_kind:
        four_of_a_kind_count += 1

four_of_a_kind_probability = (four_of_a_kind_count / tries) * 100
print(f"The odds of getting a four of a kind are {four_of_a_kind_probability}%")