from kidney.utils.common import read_yaml, create_directories
from kidney.constants import *
from kidney.entity.entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self, config=CONFIG_PATH):
        self.config = read_yaml(config)

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
