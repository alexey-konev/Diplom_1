import allure
import pytest
import pytest_cov


class TestBun:

    @allure.title("Проверка метода инициализации Bun")
    def test_bun_init(self, new_bun):

        assert new_bun.name == 'Булочка' and new_bun.price == 100

    @allure.title("Проверка методов класса Bun - получение имени")
    def test_bun_get_name(self, new_bun):

        assert new_bun.get_name() == 'Булочка'

    @allure.title("Проверка методов класса Bun - получение цены")
    def test_bun_get_price(self, new_bun):

        assert new_bun.get_price() == 100

