from wineQualityML.config.configuration import ConfigurationManager
from wineQualityML.components.data_ingestion import DataIngestion
from wineQualityML import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()  # 1. read the YAML files
        data_ingestion_config = config.get_data_ingestion_config()  # 2. build the ingestion settings
        data_ingestion = DataIngestion(config=data_ingestion_config)  # 3. create the worker object
        data_ingestion.download_file()  # 4. download the zip (if not already there)
        data_ingestion.extract_zip_file()  # 5. unzip it into artifacts/data_ingestion


if __name__ == "__main__":
    try:
        logger.info(f"started: {STAGE_NAME}")
        DataIngestionTrainingPipeline().main()
        logger.info(f"completed: {STAGE_NAME}")
    except Exception as e:
        logger.error(e)


