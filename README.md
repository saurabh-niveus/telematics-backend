# Telematics Backend API

A FastAPI-based backend service that generates mock telematics data for vehicle tracking and monitoring.

## Features

- Generate random vehicle telematics data
- Real-time alerts system
- Indian vehicle and location data
- CORS enabled for frontend integration
- Docker support

## Project Structure

```
telematics-backend/
├── app.py            
├── Dockerfile         
├── requirements.txt    
├── data/
│   └── indian_data.py 
└── utils/
    └── location_utils.py 
```

## API Endpoints

### GET /api/telematics
Returns a collection of device data and their associated alerts.

Response format:
```json
{
  "devices": [
    {
      "id": "string",
      "vehicleModel": "string",
      "vehicleNumber": "string",
      "customerName": "string",
      "customerContact": "string",
      "status": "normal|alert",
      "location": {
        "lat": float,
        "lng": float,
        "country": "string",
        "state": "string",
        "city": "string"
      },
      "lastUpdate": "datetime"
    }
  ],
  "alerts": [
    {
      "deviceId": "string",
      "severity": "high|medium|low",
      "type": "string",
      "timestamp": "datetime",
      "description": "string"
    }
  ]
}
```

## Setup & Installation

### Local Development

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app:app --reload --port 8080
```

### Docker Deployment

1. Build the Docker image:
```bash
docker build -t telematics-backend .
```

2. Run the container:
```bash
docker run -p 8080:8080 telematics-backend
```

## API Documentation

Once running, access the API documentation at:
- Swagger UI: http://localhost:8080/docs
- ReDoc: http://localhost:8080/redoc

## Environment Variables

The application uses the following default settings:
- Port: 8080
- Host: 0.0.0.0
- CORS: Enabled for all origins (*)

