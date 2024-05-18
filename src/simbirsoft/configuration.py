import os
from pathlib import Path

import dotenv

dotenv.load_dotenv()
HUB_HOST = os.environ["HUB_HOST"]
REPORTS_PATH = Path(os.environ["REPORTS_PATH"])
EXPORT_PATH = Path(os.environ["EXPORT_PATH"])
