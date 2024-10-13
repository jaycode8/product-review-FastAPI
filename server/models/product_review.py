from datetime import datetime
from beanie import Document
from pydantic import BaseModel
from typing import Optional

class ProductReview(Document):
    name: str
    product: str
    rating: float
    review: str
    date: datetime = datetime.now()

    class Settings:
        name = "product_review" # associates this model to a mongo document

    class Config: # this config adds the example fields to the swagger interactive api documentation to help api users well understand
        schema_extra = {
            "example":{
                "name":"James",
                "product":"ML apis",
                "rating":4.5,
                "review":"Excellent product",
                "date": datetime.now()
            }
        }

class UpdateProductReview(BaseModel):
    name: Optional[str]
    product: Optional[str]
    rating: Optional[float]
    review: Optional[str]
    date: Optional[datetime]

    class Config:
        schema_extra = {
            "example":{
                "name":"James",
                "product":"ML apis",
                "rating":5.0,
                "review":"Excellent product",
                "date": datetime.now()
            }
        }