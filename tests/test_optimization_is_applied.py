import pytest

from sl_optimizer import optimize_storage_layout


@pytest.mark.parametrize(
    "filename",
    (
        "simple_4_variables.json",
        "sample_contract_1_storage.json",
    ),
)
def test_optimization_is_applied(storage_layout):
    storage_, types = storage_layout.get("storage"), storage_layout.get("types")
    nstorage, ntypes = optimize_storage_layout(storage=storage_, types=types)
    assert id(storage_) != id(nstorage)
    assert id(ntypes) != id(types)
