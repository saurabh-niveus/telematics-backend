from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import random
from data.indian_data import INDIAN_NAMES
from utils.location_utils import get_random_indian_location

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

VEHICLE_MODELS = [
    "Tata Nexon",
    "Maruti Swift",
    "Hyundai Creta",
    "Mahindra XUV700",
    "Toyota Fortuner",
    "Honda City",
    "Kia Seltos",
    "MG Hector",
    "Tata Harrier",
    "Mahindra Thar"
]

@app.get("/api/telematics")
async def get_telematics_data():
    devices = []
    alerts = []
    
    # Generate devices
    for idx in range(10):
        name, contact = INDIAN_NAMES[idx]
        status = random.choice(["normal", "alert"])
        
        device = {
            "id": str(idx + 1),
            "vehicleModel": VEHICLE_MODELS[idx],
            "vehicleNumber": f"IN-{random.randint(1000, 9999)}",
            "customerName": name,
            "customerContact": contact,
            "status": status,
            "location": get_random_indian_location(),
            "lastUpdate": datetime.now().isoformat()
        }
        devices.append(device)
        
        # Generate alerts for devices with 'alert' status
        if status == "alert":
            alert_types = [
                ("high", "Speed Limit Exceeded", "Vehicle speed exceeded 100km/h"),
                ("medium", "Low Fuel", "Fuel level below 15%"),
                ("low", "Maintenance Due", "Scheduled maintenance required")
            ]
            alert_type = random.choice(alert_types)
            
            alert = {
                "deviceId": str(idx + 1),
                "severity": alert_type[0],
                "type": alert_type[1],
                "timestamp": datetime.now().isoformat(),
                "description": alert_type[2]
            }
            alerts.append(alert)
    
    return {
        "devices": devices,
        "alerts": alerts
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
