#!/usr/bin/env python
"""
Flask application for YouTube Video Explanation using CrewAI
"""
import re
import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect
from dotenv import load_dotenv
from reviewai.crew import Reviewai

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')

# In-memory cache to store video explanations
# key: video_id, value: {youtube_url, video_id, explanation, topic, embed_url}
_video_cache = {}

# Helper function to extract YouTube video ID
def extract_youtube_id(url):
    """Extract YouTube video ID from URL"""
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

# Helper function to get YouTube embed URL
def get_youtube_embed_url(video_id):
    """Get YouTube embed URL from video ID"""
    return f"https://www.youtube.com/embed/{video_id}"

# Helper function to generate explanation using crew
def get_video_explanation(youtube_url, topic="YouTube Video"):
    """
    Use CrewAI to generate explanation for the video
    """
    try:
        inputs = {
            'topic': topic,
            'youtube_url': youtube_url,
            'current_year': str(datetime.now().year)
        }
        
        

        # Fallback to CrewAI crew kickoff
        crew = Reviewai()
        result = crew.crew().kickoff(inputs=inputs)
        return str(result)
    except Exception as e:
        return f"Error generating explanation: {str(e)}"

@app.route('/')
def index():
    """Home page - YouTube URL entry"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Process YouTube URL and generate explanation
    """
    try:
        data = request.json
        youtube_url = data.get('youtube_url', '').strip()
        topic = data.get('topic', 'YouTube Video').strip()
        
        # Validate URL
        if not youtube_url:
            return jsonify({'error': 'Please provide a YouTube URL'}), 400
        
        # Extract video ID and validate
        video_id = extract_youtube_id(youtube_url)
        if not video_id:
            return jsonify({'error': 'Invalid YouTube URL. Please check and try again.'}), 400
        
        # Generate explanation using crew
        explanation = get_video_explanation(youtube_url, topic)
        embed_url = get_youtube_embed_url(video_id)
        
        # Store in memory cache for the results page
        _video_cache[video_id] = {
            'youtube_url': youtube_url,
            'video_id': video_id,
            'explanation': explanation,
            'topic': topic,
            'embed_url': embed_url
        }
        
        return jsonify({
            'success': True,
            'video_id': video_id,
            'embed_url': embed_url,
            'explanation': explanation
        })
    
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/result')
def result():
    """Results page - Display video and explanation"""
    video_id = request.args.get('video_id', '')
    if not video_id or video_id not in _video_cache:
        return redirect('/')
    
    data = _video_cache[video_id]
    return render_template('result.html',
                          embed_url=data.get('embed_url', ''),
                          explanation=data.get('explanation', ''),
                          topic=data.get('topic', 'YouTube Video'),
                          youtube_url=data.get('youtube_url', ''))

@app.route('/api/result')
def get_result():
    """API endpoint to get result data"""
    video_id = request.args.get('video_id', '')
    if not video_id or video_id not in _video_cache:
        return jsonify({'error': 'No video data found'}), 404
    
    return jsonify(_video_cache[video_id])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
