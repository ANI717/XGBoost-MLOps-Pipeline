from fastapi import APIRouter
from api.config import logger


router = APIRouter()


@router.post("/xgboost")
async def xgboost_router(inputs: int):

    logger.info(f"Received inputs: {inputs}")

    return inputs
