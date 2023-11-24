from src.context.shared.domain import AggregateRoot
from .skill_name import SkillName
from .skill_mana import SkillMana
from abc import ABC, abstractmethod

class skill(AggregateRoot, ABC):
    def __init__(self, 
                 name: SkillName,
                 mana: SkillMana,
                ):
        super()
        self.mana = SkillMana
        self.name = SkillName

    @abstractmethod
    def apply(self):
        pass

    def to_primitives(self):
        return {
            'name': self.name.value,
            'mana': self.mana.value
        }