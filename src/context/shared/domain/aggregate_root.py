from abc import ABC, abstractmethod
from typing import List
from domain_event import DomainEvent

class AggregateRoot(ABC):
    def __init__(self):
        self._domain_events = []

    def record(self, event: DomainEvent):
        self._domain_events.append(event)

    def pull_domain_events(self) -> List[DomainEvent]:
        events = self._domain_events
        self._domain_events = []
        return events

    @abstractmethod
    def to_primitives(self):
        pass