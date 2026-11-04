from fastapi import FastAPI
import joblib
import pandas as pd

model = joblib.load("churn_model.joblib")
print("model loaded:", type(model))

app = FastAPI()


@app.get("/")
def root():
    return {"message": "ok"}

from schema import CustomerInput

@app.post("/predict")
def predict(data: CustomerInput):
    X = pd.DataFrame([data.model_dump()])
    label = int(model.predict(X)[0])
    proba = float(model.predict_proba(X)[0][1])
    return {"churn": label, "churn_probability": proba}