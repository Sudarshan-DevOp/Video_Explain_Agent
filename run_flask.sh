#!/bin/bash

# Flask YouTube Video Analyzer - Startup Script

echo "🎥 Starting YouTube Video Analyzer..."
echo ""

# Check if Flask is installed
python -c "import flask" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Flask is not installed."
    echo "Installing Flask..."
    pip install flask>=3.0.0
fi

echo "✅ Starting Flask application..."
echo "📝 The app will be available at: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Change to the project directory
cd "$(dirname "$0")"

# Run the Flask app
python src/reviewai/flask_app.py
