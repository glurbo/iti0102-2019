"""EX15 Magic."""

class MismatchError(Exception):
    """Custom exception thrown when important parameters are missing while trying to add something."""
    pass

class Wand:
    """Wand class."""

    def __init__(self, wood_type, core, score, owner=None):
        """
        Class constructor.

        :param wood_type: wood type of wand.
        :param core: core of wand.
        :param score: score of wand.
        :param owner: owner of wand. None by default.
        """
        self.wood_type = wood_type
        self.core = core
        self.score = score
        self.owner = owner

    @property
    def get_wood_type(self):
        """
        Change wood type of wand.

        :return:
        """
        return self.wood_type

    @property
    def get_core(self):
        """
        Change core of wand.

        :return:
        """
        return self.core

    @staticmethod
    def check_if_proper_wand():
        """
        Check if given wand is correct.

        Must be of class Wand type and wood_type + core parameters must be filled. If correct, return nothing. if wrong,
        throw a MismatchError with message "The wand like that does not exist!".

        :return:
        """
        pass


class Wizard:
    """Wizard class."""

    def __init__(self, name, power, wand=None, school=None, fights):
        self.name = name
        self.power = power
        self.wand = wand
        self.school = school
        self.fights = fights


        

class WizardrySchool:

    def __init__(self, name, max_wizards_number):
        self.name = name
        self.max_wizards_number = max_wizards_number

    def add_wizard(self):

    def del_wizard(self):

    def add_house(self):

    def del_house(self):

    def get_wizards_in_school(self, school_name):

    def get_wizards_in_house(self, house_name):

    def get_wizards_in_each_house(self):

    def sort_wizards_by_power(self):

    def sort_wizards_by_score(self):

    def sort_wizards_by_fights(self):

    def punish_wizard(self):

    def commend_wizard(self):

    def wizard_fight(self, wizard1, wizard2):


class House(WizardrySchool):

    def __init__(self, name, max_wizards_number):
        super().__init__(name, max_wizards_number)