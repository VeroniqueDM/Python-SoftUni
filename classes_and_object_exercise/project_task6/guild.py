from project_task6.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != Player.DEFAULT_GUILD:
            return f"Player {player.name} is in another guild."
        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        existing_player = any([player_name == player.name for player in self.players])
        if not existing_player:
            return f"Player {player_name} is not in the guild."
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = Player.DEFAULT_GUILD
                return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f'Guild: {self.name}\n' + "\n".join(player.player_info() for player in self.players)
        return result


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
