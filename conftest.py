import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient



@pytest.fixture(scope='class')
def new_bun():
    bun = Bun('Булочка', 100)
    return bun

@pytest.fixture(scope='class')
def new_ingredient_1():
    ingredient = Ingredient('Тип1', 'Имя1', 10)
    return ingredient

@pytest.fixture(scope='class')
def new_ingredient_2():
    ingredient = Ingredient('Тип2', 'Имя2', 20)
    return ingredient

@pytest.fixture(scope='class')
def new_ingredient_3():
    ingredient = Ingredient('Тип3', 'Имя3', 30)
    return ingredient

@pytest.fixture(scope='function')
def new_burger():
    burger = Burger()
    return burger
