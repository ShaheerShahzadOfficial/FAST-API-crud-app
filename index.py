from fastapi import FastAPI
from routes.note import notes

app = FastAPI()
app.include_router(notes, prefix="/notes")