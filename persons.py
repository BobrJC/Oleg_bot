import time

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
    
    def take_damage(self, damage):
        self._hp -= damage
        if self._hp <= 0:
            self._alife = False
    
    _equipment = ''
    _items = ''
    _name = 'OLEG'
    _max_hp = 0
    _hp = 1000
    _attack = 0
    _armor = 0
    _level = 1
    _alife = True
    
class player(person):
    
    def __init__(self, name, max_hp, armor, attack, 
                level = 1, hp = None, equipment = None, 
                items = None, state = 'name', money = 0):
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
    
    def get_state(self):
        return self._state
    def set_state(self, state):
        self._state = state
    def level_up(self):
        self._level += 1
        self._hp += 50
        self._attack += 10

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
    
    _money = 100
    _state = ''
    