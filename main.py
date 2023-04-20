import uvicorn
from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.reviews.router import review_router
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from base import settings

STATIC_DIR = getattr(settings, "STATIC_DIR", "")
STATIC_NAME = getattr(settings, "STATIC_NAME", "static")
STATIC_ROOT = getattr(settings, "STATIC_ROOT", "/static")

CORS = getattr(settings, "CORS", {})
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS.CORS_ALLOWED_ORIGINS,
    allow_credentials=CORS.CORS_ALLOW_CREDENTIALS,
    allow_methods=CORS.CORS_ALLOWED_METHODS,
    allow_headers=CORS.CORS_ALLOWED_HEADERS,
)


if STATIC_DIR != "":
    app.mount(STATIC_ROOT, StaticFiles(directory=STATIC_DIR), name=STATIC_NAME)

TEPMLATE = Jinja2Templates(directory=getattr(settings, "TEMPLATE_DIR", "templates"))

app.include_router(review_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
