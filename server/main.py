from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory storage for data points
data_points = [{"x": 1, "y": 10}, {"x": 2, "y": 20}, {"x": 3, "y": 30}]

class DataPoint(BaseModel):
    x: int
    y: int


