import pytest

from sl_optimizer.errors import StorageLayoutError
from sl_optimizer.utils import get_contact_name


@pytest.mark.parametrize("filename", ("contract_name_storage.json",))
def test_get_contact_name(storage):
    assert get_contact_name(storage=storage) == "ContractName"


def test_get_contact_name_fail():
    with pytest.raises(StorageLayoutError):
        get_contact_name(storage=[])
