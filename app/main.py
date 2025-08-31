from fastapi import FastAPI
app = FastAPI(title="Expense Manager Api")

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is working!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}