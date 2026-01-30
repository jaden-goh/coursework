
from typing import List, Final

class Item:
    
    def __init__(self, name: str, power: int, weight: int, rarity: int) -> None:
        self.name = name
        self.weight = weight
        self.power = power
        self.rarity = rarity

    def __repr__(self) -> None:
        pass 

    def __str__(self) -> None:
        print(f"Character: {self.name} \n Weight: {self.weight}, Power: {self.power}, Rarity: {self.rarity}")
    
class Character:

    def __init__(self, name: str, HP: int, attack: int, defense: int) -> None:
        self.name = name
        self._HP = HP
        self._attack = attack
        self._defense = defense

    @property
    def HP(self) -> int: 
        return self._HP
    
    @HP.setter 
    def HP(self, hp: int) -> None:
        if hp < 0:
            raise ValueError("HP cannot be negative.")
        else:
            self._HP = hp

    @property
    def attack(self) -> int: 
        return self._attack
    
    @attack.setter 
    def attack(self, att: int) -> None:
        if att < 0:
            raise ValueError("Attack stat cannot be negative.")
        else:
            self._attack = att

    @property
    def defense(self) -> int: 
        return self._defense
    
    @attack.setter 
    def defense(self, de: int) -> None:
        if de < 0:
            raise ValueError("Defense stat cannot be negative.")
        else:
            self._defense = de

    def voiceline(self) -> None:
        print(f"(VOICE) {self.name}: Here. we. go.")

class Player(Character):
    def __init__(self, name: str, HP: int, attack: int, defense: int, mult: int):
        super.__init__(name, HP, attack, defense)
        self.multipler = mult

    def voiceline(self):
        print(f"(VOICE) {self.name}: Lets seize the day.")

class Enemy(Character):
    def __init__(self, name: str, HP: int, attack: int, defense: int, threat: int):
        super.__init__(name, HP, attack, defense)
        self.threat = threat

    
    def voiceline(self):
        print(f"(VOICE) {self.name} ({self.threat}): The fields yearn.")

class Inventory:
    def __init__(self):
        self.inventory: List[Item] = []
        self.LIMIT: Final[int] = 10
        
    def __len__(self):
        return len(self.inventory)
    
    def __iter__(self):
        pass

    def __contains__(self):
        pass
    
    def __getitem__(self):
        pass
    
    def __setitem__(self):
        pass
    
    def total_weight(self) -> int:
        sum = 0
        for item in self.inventory:
            sum += item.weight

    def add_item(self, item: Item) -> None:
        if self.__len__() >= self.LIMIT:
            raise ValueError("Item Capacity Reached.")
        else:
            self.inventory.append(item)


















































































































