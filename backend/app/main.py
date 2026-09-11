from fastapi import FastAPI

app = FastAPI(title="Doxa API")


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}
