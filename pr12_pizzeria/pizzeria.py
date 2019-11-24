"""PR12_Pizzeria."""
from math import pi


class Chef:
    """Chef class."""

    def __init__(self, name: str, experience_level: int):
        """Initialize chef properties."""
        self.name = name
        self.experience_level = experience_level
        self.money = 0

    def __repr__(self):
        """Return string when class is called."""
        return f"Pizza chef {self.name.capitalize()} with {self.experience_level} XP"


class Pizza:
    """Pizza class."""

    def __init__(self, name: str, diameter: int, toppings: list):
        """Initialize pizza properties."""
        self.name = name
        self.diameter = diameter
        self.toppings = toppings

    def calculate_complexity(self) -> int:
        """Calculate complexity of given pizza."""
        complexity = 0
        for item in self.toppings:
            one_topping_complexity = len(item) // 3
            complexity += one_topping_complexity
        return complexity

    def calculate_price(self) -> int:
        """Calculate price of given pizza."""
        pizza_area = pi * ((self.diameter / 2) ** 2)
        price = pizza_area / 40 + len(self.toppings) // 2
        return int(price * 100 // 1)

    def __repr__(self):
        """Return string when class is called."""
        return f"{self.name.capitalize()} pizza with a price of {self.calculate_price() / 100}"


class Pizzeria:
    """Pizzeria class."""

    def __init__(self, name: str, is_fancy: bool, budget: int):
        """Initialize pizzeria properties."""
        self.name = name
        self.is_fancy = is_fancy
        self.budget = budget
        self.chef_list = []
        self.menu = []
        self.baked_pizzas = []
        self.baked_pizzas_dict = {}

    def add_chef(self, chef: Chef) -> Chef or None:
        """Add chef to a chef list."""
        if chef not in self.chef_list:
            if self.is_fancy:
                if chef.experience_level >= 25:
                    self.chef_list.append(chef)
                    return chef
                else:
                    return None
            self.chef_list.append(chef)
            return chef
        else:
            return None

    def remove_chef(self, chef: Chef):
        """Remove chef from chef list. If chef not in list, do nothing."""
        if chef not in self.chef_list:
            return None
        self.chef_list.remove(chef)

    def add_pizza_to_menu(self, pizza: Pizza):
        """Add a pizza to a list of pizzas, if the budget allows it."""
        if self.budget - pizza.calculate_price() >= 0:
            if pizza not in self.menu:
                if len(self.chef_list) >= 1:
                    self.menu.append(pizza)
                    self.budget -= pizza.calculate_price()
        else:
            return None

    def remove_pizza_from_menu(self, pizza: Pizza):
        """Remove pizza from the pizza list."""
        if pizza not in self.menu:
            return None
        self.menu.remove(pizza)

    def bake_pizza(self, pizza: Pizza) -> Pizza or None:
        """Bake a pizza."""
        if pizza in self.menu:
            for i in self.chef_list:
                self.chef_list = sorted(self.chef_list, key=lambda c: (i.experience_level, self.chef_list))
                for j in range(len(self.chef_list)):
                    if self.chef_list[j].experience_level >= pizza.calculate_complexity():
                        self.chef_list[j].experience_level += len(pizza.name) // 2
                        self.chef_list[j].money += (pizza.calculate_price() * 4 + len(pizza.name)) // 2
                        self.budget += (pizza.calculate_price() * 4 + len(pizza.name)) // 2
                        self.baked_pizzas.append(pizza)
                        return pizza
        else:
            return None

    def get_pizza_menu(self) -> list:
        """Sort pizza menu by descending price. If the price is same, sort by adding order."""
        return sorted(self.menu, key=lambda pizza: (-pizza.calculate_price(), self.menu))

    def get_baked_pizzas(self) -> dict:
        """Make a dictionary of baked pizzas."""
        for i in self.baked_pizzas:
            if i in self.baked_pizzas_dict:
                self.baked_pizzas_dict[i] += 1
            self.baked_pizzas_dict[i] = 1
        return self.baked_pizzas_dict

    def get_chefs(self) -> list:
        """Sort chef list by experience level."""
        return sorted(self.chef_list, key=lambda chef: chef.experience_level)

    def __repr__(self):
        """Return string when class is called."""
        return f"{self.name.capitalize()} with {len(self.get_chefs())} pizza chef(s)."


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
