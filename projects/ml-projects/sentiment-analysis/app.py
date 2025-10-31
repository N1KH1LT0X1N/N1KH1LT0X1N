"""
Sentiment Analysis API - Flask Application
A simple API for analyzing sentiment of text inputs.
"""

from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Simple sentiment analysis (placeholder - replace with actual ML model)
def analyze_sentiment(text):
    """
    Analyzes sentiment of input text.
    Returns sentiment label and confidence score.
    """
    text = text.lower()
    
    # Simple keyword-based approach (replace with trained model)
    positive_words = ['good', 'great', 'excellent', 'amazing', 'love', 'wonderful', 'fantastic']
    negative_words = ['bad', 'terrible', 'awful', 'hate', 'horrible', 'poor', 'worst']
    
    positive_count = sum(1 for word in positive_words if word in text)
    negative_count = sum(1 for word in negative_words if word in text)
    
    if positive_count > negative_count:
        sentiment = "positive"
        confidence = min(0.6 + (positive_count * 0.1), 0.95)
    elif negative_count > positive_count:
        sentiment = "negative"
        confidence = min(0.6 + (negative_count * 0.1), 0.95)
    else:
        sentiment = "neutral"
        confidence = 0.5
    
    return sentiment, confidence

@app.route('/')
def home():
    """Home endpoint with API information."""
    return jsonify({
        "name": "Sentiment Analysis API",
        "version": "1.0.0",
        "endpoints": {
            "/analyze": "POST - Analyze sentiment of text",
            "/health": "GET - Check API health"
        }
    })

@app.route('/analyze', methods=['POST'])
def analyze():
    """Analyze sentiment of provided text."""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({"error": "Missing 'text' field in request"}), 400
        
        text = data['text']
        
        if not text or not text.strip():
            return jsonify({"error": "Text cannot be empty"}), 400
        
        sentiment, confidence = analyze_sentiment(text)
        
        return jsonify({
            "text": text,
            "sentiment": sentiment,
            "confidence": round(confidence, 2)
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "message": "API is running"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
