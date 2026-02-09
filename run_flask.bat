@echo off
REM Flask YouTube Video Analyzer - Startup Script for Windows

echo.
echo Starting 🎥 YouTube Video Analyzer...
echo.

REM Check if Flask is installed
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo ❌ Flask is not installed.
    echo Installing Flask...
    pip install flask>=3.0.0
)

echo ✅ Starting Flask application...
echo 📝 The app will be available at: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

REM Run the Flask app
python src/reviewai/flask_app.py

pause
