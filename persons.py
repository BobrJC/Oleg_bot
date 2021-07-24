import time
from abc import abstractmethod
from enum import Enum

class person:
    def get_hp(self):
        return self._hp
    def get_max_hp(self):
        return self._max_hp
    def get_attack(self):
        return self._attack
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
    
class player(person):
    
    def __init__(self, name, max_hp, armor, attack, 
                level = 1, hp = None, equipment = None, 
                items = None, money = 0, state = 'name', 
                class_of_plater = 'new player'):
        if hp == None:
            self._hp = max_hp
        else:
            self._hp = hp
        self._attack = attack
        self._armor = armor
        self._name = name
        self._equipment = equipment
        self._items = items
        self._max_hp = max_hp
        self._state = state
        self._level = level
        self._money = money
        self.__class_of_player = class_of_plater

    def set_class_of_player(self, class_of_player):
        self.__class_of_player = class_of_player
    def get_all_atributes(self):
        return({'class' : self.__class_of_player, 'name' : self._name, 
               'max_hp' : self._max_hp, 'armor' : self._armor, 'attack' : self._attack, 
               'level' : self._level, 'hp' : self._hp, 'equipment' : self._equipment, 
               'items' : self._items, 'money' : self._money, 'state' : self._state})
    def get_state(self):
        return self._state
    def set_state(self, state):
        self._state = state
    def get_money(self):
        return self._money
    def get_agility(self):
        return self._agility
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
        self.__hp -= damage
        if self.__hp <= 0:
            self.__alife = False
            if self._money >= 500:
                self._money -= 500
                self._hp = self._max_hp
            else:
                self._money -= 500
                self._hp = self._max_hp / 2
    
    __class_of_player: str = None
    _money: int = 100
    _state: str = ''
    _agility: int = 1
    _xp = 0
    _xp_next_level = 100
    
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
    
    _available_weapon = 'bows'
    _agility = 1