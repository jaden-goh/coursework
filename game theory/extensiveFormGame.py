class Node:
    def __init__(self, parent, players, action=None, outcome=None):
        self.parent = parent
        self.players = players
        self.action = action
        self.outcome = outcome
        self.children = []
    
    @property
    def isTerminal(self):
        return len(self.children) == 0

    def __repr__(self):
        return f"Node(Player: {self.players}, Action: {self.action}, Outcome: {self.outcome})"
    

class extensiveFormGameStart:
    def __init__(self, players):
        self.players = players
        self.root = Node(None, players)
        for player in players:
            print(f"Welcome, {player}!")
    
    def addBranch(self, current_node, players, action, outcome=None):
        if current_node.isTerminal:
            raise ValueError("Cannot add children to a terminal node with an Outcome")
        else:
            new_node = Node(current_node, players, action, outcome)
            current_node.children.append(new_node)
        return new_node

