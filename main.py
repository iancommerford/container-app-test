from fastapi import FastAPI
from scipy.optimize import minimize_scalar

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Python!"}

@app.get("/calculate")
def calculate():
    result = minimize_scalar(
        lambda x: (x - 5)**2
    )

    return {
        "status": "success",
        "result": result.x
    }

@app.get("/results")
def get_results():
    return {
        "data": [
            {"Bus": 1001, "Voltage": 1.02, "Angle": 10.5},
            {"Bus": 1002, "Voltage": 0.98, "Angle": 8.2},
            {"Bus": 1003, "Voltage": 1.01, "Angle": 9.1}
        ]
    }
