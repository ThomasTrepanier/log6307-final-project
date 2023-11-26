from pydantic import BaseModel, Field


class TMDB_Category(BaseModel):
    name: str = Field(alias="strCategory")
    description: str = Field(alias="strCategoryDescription")


data = {
    "strCategory": "Beef",
    "strCategoryDescription": "Beef is ..."
}


obj = TMDB_Category.parse_obj(data)

# {'name': 'Beef', 'description': 'Beef is ...'}
print(obj.dict())
