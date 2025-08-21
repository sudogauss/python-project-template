import unittest
import pytest


@pytest.fixture(scope="class")
def generate_data(request) -> None:
    request.cls.data = "test_data"


@pytest.mark.usefixtures("generate_data")
class TemplateTest(unittest.TestCase):

    def setUp(self):
        pass

    @pytest.mark.unit
    def test_generated_data_unit(self):
        assert self.data == "test_data"

    @pytest.mark.core
    def test_generated_data_core(self):
        assert self.data == "test_data"
