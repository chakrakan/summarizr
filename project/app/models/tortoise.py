# project/app/models/tortoise.py

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class TextSummary(models.Model):
    """
    Use Tortoise ORM to create a model to store URL passed in, the summary
    and the time it was created at
    """
    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url


SummarySchema = pydantic_model_creator(TextSummary) # create a pydantic model from tortoise schema
