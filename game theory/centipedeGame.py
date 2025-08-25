import extensiveFormGame
from extensiveFormGame import extensiveFormGameStart, Node

players = ["Bob", "Alice"]
centipedeGame = extensiveFormGameStart(players)

centipedeGame.addBranch(centipedeGame.root)
