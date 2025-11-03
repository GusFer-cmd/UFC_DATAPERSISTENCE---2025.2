from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import time
import asyncio

app = FastAPI()

contador_id = 1