import kagglehub
import pandas as pd
import re
import textblob
import matplotlib.pyplot as plt

# Download and load dataset
path = kagglehub.dataset_download("mansithummar67/boat-product-dataset")
df = pd.read_csv(f"{path}/BoatProduct.csv")

# Clean 'Rate' column and extract numerical ratings
df['Rate'] = pd.to_numeric(df['Rate'].str.extract(r"(\d+\.\d+)")[0], errors='coerce')

# Drop rows with missing reviews
df_clean = df.dropna(subset=['Review'])

# Sentiment analysis function
def get_sentiment(text):
    polarity = textblob.TextBlob(str(text)).sentiment.polarity
    return 'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'

# Apply sentiment analysis
df_clean['Sentiment'] = df_clean['Review'].apply(get_sentiment)

# Display sentiment counts and sample negative reviews
print(df_clean['Sentiment'].value_counts())
print("\nSample Negative Reviews:")
print(df_clean[df_clean['Sentiment'] == 'Negative'][['ProductName', 'Review', 'Summary']].head(2))

# Plot sentiment distribution
df_clean['Sentiment'].value_counts().plot(kind='bar', color=['green', 'blue', 'red'])
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.title("Sentiment Distribution of Reviews")
plt.show()

# Save negative reviews
df_clean[df_clean['Sentiment'] == 'Negative'].to_csv("Negative_Reviews.csv", index=False)
