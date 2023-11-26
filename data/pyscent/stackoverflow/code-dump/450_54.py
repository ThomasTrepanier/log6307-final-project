from datetime import datetime, date

from pydantic import BaseModel, validator


class OddDate(BaseModel):
    birthdate: date

    @validator("birthdate", pre=True)
    def parse_birthdate(cls, value):
        return datetime.strptime(
            value,
            "%d/%m/%Y"
        ).date()


if __name__ == "__main__":
    odd_date = OddDate(birthdate="12/04/1992")
    print(odd_date.json()) #{"birthdate": "1992-04-12"}
