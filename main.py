from fastapi import FastAPI  # type: ignore[import]

app = FastAPI(title="Traffic Guard")

@app.get("/")
def read_root():
    return {
        "status": "Active",
        "service": "Traffic Guard",
        "message": "Welcome to the secure AKS cluster!"
    }