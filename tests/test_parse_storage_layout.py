import pytest
from jsonschema.exceptions import ValidationError

from sl_optimizer import parse_storage_layout
from sl_optimizer.errors import LayoutError
from sl_optimizer.utils import validate_storage_layout


@pytest.mark.parametrize("filename", ("uniswap_v3_factory_storage.json",))
def test_parse_storage_layout(storage_layout):
    parse_storage_layout(data=storage_layout)


def test_parse_storage_layout_fail():
    with pytest.raises(LayoutError):
        parse_storage_layout(data={})


def test_validate_storage_layout_raises_validation_error():
    with pytest.raises(ValidationError):
        validate_storage_layout(data={})
