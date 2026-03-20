import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# load the dataset
try:
    df = pd.read_csv("spam.csv")
except FileNotFoundError:
    print("Couldn't find spam.csv, make sure it's in this folder!")
    exit()

# convert labels to numbers: ham = 0, spam = 1
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# separate messages and labels
texts = df['message']
targets = df['label']

# split into training and test sets
train_texts, test_texts, train_labels, test_labels = train_test_split(
    texts, targets, test_size=0.2, random_state=42
)

# turn text into numbers
vectorizer = CountVectorizer()
train_features = vectorizer.fit_transform(train_texts)
test_features = vectorizer.transform(test_texts)

# train the model
classifier = MultinomialNB()
classifier.fit(train_features, train_labels)

# check accuracy
preds = classifier.predict(test_features)
print(f"\nModel got about {accuracy_score(test_labels, preds)*100:.2f}% correct.\n")

# simple input loop
print("Type something to see if it's spam or not (type 'exit' to quit)\n")
while True:
    msg = input("Your text: ")
    if msg.lower() == "exit":
        print("Bye!")
        break

    msg_vec = vectorizer.transform([msg])
    pred = classifier.predict(msg_vec)

    if pred[0] == 1:
        print("Spam! 🚫\n")
    else:
        print("Not spam ✅\n")
