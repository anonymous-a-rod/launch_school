# class CircularBuffer:
#   def __init__(self, capacity):
#     self.capacity = capacity
#     self.buffer = []

#   def put(self, x):
#     if len(self.buffer) >= self.capacity:
#       self.buffer = self.buffer[-(self.capacity - 1):]
#     self.buffer.append(x)

#   def get(self):
#     if self.buffer: return self.buffer.pop(0)

# buffer = CircularBuffer(3)

# print(buffer.get() is None)          # True

# buffer.put(1)
# buffer.put(2)
# print(buffer.get() == 1)             # True

# buffer.put(3)
# buffer.put(4)
# print(buffer.get() == 2)             # True

# buffer.put(5)
# buffer.put(6)
# buffer.put(7)
# print(buffer.get() == 5)             # True
# print(buffer.get() == 6)             # True
# print(buffer.get() == 7)             # True
# print(buffer.get() is None)          # True

# buffer2 = CircularBuffer(4)

# print(buffer2.get() is None)         # True

# buffer2.put(1)
# buffer2.put(2)
# print(buffer2.get() == 1)            # True

# buffer2.put(3)
# buffer2.put(4)
# print(buffer2.get() == 2)            # True

# buffer2.put(5)
# buffer2.put(6)
# buffer2.put(7)
# print(buffer2.get() == 4)            # True
# print(buffer2.get() == 5)            # True
# print(buffer2.get() == 6)            # True
# print(buffer2.get() == 7)            # True
# print(buffer2.get() is None)         # True


# print('Number Guesser Part 1')

# import random
# import math

# class GuessingGame:
#   def __init__(self, low, high):
#     self.high = high
#     self.low = low
#     self.guesses = int(math.log2(high - low + 1)) + 1
#     self.number = random.randint(low, high)

#   def guess(self):
#       guess = int(input(f'Enter a number between {self.low} and {self.high}: '))
#       while not (self.low <= guess <= self.high):
#         guess = int(input(f'Invalid guess. Enter a number between {self.low} and {self.high}: '))
#       return guess

#   def play(self):
#     while self.guesses:
#       print(f'You have {self.guesses} guesses remaining.')
#       guess = self.guess()
#       if self.number == guess:
#         print("That's the number!\n")
#         print("You won!\n")
#         return
#       elif self.number < guess:
#         print("Your guess is too high.\n")
#       else:
#         print("Your guess is too low.\n")
#       self.guesses -= 1
#     print('You have no more guesses. You lost!')

# game = GuessingGame(501, 1500)
# game.play()

# print('Highest and Lowest Ranking Cards')

# class Card:
#     RANK_ORDER = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit

#     def __lt__(self, other):
#         return self.RANK_ORDER.index(self.rank) < self.RANK_ORDER.index(other.rank)

#     def __gt__(self, other):
#         return self.RANK_ORDER.index(self.rank) > self.RANK_ORDER.index(other.rank)

#     def __eq__(self, other):
#         return self.RANK_ORDER.index(self.rank) == self.RANK_ORDER.index(other.rank) and self.suit == other.suit
    
#     def __str__(self):
#         return f"{self.rank} of {self.suit}"

# cards = [Card(2, 'Hearts'),
#          Card(10, 'Diamonds'),
#          Card('Ace', 'Clubs')]
# print(min(cards) == Card(2, 'Hearts'))             # True
# print(max(cards) == Card('Ace', 'Clubs'))          # True
# print(str(min(cards)) == "2 of Hearts")            # True
# print(str(max(cards)) == "Ace of Clubs")           # True

# cards = [Card(5, 'Hearts')]
# print(min(cards) == Card(5, 'Hearts'))             # True
# print(max(cards) == Card(5, 'Hearts'))             # True
# print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

# cards = [Card(4, 'Hearts'),
#          Card(4, 'Diamonds'),
#          Card(10, 'Clubs')]
# print(min(cards).rank == 4)                        # True
# print(max(cards) == Card(10, 'Clubs'))             # True
# print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

# cards = [Card(7, 'Diamonds'),
#          Card('Jack', 'Diamonds'),
#          Card('Jack', 'Spades')]
# print(min(cards) == Card(7, 'Diamonds'))           # True
# print(max(cards).rank == 'Jack')                   # True
# print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

# cards = [Card(8, 'Diamonds'),
#          Card(8, 'Clubs'),
#          Card(8, 'Spades')]
# print(min(cards).rank == 8)                        # True
# print(max(cards).rank == 8)                        # True

# print('Deck Of Cards')

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self.reset_deck()

    def draw(self):
        if not self._deck: self.reset_deck() 
        return self._deck.pop()

    def reset_deck(self):
        deck = []
        for rank in self.RANKS:
            for suit in self.SUITS:
                deck.append(Card(rank, suit))
        random.shuffle(deck)
        self._deck = deck

# deck = Deck()
# drawn = []
# for _ in range(52):
#     drawn.append(deck.draw())

# count_rank_5 = sum([1 for card in drawn if card.rank == 5])
# count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

# print(count_rank_5 == 4)      # True
# print(count_hearts == 13)     # True

# drawn2 = []
# for _ in range(52):
#     drawn2.append(deck.draw())

# print(drawn != drawn2)        # True (Almost always).

print('Poker')

# Include Card and Deck classes from the last two exercises.

class PokerHand:
    RANK_ORDER = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, deck):
        self.cards = [deck.draw() for _ in range(5)]

    def print(self):
       for card in self.cards:
           print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        return self._is_straight_flush() and 'Ace' in self._ranks()

    def _is_straight_flush(self):
        return self._is_straight() and self._is_flush()

    def _is_four_of_a_kind(self):
        ranks = self._ranks()
        return any(ranks.count(rank) == 4 for rank in set(ranks))

    def _is_full_house(self):
        return self._is_three_of_a_kind() and self._is_pair()

    def _is_flush(self):
        return len({card.suit for card in self.cards}) == 1

    def _is_straight(self):
        unique_ranks = set(self._ranks())
        if len(unique_ranks) != 5: return False
        rank_values = [self.RANK_ORDER.index(rank) for rank in unique_ranks]
        return max(rank_values) - min(rank_values) == 4

    def _is_three_of_a_kind(self):
        ranks = self._ranks()
        return any(ranks.count(rank) == 3 for rank in set(ranks))

    def _is_two_pair(self):
        ranks = self._ranks()
        return len([rank for rank in set(ranks) if ranks.count(rank) == 2]) == 2

    def _is_pair(self):
        ranks = self._ranks()
        return any(rank for rank in set(ranks) if ranks.count(rank) == 2)

    def _ranks(self):
        return [card.rank for card in self.cards]


hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")