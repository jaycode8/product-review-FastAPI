from fastapi import FastAPI, Request
from server.db import init_db
from server.routes.product_review import router as Router
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(Router, prefix='/reviews')

@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/")
async def index(request: Request) -> dict:
    return templates.TemplateResponse("index.html",{"message":"Hello and welcome to this FastAPI's by jaycode8", "request":request})