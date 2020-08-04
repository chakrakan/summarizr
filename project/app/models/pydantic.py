# project/app/models/pydantic.py

from pydantic import BaseModel


class SummaryPayloadSchema(BaseModel):
    """
    Data Validation via pydantic. We expect a URL of type str for our website to be summarized
    """
    url: str
