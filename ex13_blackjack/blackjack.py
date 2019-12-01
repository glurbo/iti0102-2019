"""Blackjack."""
import importlib
import os
import pkgutil
import random
from deck import Deck, Card
from game_view import GameView, FancyView, Move
from strategy import Strategy, HumanStrategy


class Hand:
    """Hand."""

    def __init__(self, cards: list = None):
        """Init."""
        pass

    def add_card(self, card: Card) -> None:
        """Add card to hand."""
        pass

    def double_down(self, card: Card) -> None:
        """Double down."""
        pass

    def split(self):
        """Split hand."""
        pass

    @property
    def can_split(self) -> bool:
        """Check if hand can be split."""
        pass

    @property
    def is_blackjack(self) -> bool:
        """Check if is blackjack"""
        pass

    @property
    def is_soft_hand(self):
        """Check if is soft hand."""
        pass

    @property
    def score(self) -> int:
        """Get score of hand."""
        pass


class Player:
    """Player."""

    def __init__(self, name: str, strategy: Strategy, coins: int = 100):
        """Init."""
        pass

    def join_table(self):
        """Join table."""
        pass

    def play_move(self, hand: Hand) -> Move:
        """Play move."""
        pass

    def split_hand(self, hand: Hand) -> None:
        """Split hand."""
        pass


class GameController:
    """Game controller."""

    PLAYER_START_COINS = 200
    BUY_IN_COST = 10

    def __init__(self, view: GameView):
        """Init."""
        pass

    def start_game(self) -> None:
        """Start game."""
        pass

    def play_round(self) -> bool:
        """Play round."""
        pass

    def _draw_card(self, top_down: bool = False) -> Card:
        """Draw card."""

    @staticmethod
    def load_strategies() -> list:
        """
        Load strategies.
        @:return list of strategies that are in same package.
        DO NOT EDIT!
        """
        pkg_dir = os.path.dirname(__file__)
        for (module_loader, name, is_pkg) in pkgutil.iter_modules([pkg_dir]):
            importlib.import_module('.' + name, 'ex13_blackjack')
        return list(filter(lambda x: x.__name__ != HumanStrategy.__name__, Strategy.__subclasses__()))


if __name__ == '__main__':
    game_controller = GameController(FancyView())
    game_controller.start_game()
    while game_controller.play_round():
        pass
