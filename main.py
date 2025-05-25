from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks from JSON
with open('q-vercel-python.json') as f:
    marks_data = json.load(f)
    marks_db = {item['name']: item['marks'] for item in marks_data}  # Update keys based on your JSON structure

@app.get("/api")
async def get_marks(names: list[str] = Query(...)):
    return {"marks": [marks_db.get(name, 0) for name in names]}
