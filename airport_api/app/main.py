import logging
from fastapi import FastAPI
from app.interfaces.web import router


# Logger configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# FastAPI
app = FastAPI()
app.include_router(router)