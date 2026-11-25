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
