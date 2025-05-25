from fastapi import FastAPI, Query, HTTPException
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

# Load JSON data exactly as provided
with open('q-vercel-python.json') as f:
    students = json.load(f)  # Loads your array of {name, marks} objects

@app.get("/api")
async def get_marks(names: list[str] = Query(...)):
    results = []
    for name in names:
        found = False
        for student in students:  # Search through all students
            if student["name"] == name:
                results.append(student["marks"])
                found = True
                break
        if not found:
            results.append(0)  # Return 0 if name not found
    
    return {"marks": results}
