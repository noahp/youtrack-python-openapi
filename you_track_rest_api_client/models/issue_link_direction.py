from enum import Enum


class IssueLinkDirection(str, Enum):
    OUTWARD = "OUTWARD"
    INWARD = "INWARD"
    BOTH = "BOTH"

    def __str__(self) -> str:
        return str(self.value)
