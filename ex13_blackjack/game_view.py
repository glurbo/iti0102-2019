"""Game views."""
from abc import abstractmethod
from enum import Enum


class Color:
    """Colors class:
    reset all Color with Color.reset
    two subclasses Fg for foreground and Bg for background.
    use as Color.subclass.colorname.
    i.e. Color.Fg.red or Color.Bg.green
    also, the generic bold, disable, underline, reverse, strike_through,
    and invisible work with the main class
    i.e. Color.bold
    """
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strike_through = '\033[09m'
    invisible = '\033[08m'

    class Fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        light_grey = '\033[37m'
        dark_grey = '\033[90m'
        light_red = '\033[91m'
        light_green = '\033[92m'
        yellow = '\033[93m'
        light_blue = '\033[94m'
        pink = '\033[95m'
        light_cyan = '\033[96m'

    class Bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        light_grey = '\033[47m'


class Move(Enum):
    """Moves."""
    HIT = "HIT",
    STAND = "STAND",
    SPLIT = "SPLIT",
    DOUBLE_DOWN = "DOUBLE DOWN",
    SURRENDER = "SURRENDER"

    @staticmethod
    def from_str(string: str):
        """Get move from string."""
        if string.lower() in ('hit', 'h'):
            return Move.HIT
        elif string.lower() in ('stand', 's'):
            return Move.STAND
        elif string.lower() in ('split', 'x'):
            return Move.SPLIT
        elif string.lower() in ('double down', 'double', 'd'):
            return Move.DOUBLE_DOWN
        elif string.lower() in ('surrender', 'q'):
            return Move.SURRENDER
        else:
            raise ValueError("Invalid string input!")


class GameView:
    """Game View."""

    @abstractmethod
    def ask_move(self) -> Move:
        """Ask for user input for next move."""
        pass

    @abstractmethod
    def ask_decks_count(self) -> int:
        """Ask decks count."""
        pass

    @abstractmethod
    def ask_players_count(self) -> int:
        """Ask human players count."""
        pass

    @abstractmethod
    def ask_bots_count(self) -> int:
        """Ask bots count."""
        pass

    @abstractmethod
    def ask_name(self, player_nr: int) -> str:
        """Ask player to pick name."""
        pass

    @abstractmethod
    def show_table(self, players: list, house, player) -> None:
        """Show table."""
        pass

    @abstractmethod
    def show_help(self):
        """Show help."""
        pass


class SimpleView(GameView):
    """Simple view."""

    def ask_move(self) -> Move:
        """Ask move."""
        while True:
            try:
                action = Move.from_str(input("Choose your next move hit(H) or stand(S) > "))
                return action
            except ValueError:
                print("Invalid command! Use 'help' for help")

    def ask_decks_count(self) -> int:
        """Ask decks count."""
        while True:
            count = input("Please enter decks count: ")
            if count.isdigit():
                return int(count)
            else:
                print("Value must be numeric!")

    def ask_players_count(self) -> int:
        """Ask players count."""
        while True:
            count = input("Please enter human players count: ")
            if count.isdigit():
                return int(count)
            else:
                print("Value must be numeric!")

    def ask_bots_count(self) -> int:
        """Ask bots count."""
        while True:
            count = input("Please enter bots count: ")
            if count.isdigit():
                return int(count)
            else:
                print("Value must be numeric!")

    def ask_name(self, player_nr: int) -> str:
        """Ask player to pick name."""
        return input(f"Enter name for player {player_nr}: ")

    def show_table(self, players: list, house, player) -> None:
        """Print table."""
        print('-' * 60)
        print("Players:              Coins:  Hands:")
        for p in players:
            print(f"{p.name: <20} |{p.coins: >6}|: {' | '.join(' '.join([str(c) for c in h.cards]) for h in p.hands)}")
        print(f"Dealer: {' '.join([str(c) for c in house.cards])}")

    def show_help(self):
        """Show help."""
        print(f"""help -> help (print help/commands to console)
        hit (h) -> hit (get one more card)
        stand (s) -> stand (stop getting more cards, give turn to next player)
        split (x) -> split cards (if you have 2 cards with same value you can split them to 2 different decks)
        double (d) -> double down (double your bet and receive 1 last card)
        surrender (q) -> surrender (give up :( )""")


class FancyView(GameView):
    """Fancy view."""

    class CardTemplate:
        """Card templates."""
        template_width = 7
        templates = dict()
        templates['AS'] = r""" _____
|A .  |
| /.\ |
|(_._)|
|  |  |
|____V|"""
        templates['AD'] = r""" ____
|A ^  |
| / \ |
| \ / |
|  .  |
|____V|"""
        templates['AC'] = """ ____
|A _  |
| ( ) |
|(_'_)|
|  |  |
|____V|"""
        templates['AH'] = r""" _____
|A_ _ |
|( v )|
| \ / |
|  .  |
|____V|"""
        templates['2'] = """ _____
|2    |
|  ^  |
|     |
|  ^  |
|____Z|"""
        templates['3'] = """ _____
|3    |
| ^ ^ |
|     |
|  ^  |
|____E|"""
        templates['4'] = """ _____
|4    |
| ^ ^ |
|     |
| ^ ^ |
|____h|"""
        templates['5'] = """ _____
|5    |
| ^ ^ |
|  ^  |
| ^ ^ |
|____S|"""
        templates['6'] = """ _____
|6    |
| ^ ^ |
| ^ ^ |
| ^ ^ |
|____9|"""
        templates['7'] = """ _____
|7    |
| ^ ^ |
|^ ^ ^|
| ^ ^ |
|____L|"""
        templates['8'] = """ _____
|8    |
|^ ^ ^|
| ^ ^ |
|^ ^ ^|
|____8|"""
        templates['9'] = """ _____
|9    |
|^ ^ ^|
|^ ^ ^|
|^ ^ ^|
|____6|"""
        templates['0'] = """ _____
|10 ^ |
|^ ^ ^|
|^ ^ ^|
|^ ^ ^|
|___0I|"""
        templates['JS'] = """ _____
|J  ww|
| ^ {)|
|(.)% |
| | % |
|__%%[|"""
        templates['QS'] = """ _____
|Q  ww|
| ^ {(|
|(.)%%|
| |%%%|
|_%%%O|"""
        templates['KS'] = """ _____
|K  WW|
| ^ {)|
|(.)%%|
| |%%%|
|_%%%>|"""
        templates['JC'] = """ _____
|J  ww|
| o {)|
|o o% |
| | % |
|__%%[|"""
        templates['QC'] = """ _____
|Q  ww|
| o {(|
|o o%%|
| |%%%|
|_%%%O|"""
        templates['KC'] = """ _____
|K  WW|
| o {)|
|o o%%|
| |%%%|
|_%%%>|"""
        templates['JH'] = """ _____
|J  ww|
|   {)|
|(v)% |
| v % |
|__%%[|"""
        templates['QH'] = """ _____
|Q  ww|
|   {(|
|(v)%%|
| v%%%|
|_%%%O|"""
        templates['KH'] = """ _____
|K  WW|
|   {)|
|(v)%%|
| v%%%|
|_%%%>|"""
        templates['JD'] = r""" _____
|J  ww|
| /\{)|
| \/% |
|   % |
|__%%[|"""
        templates['QD'] = r""" _____
|Q  ww|
| /\{(|
| \/%%|
|  %%%|
|_%%%O|"""
        templates['KD'] = r""" _____
|K  WW|
| /\{)|
| \/%%|
|  %%%|
|_%%%>|"""
        templates['??'] = """ _____
|?    |
|     |
|     |
|     |
|____¿|"""

    def ask_move(self) -> Move:
        """Ask move."""
        while True:
            try:
                command = input(f"{Color.Fg.cyan}Choose your next move! " +
                                f"{Color.Fg.green} (Use {Color.Fg.light_blue}'help' " +
                                f"{Color.Fg.green}for help) " +
                                f"{Color.Fg.orange}> {Color.reset}")
                if command not in ['help']:
                    action = Move.from_str(command)
                    return action
                else:
                    self.show_help()
            except ValueError:
                print(f"{Color.Fg.red}Invalid command! {Color.Fg.light_blue}Use 'help' for help {Color.reset}")

    def ask_decks_count(self) -> int:
        """Ask decks count."""
        while True:
            count = input(f"{Color.Fg.light_blue}Please enter decks count: {Color.reset}")
            if count.isdigit() and 0 < int(count) <= 8:
                return int(count)
            else:
                print(f"{Color.Fg.red}Value must be numeric and between 1-8! {Color.reset}")

    def ask_players_count(self) -> int:
        """Ask players count."""
        while True:
            count = input(f"{Color.Fg.cyan}Please enter human players count:  {Color.reset}")
            if count.isdigit():
                return int(count)
            else:
                print(f"{Color.Fg.red}Value must be numeric! {Color.reset}")

    def ask_bots_count(self) -> int:
        """Ask bots count."""
        while True:
            count = input(f"{Color.Fg.light_cyan}Please enter bots count:  {Color.reset}")
            if count.isdigit():
                return int(count)
            else:
                print(f"{Color.Fg.red}Value must be numeric!{Color.reset}")

    def ask_name(self, player_nr: int) -> str:
        """Ask player to pick name."""
        color = Color.Fg.orange if player_nr % 2 == 0 else Color.Fg.yellow
        return input(f"{color}Enter name for player {player_nr}: {Color.Fg.orange}")

    def show_table(self, players: list, house, current_hand) -> None:
        """Print table."""
        ascii_suits = {'S': '♠', 'H': '♥', 'C': '♣', 'D': '♦'}
        print(Color.Fg.orange + '-' * 20 * len(players))
        print(f"{Color.Fg.light_green}House:{Color.reset}")
        card_templates = []
        for c in house.cards:
            if str(c) in self.CardTemplate.templates.keys():
                card_templates.append(self.CardTemplate.templates[str(c)].split('\n'))
            else:
                card_templates.append(
                    self.CardTemplate.templates[str(c)[0]].replace('^', ascii_suits[str(c)[-1]]).split('\n'))

        print(Color.Fg.light_red, end='')
        for l in zip(*card_templates):
            print('\t'.join(l))

        print(Color.Fg.orange + '-' * 20 * len(players))
        print(f"{Color.Fg.light_green}Players:{Color.reset}")

        player_templates = []
        hand_lengths = []
        self.prepare_players(ascii_suits, current_hand, hand_lengths, player_templates, players)

        total_width = 0
        for i, p in enumerate(players):
            width = len(p.hands) * self.CardTemplate.template_width + (len(p.hands) - 1) * 5
            total_width += width if total_width == 0 else width + 5
            name = p.name if len(p.name) < width else p.name[:width]
            color = Color.Fg.purple if current_hand in p.hands else Color.Fg.cyan
            print(f"{color}{name:^{width}}", end='')
            print(f"\t{Color.Fg.orange}#\t" if i < len(players) - 1 else '', end='')

        print('\n' + Color.Fg.orange + '-' * total_width + Color.reset)
        for l in zip(*player_templates):
            print(f"\t{Color.Fg.orange}#{Color.reset}\t".join(l))
        print(Color.Fg.orange + '-' * total_width + Color.reset)

        for i, p in enumerate(players):
            width = len(p.hands) * self.CardTemplate.template_width + (len(p.hands) - 1) * 5
            color = Color.Fg.purple if current_hand in p.hands else Color.Fg.cyan
            print(f"{color}{str(p.coins) + '$': ^{width}}", end='')
            print(f"\t{Color.Fg.orange}#\t" if i < len(players) - 1 else '', end='')
        print(Color.reset)

    def prepare_players(self, ascii_suits, current_hand, hand_lengths, player_templates, players):
        """Prepare players for printing."""
        for p in players:
            for h in p.hands:
                hand_lengths.append(len(h.cards))
        hand_length = max(hand_lengths) * 8
        for p in players:
            hand_templates = []
            for h in p.hands:
                hand_color = Color.Fg.pink if h == current_hand else Color.Fg.light_red
                cards = ''
                for c in h.cards:
                    cards += '\n' if cards != '' else ''
                    if str(c) in self.CardTemplate.templates.keys():
                        cards += self.CardTemplate.templates[str(c)]
                    else:
                        cards += self.CardTemplate.templates[str(c)[0]].replace('^', ascii_suits[str(c)[-1]])
                for _ in range(hand_length - len(h.cards) * 8):
                    cards += '\n' + ' ' * self.CardTemplate.template_width
                hand_templates.append([hand_color + c for c in cards.split('\n')])

            player = ''
            for l in zip(*hand_templates):
                player += f'\t{Color.Fg.light_green}x{Color.reset}\t'.join(l) + '\n'
            player_templates.append(player.rstrip().split('\n'))

    def show_help(self):
        """Show help."""
        print(f"""
        {Color.Fg.light_blue}help {Color.Fg.orange}-> """ +
              f""""{Color.Fg.green}help {Color.Fg.light_green}(print help/commands to console)
        {Color.Fg.light_blue}hit {Color.Fg.pink}(h) {Color.Fg.orange}-> """ +
              f""""{Color.Fg.green}hit {Color.Fg.light_green}(get one more card)
        {Color.Fg.light_blue}stand {Color.Fg.pink}(s) {Color.Fg.orange}->  """ +
              f"""{Color.Fg.green}stand {Color.Fg.light_green}(stop getting more cards, give turn to next player)
        {Color.Fg.light_blue}split {Color.Fg.pink}(x) {Color.Fg.orange}-> """ +
              f"""{Color.Fg.green}split cards {Color.Fg.light_green}(if you have 2 cards with same value you can """ +
              f"""split them to 2 different decks)
        {Color.Fg.light_blue}double {Color.Fg.pink}(d) {Color.Fg.orange}-> """ +
              f"""{Color.Fg.green}double down {Color.Fg.light_green}(double your bet and receive 1 last card)
        {Color.Fg.light_blue}surrender {Color.Fg.pink}(q) {Color.Fg.orange}-> """ +
              f"""{Color.Fg.light_green}surrender {Color.Fg.light_green}(give up :( ){Color.reset}""")
