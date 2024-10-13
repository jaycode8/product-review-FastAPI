from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from server.models.product_review import ProductReview, UpdateProductReview

router = APIRouter()

@router.post("/")
async def add_product_review(review: ProductReview) -> dict:
    await review.create()
    return {"msg":"review added successfully"}

@router.get("/")
async def get_reviews() -> List[ProductReview]:
    reviews = await ProductReview.find_all().to_list()
    return reviews

@router.get("/{id}")
async def get_specific_review(id:PydanticObjectId) -> ProductReview:
    review = await ProductReview.get(id)
    # review = await ProductReview.find_one(ProductReview.rating == 4.0)
    if not review:
        raise HTTPException(
            status_code=404,
            detail="Review not found!"
        )
    return review

@router.put("/{id}")
async def update_review(id:PydanticObjectId, rev_data: UpdateProductReview):
    rev_data = {k:v for k, v in rev_data.dict().items() if v is not None}
    update_query = {"$set":{
        field: value for field, value in rev_data.items()
    }}
    review = await ProductReview.get(id)
    if not review:
        raise HTTPException(
            status_code=404,
            detail="Review not found!"
        )
    await review.update(update_query)
    return review

@router.delete("/{id}")
async def del_review(id:PydanticObjectId) -> dict:
    record = await ProductReview.get(id)
    if not record:
        raise HTTPException(
            status_code=404,
            detail="Review record not found!"
        )
    await record.delete()
    return {"msg":"review was successfully deleted"}