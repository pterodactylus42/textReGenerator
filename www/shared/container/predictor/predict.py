#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open("etah-murr.txt", "r", encoding="utf-8") as file:
    contents = file.read()
    
contents = contents.split("\n")
contents = [line.strip() for line in contents if "#" not in line]

contents = "\n".join(contents)


# In[2]:


import pickle

with open("word_to_int.etah.pickle", "rb") as file:
    word_to_int = pickle.load(file)
    
with open("int_to_word.etah.pickle", "rb") as file:
    int_to_word = pickle.load(file)


# In[3]:


import nltk
from nltk import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')
tokens = word_tokenize(contents)

tokens_transformed = [word_to_int[word] for word in tokens if word in word_to_int]


# In[5]:


from keras.models import load_model

model = load_model("etah.keras")


# In[6]:


sentence = tokens_transformed[100:140]

# print(" ".join([int_to_word[token] for token in sentence]).replace("\\n", "\n"))


# In[7]:


# sentence


# In[8]:


import numpy as np

def predict_text() :
    sentence = np.array(tokens_transformed[100:140])
    predicted_text = np.array([]);
    for i in range(0, 300):
        prediction = model.predict(sentence.reshape(1, 40))
        
        # word = np.argmax(prediction[0])
        word = np.random.choice(len(int_to_word), p=prediction[0])
        sentence = np.append(sentence[1:], [word])
        predicted_text = np.append(predicted_text, int_to_word[word])

    result = " ".join(predicted_text).replace("\\n", "\n")
    return result


# In[9]:


# predicted_text = predict_text()
# print(predicted_text)


# In[10]:


from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    # data = request.get_json(force=True)
    prediction = predict_text()
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
