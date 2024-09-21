from src.diseaseclassifier import logger
from src.diseaseclassifier.pipeline.stage_01_ingestion import DataIngestionTrainingPipeline
STAGE_NAME="Data Ingestion Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e