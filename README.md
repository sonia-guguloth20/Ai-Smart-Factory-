# 🏭 AI-Powered Smart Factory Safety & Digital Twin

An AI-driven industrial safety monitoring system that combines **Computer Vision, IoT sensors, and Digital Twin technology** to improve workplace safety, monitor factory conditions, and support faster hazard response.

## 📌 Overview

Traditional factory safety monitoring often depends on manual inspections and separate monitoring systems. This project aims to bring safety monitoring into a unified platform by analyzing camera and sensor data, identifying potential hazards, and visualizing factory conditions through a digital representation of the factory.

The prototype is designed to connect real-world factory conditions with AI-based safety analysis, a monitoring dashboard, and real-time safety alerts.

## 🎯 Objectives

- Improve industrial workplace safety through AI-assisted monitoring.
- Detect workers and potential PPE compliance violations.
- Monitor environmental conditions such as temperature and gas/smoke.
- Identify restricted-zone entry using camera-based monitoring.
- Represent factory zones and machine conditions in a Digital Twin.
- Generate alerts when configured safety rules are violated.

## ✨ Key Features

- **AI-Based Object Detection:** Uses YOLO and OpenCV for camera-based object detection.
- **Worker Safety Monitoring:** Designed to support helmet and safety-vest compliance checks.
- **IoT Sensor Integration:** Supports integration of temperature, gas/smoke, and vibration sensors.
- **Restricted-Zone Monitoring:** Detects or flags unauthorized entry into configured safety zones.
- **Digital Twin Visualization:** Provides a virtual representation of factory zones and equipment status.
- **Safety Alert System:** Reports potential hazards through the monitoring platform.
- **REST API:** Uses FastAPI to expose factory status, worker information, machine status, and alerts.
- **Modular Architecture:** Designed to support additional sensors, AI models, and factory zones.

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| AI / Object Detection | YOLO, Ultralytics |
| Computer Vision | OpenCV |
| Backend API | FastAPI |
| API Server | Uvicorn |
| IoT Hardware | ESP32 and compatible sensors |
| Frontend | HTML, CSS, JavaScript (planned/in development) |
| Digital Twin | 3D factory visualization (planned/in development) |
| Data Storage | To be selected based on prototype requirements |

## 🏗️ System Architecture

```text
        PHYSICAL FACTORY / PROTOTYPE
                    |
          +---------+---------+
          |                   |
      Camera Feed          IoT Sensors
          |                   |
      OpenCV + YOLO       Sensor Readings
          |                   |
          +---------+---------+
                    |
             SAFETY ANALYSIS
                    |
          +---------+---------+
          |         |         |
        Worker    Hazard    Machine
       Monitoring Detection Monitoring
          |         |         |
          +---------+---------+
                    |
               FASTAPI BACKEND
                    |
          +---------+---------+
          |                   |
     Safety Alerts       Digital Twin
          |                   |
          +---------+---------+
                    |
           MONITORING DASHBOARD
```

## 📂 Project Structure

```text
AI-Smart-Factory/
│
├── backend/
│   ├── main.py
│   ├── ai_detection.py
│   ├── safety.py
│   └── database.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── models/
├── data/
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: Update this structure to match the files actually present in your repository.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Smart-Factory
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the initial backend dependencies:

```bash
pip install fastapi "uvicorn[standard]" ultralytics opencv-python
```

### 4. Start the FastAPI backend

Run this command from the project root:

```bash
uvicorn backend.main:app --reload
```

Open the API at:

- **API Base URL:** http://127.0.0.1:8000
- **Interactive API Documentation:** http://127.0.0.1:8000/docs
- **Application Status:** http://127.0.0.1:8000/app/status

### 5. Run AI camera detection

Open a second terminal, activate the same virtual environment, and run:

```powershell
python backend\ai_detection.py
```

Allow camera access if prompted. Press **Q** in the camera window to exit.

The YOLO model may download its weights on the first run. A working webcam and internet access may be needed for initial setup.

## 🔍 API Endpoints

The initial backend provides or is intended to provide endpoints such as:

| Endpoint | Purpose |
|---|---|
| `GET /` | API welcome message |
| `GET /app/status` | Application status |
| `GET /factory/status` | Factory safety summary |
| `GET /factory/workers` | Worker monitoring summary |
| `GET /factory/machines` | Machine status |
| `GET /alerts` | Safety alerts |
| `GET /digital-twin` | Digital Twin zone information |

Open `/docs` to verify which endpoints are implemented in your current version.

## 🚧 Current Prototype Status

This project is under active development.

The current development focuses on establishing the FastAPI backend and testing camera-based object detection. The full integration of AI safety analysis, IoT hardware, persistent alert storage, and Digital Twin visualization is planned as part of the prototype roadmap.

**Important:** Basic YOLO object detection does not automatically identify every safety violation. Dedicated PPE, fire/smoke, and industrial hazard detection models or validated detection logic may be required.

## 🗺️ Development Roadmap

- [x] Set up the Python development environment.
- [x] Create the initial FastAPI backend.
- [x] Begin camera-based YOLO object detection.
- [ ] Implement and validate PPE compliance detection.
- [ ] Integrate ESP32 and compatible IoT sensors.
- [ ] Implement restricted-zone monitoring.
- [ ] Build the factory monitoring dashboard.
- [ ] Develop the Digital Twin visualization.
- [ ] Connect AI detections and sensor readings to the Digital Twin.
- [ ] Add persistent alert history and real-time notifications.
- [ ] Test the integrated prototype under controlled conditions.

## 🔒 Safety and Limitations

- This is a prototype intended for development and demonstration.
- Sensor readings and AI detections must be validated before being used for operational decisions.
- Camera-based monitoring may be affected by lighting, occlusion, camera placement, and model accuracy.
- The prototype should not replace certified industrial safety systems, emergency procedures, or human safety supervision.

## 🔮 Future Scope

- 3D Digital Twin with live machine and zone status.
- Predictive maintenance using machine vibration and temperature data.
- Edge AI deployment for lower-latency monitoring.
- Historical safety analytics and incident reports.
- Role-based dashboards for safety officers and factory managers.
- Integration with industrial IoT platforms and additional sensors.

## 🤝 Contributions

Contributions, suggestions, and feedback are welcome. You can open an issue or submit a pull request to propose improvements.

## 👩‍💻 Project Information

**Project Name:** AI-Powered Smart Factory Safety & Digital Twin

**Domain:** Artificial Intelligence, Machine Learning, Computer Vision, IoT, and Digital Twin Technology

**Project Type:** Prototype / Ongoing Development

---

*Building safer factories through AI-powered monitoring and connected digital intelligence.*
