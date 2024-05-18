from pathlib import Path

import simbirsoft.configuration as configuration


def test_configuration() -> None:
    assert isinstance(configuration.EXPORT_PATH, Path)
