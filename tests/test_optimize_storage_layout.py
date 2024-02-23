import pytest

from sl_optimizer import get_number_of_slots, optimize_storage_layout


@pytest.mark.parametrize(
    "filename,expected",
    (
        ("simple_4_variables.json", 2),
        ("uniswap_v3_factory_storage.json", 6),
        ("sample_contract_1_storage.json", 14),
    ),
)
def test_optimize_storage_layout_check_number_of_slots(storage_layout, expected):
    storage, types = storage_layout.get("storage"), storage_layout.get("types")
    nstorage, ntypes = optimize_storage_layout(storage=storage, types=types)
    assert get_number_of_slots(storage=nstorage, types=ntypes) == expected
