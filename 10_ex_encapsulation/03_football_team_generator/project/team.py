from typing import List

from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    def add_player(self, player: Player):
        fnp = []
        for fp in self.__players:
            if player.name == fp.name:
                fnp = [fp]
                break
        if fnp:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        fnp = []
        for fp in self.__players:
            if player_name == fp.name:
                fnp = [fp]
                break
        if not fnp:
            return f"Player {player_name} not found"
        fnp = fnp[0]
        self.__players.remove(fnp)
        return fnp
