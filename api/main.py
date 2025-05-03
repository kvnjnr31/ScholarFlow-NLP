
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Phage Review Assistant API")

@app.get("/")
def root():
    return {"status": "Phage Review Assistant API is live."}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename, "status": "File received"}

@app.post("/cluster")
def cluster_data():
    return {"message": "Clustering run complete."}

@app.post("/summarize")
def summarize_clusters():
    return {"summary": "Cluster synthesis complete."}

@app.get("/graph")
def get_graph():
    return {"graph": "Graph JSON here."}
