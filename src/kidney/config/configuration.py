from kidney.utils.common import read_yaml, create_directories
from kidney.constants import *
import os
from kidney.entity.entity import (DataIngestionConfig,
                                  BaseModelConfig,
                                  CallBackConfig,
                                  ModelTrainingConfig)


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

    def get_call_back_config(self) -> CallBackConfig:
        config = self.config.call_backs
        create_directories([config.root_dir])

        call_back_config = CallBackConfig(
            root_dir=config.root_dir,
            tensorboard_root_log_dir=config.tensorboard_root_log_dir,
            checkpoint_model_filepath=config.checkpoint_model_filepath
        )
        return call_back_config

    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training
        params = self.params
        base_model = self.config.base_model
        training_data = os.path.join(
            self.config.data_ingestion.unzip_dir, "kidney-ct-scan-image")

        create_directories([config.root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir=config.root_dir,
            model_trained_path=config.model_trained_path,
            updated_base_model_path=base_model.updated_base_model_path,
            training_data=training_data,
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )
        return model_training_config
