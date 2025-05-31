from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.post("/batch-analysis")
async def analyze_batch(file: UploadFile):
    df = pd.read_csv(file.file)
    results = []
    for text in df['reviews']:
        analysis = analyze_text(text)  # Função do modelo
        results.append(analysis)
    return {"results": results}