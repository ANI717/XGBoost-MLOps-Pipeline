import sys
import datetime
from fastapi import APIRouter


deployment_date = str(datetime.datetime.now().ctime())
router = APIRouter()


@router.get("/metadata", tags=["metadata"])
async def metadata():
    return {
        "deployment_date": deployment_date,
        "python_version": sys.version
        }
