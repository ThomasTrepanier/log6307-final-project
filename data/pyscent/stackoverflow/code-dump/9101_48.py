from django.db import models
from pydantic import BaseModel

class CustomList(BaseModel):
    data: list[dict]
