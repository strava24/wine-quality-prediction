# dataclass auto-generates __init__, __repr__ etc. for classes that only hold data
from dataclasses import dataclass
# Path is a cleaner, cross-platform way to represent file/folder paths than plain strings
from pathlib import Path

# frozen=True makes the object read-only after creation, so settings can't be
# changed by accident somewhere else in the code.
@dataclass(frozen=True)
class DataIngestionConfig:
    """Holds all the settings needed by the data ingestion step (values come from config.yaml)."""
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path