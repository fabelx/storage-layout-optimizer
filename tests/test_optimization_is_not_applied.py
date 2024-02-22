import pytest

from sl_optimizer import optimize_storage_layout


@pytest.mark.parametrize(
    "filename",
    (
        "sample_optimization_is_not_applied_storage.json",
        "uniswap_v3_factory_storage.json",
    ),
)
def test_optimization_is_not_applied(storage_layout):
    storage, types = storage_layout.get("storage"), storage_layout.get("types")
    nstorage, ntypes = optimize_storage_layout(storage=storage, types=types)
    assert id(storage) == id(nstorage)
    assert id(ntypes) == id(types)
