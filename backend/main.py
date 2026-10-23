from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="AI Smart Factory Safety API",
    description="AI-powered Smart Factory Safety & Digital Twin",
    version="1.0.0"
)


# -----------------------------
# HOME
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "AI Smart Factory Safety API is running",
        "project": "AI-Powered Smart Factory Safety & Digital Twin",
        "status": "online"
    }


# -----------------------------
# APPLICATION STATUS
# -----------------------------
@app.get("/app/status")
def app_status():
    return {
        "status": "online",
        "factory": "AI Smart Factory",
        "ai_monitoring": "active",
        "digital_twin": "active",
        "safety_monitoring": "active",
        "timestamp": datetime.now().isoformat()
    }


# -----------------------------
# FACTORY STATUS
# -----------------------------
@app.get("/factory/status")
def factory_status():
    return {
        "factory_status": "SAFE",
        "workers_detected": 0,
        "ppe_violations": 0,
        "fire_detected": False,
        "smoke_detected": False,
        "restricted_zone_violation": False
    }


# -----------------------------
# WORKER INFORMATION
# -----------------------------
@app.get("/factory/workers")
def workers():
    return {
        "total_workers": 0,
        "helmet_compliant": 0,
        "vest_compliant": 0,
        "ppe_violations": 0
    }


# -----------------------------
# MACHINE STATUS
# -----------------------------
@app.get("/factory/machines")
def machines():
    return {
        "machines": [
            {
                "id": "M001",
                "name": "Machine 1",
                "status": "RUNNING",
                "temperature": 0,
                "vibration": 0
            },
            {
                "id": "M002",
                "name": "Machine 2",
                "status": "RUNNING",
                "temperature": 0,
                "vibration": 0
            },
            {
                "id": "M003",
                "name": "Machine 3",
                "status": "RUNNING",
                "temperature": 0,
                "vibration": 0
            }
        ]
    }


# -----------------------------
# SAFETY ALERTS
# -----------------------------
@app.get("/alerts")
def alerts():
    return {
        "alerts": [
            {
                "id": 1,
                "type": "SYSTEM",
                "message": "No active safety alerts",
                "severity": "LOW",
                "time": datetime.now().isoformat()
            }
        ]
    }


# -----------------------------
# DIGITAL TWIN STATUS
# -----------------------------
@app.get("/digital-twin")
def digital_twin():
    return {
        "digital_twin": "active",
        "factory_status": "SAFE",
        "zones": [
            {
                "zone_id": "Z01",
                "name": "Production Area",
                "status": "SAFE"
            },
            {
                "zone_id": "Z02",
                "name": "Assembly Area",
                "status": "SAFE"
            },
            {
                "zone_id": "Z03",
                "name": "Restricted Area",
                "status": "SAFE"
            }
        ]
    }