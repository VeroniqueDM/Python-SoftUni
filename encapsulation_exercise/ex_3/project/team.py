from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player._Player__name} has already joined"
        self.__players.append(player)
        return f"Player {player._Player__name} joined team {self.__name}"

    def remove_player(self, player_name):
        for team_player in self.__players:
            if team_player.name == player_name:
                self.__players.remove(team_player)
                return team_player
            # if player._Player__name == player_name:
            #     self.__players.remove(player)
            #     return player
        return f"Player {player_name} not found"
