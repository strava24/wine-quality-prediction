from wineQualityML.constants import *
from wineQualityML.utils.common import read_yaml, create_directories
from wineQualityML.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    """Reads the YAML files and hands out ready-to-use config objects for each pipeline step."""

    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        # Load each YAML file into memo
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        # Make sure the top-level "artifacts" folder exists (all pipeline outputs go inside it)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        # Create artifacts/data_ingestion so there is a place to save the download
        create_directories([config.root_dir])

        # Copy the YAML values into a DataIngestionConfig object
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config