# project/app/api/crud.py

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    """
    Utility func for creating new summaries takes a payload object then:
        1. Creates a new TextSummary instance
        2. returns the generated ID
    :param payload:
    :return: int ID of the summary instance
    """
    summary = TextSummary(
        url=payload.url,
        summary="test summary"
    )
    await summary.save()
    return summary.id