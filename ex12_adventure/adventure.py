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
        "Su sõber ütleb: \"Kui kõik need testid andsid sinu koodiga sama tulemuse mille ma siin ette kirjutasin, peaks kõik okei olema, proovi testerisse pushida! \" ")