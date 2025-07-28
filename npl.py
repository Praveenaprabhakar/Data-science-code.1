
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
import string
from nltk.corpus import stopwords

nltk.download("stopwords")

df=pd.read_csv("fake reviews dataset.csv")
df=df.head(100)
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))  
    tokens = text.split()
    tokens = [word for word in tokens if word not in stopwords.words('english')]  
    return " ".join(tokens)

df['CleanText'] = df['text_'].apply(clean_text)
print(df['CleanText'])

one=" ".join(df[df["rating"]=="1"]["CleanText"])
two=" ".join(df[df["rating"]=="2"]["CleanText"])
three=" ".join(df[df["rating"]=="3"]["CleanText"])
four=" ".join(df[df["rating"]=="4"]["CleanText"])
five=" ".join(df[df["rating"]=="5"]["CleanText"]
              
onewc=WordCloud(width=800,height=400,background_color="black",colormap="Reds").generate(one)
twowc=WordCloud(width=800,height=400,background_color="white",colormap="Reds").generate(two)
threewc=WordCloud(width=800,height=400,background_color="black",colormap="Reds").generate(three)
fourwc=WordCloud(width=800,height=400,background_color="white",colormap="Reds").generate(four)
fivewc=WordCloud(width=800,height=400,background_color="black",colormap="Reds").generate(five)

plt.subplot(1,5,1)
plt.imshow(onewc)
plt.subplot(1,5,2)
plt.imshow(twowc)
plt.subplot(1,5,3)
plt.imshow(threewc)
plt.subplot(1,5,4)
plt.imshow(fourwc)
plt.subplot(1,5,5)
plt.imshow(fivewc)

plt.tight_layout()
plt.show()
