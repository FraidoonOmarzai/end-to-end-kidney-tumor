from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: str
    unzip_dir: Path


@dataclass
class BaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    IMAGE_SIZE: list
    INCLUDE_TOP: bool
    CLASSES: int
    WEIGHTS: str
    LEARNING_RATE: float
