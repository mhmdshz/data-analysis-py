import logging
from src.main import bootstrap
from src.utils import myLogger


try:
    bootstrap()
except Exception as e:
    myLogger(level="error", msg=e)
