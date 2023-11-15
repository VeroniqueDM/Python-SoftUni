
class Controller:
    SUPPLIES_TYPES = ['Food', 'Drink']
    def __init__(self):
        self.players = []
        self.supplies = []

    # def find_if_same_name_player_exists(self, new_player):
    #     for player in self.players:
    #         if player.name == new_player.name:
    #             return player
    #     return None
    def find_player_by_name(self, name):
        for player in self.players:
            if player.name == name:
                return player
        return None

    def find_last_supply_by_supply_type(self, supply_type):
        if supply_type not in self.SUPPLIES_TYPES:
            return None
        for ind in range(len(self.supplies)-1, -1, -1):
            supply = self.supplies[ind]
            if supply.__class__.__name__ == supply_type:
                return supply
        raise Exception(f"There are no {supply_type.lower()} supplies left!")

    def add_player(self, *args):
        new_players = []
        for player in args:
            if player in self.players:
                continue
            new_players.append(player)
            self.players.append(player)
        return f"Successfully added: {', '.join([player.name for player in new_players])}"
            # if self.find_if_same_name_player_exists() is None:
            #     self.players.append(player)

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        supply = self.find_last_supply_by_supply_type(sustenance_type)
        if supply is None:
            return
        player = self.find_player_by_name(player_name)
        if player:
            if player.need_sustenance:
                sustenance_needed = player.STAMINA_MAX_VALUE - player.stamina
                energy = supply.energy

                if sustenance_needed <= energy:
                    player.stamina = player.STAMINA_MAX_VALUE
                else:
                    player.stamina += supply.energy
                self.supplies.remove(supply)
                return f"{player_name} sustained successfully with {supply.name}."
            else:
                return f"{player_name} have enough stamina."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.find_player_by_name(first_player_name)
        second_player = self.find_player_by_name(second_player_name)

        if first_player.stamina <= 0:
            if second_player.stamina <= 0:
                res = f"Player {first_player.name} does not have enough stamina."\
                      + '\n'\
                      + f"Player {second_player.name} does not have enough stamina."
                return res
            return f"Player {first_player.name} does not have enough stamina."
        elif second_player.stamina <= 0:
            f"Player {second_player.name} does not have enough stamina."
        return self.duel_two_players(first_player, second_player)

    def duel_two_players(self, first_player, second_player):
        sorted_players = sorted([first_player, second_player], key=lambda x:x.stamina)
        lower_value, higher_value = sorted_players[0], sorted_players[1]
        if higher_value.stamina < lower_value.stamina / 2:
            higher_value.stamina = higher_value.STAMINA_MIN_VALUE
            return f"Winner: {lower_value.name}"
        else:
            higher_value.stamina -= lower_value.stamina / 2
        if lower_value.stamina < higher_value.stamina / 2:
            lower_value.stamina = lower_value.STAMINA_MIN_VALUE
            return f"Winner: {higher_value.name}"
        else:
            lower_value.stamina -= higher_value.stamina / 2
        if lower_value.stamina > higher_value.stamina:
            return f"Winner: {lower_value.name}"
        return f"Winner: {higher_value.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = player.STAMINA_MIN_VALUE
            else:
                player.stamina -= (player.age * 2)
        for player in self.players:
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')



    def __str__(self):
        players = '\n'.join([str(player) for player in self.players])
        supplies = '\n'.join([supply.details() for supply in self.supplies])
        return players + '\n' + supplies
