import os
import sys
import datetime
from pathlib import Path
from contextlib import asynccontextmanager

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from fastapi import FastAPI, Query, HTTPException, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any

CHAT_HISTORY = []

# Ensure module path resolution
backend_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(backend_dir))
sys.path.insert(0, str(backend_dir.parent))
sys.path.append(str(backend_dir / "warehouse"))
sys.path.append(str(Path(__file__).resolve().parent / "analytics"))
sys.path.append(str(Path(__file__).resolve().parent / "ml_engine"))
sys.path.append(str(Path(__file__).resolve().parent / "simulator"))
sys.path.append(str(Path(__file__).resolve().parent / "ai_agent"))
sys.path.append(str(Path(__file__).resolve().parent / "exports"))
sys.path.append(str(Path(__file__).resolve().parent / "ingestion"))
sys.path.append(str(Path(__file__).resolve().parent / "workspace"))

# Analytical Engines & Core Modules
from kpi_engine import get_executive_kpis, get_revenue_trends, get_breakdown_by_category, get_breakdown_by_region
from variance_engine import decompose_revenue_variance
from cohort_analysis import get_cohort_retention_matrix
from marketing_roi import get_marketing_performance
from forecaster import train_and_forecast_revenue
from churn_model import train_and_score_churn
from segmentation import get_customer_segmentation
from anomaly_detector import detect_anomalies
from scenario_engine import simulate_price_change, simulate_retention_discount, simulate_marketing_reallocation
from assistant import process_natural_language_query
from powerbi_pack import generate_powerbi_asset_pack
from seed_data import seed_enterprise_warehouse

# Data ingestion modules
from csv_connector import parse_uploaded_file
from schema_detector import detect_column_schema
from data_quality import profile_data 

# -------------------------------------------------------------------------
# LIFESPAN & APPLICATION SETUP
# -------------------------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handles startup tasks like seeding data and cleanup tasks on shutdown."""
    print("[Startup] Seeding enterprise warehouse database...")
    try:
        seed_enterprise_warehouse()
        print("[Startup] Database seed successful.")
    except Exception as e:
        print(f"[Startup Danger] Failed to seed database: {e}")
    yield
    print("[Shutdown] Cleaning up application resources...")

app = FastAPI(
    title="Enterprise Business Intelligence API",
    description="Advanced analytics, machine learning engines, and simulation backend.",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to specific domains for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------------------------
# PYDANTIC SCHEMAS FOR INCOMING PAYLOADS
# -------------------------------------------------------------------------

class QueryRequest(BaseModel):
    prompt: str

class PriceSimulationRequest(BaseModel):
    sku_or_category: str
    percentage_change: float

class DiscountSimulationRequest(BaseModel):
    cohort_id: str
    discount_rate: float

class MarketingSimulationRequest(BaseModel):
    reallocations: Dict[str, float]

# -------------------------------------------------------------------------
# CORE API ENDPOINTS
# -------------------------------------------------------------------------

@app.get("/")
def read_root():
    return {"status": "online", "message": "Enterprise Analytics Platform API is running."}

# --- 📊 BI & KPI ENGINE ROUTES ---

@app.get("/api/v1/kpis/executive")
def fetch_executive_kpis():
    """Retrieve top-level operational performance metrics."""
    try:
        return get_executive_kpis()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/analytics/trends")
def fetch_revenue_trends():
    try:
        return get_revenue_trends()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/analytics/breakdown/category")
def fetch_categorical_breakdown():
    try:
        return get_breakdown_by_category()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/analytics/breakdown/region")
def fetch_regional_breakdown():
    try:
        return get_breakdown_by_region()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/analytics/variance")
def fetch_variance_decomposition():
    try:
        return decompose_revenue_variance()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/analytics/cohort-retention")
def fetch_cohort_matrix():
    try:
        return get_cohort_retention_matrix()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/analytics/marketing-roi")
def fetch_marketing_roi():
    try:
        return get_marketing_performance()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- 🤖 MACHINE LEARNING MODEL ROUTES ---

@app.get("/api/v1/ml/forecast")
def get_revenue_forecast(periods: int = Query(default=12, ge=1)):
    try:
        return train_and_forecast_revenue(periods=periods)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/ml/churn-scores")
def get_churn_risk_scores():
    try:
        return train_and_score_churn()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/ml/segmentation")
def get_segments():
    try:
        return get_customer_segmentation()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/ml/anomalies")
def get_warehouse_anomalies():
    try:
        return detect_anomalies()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- 🔮 WHAT-IF SIMULATION ROUTES ---

@app.post("/api/v1/simulator/price")
def run_price_simulation(payload: PriceSimulationRequest):
    try:
        return simulate_price_change(payload.sku_or_category, payload.percentage_change)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/simulator/discount")
def run_discount_simulation(payload: DiscountSimulationRequest):
    try:
        return simulate_retention_discount(payload.cohort_id, payload.discount_rate)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/simulator/marketing")
def run_marketing_simulation(payload: MarketingSimulationRequest):
    try:
        return simulate_marketing_reallocation(payload.reallocations)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- 📥 INGESTION & DATA QUALITY ROUTES ---

@app.post("/api/v1/ingestion/upload-csv")
async def upload_and_profile_csv(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file type. Only CSV format is supported.")
    try:
        contents = await file.read()
        # Parse data, extract schema specifications, and evaluate data health profiles
        parsed_data = parse_uploaded_file(contents)
        schema = detect_column_schema(parsed_data)
        quality_profile = profile_data(parsed_data)
        
        return {
            "filename": file.filename,
            "schema": schema,
            "quality_metrics": quality_profile,
            "status": "Ready for staging"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- 📄 AI ASSISTANT & BI EXPORTS ---

@app.post("/api/v1/ai/chat")
async def ai_assistant_endpoint(request: QueryRequest):
    """Processes natural language inquiries via the integrated AI agent."""
    try:
        response = process_natural_language_query(request.prompt, CHAT_HISTORY)
        CHAT_HISTORY.append({"user": request.prompt, "assistant": response})
        return {"response": response, "history_length": len(CHAT_HISTORY)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/exports/powerbi")
def download_powerbi_pack():
    try:
        file_path = generate_powerbi_asset_pack()
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="Generated asset pack not found on disk.")
        return FileResponse(path=file_path, filename="BI_Asset_Pack.pbit", media_type='application/octet-stream')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
