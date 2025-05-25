from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the marks database from JSON file
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)
    marks_db = {entry["name"]: entry["marks"] for entry in data}

@app.get("/api")
def get_marks(name: list[str] = []):
    return {"marks": [marks_db.get(n, None) for n in name]}
