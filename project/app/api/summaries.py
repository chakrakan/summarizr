# project/app/api/summaries.py

from fastapi import APIRouter, HTTPException
from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    """
    Handler to expect payload with a URL. When route is hit with POST req, FastAPI will read the body and validate the
    data:
        - if valid, data will be available in the payload param. FastAPI also created the JSON schema to gereante the
        OpenAPI schema and docs
        - if invalid, error is returned
    We use async declaration since db communication is async and there are no blocking I/O ops in the handler
    :param payload: payload object with URL info
    :return: response
    """
    summary_id = await crud.post(payload)
    resp_obj = {
        "id": summary_id,
        "url": payload.url
    }
    return resp_obj
