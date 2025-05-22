import random
import extensiveFormGame
from extensiveFormGame import extensiveFormGameStart, Node

players = ["Bob", "Alice"]
splitOrSteal = extensiveFormGameStart(players)

splitFirst = splitOrSteal.addBranch(splitOrSteal.root, players, action=["Split"])
stealFirst = splitOrSteal.addBranch(splitOrSteal.root, players, action=["Steal"])