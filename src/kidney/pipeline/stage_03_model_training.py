from kidney.config.configuration import ConfigurationManager
from kidney.components.callbacks import CallBacks
from kidney.components.model_training import ModelTraining
from kidney.logging import logger


STAGE_NAME = 'Model Training'


class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
            config = ConfigurationManager()
            config = ConfigurationManager()
            call_backs_config = config.get_call_back_config()
            call_backs = CallBacks(config=call_backs_config)
            callback_list = call_backs.get_tb_ckpt_callbacks()

            training_config = config.get_model_training_config()
            training = ModelTraining(config=training_config)
            training.get_base_model()
            training.train_val_gen()
            training.train(
                callback_list=callback_list
            )


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
