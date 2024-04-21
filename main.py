import nltk
import re
from nltk.corpus import stopwords
from collections import Counter


with open('paragraph.txt', 'r', encoding='utf-8') as file:
    text = file.read()

#Remove punctuation and convert the text to lower text
def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text

text = preprocess_text(text)

words = nltk.word_tokenize(text)

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

word_count = Counter(filtered_words)

most_common_words = word_count.most_common(20)

print("Top 20 Most Common Words:")
for word, count in most_common_words:
    print(f"[{word}]: {count}")
