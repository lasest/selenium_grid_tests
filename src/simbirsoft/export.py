import csv
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from simbirsoft.models import Transaction


def get_timestamp_filename(file_extension: str, index: int | None = None) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    if index:
        timestamp += f"-{index}"

    filename = f"{timestamp}{file_extension}"
    return filename


def export_transactions(transactions: list[Transaction], output_path: Path) -> None:
    data = [asdict(transaction) for transaction in transactions]
    if not data:
        return

    column_names = list(data[0].keys())
    with open(output_path, "w") as fh:
        writer = csv.DictWriter(fh, fieldnames=column_names)
        writer.writeheader()
        writer.writerows(data)
