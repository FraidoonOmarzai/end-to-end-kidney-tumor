from kidney.utils.common import read_yaml, create_directories
from kidney.constants import *
from kidney.entity.entity import (DataIngestionConfig,
                                  BaseModelConfig)


class ConfigurationManager:
    def __init__(self,
                 config=CONFIG_PATH,
                 params=PARAMS_PATH):
        self.config = read_yaml(config)
        self.params = read_yaml(params)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config

    def get_base_model_config(self) -> BaseModelConfig:
        config = self.config.base_model
        params = self.params

        create_directories([config.root_dir])

        base_model_config = BaseModelConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_path,
            updated_base_model_path=config.updated_base_model_path,
            IMAGE_SIZE=params.IMAGE_SIZE,
            INCLUDE_TOP=params.INCLUDE_TOP,
            CLASSES=params.CLASSES,
            WEIGHTS=params.WEIGHTS,
            LEARNING_RATE=params.LEARNING_RATE
        )

        return base_model_config
