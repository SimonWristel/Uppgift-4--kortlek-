import random
import os
os.system("cls")

class Card:
    def init(self, suit, value) -> None:
        self.suit = suit
        self.value = value

    def str(self) -> str:
        return f"{self.suit} {self.value}"

class Deck:
    def init(self, cards=None) -> None:
        if cards == None:
            cards = []
        self.cards = cards

    @staticmethod
    def create_deck():
        cards = []
        suits = ["♠", "♥", "♣", "♦"]
        values = ["Ess", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

        for suit in range(0, len(suits)):
            for value in range(0, len(values)):
                card = f"{suits[suit]} {values[value]}"
                if suits[suit] in ["♥", "♦"]:
                    card = f"\033[91m{card}\033[0m"  
                cards.append(card)

        return cards

    def print_cards(deck):
        text = "All the cards: "
        for card in deck:
            text += f"{card},"
        print(text)

    def print_random_card(deck):
        random_card_index = random.randint(0, len(deck) - 1) 
        print(f"\nPicked card: {deck[random_card_index]}")

deck = Deck.create_deck()
Deck.print_cards(deck)
Deck.print_random_card(deck)
