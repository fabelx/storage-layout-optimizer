from sl_optimizer import new_storage_layout
from tests.conftest import get_fixture_path


def test_new_storage_layout():
    sl = new_storage_layout(get_fixture_path("simple_4_variables.json"))
    assert sl.contract_name == "Simple4Variables"
