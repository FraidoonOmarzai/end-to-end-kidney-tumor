from pathlib import Path
import tensorflow as tf
from kidney.entity.entity import ModelTrainingConfig
from tensorflow.keras.preprocessing.image import ImageDataGenerator


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig) -> None:
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path)

    def train_val_gen(self):
        datagenerator_kwargs = dict(
            rescale=1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_data_generator = ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_gen = valid_data_generator.flow_from_directory(
            directory=self.config.training_data,
            subset='validation',
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_data_generator = ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_data_generator = ImageDataGenerator(
                **datagenerator_kwargs
            )

        self.train_gen = train_data_generator.flow_from_directory(
            directory=self.config.training_data,
            subset='training',
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def train(self, callback_list: list):
        self.model.fit(
            self.train_gen,
            epochs=self.config.params_epochs,
            validation_data=self.valid_gen,
            callbacks=callback_list
        )

        self.save_model(
            path=self.config.model_trained_path,
            model=self.model
        )
