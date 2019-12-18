import requests
import json
import os


class SamePokemonFightException(Exception):
    """Custom exception thrown when same pokemons are fighting."""
    pass


class PokemonFightResultsInATieException(Exception):
    """Custom exception thrown when the fight lasts longer than 100 rounds."""
    pass


class Pokemon:
    """Class for Pokemon."""
    def __init__(self, url_or_path_name: str):
        """
        Class constructor.
        :param url_or_path_name: url or json object.
        If it is url, then parse information from request to proper
        json file and save it to self.data.
        If it is a string representation of a json object, then parse it into json object and save to self.data
        """
        self.score = 0
        self.data = {}
        if url_or_path_name[:5] == "https":
            self.parse_json_to_pokemon_information(url_or_path_name)
        else:
            self.data = json.loads(url_or_path_name)

    def parse_json_to_pokemon_information(self, url):
        """
        :param url: url where the information is requested.
        Called from constructor and this method requests data from url to parse it into proper json object
        and then saved under self.data example done previously
        """
        result = requests.get(url).json()
        self.data["name"] = result["name"]
        for i in range(len(result["stats"])):
            self.data[result["stats"][i]["stat"]["name"]] = result["stats"][i]["base_stat"]
        self.data["types"] = [result["types"][i]["type"]["name"] for i in range(len(result["types"]))]
        self.data["abilities"] = [result["abilities"][i]["ability"]["name"] for i in range(len(result["abilities"]))]
        self.data["forms"] = [result["forms"][i]["name"] for i in range(len(result["forms"]))]
        self.data["moves"] = [result["moves"][i]["move"]["name"] for i in range(len(result["moves"]))]
        self.data["height"] = result["height"]
        self.data["weight"] = result["weight"]
        self.data["base_experience"] = result["base_experience"]

    def get_attack_multiplier(self, other: list):
        """
        self.pokemon is attacking, other is defending
        :param other: list of other pokemon2.data['types']
        Calculate Pokemons attack multiplier against others types and take the best result.
        get the initial multiplier from Fighting Multiplier matrix.
        For example if self.type == ['fire'] and other == ['ground']: return fighting_multipliers['fire']['ground']
        if the defendant has dual types, then multiply the multipliers together.
        if the attacker has dual-types, then the best option is
        chosen(attack can only be of 1 type, choose better[higher multiplier])
        :return: Multiplier.
        """
        "ax * ay * az * bx * by * bz * cx * cy * cz"
        results = []
        highest_multiplier_selector = []
        for x in self.data["types"]:
            multipliers = []
            for y in other:
                multipliers.append(self.get_multiplier(x, y))  # leiab kõik kordajad
            highest_multiplier_selector.append(multipliers)  # lisab leitud kordajad listi
        for multiplier in highest_multiplier_selector:
            multiplier_result = 1
            for x in multiplier:
                multiplier_result = multiplier_result * float(x)  # mitme tüübi puhul korrutatakse kordajad omavahel
            results.append(multiplier_result)
        return max(results)  # tagastab kõige kõrgema kordaja

    def get_multiplier(self, type1, type2):
        """
        Calculate attack multiplier using multipliers.txt.

        :param type1: your pokemon type.
        :param type2: enemy pokemon type.
        :return:
        """
        data = []
        dic = {}
        with open("multipliers.txt", "r") as f:
            for line in f:
                line = line.rstrip()
                line = line.split(" ")
                data.append([x for x in line if x != ""])
        classes = data[:1]
        classes = classes[0]
        data = data[1:]
        for i in range(len(data)):
            data[i] = data[i][1:]
        for i in range(len(classes)):
            dic[classes[i]] = data[i]
        return dic[type1][classes.index(type2)]

    def get_pokemon_attack(self, turn_counter):
        """
        :param turn_counter: every third round the attack is empowered. (return self.data['special-attack'])
        otherwise basic attack is returned (self.data['attack'])
        """
        if turn_counter % 3 == 0:
            return self.data["special-attack"]
        else:
            return self.data["attack"]

    def get_pokemon_defense(self, turn_counter):
        """
        Note: whatever the result is returned, return half of it instead (for example return self.data['defense'] / 2)
        :param turn_counter: every second round the defense is empowered. (return self.data['special-defense'])
        otherwise basic defense is returned (self.data['defense'])
        """
        if turn_counter % 2 == 0:
            return self.data["special-defense"] / 2
        return self.data["defense"] / 2

    def __str__(self):
        """
        String representation of json(self.data) object.
        One way to accomplish this is to use json.dumps functionality
        :return: string version of json file with necessary information
        """
        return json.dumps(self.data)

    def __repr__(self):
        """
        Object representation.
        :return: Pokemon's name in string format and his score, for example: "garchomp-mega 892"
        """
        return f"{self.data['name']}  {self.score}"


class World:
    """World class."""
    def __init__(self, name, offset, limit):
        """
        Class constructor.
        :param name: name of the pokemon world
        :param offset: offset for api request
        :param limit: limit for api request
        Check if f"{name}_{offset}_{limit}.txt" file exists, if it does, read pokemons in from that file, if not, then make an api
        request to f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}" to get pokemons and dump them to
        f"{name}_{offset}_{limit}.txt" file
        """
        self.pokemons = []
        url = f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}"
        filename = f"{name}_{offset}_{limit}.txt"
        result = requests.get(url).json()
        for pokemon_data in result["results"]:
            url = pokemon_data["url"]
            self.pokemons.append(Pokemon(url))
        if os.path.exists(name):
            f = open(name, "r")
            for line in f:
                print(line)
        else:
            self.dump_pokemons_to_file_as_json(filename)

    def dump_pokemons_to_file_as_json(self, name):
        """
        :param name: name of the .txt file
        Write all self.pokemons separated by a newline to the given filename(if it doesnt exist, then create one)
        PS: Write the pokemon.__str__() version, not __repr__() as only name is useless :)
        """
        with open(name, "w+") as f:
            for p in self.pokemons:
                f.write(p.__str__() + "\n")

    def fight(self):
        """
        A wild brawl between all pokemons where points are assigned to winners
        Note, every pokemon fights another pokemon only once
        Fight lasts until one pokemon runs out of hp.
        every pokemon hits only 1 time per turn and they take turns when they attack.
        Call choose_which_pokemon_hits_first(pokemon1, pokemon2): to determine which pokemon hits first
        Call pokemon_duel function in this method with the aforementioned pokemons.
        every exception thrown by called sub methods must be caught and dealt with.
        """
        for i in range(len(self.pokemons)):
            for j in range(i + 1, len(self.pokemons)):
                order = self.choose_which_pokemon_hits_first(self.pokemons[i], self.pokemons[j])
                self.pokemon_duel(order[0], order[1])

    @staticmethod
    def pokemon_duel(pokemon1, pokemon2):
        """
        :param pokemon1: pokemon, who attacks first.
        :param pokemon2: pokemon, who attacks second.
        :return winner: pokemon, who won.

        Here 2 pokemons fight.
        To get the attack and defense of the pokemon, call pokemon1.get_pokemon_attack()
        and pokemon1.get_pokemon_defense() respectively.
        Attack is multiplied by the pokemon1.get_attack_multiplier(list(second.data['types'])) multiplier
        Total attack is
        pokemon1.get_pokemon_attack(turn_counter) * multiplier1 - second.get_pokemon_defense(turn_counter)
        [turn counter starts from 1]
        Total attack is subtracted from other pokemons hp.
        Pokemons can not heal during the fight. (when total attack is negative, no damage is dealt)
        If the fight between 2 pokemons lasts more than 100 turns, then PokemonFightResultsInATieException() is thrown.
        If one pokemon runs out of hp, fight ends and the winner gets 1 point, (self.score += 1)
        then both pokemons are healed to full hp.
        """
        p1_full_hp = pokemon1.data["hp"]
        p2_full_hp = pokemon2.data["hp"]
        turn_counter = 1
        while True:
            if turn_counter > 100:
                pokemon1.data["hp"] = p1_full_hp
                pokemon2.data["hp"] = p2_full_hp
                raise PokemonFightResultsInATieException("Pokemon fight results in a tie.")
            total_attack1 = pokemon1.get_pokemon_attack(turn_counter) * \
                pokemon1.get_attack_multiplier(list(pokemon2.data["types"])) - \
                pokemon2.get_pokemon_defense(turn_counter)
            pokemon2.data["hp"] -= total_attack1

            total_attack2 = pokemon2.get_pokemon_attack(turn_counter) * \
                pokemon2.get_attack_multiplier(list(pokemon1.data["types"])) - \
                pokemon1.get_pokemon_defense(turn_counter)

            pokemon1 .data["hp"] -= total_attack2
            if pokemon2.data["hp"] <= 0:
                pokemon1.score += 1
                break
            elif pokemon1.data["hp"] <= 0:
                pokemon2.score += 1
                break
            turn_counter += 1
        pokemon1.data["hp"] = p1_full_hp
        pokemon2.data["hp"] = p2_full_hp

    @staticmethod
    def choose_which_pokemon_hits_first(pokemon1, pokemon2):
        """
        :param pokemon1:
        :param pokemon2:
        Pokemon who's speed is higher, goes first. if both pokemons have the same speed, then pokemon who's weight
        is lower goes first, if both pokemons have same weight, then pokemon who's height is lower goes first,
        if both pokemons have the same height, then the pokemon with more abilities goes first, if they have the same
        amount of abilities, then the pokemon with more moves goes first, if the pokemons have the same amount of
        moves, then the pokemon with higher base_experience goes first, if the pokemons have the same
        base_experience then SamePokemonFightException() is thrown
        :return pokemon1 who goes first and pokemon2 who goes second (return pokemon1, pokemon2)
        """
        if pokemon1.data["speed"] == pokemon2.data["speed"]:
            if pokemon1.data["weight"] == pokemon2.data["weight"]:
                if pokemon1.data["height"] == pokemon2.data["height"]:
                    if len(pokemon1.data["abilities"]) == len(pokemon2.data["abilities"]):
                        if len(pokemon1.data["moves"]) == len(pokemon2.data["moves"]):
                            if pokemon1.data["base_experience"] == pokemon2.data["base_experience"]:
                                raise SamePokemonFightException("Can't decide who goes first.")
                            else:
                                return sorted((pokemon1, pokemon2), key=lambda x: -x.data["base_experience"])
                        else:
                            return sorted((pokemon1, pokemon2), key=lambda x: -len(x.data["moves"]))
                    else:
                        return sorted((pokemon1, pokemon2), key=lambda x: -len(x.data["abilities"]))
                else:
                    return sorted((pokemon1, pokemon2), key=lambda x: x.data["height"])
            else:
                return sorted((pokemon1, pokemon2), key=lambda x: x.data["weight"])
        else:
            return sorted((pokemon1, pokemon2), key=lambda x: -x.data["speed"])

    def get_leader_board(self):
        """
        Get Pokemons by given format in a list sorted by the pokemon.score.

         In case of the same score, order pokemons by their name (ascending).

        :return: List of leader board. where winners are first
        """
        return sorted(self.pokemons, key=lambda x: (-x.score, x.data["name"]))

    def get_pokemons_sorted_by_attribute(self, attribute: str):
        """
        Get Pokemons by given format in a list sorted by the pokemon.data[attribute]
        :param attribute:  pokemon data attribute to sort by
        :return: sorted List of pokemons
        """
        return sorted(self.pokemons, key=lambda x: x.data[attribute])


if __name__ == '__main__':
    world = World("PokeLand", 15, 20)
    world.fight()
    print(world.get_leader_board())
