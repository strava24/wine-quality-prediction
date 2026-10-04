from wineQualityML.components.data_validation import DataValidation
from wineQualityML.config.configuration import ConfigurationManager
from wineQualityML import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f"started: {STAGE_NAME}")
        DataValidationTrainingPipeline().main()
        logger.info(f"completed: {STAGE_NAME}")
    except Exception as e:
        logger.error(e)