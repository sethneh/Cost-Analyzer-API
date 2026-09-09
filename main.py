from fastapi import FastAPI
app= FastAPI()

@app.get("/customers/{customer_id}")
def get_cost(customer_id: int):
  
  # Imagine this came from database
  customer = {
    "customer": "customer123",
    "total_cost": 1250.50,
    "currency": "USD"
  }

  return custome["total_cost"]
