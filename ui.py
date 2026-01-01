from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="web/templates")

def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})