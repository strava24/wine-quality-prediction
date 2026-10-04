from wineQualityML.components.model_evaluation import ModelEvaluation
from wineQualityML.config.configuration import ConfigurationManager
from wineQualityML import logger

STAGE_NAME = "Data Trainer Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()

if __name__ == "__main__":
    try:
        logger.log(f"Starting {STAGE_NAME} stage")
        model_evaluation_pipeline = ModelEvaluationTrainingPipeline()
        model_evaluation_pipeline.main()
        logger.log(f"Finished {STAGE_NAME} stage")
    except Exception as e:
        logger.exception(f"Exception occurred {STAGE_NAME} stage: {e}")
        raise e
