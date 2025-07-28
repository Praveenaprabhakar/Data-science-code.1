import pandas as pd
import matplotlib.pyplot as plt
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from wordcloud import WordCloud
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

df = pd.read_csv("datasets/Baby.csv", encoding='ISO-8859-1')
df = df.head(1000)

df["review"] = df["review"].fillna("") 
tf = TfidfVectorizer(stop_words='english')
x = tf.fit_transform(df["review"])
print(x)

tf_df = pd.DataFrame(x.toarray(), columns=tf.get_feature_names_out())
print(tf_df)

def clean_text(text):
    
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    tokens = text.split()
    tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    return " ".join(tokens)


df['CleanText'] = df['review'].apply(clean_text)
print(df['CleanText'])

five_star = " ".join(df[df["rating"] == 5]["CleanText"])
four_star = " ".join(df[df["rating"] == 4]["CleanText"])
three_star = " ".join(df[df["rating"] == 3]["CleanText"])
two_star = " ".join(df[df["rating"] == 2]["CleanText"])
one_star = " ".join(df[df["rating"] == 1]["CleanText"])


fivewc = WordCloud(width=800, height=400, background_color="white", colormap="Blues").generate(five_star)
fourwc = WordCloud(width=800, height=400, background_color="white", colormap="RdYlBu_r").generate(four_star)
threewc = WordCloud(width=800, height=400, background_color="white", colormap="Purples_r").generate(three_star)
twowc = WordCloud(width=800, height=400, background_color="white", colormap="Oranges").generate(two_star)
onewc = WordCloud(width=800, height=400, background_color="white", colormap="Greens").generate(one_star)


fig, axs = plt.subplots(3, 2, figsize=(10,6))

axs[0, 0].imshow(fivewc)
axs[0, 0].set_title("5 Stars")

axs[0, 1].imshow(fourwc)
axs[0, 1].set_title("4 Stars")

axs[1, 0].imshow(threewc)
axs[1, 0].set_title("3 Stars")

axs[1, 1].imshow(twowc)
axs[1, 1].set_title("2 Stars")

axs[2, 0].imshow(onewc)
axs[2, 0].set_title("1 Star")
axs[2, 1].axis('off')

plt.tight_layout()
plt.show()

