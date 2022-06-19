from src.main import bootstrap
from src.utils import myLogger


try:
    myLogger(level="info", msg="process started...")
    bootstrap()
    myLogger(level="info", msg="process finished")
except Exception as e:
    myLogger(level="error", msg=e)
