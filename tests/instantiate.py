import pytest
from src.item import Item
from src.instantiate import InstantiateCSVError


def test_instantiate_from_csv_inst_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()


def test_instantiate_from_csv_found_error():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()