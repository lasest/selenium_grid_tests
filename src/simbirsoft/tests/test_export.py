from datetime import datetime
from pathlib import Path

import freezegun
from pyfakefs.fake_filesystem import FakeFilesystem

import simbirsoft.export as export
from simbirsoft.models import Transaction


@freezegun.freeze_time("2020-01-10 15:00:00")
def test_get_timestamp_filename() -> None:
    filename = export.get_timestamp_filename(".csv")
    assert filename == "2020-01-10_150000.csv"


@freezegun.freeze_time("2020-01-10 15:00:00")
def test_export_transactions(fs: FakeFilesystem) -> None:
    transactions = [
        Transaction(datetime.now(), 50, "Credit"),
        Transaction(datetime.now(), 100, "Debit"),
    ]

    filename = export.get_timestamp_filename(".csv")
    output_path = Path("/data") / filename

    fs.create_dir("/data")  # type: ignore
    assert not fs.exists(output_path)  # type: ignore

    export.export_transactions(transactions, output_path=output_path)
    assert fs.exists(output_path)  # type: ignore
