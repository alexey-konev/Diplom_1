import allure
import pytest
import pytest_cov


class TestIngredient:

    @allure.title("Проверка метода инициализации Ingredient")
    def test_ingredient_init(self, new_ingredient_1):

        assert (new_ingredient_1.type == 'Тип1' and new_ingredient_1.name == 'Имя1'
                and new_ingredient_1.price == 10)

    @allure.title("Проверка методов класса Ingredient - получение типа")
    def test_ingredient_get_type(self, new_ingredient_1):

        assert new_ingredient_1.get_type() == 'Тип1'

    @allure.title("Проверка методов класса Ingredient - получение имени")
    def test_ingredient_get_name(self, new_ingredient_1):

        assert new_ingredient_1.get_name() == 'Имя1'

    @allure.title("Проверка методов класса Ingredient - получение цены")
    def test_ingredient_get_price(self, new_ingredient_1):

        assert new_ingredient_1.get_price() == 10

