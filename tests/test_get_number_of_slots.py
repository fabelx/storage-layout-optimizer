import pytest

from sl_optimizer import get_number_of_slots


@pytest.mark.parametrize(
    "filename,expected",
    (
        ("uniswap_v3_factory_storage.json", 6),
        ("super_nested_structure_storage.json", 303),
        ("simple_4_variables.json", 3),
        ("sample_optimization_is_not_applied_storage.json", 2),
        ("sample_contract_1_storage.json", 22),
        ("huge_number_of_variables_storage.json", 132),
        ("cross_nested_structure_storage.json", 239),
        ("contacts/arrays/output/Arrays_storage.json", 38),
        ("contacts/bytes/output/Bytes_storage.json", 5),
        ("contacts/enums/output/Enums_storage.json", 4),
        ("contacts/mappings/output/Mapping_storage.json", 4),
    )
)
def test_get_number_of_slots(storage_layout, expected):
    assert (
        get_number_of_slots(
            storage=storage_layout.get("storage"), types=storage_layout.get("types")
        )
        == expected
    )
