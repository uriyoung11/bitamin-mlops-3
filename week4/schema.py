
from pydantic import BaseModel


class CustomerInput(BaseModel):
    tenure: int
    MonthlyCharges: float
    Contract: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "tenure": 12,
                    "MonthlyCharges": 70.5,
                    "Contract": "Month-to-month"
                }
            ]
        }
    }
