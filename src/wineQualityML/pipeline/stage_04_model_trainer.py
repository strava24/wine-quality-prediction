from wineQualityML.config.configuration import ConfigurationManager
from wineQualityML.components.model_trainer import ModelTrainer
from wineQualityML import logger

STAGE_NAME = "Data Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()