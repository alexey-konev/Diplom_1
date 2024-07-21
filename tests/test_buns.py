from praktikum.bun import Bun

import pytest
import pytest_cov


class TestBuns:

    def test_bun_init(self):

        bun = Bun('Булочка', 100)

        assert bun.name == 'Булочка'
