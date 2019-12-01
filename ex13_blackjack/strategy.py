"""Strategy."""
from abc import abstractmethod

from game_view import GameView, Move


class Strategy:
    """Strategy."""

    def __init__(self, other_players: list, house, decks_count: int):
        """Init."""
        self.player = None
        self.house = house
        self.decks_count = decks_count
        self.other_players = other_players

    @abstractmethod
    def on_card_drawn(self, card) -> None:
        """Called every time when card is drawn"""

    @abstractmethod
    def play_move(self, hand) -> Move:
        """Play move."""

    @abstractmethod
    def on_game_end(self) -> None:
        """Called on game end."""


class HumanStrategy(Strategy):
    """Human strategy."""

    def __init__(self, other_players: list, house, decks_count, view: GameView):
        """Init."""
        super().__init__(other_players, house, decks_count)
        self.view = view

    def play_move(self, hand) -> Move:
        """Play move."""
        return self.view.ask_move()

    def on_card_drawn(self, card) -> None:
        """Called every time card is drawn."""

    def on_game_end(self) -> None:
        """Called on game end."""


class MirrorDealerStrategy(Strategy):
    """Very simple strategy."""

    def play_move(self, hand) -> Move:
        """Get next move."""
        if hand.score < 17 or hand.is_soft_hand:
            return Move.HIT
        return Move.STAND

    def on_card_drawn(self, card) -> None:
        """Called every time card is drawn."""

    def on_game_end(self) -> None:
        """Called on game end."""