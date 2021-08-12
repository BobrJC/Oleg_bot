from typing import Dict
from constants import weapon_types, weapon_left_properties, weapon_right_properties
from random import randrange
from abc import ABC, abstractmethod
from dataclasses import dataclass
from ast import literal_eval


@dataclass
class weapon:
    _level: int
    _left_property: str
    _right_property: str
    _attack: int = None
    _attack_coeff: int = None
    _attack_speed: int = None
    _type: str = None
    _name: str = None
    def get_full_name(self) -> str:
        return self._left_property + ' ' + self._name + ' ' + self._right_property
    def get_attack(self):
        return self._attack

    def dict(self):
        return vars(self)
    
@dataclass
class hard(weapon):
    _attack: int = 0
    _attack_speed: int = 1
    _type: str = 'hard'
    _attack_coeff = 100
    
    
@dataclass
class bow(weapon):
    _attack: int = 0
    _attack_speed: int = 1
    _type: str = 'bow'
    _attack_coeff = 70
    
@dataclass
class light(weapon):
    _attack: int = 0
    _attack_speed: int = 1
    _type: str = 'light'
    _attack_coeff = 50
    

def type_parse_from_type(type: str):
    if type == 'hard':
        return hard
    if type == 'light':
        return light
    if type == 'bow':
        return bow

def type_parse_from_name(weapon_type: str) -> weapon:
    for type in weapon_types:
        if weapon_type in weapon_types[type]:
            return type_parse_from_type(type)

def generate_weapon(type_str: str, level: int):
    type = type_parse_from_type(type_str)
    left_property = weapon_left_properties[randrange(0, len(weapon_left_properties))]
    right_property = weapon_right_properties[randrange(0, len(weapon_right_properties))]
    name = weapon_types[type_str][randrange(0, len(weapon_types[type_str]))]
    attack = level*type._attack_coeff + randrange(-type._attack_coeff, type._attack_coeff)
    return type(level, left_property, right_property, attack, _attack_coeff=type._attack_coeff, _name= name)

# def get_weapon_from_string(weapon_string: str) -> weapon:
#     weapon_string = weapon_string.split()
#     left_property = weapon_string[0]
#     weap_name = weapon_string[1]
#     right_property = ' '.join([weapon_string[part] for part in range(2, len(weapon_string) - 1)])
#     weap_level = int(weapon_string[len(weapon_string) - 1])
#     return type_parse_from_name(weap_name)(weap_level, left_property, right_property)

def load_weapon_from_dict(dict):
        level = dict['_level']
        left_property = dict['_left_property']
        name = dict['_name']
        type = dict['_type']
        right_property = dict['_right_property']
        attack = dict['_attack']
        attack_speed = dict['_attack_speed']
        return weapon(level, left_property, right_property, attack, type_parse_from_type(type)._attack_coeff, attack_speed, type, name)
