from abc import ABC, abstractmethod

class ValueObject(ABC):
    def __init__(self, value):
        self._value = value

    @property
    @abstractmethod
    def value(self):
        pass


class IntValueObject(ValueObject):
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")
        super().__init__(value)

    @property
    def value(self) -> int:
        return self._value

class StringValueObject(ValueObject):
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        super().__init__(value)

    @property
    def value(self) -> str:
        return self._value

class FloatValueObject(ValueObject):
    def __init__(self, value):
        if not isinstance(value, float):
            raise ValueError("Value must be a float")
        super().__init__(value)

    @property
    def value(self) -> float:
        return self._value

class BoolValueObject(ValueObject):
    def __init__(self, value):
        if not isinstance(value, bool):
            raise ValueError("Value must be a boolean")
        super().__init__(value)

    @property
    def value(self) -> bool:
        return self._value