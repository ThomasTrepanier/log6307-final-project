def clean_article_url(cls, v):
    return clean_context_url(v.strip())

class MyModel(BaseModel):
    article_url: str

    _clean_url = pydantic.validator("article_url", allow_reuse=True)(clean_article_url)
