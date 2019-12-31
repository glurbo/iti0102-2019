"""EX15 Magic."""


class MismatchError(Exception):
    """Custom exception thrown when important parameters are missing while trying to add something."""
    pass


class Wand:
    """Wand class."""

    def __init__(self, wood_type, core, score=0, owner=None):
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

    def __init__(self, name, power, fights, wand=None, school=None):
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
        pass

    def del_wizard(self):
        pass

    def add_house(self):
        pass

    def del_house(self):
        pass

    def get_wizards_in_school(self, school_name):
        pass

    def get_wizards_in_house(self, house_name):
        pass

    def get_wizards_in_each_house(self):
        pass

    def sort_wizards_by_power(self):
        pass

    def sort_wizards_by_score(self):
        pass

    def sort_wizards_by_fights(self):
        pass

    def punish_wizard(self):
        pass

    def commend_wizard(self):
        pass

    def wizard_fight(self, wizard1, wizard2):
        pass


class House(WizardrySchool):

    def __init__(self, name, max_wizards_number):
        super().__init__(name, max_wizards_number)


if __name__ == '__main__':
    w1 = Wand("mahogany", "süda", 0)
    print(type(w1))