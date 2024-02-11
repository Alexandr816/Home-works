import pytest
from c.calculator import Calculator


class Test_Calc:
    '''Только позитивные тесты функций калькулятора'''
    def setup(self):
        self.calc = Calculator


    def test_multi(self):
        '''Проверяем умножение'''
        assert self.calc.multiply(self.calc,5,5) == 25



    def test_division(self):
        '''Проверяем деление'''
        assert self.calc.division(self, 36,6) == 6


    def test_succ_addi(self):
        '''Проверяем сложение'''
        assert self.calc.adding(self,30.6,6,) == 36.6


    def test_subtraction(self):
        '''Проверяем вычетание'''
        assert self.calc.subtraction(self,50,49) == 1