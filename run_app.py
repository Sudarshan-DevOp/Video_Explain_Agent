#!/usr/bin/env python
"""
Flask YouTube Video Analyzer - Python Startup Script
Run this script to start the Flask application with automatic Flask installation check.
"""

import subprocess
import sys
import os

def check_and_install_flask():
    """Check if Flask is installed, if not, install it."""
    try:
        import flask
        print("✅ Flask is already installed")
        return True
    except ImportError:
        print("❌ Flask is not installed")
        print("📦 Installing Flask...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "flask>=3.0.0"])
            print("✅ Flask installed successfully!")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install Flask")
            return False

def main():
    """Main function to start the Flask app."""
    print("🎥 Flask YouTube Video Analyzer")
    print("=" * 50)
    print()
    
    # Check and install Flask if needed
    if not check_and_install_flask():
        print("\n❌ Could not install Flask. Please install it manually:")
        print("   pip install flask>=3.0.0")
        sys.exit(1)
    
    print()
    print("✅ Starting Flask application...")
    print("📝 The app will be available at: http://localhost:5000")
    print()
    print("💡 Tips:")
    print("   - Open http://localhost:5000 in your browser")
    print("   - Press Ctrl+C to stop the server")
    print("   - The app will auto-reload when you make code changes")
    print()
    
    # Change to the project directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Import and run the Flask app
    try:
        from src.reviewai.flask_app import app
        print("=" * 50)
        app.run(debug=True, port=5000, host='0.0.0.0')
    except ImportError as e:
        print(f"❌ Error importing Flask app: {e}")
        print("\n💡 Make sure you're running this from the project root directory")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error starting Flask app: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
