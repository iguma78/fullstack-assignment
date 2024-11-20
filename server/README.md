# FastAPI Data Server

A RESTful API server built with FastAPI for managing and serving data points.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup

1. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

Start the development server:
```bash
uvicorn main:app --reload
```

The server will be available at `http://localhost:8000`