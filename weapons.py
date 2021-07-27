from constants import weapon_types, weapon_left_properties, weapon_right_properties
import random
from abc import ABC, abstractmethod
from dataclasses import dataclass

def type_parse_from_type(type: str):
    if type == 'hard':
        return hard
    if type == 'light':
        return light
    if type == 'bow':
        return bow

def generate_weapon(type: str, level: int):
    left_property = weapon_left_properties[random.randrange(0, len(weapon_left_properties))]
    right_property = weapon_right_properties[random.randrange(0, len(weapon_right_properties))]
    return type_parse_from_type(type)(level, left_property, right_property)
@dataclass
class weapon:
    # def __init__(self, level: int, attack: int, left_property: str, right_property: str, attack_speed: int, type: str):
    #     self._level = level
    #     self._attack = attack
    #     self._attack_speed = attack_speed
    #     self._left_property = left_property
    #     self._type = type
    #     self._right_property = right_property
    _level: int
    _left_property: str
    _right_property: str
    _attack: int = None
    _attack_speed: int = None
    _name: str = None
    _type: str = None
    
@dataclass
class hard(weapon):
    _attack: int = 0
    _attack_speed: int = 1
    _name: str = ''
    _type: str = 'hard'
    def __post_init__(self):
        self._attack = self._level*100 + random.randrange(-100, 100)
        self._name = self._left_property + ' ' + weapon_types[self._type][random.randrange(0, len(weapon_types[self._type]))] + ' ' + self._right_property
    
@dataclass
class bow(weapon):
    _attack: int = 0
    _attack_speed: int = 1
    _name: str = ''
    _type: str = 'bow'
    def __post_init__(self):
        self._attack = self._level*70 + random.randrange(-70, 70)
        self._name = self._left_property + ' ' + weapon_types[self._type][random.randrange(0, len(weapon_types[self._type]))] + ' ' + self._right_property

@dataclass
class light(weapon):
    _attack: int = 0
    _attack_speed: int = 1
    _name: str = ''
    _type: str = 'light'
    def __post_init__(self):
        self._attack = self._level*50 + random.randrange(-50, 50)
        self._name = self._left_property + ' ' + weapon_types[self._type][random.randrange(0, len(weapon_types[self._type]))] + ' ' + self._right_property

def type_parse_from_name(weapon_type: str) -> weapon:
    for type in weapon_types:
        if weapon_type in weapon_types[type]:
            return type_parse_from_type(type)


def get_weapon_from_string(weapon_string: str) -> weapon:
    weapon_string = weapon_string.split()
    left_property = weapon_string[0]
    weap_name = weapon_string[1]
    right_property = ' '.join([weapon_string[part] for part in range(2, len(weapon_string) - 1)])
    weap_level = int(weapon_string[len(weapon_string) - 1])
    return type_parse_from_name(weap_name)(weap_level, left_property, right_property)


