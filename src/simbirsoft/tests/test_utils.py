import freezegun
import pytest

import simbirsoft.utils as utils


def test_get_fibbonachi_number_by_index() -> None:
    assert utils.get_fibbonachi_number_by_index(9) == 21

    with pytest.raises(ValueError):
        utils.get_fibbonachi_number_by_index(0)


@freezegun.freeze_time("2020-01-10 15:00:00")
def test_get_day_number() -> None:
    assert utils.get_day_number() == 10
