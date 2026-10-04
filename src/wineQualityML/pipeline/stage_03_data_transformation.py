from wineQualityML.config.configuration import ConfigurationManager
from wineQualityML.components.data_transformation import DataTransformation
from wineQualityML import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipline:
    def __init__(self):
        pass

    def main(self):
        try:
            # checkin the validation stage's output to make sure that the data is ready for the transformation
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                configuration_manager = ConfigurationManager()
                data_transformation_config = configuration_manager.get_data_transformation_config()
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("You data schema is not valid") # Not processing if the data is not valid

        except Exception as ex:
            logger.error(ex)

if __name__ == "__main__":
    try:
        logger.info(f"started: {STAGE_NAME}")
        DataTransformationPipline().main()
        logger.info(f"completed: {STAGE_NAME}")
    except Exception as e:
        logger.error(e)