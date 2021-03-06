"""Deck."""
from typing import Optional, List
import requests
import random


class Card:
    """Simple dataclass for holding card information.."""

    def __init__(self, value: str, suit: str, code: str):
        """Constructor."""
        self.value = value
        self.suit = suit
        self.code = code
        self.top_down = False

    def __str__(self):
        """Str."""
        if not self.top_down:
            return f"{self.code}"
        return "??"

    def __repr__(self) -> str:
        """Repr."""
        return f"{self.code}"

    def __eq__(self, o) -> bool:
        """Eq."""
        if isinstance(o, Card):
            return self.value == o.value and self.suit == o.suit
        else:
            return False


class Deck:
    """Deck."""

    DECK_BASE_API = "https://deckofcardsapi.com/api/deck/"

    def __init__(self, deck_count: int = 1, shuffle: bool = False):
        """Constructor."""
        self._backup_deck = self._generate_backup_pile(deck_count)
        if shuffle is True:
            random.shuffle(self._backup_deck)
        self.deck_count = deck_count
        self.is_shuffled = shuffle
        self.result = self._request(Deck.DECK_BASE_API + "new/")
        self.deck_id = self.result.get("deck_id", None)
        self.remaining = self.result["remaining"]
        self.shuffle = shuffle

    def shuffle(self) -> None:
        """Shuffle the deck."""
        url = Deck.DECK_BASE_API + f"{self.deck_id}/shuffle/"
        result = requests.get(url).json()
        if result.get("success", False) is True:
            self._request(url)
        else:
            random.shuffle(self._backup_deck)

    def draw_card(self, top_down: bool = False) -> Optional[Card]:
        """
        Draw card from the deck.

        :return: card instance.
        """
        url = Deck.DECK_BASE_API + f"{self.deck_id}/draw/?count=1"
        self._request(url)
        result = requests.get(url).json()
        if result.get("success", False) is True:
            card = result["cards"][0]
            new_card = Card(card["value"], card["suit"], card["code"])
            print(new_card)
            for i in range(len(self._backup_deck)):
                if self._backup_deck[i] == new_card:
                    self._backup_deck.remove(new_card)
        else:
            new_card = random.choice(self._backup_deck)
            for i in range(len(self._backup_deck)):
                if self._backup_deck[i] == new_card:
                    self._backup_deck.remove(new_card)
        return new_card

    def _request(self, url: str) -> dict:
        """Update deck."""
        response = None
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError as e:
            print(e)
        result = response.json()
        return result

    @staticmethod
    def _generate_backup_pile(deck_count) -> List[Card]:
        """Generate backup pile."""
        backup_deck = []
        for char in "HSCD":
            for nr in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "0", "J", "Q", "K"]:
                backup_deck.append(Card(nr, char, nr + char))
        return backup_deck * deck_count


if __name__ == '__main__':
    d = Deck(shuffle=True)
    print(d.remaining)  # 52
    card1 = d.draw_card()  # Random card
    print(card1 in d._backup_deck)  # False
    print(d._backup_deck)  # 51 shuffled cards
    print(f"{len(d._backup_deck)}, should be 51")
    d2 = Deck(deck_count=2)
    print(d2._backup_deck)  # 104 ordered cards (deck after deck)
    print(f"{len(d2._backup_deck)}, should be 104")

