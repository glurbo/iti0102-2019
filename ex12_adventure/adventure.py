"""EX12 Adventure."""


class Adventurer:
    """Adventurer class."""

    def __init__(self, name, class_type, power, experience=0):
        """Initiate adventurer properties."""
        self.name = name
        if class_type not in ["Fighter", "Druid", "Wizard", "Paladin"]:
            self.class_type = "Fighter"
        else:
            self.class_type = class_type
        self.power = power
        self.experience = experience

    def add_experience(self, exp):
        """Add experience to an adventurer."""
        self.experience += exp

    def add_power(self, power):
        """Add power to an adventurer."""
        self.power += power

    def __repr__(self):
        """Return a string representation of adventurer class."""
        return f"{self.name}, the {self.class_type}, Power: {self.power}, Experience: {self.experience}."


class Monster:
    """Monster class."""

    def __init__(self, name, mon_type, power=0):
        """Initialize monster properties."""
        self.name = name
        self.mon_type = mon_type
        self.power = power

    @property
    def get_name(self):
        """Find out the name of a monster. If monster is type zombie, add an undead prefix."""
        if self.mon_type == "Zombie":
            return "Undead " + self.name
        return self.name

    def __repr__(self):
        """Return a string representation of monster class."""
        return f"{self.get_name} of type {self.mon_type}, Power: {self.power}."


class World:
    """World class."""

    def __init__(self, pm):
        """Initialize world properties."""
        self.adventurerlist = []
        self.monsterlist = []
        self.graveyard = []
        self.pm = pm
        self.active_adventurers = []
        self.active_monsters = []

    def add_adventurer(self, adventurer):
        """Add an adventurer to adventurer list if it is the correct type."""
        if isinstance(adventurer, Adventurer):
            self.adventurerlist.append(adventurer)
        else:
            return

    def add_monster(self, monster):
        """Add a monster to monster list if it is the correct type."""
        if isinstance(monster, Monster):
            self.monsterlist.append(monster)
        else:
            return

    def get_adventurerlist(self):
        """Get adventurer list."""
        return self.adventurerlist

    def get_monsterlist(self):
        """Get monster list."""
        return self.monsterlist

    def get_graveyard(self):
        """Get a list of characters who have died."""
        return self.graveyard

    def get_python_master(self):
        """Get the name of python master."""
        return self.pm

    def change_necromancer(self, boolean) -> bool:
        """Find if a necromancer is present or not."""
        if boolean:
            return True
        else:
            return False

    def revive_graveyard(self):
        """
        Revive all characters who have died previously.

        Revived monsters are all type zombies and revived adventurers are all type undead class name.

        :return:
        """
        if self.change_necromancer:
            for i in range(len(self.graveyard)):
                current = self.graveyard[i]
                if isinstance(current, Monster):
                    self.monsterlist.append(Monster(current.name, "Zombie", current.power))
                if isinstance(current, Adventurer):
                    undead_adventurer = Monster("Undead " + current.name, "Zombie " + current.class_type, current.power)
                    self.monsterlist.append(undead_adventurer)
            for i in range(len(self.graveyard)):
                self.graveyard.remove(self.graveyard[0])
            self.change_necromancer(False)
        else:
            return

    def add_strongest(self, class_type):
        """Add the strongest adventurer to active adventurer list."""
        strongest = sorted([c for c in self.adventurerlist if c.class_type == class_type], key=lambda x: -x.power)[0]
        self.active_adventurers.append(strongest)
        self.adventurerlist.remove(strongest)

    def add_weakest(self, class_type):
        """Add the weakest adventurer to active adventurer list."""
        weakest = sorted([c for c in self.adventurerlist if c.class_type == class_type], key=lambda x: x.power)[0]
        self.active_adventurers.append(weakest)
        self.adventurerlist.remove(weakest)

    def add_most_experience(self, class_type):
        """Add the most experienced adventurer to active adventurer list."""
        xp = sorted([c for c in self.adventurerlist if c.class_type == class_type], key=lambda x: -x.experience)[0]
        self.active_adventurers.append(xp)
        self.adventurerlist.remove(xp)

    def add_least_experience(self, class_type):
        """Add the least experienced adventurer to active adventurer list."""
        no_xp = sorted([c for c in self.adventurerlist if c.class_type == class_type], key=lambda x: x.experience)[0]
        self.active_adventurers.append(no_xp)
        self.adventurerlist.remove(no_xp)

    def add_by_name(self, name):
        """Add an adventurer to active adventurer list by name."""
        for c in self.adventurerlist:
            if c.name == name:
                self.active_adventurers.append(c)
                self.adventurerlist.remove(c)

    def add_all_of_class_type(self, class_type):
        """Add all adventurers of a certain class type to active adventurer list."""
        for c in self.adventurerlist:
            if c.class_type == class_type:
                self.active_adventurers.append(c)
        for c in self.active_adventurers:
            self.adventurerlist.remove(c)

    def add_all(self):
        """Add all adventurers to active adventurer list."""
        for c in self.adventurerlist:
            self.active_adventurers.append(c)
        for _ in range(len(self.adventurerlist)):
            self.adventurerlist.remove(self.adventurerlist[0])

    def get_active_adventurers(self):
        """Get active adventurer list, sorted by highest experience to lowest."""
        return sorted(self.active_adventurers, key=lambda x: -x.experience)

    def add_monster_by_name(self, name):
        """Add a monster to active monster list by name."""
        for c in self.monsterlist:
            if c.name == name:
                self.active_monsters.append(c)
                self.monsterlist.remove(c)

    def add_strongest_monster(self):
        """Add the monster with highest power level to active monster list."""
        strongest = sorted(self.monsterlist, key=lambda x: -x.power)[0]
        self.active_monsters.append(strongest)
        self.monsterlist.remove(strongest)

    def add_weakest_monster(self):
        """Add the monster with lowest power level to active monster list."""
        weakest = sorted(self.monsterlist, key=lambda x: x.power)[0]
        self.active_monsters.append(weakest)
        self.monsterlist.remove(weakest)

    def add_all_of_type(self, mon_type):
        """Add all monsters of a certain type to active monster list."""
        for c in self.monsterlist:
            if c.mon_type == mon_type:
                self.active_monsters.append(c)
        for c in self.active_monsters:
            self.monsterlist.remove(c)

    def add_all_monsters(self):
        """Add all monsters to active monster list."""
        for c in self.monsterlist:
            self.active_monsters.append(c)
        for _ in range(len(self.monsterlist)):
            self.monsterlist.remove(self.monsterlist[0])

    def get_active_monsters(self):
        """Get a list of active monsters sorted by power from highest to lowest."""
        return sorted(self.active_monsters, key=lambda x: -x.power)

    def remove_character(self, name):
        """
        Remove a character by name from any list.

        Only one name can be removed with one callout.

        Priority order being adventurer list > monster list > graveyard.

        :param name:
        :return:
        """
        for c in self.adventurerlist:
            if c.name == name:
                self.adventurerlist.remove(c)
                return
        for c in self.monsterlist:
            if c.name == name:
                self.monsterlist.remove(c)
                return
        for c in self.graveyard:
            if c.name == name:
                self.graveyard.remove(c)
                return

    def if_druid(self):
        """
        Druid and monster type interaction.

        If a druid is in active adventurers list and active monsters list has an animal or ent, then these monsters
        will not be included in the battle and inserted back into monster list.

        :return:
        """
        is_druid = False
        for c in self.active_adventurers:
            if c.class_type == "Druid":
                is_druid = True
        for i in range(len(self.active_monsters)):
            if (self.active_monsters[i].mon_type == "Animal" or self.active_monsters[i].mon_type == "Ent") and is_druid:
                self.monsterlist.append(self.active_monsters[i])
                self.active_monsters.remove(self.active_monsters[i])

    def paladin_power(self):
        """Double the power of paladins if there is a type zombie on active monsters list."""
        is_zombie = False
        for c in self.active_monsters:
            if c.mon_type in ["Zombie", "Zombie Fighter", "Zombie Druid", "Zombie Paladin", "Zombie Wizard"]:
                is_zombie = True
        for c in self.active_adventurers:
            if c.class_type == "Paladin" and is_zombie:
                c.power = c.power * 2

    def empty_the_field(self, activelist, regularlist):
        """Remove all characters from active list and places them back into regular list."""
        for c in activelist:
            regularlist.append(c)
        for i in range(len(activelist)):
            activelist.remove(activelist[i])

    def is_deadly_loser(self, activelist):
        """Send all losing characters to a graveyard if the game is deadly."""
        for c in activelist:
            self.graveyard.append(c)
        for i in range(len(activelist)):
            activelist.remove(activelist[i])

    def get_xp(self, total_xp, nr_of_adv):
        """Add experience to all active adventurers if battle was victorious."""
        xp_per_adv = total_xp / nr_of_adv
        xp_per_adv //= 1
        for c in self.active_adventurers:
            c.add_experience(int(xp_per_adv))

    def go_adventure(self, deadly=False):
        """
        Main game.

        Initialize the game. If the power sum of adventurers is higher than power sum of monsters, then adventurers
        gain their total power level as experience, divided between the adventurers.

        :param deadly:
        :return:
        """
        total_adv_power = 0
        total_monster_power = 0
        for c in self.active_adventurers:
            self.paladin_power()
            total_adv_power += c.power
        for c in self.active_monsters:
            self.if_druid()
            total_monster_power += c.power

        if total_adv_power > total_monster_power:  # WIN
            if not deadly:
                self.get_xp(total_monster_power, len(self.active_adventurers))
                self.empty_the_field(self.active_adventurers, self.adventurerlist)
                self.empty_the_field(self.active_monsters, self.monsterlist)
            elif deadly:
                self.get_xp(total_monster_power * 2, len(self.active_adventurers))
                self.empty_the_field(self.active_adventurers, self.adventurerlist)
                self.is_deadly_loser(self.active_monsters)
        elif total_adv_power < total_monster_power:  # LOSS
            if not deadly:
                self.empty_the_field(self.active_adventurers, self.adventurerlist)
                self.empty_the_field(self.active_monsters, self.monsterlist)
            elif deadly:
                self.empty_the_field(self.active_monsters, self.monsterlist)
                self.is_deadly_loser(self.active_adventurers)
        elif total_adv_power == total_monster_power:  # DRAW
            self.get_xp(total_monster_power, len(self.active_adventurers))
            self.empty_the_field(self.active_adventurers, self.adventurerlist)
            self.empty_the_field(self.active_monsters, self.monsterlist)


if __name__ == "__main__":
    print("Kord oli maailm.")
    Maailm = World("Sõber")
    print(Maailm.get_python_master())  # -> "Sõber"
    print(Maailm.get_graveyard())  # -> []
    print()
    print("Tutvustame tegelasi.")
    Kangelane = Adventurer("Sander", "Paladin", 50)
    Tüütu_Sõber = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)
    Lahe_Sõber = Adventurer("Peep", "Druid", 25)
    Teine_Sõber = Adventurer("Toots", "Wizard", 40)

    print(Kangelane)  # -> "Sander, the Paladin, Power: 50, Experience: 0."
    # Ei, tüütu sõber, sa ei saa olla tulevikurändaja ja ninja, nüüd sa pead fighter olema.
    print(Tüütu_Sõber)  # -> "XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 999999, Experience: 0."

    print("Sa ei tohiks kohe alguses ka nii tugev olla.")
    Tüütu_Sõber.add_power(-999959)
    print(Tüütu_Sõber)  # -> XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 40, Experience: 0.
    print()
    print(Lahe_Sõber)  # -> "Peep, the Druid, Power: 25, Experience: 0."
    print(Teine_Sõber)  # -> "Toots, the Wizard, Power: 40, Experience: 0."
    print()
    Lahe_Sõber.add_power(20)
    print("Sa tundud kuidagi nõrk, ma lisasin sulle natukene tugevust.")
    print(Lahe_Sõber)  # -> "Peep, the Druid, Power: 45, Experience: 0."

    Maailm.add_adventurer(Kangelane)
    Maailm.add_adventurer(Lahe_Sõber)
    Maailm.add_adventurer(Teine_Sõber)
    print(Maailm.get_adventurerlist())  # -> Sander, Peep ja Toots

    Maailm.add_monster(Tüütu_Sõber)
    # Ei, tüütu sõber, sa ei saa olla vaenlane.
    print(Maailm.get_monsterlist())  # -> []
    Maailm.add_adventurer(Tüütu_Sõber)

    print()
    print()
    print("Oodake veidikene, ma tekitan natukene kolle.")
    Zombie = Monster("Rat", "Zombie", 10)
    GoblinSpear = Monster("Goblin Spearman", "Goblin", 10)
    GoblinArc = Monster("Goblin Archer", "Goblin", 5)
    BigOgre = Monster("Big Ogre", "Ogre", 120)
    GargantuanBadger = Monster("Massive Badger", "Animal", 1590)

    print(BigOgre)  # -> "Big Ogre of type Ogre, Power: 120."
    print(Zombie)  # -> "Undead Rat of type Zombie, Power: 10."

    Maailm.add_monster(GoblinSpear)

    print()
    print()
    print("Mängime esimese kakluse läbi!")
    Maailm.add_strongest("Druid")
    Maailm.add_strongest_monster()
    print(Maailm.get_active_adventurers())  # -> Peep
    print(Maailm.get_active_monsters())  # -> [Goblin Spearman of type Goblin, Power: 10.]

    Maailm.go_adventure(True)

    Maailm.add_strongest("Druid")
    print(Maailm.get_active_adventurers())  # -> [Peep, the Druid, Power: 45, Experience: 20.]
    print("Surnuaias peaks üks goblin olema.")
    print(Maailm.get_graveyard())  # ->[Goblin Spearman of type Goblin, Power: 10.]

    Maailm.add_monster(GargantuanBadger)
    Maailm.add_strongest_monster()

    Maailm.go_adventure(True)
    # Druid on loomade sõber, ja ajab massiivse mägra ära.
    print(Maailm.get_adventurerlist())  # -> Kõik 4 mängijat.
    print(Maailm.get_monsterlist())  # -> [Massive Badger of type Animal, Power: 1590.]

    Maailm.remove_character("Massive Badger")
    print(Maailm.get_monsterlist())  # -> []

    print(
        "Su sõber ütleb: \"Kui kõik need testid andsid sinu koodiga sama tulemuse mille ma siin ette kirjutasin, peaks "
        "kõik okei olema, proovi testerisse pushida! \" ")
