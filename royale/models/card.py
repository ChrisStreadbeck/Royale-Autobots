from pydantic.dataclasses import dataclass


@dataclass
class Card:
    id: int
    name: str
    icon: str
    cost: int
    rarity: str
    type: str
    arena: int
