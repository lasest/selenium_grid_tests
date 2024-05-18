from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class TransactionType(Enum):
    CREDIT = "Credit"
    DEBIT = "Debit"


@dataclass
class Transaction:
    timestamp: datetime
    amount: int
    type: TransactionType

    @staticmethod
    def parse_timestamp(timestamp_string: str) -> datetime:
        format_string = "%B %d, %Y %I:%M:%S %p"
        return datetime.strptime(timestamp_string, format_string)

    @classmethod
    def from_tr(cls, tr: WebElement) -> "Transaction":
        cells = tr.find_elements(By.TAG_NAME, "td")  # type: ignore
        timestamp_str, amount_str, type_str = [cell.text for cell in cells]

        if type_str not in ["Credit", "Debit"]:
            raise ValueError()

        timestamp = cls.parse_timestamp(timestamp_str)
        amount = int(amount_str)
        transaction_type = TransactionType(type_str)

        return Transaction(timestamp=timestamp, amount=amount, type=transaction_type)

    def to_dict(self) -> dict[str, str]:
        data: dict[str, str] = {}
        data["Date"] = self.timestamp.strftime("%d %B %Y %H:%M:%S")
        data["Amount"] = str(self.amount)
        data["Type"] = self.type.value

        return data
