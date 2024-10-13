from beanie import init_beanie
import motor.motor_asyncio
from server.models.product_review import ProductReview
import os
from dotenv import load_dotenv
load_dotenv()

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("DB_URI"))
    await init_beanie(database=client.fastapi, document_models=[ProductReview])