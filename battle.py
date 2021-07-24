from persons import *
import asyncio

class battle:

    def __init__(self, first_fighter: player, second_fighter: person):
        self._first_fighter = first_fighter
        self._second_fighter = second_fighter
    async def start(self):
        while self._first_fighter.is_alife() and self._second_fighter.is_alife():
            
    
    _first_fighter: player
    _second_fighter: person 