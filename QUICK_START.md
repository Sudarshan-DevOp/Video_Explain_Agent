# 🎥 Quick Start Guide - Flask YouTube Analyzer

## What Was Created

A fully functional Flask web application with:
- **Entry Page**: Form to input YouTube video URLs
- **Split-Screen Results Page**: 
  - Left side: YouTube video player
  - Right side: AI-generated explanation of the video

## How to Run

### Option 1: Using Python Script (Recommended - Cross-platform)
```bash
python run_app.py
```
This script automatically checks and installs Flask if needed.

### Option 2: Using Bash Script (Linux/Mac)
```bash
bash run_flask.sh
```

### Option 3: Using Batch File (Windows)
```bash
run_flask.bat
```

### Option 4: Direct Python
```bash
python src/reviewai/flask_app.py
```

## After Starting

1. **Open your browser** and go to: http://localhost:5000
2. **Paste a YouTube URL** in the form (e.g., `https://www.youtube.com/watch?v=...`)
3. **Optionally add a topic** to focus the explanation
4. **Click "Analyze Video"** and wait for the analysis
5. **View your results** with the video and explanation side-by-side

## File Structure

```
reviewai/
├── src/reviewai/
│   ├── flask_app.py          ← Main Flask application
│   ├── templates/            ← HTML templates
│   │   ├── index.html        ← Entry page
│   │   └── result.html       ← Results page
│   └── static/
│       └── style.css         ← Styling
├── run_app.py                ← Easy startup script
├── run_flask.sh              ← Linux/Mac startup script
├── run_flask.bat             ← Windows startup script
└── FLASK_APP_GUIDE.md        ← Detailed documentation
```

## Features

✅ Clean, modern UI with YouTube-inspired design
✅ Responsive design (works on mobile, tablet, desktop)
✅ Real-time URL validation
✅ Error handling with helpful messages
✅ Integration with your CrewAI agents
✅ Session-based data management
✅ Professional styling with animations

## Supported YouTube URLs

All of these work:
- `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- `https://youtu.be/dQw4w9WgXcQ`
- `https://www.youtube.com/embed/dQw4w9WgXcQ`

## Troubleshooting

**Flask not installed?**
```bash
pip install flask>=3.0.0
```

**Port 5000 in use?** Edit `flask_app.py` last line and change the port:
```python
app.run(debug=True, port=8000)  # Change to any free port
```

**Want to stop the server?**
Press `Ctrl+C` in your terminal

## Next Steps

- Customize the styling in `src/reviewai/static/style.css`
- Modify the form in `src/reviewai/templates/index.html`
- Adjust the explanation layout in `src/reviewai/templates/result.html`
- Change the secret key in `flask_app.py` for production

Enjoy your YouTube Video Analyzer! 🚀
