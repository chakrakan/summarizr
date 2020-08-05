# project/app/api/crud.py

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary
from typing import Optional


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


async def get(summary_id: int) -> Optional[dict]:
    """
    Use values method to create a ValuesQuery object. If TextSummary exists, we return it as a dict
    Union[dict, None] is the same as Optional[dict], they are interchangeable
    :param summary_id:
    :param id:
    :return:
    """
    summary = await TextSummary.filter(id=summary_id).first().values()
    if summary:
        return summary[0]
    return None
