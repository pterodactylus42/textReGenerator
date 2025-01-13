#!/usr/bin/env python
# coding: utf-8

with open("etah-murr.txt", "r", encoding="utf-8") as file:
    contents = file.read()
    
contents = contents.split("\n")
contents = [line.strip() for line in contents if "#" not in line]
contents = "\n".join(contents)

import pickle

with open("word_to_int.etah.pickle", "rb") as file:
    word_to_int = pickle.load(file)
    
with open("int_to_word.etah.pickle", "rb") as file:
    int_to_word = pickle.load(file)

import nltk
from nltk import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

tokens = word_tokenize(contents)

tokens_transformed = [word_to_int[word] for word in tokens if word in word_to_int]

from keras.models import load_model

model = load_model("etah.keras")

import numpy as np

def random_sequence() :
  x = np.random.randint(100)
  return np.array(tokens_transformed[100+x:140+x])


def seed() :
  return random_sequence()


def next(sequence) :
    prediction = model.predict(sequence.reshape(1, 40))
    return np.random.choice(len(int_to_word), p=prediction[0])
    

def nudge(sequence) :
    word = next(sequence)
    return np.append(sequence[1:], [word])


from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/seed', methods=['POST'])
def seed_endpoint():
    my_seed = seed()
    return jsonify({'sequence': my_seed})


@app.route('/next', methods=['POST'])
def next_endpoint():
    data = request.get_json()
    if not data or 'sequence' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    sequence = data['sequence']
    if not all(isinstance(n, int) for n in sequence):
        return jsonify({'error': 'All elements must be integers'}), 400
    
    if not len(sequence) == 40:
        return jsonify({'error': 'Sequence length is not 40'}), 400

    result = next(np.array(sequence))
    return jsonify({'next': result})


@app.route('/nudge', methods=['POST'])
def nudge_endpoint():
    data = request.get_json()
    if not data or 'sequence' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    sequence = data['sequence']
    if not all(isinstance(n, int) for n in sequence):
        return jsonify({'error': 'All elements must be integers'}), 400

    if not len(sequence) == 40:
        return jsonify({'error': 'Sequence length is not 40'}), 400

    result = nudge(np.array(sequence))
    return jsonify({'sequence': result.tolist()})


@app.route('/word', methods=['POST'])
def word_endpoint():
    data = request.get_json()
    if not data or 'sequence' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    sequence = data['sequence']
    if not isinstance(sequence, int):
        return jsonify({'error': 'Element must be integer'}), 400

    result = int_to_word[sequence]
    return jsonify({'word': result})


@app.route('/sum', methods=['POST'])
def sum_endpoint():
    data = request.get_json()
    if not data or 'sequence' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    numbers = data['sequence']
    if not all(isinstance(n, int) for n in numbers):
        return jsonify({'error': 'All elements must be integers'}), 400
    
    result = sum(numbers)
    return jsonify({'sum': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
