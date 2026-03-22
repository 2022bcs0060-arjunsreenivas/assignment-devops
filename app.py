from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import datetime
from compute_risk import compute_risk
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()

class Ticket(BaseModel):
    type: str
    date: datetime

class Customer(BaseModel):
    customerID: str
    monthly_charges: float
    previous_month_charges: float
    contract_type: str
    tickets: List[Ticket]

@app.get("/health")
def health():
    return {
        "status": "UP",
        "service": "churn-risk-api",
        "time": datetime.now()
    }

@app.post("/predict-risk")
def predict(customer: Customer):
    logger.info(f"Received request for customer: {customer.customerID}")
    risk = compute_risk(customer)
    logger.info(f"Computed risk: {risk} for customer: {customer.customerID}")
    return {"risk": risk}