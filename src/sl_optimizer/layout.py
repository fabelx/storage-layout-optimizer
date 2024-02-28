# Copyright (c) 2024 to present Vladyslav Novotnyi and individual contributors.
"""
Contains storage layout models.
"""
import copy
import json
from pathlib import Path

from sl_optimizer.core import optimize_storage_layout
from sl_optimizer.utils import (
    check_file_exists,
    get_contact_name,
    get_number_of_slots,
    parse_storage_layout,
)

__all__ = (
    "StorageLayout",
    "OptimizedStorageLayout",
    "new_storage_layout",
)


class BaseStorageLayout:
    def __init__(self, storage: list, types: dict):
        """Initialize the BaseStorageLayout with storage and types information.

        Args:
            storage: List containing storage information.
            types: Dictionary containing type information.
        """
        self.__storage = storage
        self.__types = types
        self.__contract_name = get_contact_name(self.__storage)
        self.__number_of_slots = get_number_of_slots(
            storage=self.__storage, types=self.__types
        )

    @property
    def storage(self) -> list:
        """Getter for the storage property."""
        return self.__storage

    @property
    def types(self) -> dict:
        """Getter for the types property."""
        return self.__types

    @property
    def contract_name(self) -> str:
        """Getter for the contract_name property."""
        return self.__contract_name

    @property
    def number_of_slots(self) -> int:
        """Getter for the number_of_slots property."""
        return self.__number_of_slots

    def save(self, filepath: str | Path, force: bool = False) -> str:
        """Save the storage layout data to a JSON file.

        Args:
            filepath: Path to the file where the data will be saved.
            force: If True, overwrite the file even if it already exists.

        Returns:
            str: The filepath where the data is saved.
        """
        if not force:
            check_file_exists(filepath=filepath)

        with open(filepath, "w") as f:
            json.dump(self.to_dict(), f, indent=2)

        return filepath

    def to_dict(self) -> dict:
        """Convert the storage layout data to a dictionary.

        Returns:
            dict: Dictionary representation of the storage layout data.
        """
        return {"storage": self.__storage, "types": self.__types}


class OptimizedStorageLayout(BaseStorageLayout):
    def __init__(self, storage: list = None, types: dict = None):
        """Initialize the OptimizedStorageLayout with storage and types information.

        Args:
            storage: List containing storage information.
            types: Dictionary containing type information.
        """
        super().__init__(storage=storage, types=types)

    def save(
        self,
        filepath: str | Path,
        force: bool = False,
    ):
        """Save the storage layout data to a JSON file.

        Args:
            filepath: Path to the file where the data will be saved.
            force: If True, overwrite the file even if it already exists.

        Returns:
            str: The filepath where the data is saved.
        """  # noqa: E501
        return super().save(filepath=filepath, force=force)


class StorageLayout(BaseStorageLayout):
    def __init__(self, data: dict):
        """Initialize the StorageLayout instance.

        Args:
            data: Storage layout data.
        """
        storage, types = parse_storage_layout(data=data)
        super().__init__(storage=storage, types=types)

    def optimize(self) -> "OptimizedStorageLayout":
        """Optimize the storage layout and return an instance of OptimizedStorageLayout.

        Returns:
            OptimizedStorageLayout: An optimized storage layout.
        """
        storage, types = optimize_storage_layout(storage=self.storage, types=self.types)
        return OptimizedStorageLayout(
            storage=copy.deepcopy(storage), types=copy.deepcopy(types)
        )


def new_storage_layout(filepath: str | Path) -> StorageLayout:
    """Create a new StorageLayout instance by loading data from a JSON file.

    Args:
        filepath: The path to the JSON file containing storage layout data.

    Returns:
        StorageLayout: An instance of the StorageLayout class created from the loaded data.
    """
    with open(filepath, mode="r") as f:
        data = json.load(f)

    return StorageLayout(data=data)
