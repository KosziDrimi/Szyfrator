# -*- coding: utf-8 -*-



from __future__ import annotations
from abc import ABC, abstractmethod


class Szyfr:
    
    def __init__(self, strategy: SzyfratorBase) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> SzyfratorBase:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: SzyfratorBase) -> None:
        self._strategy = strategy

    def szyfrowanie(self, text) -> None:
        result = self._strategy.zaszyfruj(text)
        return result

      
class SzyfratorBase(ABC):

    @abstractmethod
    def zaszyfruj(self, text):
        pass


class Gaderypoluki(SzyfratorBase):
    
    def zaszyfruj(self, text):
        gaderypoluki = {'g': 'a', 'd': 'e', 'r': 'y', 'p': 'o', 'l': 'u', 'k': 'i'} 
        gaderypoluki_inv = {val: key for key, val in gaderypoluki.items()}
    
        result = ''    
        for char in text:
            if char in gaderypoluki.keys():
                result += gaderypoluki[char]
            elif char in gaderypoluki_inv.keys():
                result += gaderypoluki_inv[char]
            else:
                result += char
        return result     
            

class Politykarenu(SzyfratorBase):
    
    def zaszyfruj(self, text):
        politykarenu = {'p': 'o', 'l': 'i', 't': 'y', 'k': 'a', 'r': 'e', 'n': 'u'} 
        politykarenu_inv = {val: key for key, val in politykarenu.items()}
    
        result = ''    
        for char in text:
            if char in politykarenu.keys():
                result += politykarenu[char]
            elif char in politykarenu_inv.keys():
                result += politykarenu_inv[char]
            else:
                result += char
        return result  


class Drukarka:
    
    def wydrukuj(wynik):
        print(f'Wydrukowałem: "{wynik}"')
        

class Ekran:
    
    def wypisz(wynik):
        print(f'Wypisałem: "{wynik}"')        
        

class Email:
    
    def wyslij(wynik):
        print(f'Wysłałem: "{wynik}"')
        
    
if __name__ == '__main__': 
    
    
    szyfr = Szyfr(Gaderypoluki())
    wynik = szyfr.szyfrowanie('kłobuck')
    
    Drukarka.wydrukuj(wynik)

    szyfr.strategy = Politykarenu()
    wynik = szyfr.szyfrowanie('kłobuck')
    
    Ekran.wypisz(wynik)
    Email.wyslij(wynik)