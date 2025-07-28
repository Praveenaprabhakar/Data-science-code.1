import pandas as pd
import nltk
import string
from nltk.corpus import stopwords

nltk.download("stopwords", quiet=True)

try:
    df = pd.read_csv("fake reviews dataset.csv")
    df = df.head(100)
except FileNotFoundError:
    print("The specified file was not found.")
    exit()


def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))  
    tokens = text.split()
    tokens = [word for word in tokens if word not in stopwords.words('english')]  
    return " ".join(tokens)


df['CleanText'] = df['text_'].apply(clean_text)


for index, row in df.iterrows():
    print(f"Rating: {row['rating']}, Cleaned Text: {row['CleanText']}")
    
grouped=df.groupby('rating').sum()
print("\n grouped data:",grouped)
