# Sentiment Analysis API

A simple Flask-based sentiment analysis API using machine learning.

## 🎯 Overview

This project demonstrates a RESTful API that analyzes the sentiment of text input and returns positive, negative, or neutral classifications.

## 🛠️ Technologies Used

- Python 3.x
- Flask
- scikit-learn
- NLTK
- pandas

## 📦 Installation

```bash
pip install flask scikit-learn nltk pandas
```

## 🚀 Quick Start

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## 📡 API Endpoints

### POST /analyze
Analyzes sentiment of provided text.

**Request:**
```json
{
  "text": "I love this product!"
}
```

**Response:**
```json
{
  "sentiment": "positive",
  "confidence": 0.87
}
```

## 📊 Model Details

- Algorithm: Logistic Regression
- Features: TF-IDF vectorization
- Training accuracy: ~85%

## 🔮 Future Enhancements

- [ ] Add support for multiple languages
- [ ] Implement deep learning model (LSTM/BERT)
- [ ] Add batch processing endpoint
- [ ] Deploy to cloud platform

## 📝 License

MIT License - See main repository LICENSE file
