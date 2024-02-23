import pytest

from sl_optimizer import get_number_of_slots


@pytest.mark.parametrize("filename", ("uniswap_v3_factory_storage.json",))
def test_get_number_of_slots(storage_layout):
    assert (
        get_number_of_slots(
            storage=storage_layout.get("storage"), types=storage_layout.get("types")
        )
        == 6
    )
