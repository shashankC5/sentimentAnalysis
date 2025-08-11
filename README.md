# Sentiment Analysis using NLTK VADER

A simple Python project that performs **sentiment analysis** on text using the **VADER (Valence Aware Dictionary and sEntiment Reasoner)** model from the [NLTK](https://www.nltk.org/) library.  

This tool analyzes text input and returns sentiment scores for:
- **Positive**
- **Negative**
- **Neutral**
- **Compound** (overall sentiment)

---

## 🚀 Features
- Easy-to-use function for analyzing any text string.
- Based on the VADER lexicon, optimized for **social media**, **reviews**, and **general text**.
- Requires minimal setup with NLTK.
- Beginner-friendly Python script.

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/sentiment-analysis.git
cd sentiment-analysis
pip install nltk
import nltk
nltk.download('vader_lexicon')

python sentiment_analysis.py
