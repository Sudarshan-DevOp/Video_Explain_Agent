# Flask YouTube Video Analyzer

A web application built with Flask that allows you to analyze YouTube videos using CrewAI. Upload a YouTube video URL and get AI-powered explanations of the video content.

## Features

- 🎥 **Clean Entry Page** - Simple form to input YouTube video URLs
- 📺 **Split-Screen View** - Watch videos on the left, read explanations on the right
- 🤖 **AI-Powered Analysis** - Uses CrewAI to generate detailed video explanations
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile devices
- ⚡ **Fast & Lightweight** - Built with Flask and modern web technologies

## Installation

1. Install Flask dependency:
```bash
pip install flask>=3.0.0
```

Or update your dependencies:
```bash
pip install -e .
```

## Running the Application

### Method 1: Direct Python Execution

```bash
python src/reviewai/flask_app.py
```

### Method 2: Using Flask CLI

```bash
export FLASK_APP=src/reviewai/flask_app.py
export FLASK_ENV=development
flask run
```

### Method 3: From your project root

```bash
python -m flask --app src/reviewai/flask_app run
```

## Usage

1. **Start the Application**
   - Run one of the commands above
   - The app will be available at `http://localhost:5000`

2. **Enter YouTube URL**
   - Paste a YouTube video URL (e.g., `https://www.youtube.com/watch?v=...`)
   - Optionally specify a topic to focus the analysis
   - Click "Analyze Video"

3. **View Results**
   - The video will appear on the left side
   - AI-generated explanation appears on the right side
   - You can watch the video while reading the explanation

4. **Return Home**
   - Click "Back to Home" to analyze another video

## How It Works

The application integrates with your CrewAI crew to:
1. Accept YouTube video URLs from users
2. Extract video ID and validate the URL
3. Generate detailed explanations using CrewAI agents
4. Present the video and explanation in a side-by-side layout

## File Structure

```
src/reviewai/
├── flask_app.py                 # Main Flask application
├── templates/
│   ├── index.html              # Entry page (URL input)
│   └── result.html             # Results page (video + explanation)
└── static/
    └── style.css               # Styling for both pages
```

## Supported YouTube URL Formats

The application supports the following YouTube URL formats:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`

## Configuration

### Change Secret Key
Edit `flask_app.py` and update the secret key:
```python
app.secret_key = 'your-secret-key-change-this'
```

### Change Port
Modify the last line of `flask_app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Change port here
```

### Disable Debug Mode
For production, set `debug=False`:
```python
app.run(debug=False, port=5000)
```

## Troubleshooting

### Flask not found
```bash
pip install flask>=3.0.0
```

### Port 5000 already in use
Change the port in `flask_app.py` or use:
```bash
flask run --port 8000
```

### YouTube video won't load
- Check if the URL is valid
- Ensure the video is not age-restricted
- Try accessing the YouTube URL directly in your browser

### Explanation takes too long
- The CrewAI crew is processing the request
- This is normal for the first request as models are loading
- Subsequent requests will be faster

## Future Enhancements

- [ ] Video transcription integration
- [ ] Explanation language selection
- [ ] Save explanations as PDF
- [ ] Video timestamp-specific explanations
- [ ] Comparison of multiple videos
- [ ] Dark mode toggle
- [ ] User accounts and history

## License

This project is part of the reviewai CrewAI project.
