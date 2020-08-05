# project/app/api/summaries.py

from fastapi import APIRouter

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema
from app.models.tortoise import SummarySchema

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    """
    Handler to create a summary for a given website
    """
    summary_id = await crud.post(payload)
    resp_obj = {
        "id": summary_id,
        "url": payload.url
    }
    return resp_obj


@router.get("/{id}/", response_model=SummarySchema)
async def read_summary(summary_id: int) -> SummaryScehma:
    summary = await crud.get(summary_id)
    return summary
