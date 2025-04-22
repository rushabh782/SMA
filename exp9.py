import pandas as pd, numpy as np, matplotlib.pyplot as plt, random
from datetime import datetime, timedelta
from textblob import TextBlob
import seaborn as sns

def clean_text(text):
    return ' '.join(text.split())

def get_sentiment_score(text):
    return TextBlob(text).sentiment.polarity

def categorize(score):
    return "Positive" if score > 0.1 else "Negative" if score < -0.1 else "Neutral"

def generate_fake_tweets(brand, count=100):
    tweets = []
    for _ in range(count):
        bias = {"chatgpt 4": 0.2, "chatsonic": 0.1, "google bard": -0.05}.get(brand.lower(), 0)
        score = max(-1.0, min(1.0, random.uniform(-1, 1) + bias))
        text = f"{brand} is {'awesome' if score > 0.3 else 'okay' if score > 0 else 'frustrating'}!"
        tweets.append({
            'date': datetime.now() - timedelta(days=random.randint(1, 30)),
            'text': text,
            'score': score,
            'sentiment': categorize(score),
        })
    return pd.DataFrame(tweets)

def analyze_brands(brands, count=100):
    all_data, summary = [], {}
    for brand in brands:
        df = generate_fake_tweets(brand, count)
        sentiment_pct = df['sentiment'].value_counts(normalize=True) * 100
        summary[brand] = {
            'Positive': sentiment_pct.get('Positive', 0),
            'Neutral': sentiment_pct.get('Neutral', 0),
            'Negative': sentiment_pct.get('Negative', 0),
            'Average Score': df['score'].mean()
        }
        df['brand'] = brand
        all_data.append(df)
    return pd.concat(all_data), summary

def plot_sentiment_bars(summary):
    brands = list(summary.keys())
    pos = [summary[b]['Positive'] for b in brands]
    neu = [summary[b]['Neutral'] for b in brands]
    neg = [summary[b]['Negative'] for b in brands]
    
    x = np.arange(len(brands))
    plt.figure(figsize=(8, 5))
    plt.bar(x-0.2, pos, 0.2, label='Positive', color='green')
    plt.bar(x, neu, 0.2, label='Neutral', color='gray')
    plt.bar(x+0.2, neg, 0.2, label='Negative', color='red')
    plt.xticks(x, brands)
    plt.ylabel('Percentage')
    plt.title('Sentiment Distribution')
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_average_sentiment(summary):
    brands = list(summary.keys())
    scores = [summary[b]['Average Score'] for b in brands]
    colors = ['green' if s >= 0 else 'red' for s in scores]
    plt.figure(figsize=(6, 4))
    bars = plt.bar(brands, scores, color=colors)
    plt.axhline(0, color='black', linestyle='--', linewidth=0.7)
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f"{bar.get_height():.2f}",
                 ha='center', va='bottom' if bar.get_height() >= 0 else 'top')
    plt.title('Average Sentiment Score')
    plt.tight_layout()
    plt.show()

# Run analysis
brands = ["ChatGPT 4", "ChatSonic", "Google Bard"]
data, summary = analyze_brands(brands, count=200)
plot_sentiment_bars(summary)
plot_average_sentiment(summary)

# Print summary
for b, s in summary.items():
    print(f"\n{b} → Positive: {s['Positive']:.1f}%, Neutral: {s['Neutral']:.1f}%, "
          f"Negative: {s['Negative']:.1f}%, Avg Score: {s['Average Score']:.2f}")
