from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/healthz")
def healthz():
    """
    Liveness probe: tells Kubernetes the app is alive.
    """
    return {"status": "ok"}

@app.get("/ready")
def readiness():
    """
    Readiness probe: tells Kubernetes the app is ready to serve requests.
    """
    # In a real app, you might check DB, cache, etc.
    return {"status": "ready"}

if __name__ == "__main__":
    # Run with uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
