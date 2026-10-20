from fastapi import FastAPI

app = FastAPI(title="agentops")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
