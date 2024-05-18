from datetime import datetime

from simbirsoft.models import Transaction, TransactionType


def test_transaction_parse_timestamp() -> None:
    assert Transaction.parse_timestamp("May 18, 2024 1:50:01 PM") == datetime(
        year=2024, month=5, day=18, hour=13, minute=50, second=1
    )


def test_transaction_to_dict() -> None:
    dt = datetime(2020, 10, 5, 10, 2, 1)
    amount = 50
    transaction_type = TransactionType.CREDIT
    transaction = Transaction(dt, amount, transaction_type)

    dict_data = transaction.to_dict()
    assert dict_data["Date"] == "05 October 2020 10:02:01"
    assert dict_data["Amount"] == str(amount)
    assert dict_data["Type"] == transaction_type.value
