from context.shared.domain import AggregateRoot
from .character_health import CharacterHealth
from .character_attack import CharacterAttack
from .character_name import CharacterName
from .character_mana import CharacterMana 
from .character_level import CharacterLevel
from .character_defense import CharacterDefense

class Character(AggregateRoot):
    def __init__(self, 
                 name: CharacterName,  
                 health: CharacterHealth, 
                 attack: CharacterAttack,
                 defense: CharacterDefense,
                 mana: CharacterMana,
                 level: CharacterLevel
                ):
        super()
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.mana = mana
        self.level = level

    def calculate_received_damage(self, damage: int) -> int:
        received_damage = damage - self.defense.value
        if received_damage < 0:
            received_damage = 0
        return received_damage    

    def to_primitives(self):
        return {
            'health': self.health.value,
            'attack': self.attack.value
        }