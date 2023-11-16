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


@dataclass
class CallBackConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path


@dataclass
class ModelTrainingConfig:
    root_dir: Path
    model_trained_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list
