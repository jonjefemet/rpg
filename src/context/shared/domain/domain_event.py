from abc import ABC
from datetime import datetime
import uuid

class DomainEvent(ABC):
    def __init__(self):
        self._event_id = str(uuid.uuid4())
        self._occurred_on = datetime.now()

    @property
    def event_id(self):
        return self._event_id

    @property
    def occurred_on(self):
        return self._occurred_on