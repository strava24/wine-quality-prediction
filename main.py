from wineQualityML import logger
from wineQualityML.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from wineQualityML.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from wineQualityML.pipeline.stage_03_data_transformation import DataTransformationPipline
from wineQualityML.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from wineQualityML.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started")
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started")
    data_transformation = DataTransformationPipline()
    data_transformation.main()
    logger.info(f"completed: {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Trainer Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f"completed: {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f"completed: {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e
