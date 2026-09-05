"""Bayan serving skeleton. Completed in Lab 7 / Capstone."""
from fastapi import FastAPI

app = FastAPI(title="Bayan — Bilingual Citizen-Feedback Intelligence Service")

@app.get("/health")
def health():
    return {"status": "starter", "message": "Complete Labs 1–7 before final serving."}
