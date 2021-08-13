import time
from abc import ABC, abstractmethod
from enum import Enum
from weapons import bow, generate_weapon, hard, load_weapon_from_dict, weapon
import json

def player_class_parser(class_of_player: str):
    if class_of_player == 'warrior':
        return warrior
    elif class_of_player == 'thief':
        return thief
    elif class_of_player == 'bower':
        return bower

class person:
    def get_hp(self):
        return self._hp
    def get_max_hp(self):
        return self._max_hp
    def get_attack(self):
        return self._attack + self._weapon.get_attack()
    def get_armor(self):
        return self._armor
    def get_level(self):
        return self._level
    def get_name(self):
        return self._name
    def get_eqip(self):
        return self._equipment
    def get_items(self):
        return self._items
    def get_weapon(self):
        return self._weapon
    def set_hp(self, hp):
        self._hp = hp
    def set_max_hp(self, hp):
        self._max_hp = hp
    def set_armor(self, armor):
        self._armor = armor
    def set_attack(self, attack):
        self._attack = attack
    def set_name(self, name):
        self._name = name
    def set_eqip(self, equipment):
        self._equipment = equipment
    def set_items(self, items):
        self._items = items
    def set_weapon(self, weapon):
        self._weapon = weapon
    def get_equipment(self):
        return json.dumps({'weapon' : self._weapon.dict()})

    def __init__(self, hp, attack, armor):
        self._hp = hp
        self._attack = attack
        self._armor = armor
    def is_alife(self):
        return self._alife
    
    def take_damage(self, damage):
        self._hp -= damage
        if self._hp <= 0:
            self._alife = False

    _equipment: str = ''
    _items: str = ''
    _name: str = 'OLEG'
    _max_hp: int = 0
    _hp: int = 1000
    _attack: int = 0
    _armor: int = 0
    _level: int = 1
    _alife: bool = True
    _weapon: weapon = None
    
class player(person, ABC):
    
    def __init__(self, id, class_of_player, name, max_hp, 
                armor, attack, level = 1, hp = None, equipment = None, 
                items = None, money = 0, state = 'class', weapon = None):
        if hp == None:
            self._hp = max_hp
        else:
            self._hp = hp
        self._id_of_owner = id
        self._attack = attack
        self._armor = armor
        self._name = name
        self._equipment = equipment
        self._items = items
        self._max_hp = max_hp
        self._state = state
        self._level = level
        self._money = money
        self.__class_of_player = class_of_player
        #print(equipment)
        if equipment != None:
            self._weapon = load_weapon_from_dict(json.loads(equipment)['weapon'])
        
        
    def get_all_atributes(self):
        return({'id' : self._id_of_owner, 'class' : self.__class_of_player, 'name' : self._name, 
               'max_hp' : self._max_hp, 'armor' : self._armor, 'attack' : self._attack, 
               'level' : self._level, 'hp' : self._hp, 'equipment' : self._equipment, 
               'items' : self._items, 'money' : self._money, 'state' : self._state})
    def set_class_of_player(self, class_of_player):
        self.__class_of_player = class_of_player
    def get_state(self):
        return self._state
    def set_state(self, state):
        self._state = state
    def get_money(self):
        return self._money
    def get_agility(self):
        return self._agility
    def get_id(self):
        return self._id_of_owner
    def add_money(self, money):
        self._money += money
    def add_xp(self, xp):
        self._xp += xp
        if self._xp >= self._xp_next_level:
            self.level_up()
            self._xp -= self._xp_next_level
            self._xp_next_level *= 1.25
    def get_available_weapon(self):
        return self._available_weapon

    @abstractmethod
    def level_up(self):
        self._level += 1
    
    def take_damage(self, damage):
        self._hp -= damage
        if self._hp <= 0:
            self._alife = False
            if self._money >= 500:
                self._money -= 500
                self._hp = self._max_hp
            else:
                self._money -= 500
                self._hp = self._max_hp / 2
                
    _id_of_owner: int = 0
    _available_weapon = None
    __class_of_player: str = None
    _money: int = 100
    _state: str = ''
    _agility: int = 1
    _xp = 0
    _xp_next_level = 100
    
#слишком похожие классы
class warrior(player):
    def get_class(self):
        return 'Воин'
    def level_up(self):
        self._level += 1
        self._max_hp += 100
        self._attack += 100
        self._armor += 50
    
    _available_weapon = 'hard'
    _agility = 0.75

class thief(player):
    
    def get_class(self):
        return 'Вор'
    
    def level_up(self):
        self._level += 1
        self._max_hp += 50
        self._attack += 75
        self._armor += 25
    
    _available_weapon = 'light'
    _agility = 1.5

class bower(player):
    
    def get_class(self):
        return 'Лучник'
    
    def level_up(self):
        self._level += 1
        self._max_hp += 75
        self._attack += 100
        self._armor += 25
    
    _available_weapon = 'bow'
    _agility = 1
