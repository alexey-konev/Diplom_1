import allure
import pytest
import pytest_cov


class TestBurger:

    @allure.title("Проверка метода инициализации - булка")
    def test_burger_init_bun_none(self, new_burger):

        assert new_burger.bun is None

    @allure.title("Проверка метода инициализации - ингредиенты")
    def test_burger_init_ingredients_empty(self, new_burger):

        assert new_burger.ingredients == []

    @allure.title("Проверка метода выбора булки для бургера")
    def test_burger_set_bun(self, new_burger, new_bun):
        new_burger.set_buns(new_bun)

        assert new_burger.bun.get_name() == 'Булочка' and new_burger.bun.get_price() == 100

    @allure.title("Проверка метода добавления ингредиента в бургер")
    def test_burger_add_ingredient(self, new_burger, new_ingredient_1):
        new_burger.add_ingredient(new_ingredient_1)

        assert len(new_burger.ingredients) == 1 and new_burger.ingredients[0].get_name() == 'Имя1'

    @allure.title("Проверка метода удаления ингредиента из бургера")
    @pytest.mark.parametrize('index, remaining_name',
                             [
                                 [0, 'Имя2'],  # удаление певой позиции - остается второй ингредиент
                                 [1, 'Имя1']   # удаление второй позиции - остается первый ингредиент
                             ])
    def test_burger_remove_ingredient(self, new_burger, new_ingredient_1, new_ingredient_2, index, remaining_name):
        new_burger.add_ingredient(new_ingredient_1)
        new_burger.add_ingredient(new_ingredient_2)

        new_burger.remove_ingredient(index)

        assert len(new_burger.ingredients) == 1 and new_burger.ingredients[0].get_name() == remaining_name

    @allure.title("Проверка метода перестановки ингредиентов в бургере")
    @pytest.mark.parametrize('new_index, index, pos_1, pos_3',
                             [
                                 [0, 1, 'Имя2', 'Имя3'],  # второй на место певрого - Имя2, Имя1, Имя3
                                 [0, 2, 'Имя3', 'Имя2'],  # третий на место певрого - Имя3, Имя1, Имя2
                                 [1, 2, 'Имя1', 'Имя2'],  # третий на место второго - Имя1, Имя3, Имя2
                                 [2, 0, 'Имя2', 'Имя1']  # первый на место третьего - Имя2, Имя3, Имя1
                             ])
    def test_burger_move_ingredient(self, new_burger, new_ingredient_1, new_ingredient_2, new_ingredient_3,
                                    new_index, index, pos_1, pos_3):
        new_burger.add_ingredient(new_ingredient_1)
        new_burger.add_ingredient(new_ingredient_2)
        new_burger.add_ingredient(new_ingredient_3)

        new_burger.move_ingredient(index, new_index)  # индекс первой позиции = 0

        assert new_burger.ingredients[0].get_name() == pos_1 and new_burger.ingredients[2].get_name() == pos_3

    @allure.title("Проверка метода получения цены бургера")
    def test_burger_get_price(self, new_burger, new_bun, new_ingredient_1, new_ingredient_2):
        new_burger.set_buns(new_bun)  # цена 100
        new_burger.add_ingredient(new_ingredient_1)  # цена 10
        new_burger.add_ingredient(new_ingredient_2)  # цена 20

        assert new_burger.get_price() == 230

    @allure.title("Проверка метода получения чека бургера")
    def test_burger_get_price(self, new_burger, new_bun, new_ingredient_1, new_ingredient_2, new_ingredient_3):
        new_burger.set_buns(new_bun)
        new_burger.add_ingredient(new_ingredient_1)
        new_burger.add_ingredient(new_ingredient_2)
        new_burger.add_ingredient(new_ingredient_3)

        assert new_burger.get_receipt() == ('(==== Булочка ====)\n'
                                            '= тип1 Имя1 =\n'
                                            '= тип2 Имя2 =\n'
                                            '= тип3 Имя3 =\n'
                                            '(==== Булочка ====)\n\n'
                                            'Price: 260')

