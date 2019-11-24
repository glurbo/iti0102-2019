    from math import pi
class Chef:
    def __init__(self, name: str, experience_level: int):
        self.name = name
        self.experience_level = experience_level


class Pizza:
    def __init__(self, name: str, diameter: int, toppings: list):
        self.name = name
        self.diameter = diameter
        self.toppings = toppings

    def calculate_complexity(self) -> int:
        pass

    def calculate_price(self) -> int:
        pass


class Pizzeria:
    def __init__(self, name: str, is_fancy: bool, budget: int):
        self.name = name
        self.is_fancy = is_fancy
        self.budget = budget

    def add_chef(self, chef: Chef) -> Chef or None:
        pass

    def remove_chef(self, chef: Chef):
        pass

    def add_pizza_to_menu(self, pizza: Pizza):
        pass

    def remove_pizza_from_menu(self, pizza: Pizza):
        pass

    def bake_pizza(self, pizza: Pizza) -> Pizza or None:
        pass

    def get_pizza_menu(self) -> list:
        pass

    def get_baked_pizzas(self) -> dict:
        pass

    def get_chefs(self) -> list:
        pass


if __name__ == '__main__':
        pizzeria1 = Pizzeria("Mama's Pizza", True, 10000)
    print(pizzeria1)  # Mama's pizza with 0 pizza chef(s).

    pizzeria1.add_chef(Chef("Clara", 24))
    print(pizzeria1)
    # Mama's pizza with 0 pizza chef(s). -> Clara was not added because of low XP (24) since it's a fancy pizzeria.

    pizza1 = Pizza("basic", 20, ["Cheese", "Ham"])
    print(pizzeria1.bake_pizza(pizza1))  # None -> No such pizza on the menu nor a chef in the pizzeria.

    ##########################################################
    sebastian = Chef("Sebastian", 58)
    charles = Chef("Charles", 35)
    kimi = Chef("Kimi", 83)

    pizzeria1.add_chef(sebastian)
    pizzeria1.add_chef(charles)
    pizzeria1.add_chef(kimi)

    # Trying to order a pizza which is not on the menu.

    print(pizzeria1.bake_pizza(pizza1))  # None

    pizzeria1.add_pizza_to_menu(pizza1)  # Price is 8.85

    print(pizzeria1.budget)  # 9115
    print(pizzeria1.get_pizza_menu())  # [Basic pizza with a price of 8.85]

    print(pizzeria1.bake_pizza(pizza1))  # Basic pizza with a price of 8.85

    print(pizzeria1.get_chefs())
    # Charles was chosen to bake the pizza, because Charles' XP was the closest to pizza's complexity

    print(pizzeria1.budget)  # 10887
    print(charles.money)  # 1772

    print(pizzeria1.get_baked_pizzas())  # {Basic pizza with a price of 8.85: 1}

    ##########################################################
    pizzeria2 = Pizzeria("Maranello", False, 10000)

    fernando = Chef("Fernando", 9)
    felipe = Chef("Felipe", 6)
    michael = Chef("Michael", 17)
    rubens = Chef("Rubens", 4)
    eddie = Chef("Eddie", 5)

    pizzeria2.add_chef(fernando)
    pizzeria2.add_chef(felipe)
    pizzeria2.add_chef(michael)
    pizzeria2.add_chef(rubens)
    pizzeria2.add_chef(eddie)

    margherita = Pizza("Margherita", 20, ["Sauce", "Mozzarella", "Basil"])
    smoke = Pizza("Big Smoke", 30, ["nine", "NINE", "six w/dip", "seven", "45", "45 w/cheese", "SODA"])

    pizzeria2.add_pizza_to_menu(margherita)
    pizzeria2.add_pizza_to_menu(smoke)

    print(pizzeria2.get_pizza_menu())  # [Big smoke pizza with a price of 20.67, Margherita pizza with a price of 8.85]
    print(pizzeria2.get_chefs())
    # [Pizza chef Rubens with 4 XP, Pizza chef Eddie with 5 XP, Pizza chef Felipe with 6 XP, Pizza chef Fernando with 9 XP, Pizza chef Michael with 17 XP]

    pizzeria2.bake_pizza(margherita)
    print(pizzeria2.get_chefs())
    # [Pizza chef Rubens with 4 XP, Pizza chef Felipe with 6 XP, Pizza chef Fernando with 9 XP, Pizza chef Eddie with 10 XP, Pizza chef Michael with 17 XP]

    pizzeria2.bake_pizza(smoke)
    print(pizzeria2.get_chefs())
    # [Pizza chef Rubens with 4 XP, Pizza chef Felipe with 6 XP, Pizza chef Fernando with 9 XP, Pizza chef Eddie with 14 XP, Pizza chef Michael with 17 XP]