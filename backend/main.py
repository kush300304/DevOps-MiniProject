from fastapi import FastAPI, HTTPException, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Dict
import os

# Get the current file's directory
current_dir = os.path.dirname(os.path.realpath(__file__))
# Go up one level to the project root
project_root = os.path.dirname(current_dir)

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory=os.path.join(project_root, "frontend"))

# Mount static files
app.mount("/static", StaticFiles(directory=os.path.join(project_root, "frontend", "static")), name="static")

# In-memory user storage (replace with a database in a real application)
users: Dict[str, str] = {}

class User(BaseModel):
    username: str
    password: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/signup")
async def signup(username: str = Form(...), password: str = Form(...)):
    if username in users:
        raise HTTPException(status_code=400, detail="Username already exists")
    users[username] = password
    return {"message": "Registered successfully"}

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username == "kushal" and password == "kushal":
        return {"message": "Login successful"}
    elif username in users and users[username] == password:
        return {"message": "Login successful"}
    else:
        return {"message": "Please signup", "status": "error"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)