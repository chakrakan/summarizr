# project/app/models/pydantic.py

from pydantic import BaseModel


class SummaryPayloadSchema(BaseModel):
    """
    Data Validation via pydantic. We expect a URL of type str for our website to be summarized
    """
    url: str


class SummaryResponseSchema(SummaryPayloadSchema):
    """
    Response schema inherits from PayloadSchema and adds an ID to the payload
    """
    id: int
