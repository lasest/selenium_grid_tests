from datetime import datetime

from simbirsoft.models import Transaction


def test_transaction_parse_timestamp() -> None:
    assert Transaction.parse_timestamp("May 18, 2024 1:50:01 PM") == datetime(
        year=2024, month=5, day=18, hour=13, minute=50, second=1
    )
