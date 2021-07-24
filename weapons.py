from constants import weapon_types, weapon_left_properties, weapon_right_properties
import random
def type_attack(type: str):
    pass
def generate_weapon(type: str, level: int):
    return weapon(level, random.randrange(0, len(weapon_types)))
class weapon():

    def __init__(self, level: int, attack: int, attack_speed: int, left_property: str, type: str, right_property: str):
        self._level = level
        self._attack = attack
        self._attack_speed = attack_speed
        self._left_property = left_property
        self._type = type
        self._right_property = right_property
    
    _level: int
    _attack: int
    _attack_speed: int
    _left_property: str
    _right_property: str
    _type: str

